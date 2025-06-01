from flask import Flask, render_template, request, redirect, jsonify, send_file
import requests
import sqlite3
import pandas as pd
from datetime import datetime
import os  # ✅ add this at the top

# ✅ replace your existing app.run() with this


app = Flask(__name__)
API_KEY = "a914daeff19033d64653a6aebe154296"  # Replace this

# --- DB Setup ---
def init_db():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS weather_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        location TEXT,
        date TEXT,
        temperature REAL,
        description TEXT
    )''')
    conn.commit()
    conn.close()

init_db()

# --- Get weather ---
def get_weather(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    res = requests.get(url).json()
    if res.get("cod") != 200:
        return None
    data = {
        "location": res["name"],
        "temperature": res["main"]["temp"],
        "description": res["weather"][0]["description"],
        "icon": res["weather"][0]["icon"],
        "lat": res["coord"]["lat"],
        "lon": res["coord"]["lon"]
    }
    return data
# --- 5-day forecast ---
def get_forecast(location):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}&units=metric"
    res = requests.get(url).json()
    if res.get("cod") != "200":
        return []
    # Filter for one record per day (every 8th entry ~24h)
    return res["list"][::8]

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    forecast = []
    coords = None

    if request.method == "POST":
        location = request.form["location"]
        weather = get_weather(location)
        forecast = get_forecast(location)
        if weather:
            coords = (weather["lat"], weather["lon"])
            conn = sqlite3.connect('weather.db')
            c = conn.cursor()
            c.execute("INSERT INTO weather_data (location, date, temperature, description) VALUES (?, ?, ?, ?)",
                      (weather["location"], datetime.now().strftime("%Y-%m-%d %H:%M"), weather["temperature"], weather["description"]))
            conn.commit()
            conn.close()

    # Read all saved entries
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute("SELECT * FROM weather_data")
    saved_data = c.fetchall()
    conn.close()

    return render_template("index.html", weather=weather, forecast=forecast, coords=coords, saved_data=saved_data)

@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute("DELETE FROM weather_data WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    if request.method == "POST":
        new_temp = request.form["temperature"]
        new_desc = request.form["description"]
        c.execute("UPDATE weather_data SET temperature = ?, description = ? WHERE id = ?",
                  (new_temp, new_desc, id))
        conn.commit()
        conn.close()
        return redirect("/")
    else:
        c.execute("SELECT * FROM weather_data WHERE id = ?", (id,))
        record = c.fetchone()
        conn.close()
        return render_template("update.html", record=record)

@app.route("/export")
def export():
    conn = sqlite3.connect('weather.db')
    df = pd.read_sql_query("SELECT * FROM weather_data", conn)
    df.to_csv("weather_export.csv", index=False)
    conn.close()
    return send_file("weather_export.csv", as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # fallback for local dev
    app.run(host="0.0.0.0", port=port)
