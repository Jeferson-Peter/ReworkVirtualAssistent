import pyttsx3
import pyautogui
import psutil
import pyjokes
import speech_recognition as sr
import json
import requests
import geocoder
from difflib import get_close_matches
from currency_converter import CurrencyConverter
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
g = geocoder.ip('me')
data = json.load(open('data.json'))
c = CurrencyConverter()

currencies = {
    'dollar': 'USD',
    'real': 'BRL'
}


def get_location():
    g = geocoder.ip('me')
    return g


def get_lat_long():
    location = get_location()
    return location.lat, location.lng

def get_ip_address():
    location = get_location()
    return location.ip


def speak(audio) -> None:
    engine.say(audio)
    engine.runAndWait()


def screenshot() -> None:
    img = pyautogui.screenshot()
    home = os.path.expanduser('~')
    path = f'{home}{os.sep}Downloads{os.sep}screenshot_jarvis.png'
    speak("taking screenshot")
    img.save(path)
    speak("screenshot taken")

def cpu() -> None:
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    if battery is not None:
        speak("battery is at")
        speak(battery.percent)

def joke() -> None:
    for i in range(5):
        speak(pyjokes.get_jokes()[i])

def takeCommand() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        query = ""
        while True:
            print('Listening...')
            r.pause_threshold = 0.7
            r.energy_threshold = 494
            r.adjust_for_ambient_noise(source, duration=1.5)
            audio = r.listen(source)
            
            try:
                print("Recognizing..")
                
                query = r.recognize_google(audio, language='en-US')
                print(f'User said: {query}\n')
                
            except Exception as e:
                print(e)
                print("Say that again sir..")
            
            if query != "":
                break
            
        return query.lower()

def weather():
    api_url = "https://fcc-weather-api.glitch.me/api/current?lat=" + \
        str(g.latlng[0]) + "&lon=" + str(g.latlng[1])

    data = requests.get(api_url)
    data_json = data.json()
    if data_json['cod'] == 200:
        main = data_json['main']
        wind = data_json['wind']
        weather_desc = data_json['weather'][0]
        speak(str(data_json['coord']['lat']) + 'latitude' + str(data_json['coord']['lon']) + 'longitude')
        speak('Current location is ' + data_json['name'] + data_json['sys']['country'] + 'dia')
        speak('weather type ' + weather_desc['main'])
        speak('Wind speed is ' + str(wind['speed']) + ' metre per second')
        speak('Temperature: ' + str(main['temp']) + 'degree celcius')
        speak('Humidity is ' + str(main['humidity']))


def translate(word):
    word = word.lower()
    if word in data:
        speak(data[word])
    elif len(get_close_matches(word, data.keys())) > 0:
        x = get_close_matches(word, data.keys())[0]
        speak('Did you mean ' + x +
              ' instead,  respond with Yes or No.')
        ans = takeCommand()
        if 'yes' in ans:
            speak(data[x])
        elif 'no' in ans:
            speak("Word doesn't exist. Please make sure you spelled it correctly.")
        else:
            speak("We didn't understand your entry.")

    else:
        speak("Word doesn't exist. Please double check it.")

def currency_converter():

    value = getActualCurrencyValue()
    currency = getActualCurrency()
    converter = getCurrencyToChange()

    valueConverted = convert(value, currency, converter)

    speak("this value equals " + str(valueConverted) + " " + converter + " " + "in the current quote")
    print("this value equals " + str(valueConverted) + " " +converter + " " + "in the current quote")

def convert(value, currency, converter):
    try:
        valueConverted = c.convert(value, currency, converter)
    except Exception as e:
        print(e)
        convert(value, currency, converter)
    return round(valueConverted, 2)

def getActualCurrencyValue():
    speak("What's the value you want to convert?")
    value = takeCommand()
    try:
        int(value) or float(value)
        return value
    except:
        getActualCurrencyValue()

def getActualCurrency():
    has_value = False
    speak("What's the actual currency?")
    while not has_value:
        currency = takeCommand().lower()
        if currency in currencies.keys():
            has_value = True
            return currencies[currency]
        else:
            speak("Currency not found, please try again?")

def getCurrencyToChange():
    has_value = False
    speak("What's the currency you want to convert?")
    while not has_value:
        currency = takeCommand().lower()
        if currency in currencies.keys():
            has_value = True
            return currencies[currency]
        else:
            speak("Currency not found, please try again?")