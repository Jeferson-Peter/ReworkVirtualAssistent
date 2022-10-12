import pyttsx3
import speech_recognition as sr
import webbrowser 
import datetime 
import os
import sys
import smtplib
# from OCR import OCR
from diction import translate
from helpers import *
from youtube import youtube
from sys import platform
import os
import getpass

## todo: 
## pesquisa por voz
## previsao do tempo (cidade/uf)
## cotação de moedas (brl/usd)
## lembretes
## tradução
## abrir programas (vscode/office/chrome/explorer)
## 
## recursos:
## nlp (natural language processor)
## ibm watson/ google cloud
## speech to text

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
 
# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing
def takeCommand():
 
    r = sr.Recognizer()
 
    # from the speech_Recognition module
    # we will use the Microphone module
    # for listening the command
    with sr.Microphone() as source:
        print('Listening')
         
        # seconds of non-speaking audio before
        # a phrase is considered complete
        r.pause_threshold = 0.7
        audio = r.listen(source)
         
        # Now we will be using the try and catch
        # method so that if sound is recognized
        # it is good else we will have exception
        # handling
        try:
            print("Recognizing")
             
            # for Listening the command in indian
            # english we can also use 'hi-In'
            # for hindi recognizing
            Query = r.recognize_google(audio, language='en-US')
            print("the command is printed=", Query)
             
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
         
        return Query
 
def speak(audio):
     
    engine = pyttsx3.init()
    # getter method(gets the current value
    # of engine property)
    voices = engine.getProperty('voices')
     
    # setter method .[0]=male voice and
    # [1]=female voice in set Property.
    engine.setProperty('voice', voices[0].id)
     
    # Method for the speaking of the assistant
    engine.say(audio) 
     
    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()
 
 
class Jarvis:
    def __init__(self) -> None:
        if platform == "linux" or platform == "linux2":
            self.chrome_path = '/usr/bin/google-chrome'

        elif platform == "darwin":
            self.chrome_path = 'open -a /Applications/Google\ Chrome.app'

        elif platform == "win32":
            self.chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        else:
            print('Unsupported OS')
            exit(1)
        webbrowser.register(
            'chrome', None, webbrowser.BackgroundBrowser(self.chrome_path)
        )

    def wishMe(self) -> None:
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning SIR")
        elif hour >= 12 and hour < 18:
            speak("Good Afternoon SIR")

        else:
            speak('Good Evening SIR')

        weather()
        speak('I am JARVIS. Please tell me how can I help you SIR?')

    def execute_query(self, query):
        print(query)
        if 'Optical Text Recognition' or 'Text Recognition' in query:
            pass
        if 'jarvis are you there' in query:
            print()
            speak("Yes Sir, at your service")
        if 'jarvis who made you' in query:
            speak("Yes Sir, my master build me in AI")

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif 'open youtube' in query:

            webbrowser.get('chrome').open_new_tab('https://youtube.com')

        elif 'open amazon' in query:
            webbrowser.get('chrome').open_new_tab('https://amazon.com')

        elif 'open google' in query:
            webbrowser.get('chrome').open_new_tab('https://google.com')

        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open_new_tab('https://stackoverflow.com')

        elif 'play music' in query:
            os.startfile("D:\\RoiNa.mp3")

        elif 'search youtube' in query:
            speak('What you want to search on Youtube?')
            youtube(takeCommand())
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir, the time is {strTime}')

        elif 'search' in query:
            speak('What do you want to search for?')
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.get('chrome').open_new_tab(
                url)
            speak('Here is What I found for' + search)

        elif 'location' in query:
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Here is the location ' + location)

        elif 'your master' in query:
            if platform == "win32" or "darwin":
                speak('I have a team who created me. They created me a couple of days ago')
            elif platform == "linux" or platform == "linux2":
                name = getpass.getuser()
                speak(name, 'is my master. He is running me right now')

        elif 'your name' in query:
            speak('My name is JARVIS')
        elif 'who made you' in query:
            speak('I was created by my AI master in 2022')

        elif 'stands for' in query:
            speak('J.A.R.V.I.S stands for JUST A RATHER VERY INTELLIGENT SYSTEM')
        elif 'open code' in query:
            if platform == "win32":
                os.startfile(
                    "C:\\Users\\gs935\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('code .')

        elif 'shutdown' in query:
            if platform == "win32":
                os.system('shutdown /p /f')
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('poweroff')

        elif 'cpu' in query:
            cpu()
        elif 'your friend' in query:
            speak('My friends are Google assistant alexa and siri')

        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif 'github' in query:
            webbrowser.get('chrome').open_new_tab(
                'https://github.com/gauravsingh9356')

        elif 'remember that' in query:
            speak("what should i remember sir")
            rememberMessage = takeCommand()
            speak("you said me to remember"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'sleep' in query:
            sys.exit()

        elif 'dictionary' in query:
            speak('What you want to search in your intelligent dictionary?')
            translate(takeCommand())
        # elif 'voice' in query:
        #     print('Query: ' + query)
        #     if 'female' in query:
        #         engine.setProperty('voice', voices[1].id)
        #     else:
        #         engine.setProperty('voice', voices[2].id)
        #     speak("Hello Sir, I have switched my voice. How is it?")

        elif 'convert currency' in query:
            speak("What's the value you want to convert?")
            value = takeCommand()
            speak("What's the actual currency?")
            currency = takeCommand()
            speak("What's the currency you want to convert?")
            converter = takeCommand()
            currency_converter(value, currency, converter)


if __name__ == '__main__':
     
    # main method for executing
    # the functions
    bot_ = Jarvis()
    bot_.wishMe()
    while True:
        query = takeCommand().lower()
        bot_.execute_query(query)