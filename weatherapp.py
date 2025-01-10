import requests
import json
import pyttsx3

def robot_speaker(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
while True:

    city = input("Enter City(type 'exit'to end):")
    if city == "exit":
        robot_speaker("Thanks For Using Weather Api")
        break
    url = f"http://api.weatherapi.com/v1/current.json?key=b8a04a6cbf0b408687c163720242702&q={city}"

    r = requests.get(url)
    #print(r.text)
    wdic = json.loads(r.text)
    current_temp = wdic["current"]["temp_c"]
    print(f"Current Temperature in {city}:{current_temp}")

    robot_speaker(f"The temperature in {city} is {current_temp} degree")



