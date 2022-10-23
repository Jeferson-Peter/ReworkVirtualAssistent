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
from sys import platform
import os
from open_applications import OpenApplications
from reminder.reminder import Reminder
from search import SearchThings
from _play import PlayThings
from translate import Translate
## Defined English as Standard language
## todo: 
## pesquisa por voz - ok
## previsao do tempo (cidade/uf) - ok
## cotação de moedas (brl/usd) -ongoing
## lembretes -ok
## tradução - ok
## abrir programas (vscode/office/chrome/explorer) -ok
## 
## recursos:
## nlp (natural language processor)
## ibm watson/ google cloud
## speech to text

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 120)
# engine.setProperty('voice', voices[0].id)
 
# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing
# def takeCommand(): 
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         query = ""
#         while True:
#             print('Listening...')
#             r.pause_threshold = 0.7
#             audio = r.listen(source)
            
#             try:
#                 print("Recognizing")
                
#                 query = r.recognize_google(audio, language='en-US')
#                 print("the command is printed=", query)
                
#             except Exception as e:
#                 print(e)
#                 print("Say that again sir")
            
#             if query != "":
#                 break
            
#         return query

def speak(audio):
     
    # engine = pyttsx3.init()
    # getter method(gets the current value
    # of engine property)
    # voices = engine.getProperty('voices')
     
    # setter method .[0]=male voice and
    # [1]=female voice in set Property.
    # engine.setProperty('voice', voices[0].id)
     
    # Method for the speaking of the assistant
    engine.say(audio) 
     
    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()

def defineLanguage():
    changeVoice()

def changeVoice():
    for voice in voices:
        if voice.id.find('EN-US') >= 0:
            engine.setProperty('voice', voice.id)
            break

def changeVoiceByGender():
    actualVoice = engine.getProperty('voice')
    for voice in voices:
        if voice.id.find('EN-US') >= 0 and actualVoice != voice.id:
            engine.setProperty('voice', voice.id)
            break
 
class Jarvis:


    def __init__(self) -> None:
        if platform == "linux" or platform == "linux2":
            self.chrome_path = '/usr/bin/google-chrome'

        elif platform == "darwin":
            self.chrome_path = 'open -a /Applications/Google\ Chrome.app'

        elif platform == "win32":
            self.chrome_path = 'C:\Program Files (x86)\Google\ChromeDriver\chromedriver.exe'
        else:
            print('Unsupported OS')
            exit(1)
        webbrowser.register(
            'chrome', None, webbrowser.BackgroundBrowser(self.chrome_path)
        )

    @staticmethod
    def innitialize():
        playsound('Jarvis - Welcome Back Sir.mp3')

    def wishMe(self) -> None:
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            speak("Good Morning SIR")
        elif 12 <= hour < 18:
            speak("Good Afternoon SIR")

        else:
            speak('Good Evening SIR')

        weather()
        speak('I am JARVIS. Please tell me how can I help you SIR?')


    def execute_query(self, query):
        if 'Optical Text Recognition' or 'Text Recognition' in query:
            pass
        if 'jarvis are you there' in query:
            speak("Yes Sir, at your service")
        if 'jarvis who made you' in query:
            speak("Yes Sir, my master build me in AI")
        elif 'open' in query:
            application = OpenApplications(query)
            application.parse_commands()
        elif 'search' in query:
            SearchThings(query)
        elif 'play' in query:
            PlayThings(query)
        elif 'translate' in query:
            Translate(query)
        elif 'reminder' in query or \
                'remember me' in query:
            speak("Feature Under development")
            # Reminder(query)
            # pass
        elif 'what time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir, the time is {strTime}')
        elif 'location' in query:
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Here is the location ' + location)
        elif 'your master' in query:
                speak('I have a team who created me a couple of days ago')
        elif 'your name' in query:
            speak('My name is JARVIS')
        elif 'who made you' in query:
            speak("I was created by my AI masters in 2022, I can not say you whom they are but the tip is"
                  "one of them is the chief of illuminati's organization ")
        elif 'stands for' in query:
            speak('J.A.R.V.I.S stands for JUST A RATHER VERY INTELLIGENT SYSTEM')
        elif 'you have a sister' in query:
            speak("Yes, My sister's name is EDITH, she was created by my AI masters in 2022 too, "
                  "however She is focused on tactical tasks, such as reconnaissance of enemy territories."
                  "She stands for Even Death, I'm the hero. ")
        elif 'shutdown' in query:
            if platform == "win32":
                os.system('shutdown /p /f')
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('poweroff')
        elif 'your friend' in query:
            speak('My friends are Google assistant alexa and siri')
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            joke()
        elif 'screenshot' in query:
            screenshot()
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
        elif 'voice' in query:
            changeVoiceByGender()
            speak("Hello Sir, I have switched my voice. How is it?")
        elif 'convert currency' in query:
            currency_converter()


if __name__ == '__main__':
    from playsound import playsound
    # main method for executing
    # the functions
    bot_ = Jarvis()
    defineLanguage()
    bot_.innitialize()
    bot_.wishMe()
    while True:
        query = takeCommand()
        bot_.execute_query(query)