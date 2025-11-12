import speech_recognition as sr
import sys
import pyttsx3
import pyjokes
import webbrowser
import requests
import json
from datetime import date

def speech_to_text():
  r=sr.Recognizer()
  with sr.Microphone() as souce:
    print("listening")
    audio=r.listen(souce)
    try:
        text=r.recognize_google(audio)
        print("you said",text)
    except:
        print("sorry, I Couldn't understand ")
def text_to_speech(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def tell_me_jokes():
  jokes=pyjokes.get_joke()
  print(jokes)
def open_youtube():
  webbrowser.open("https://www.youtube.com")

def run_asistance():
   command = int(input("welcome to the voice asistance\n1.Speech to text\n2.Text to speech\n3.Tell me Jokes\n4.Open Youtube\n5.Today date\n6.Today weather\nEnter the option"))
   if command == 1:
    speech_to_text()
   elif command == 2:
    value=input("enter the value")
    text_to_speech(value)
   elif command == 3:
     tell_me_jokes()
   elif command == 4:
    open_youtube()
   elif command == 5:
    today=date.today()
    print("today date",today)
   elif command == 6:
    api_key = "74eda551c03aca5012fce51cdb641e7b"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = input("Enter city name : ")
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    print(x)
   else:
    sys.exit(0)
while True:
  run_asistance()
    



