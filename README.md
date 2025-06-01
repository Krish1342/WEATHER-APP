

````markdown
# 🌤️ Weather App by Krish Lodha

A lightweight weather app built with **Python Flask** and **Bootstrap**, using the **OpenWeatherMap API**. It allows users to check current weather and a 5-day forecast, save results, update/delete them, and export to CSV. Includes dark mode toggle and an info tooltip.

---

## 🚀 How to Run This App

### 1. Clone the project

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

If the file is missing, you can install manually:

```bash
pip install Flask requests pandas
```

### 3. Get a free API key from OpenWeatherMap

* Sign up at: [https://home.openweathermap.org/users/sign\_up](https://home.openweathermap.org/users/sign_up)
* Go to your API keys page: [https://home.openweathermap.org/api\_keys](https://home.openweathermap.org/api_keys)
* Copy your API key and open `app.py`
* Replace this line:

```python
API_KEY = "your_openweathermap_api_key"
```

with:

```python
API_KEY = "your_actual_key_here"
```

### 4. Run the app

```bash
python app.py
```

Visit in your browser:

```
http://127.0.0.1:5000
```

---

## 🧠 How to Use

1. **Enter a location** (city name) and click **Get Weather**
2. See the **current weather** and **5-day forecast**
3. Weather info is automatically saved to the database
4. Scroll down to see the **saved weather records**

   * Use **Update** to change temperature/description
   * Use **Delete** to remove a record
5. Click **Export to CSV** to download saved data
6. Use 🌗 **Toggle Mode** (top-right) to switch between light and dark themes
7. Hover over ℹ️ **Info icon** (top-left) to see app details

---

## 📁 File Structure

```
weather_app/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── update.html
├── static/
│   └── style.css
└── weather.db  # Created automatically
```

---

## 🛠 Tech Stack

* Flask (Python)
* Jinja2 Templates
* Bootstrap 5
* SQLite3 (local DB)
* OpenWeatherMap API

---

## 📤 Output

Click **Export to CSV** to download all stored weather queries in one click.

---

## 🙋‍♂️ Author

**Krish Lodha**
📧 Email: \[[lodhakrish11@gmail.com](mailto:lodhakrish11@gmail.com)]

---

## 🎥 Demo Video

Watch the app in action here:  
👉 [Click to view demo](https://drive.google.com/file/d/1E6rFLiqy0FvI3vLSpQURRuuytRBsg7Un/view?usp=sharing)