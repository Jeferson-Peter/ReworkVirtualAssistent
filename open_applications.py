import webbrowser
from helpers import speak
import os

class OpenApplications:
    __os_init_apps = {
        'excel': 'excel',
        'word': 'winword',
        'notepad': 'notepad',
        'arquivos': 'explorer',
        'paint': 'mspaint',
        'gedit': 'gedit',
        'gimp': 'gimp',
        # 'discord': 'discord',
    }
    def __init__(self, query:str):
        self.query = query
        self.__query_list = self.query.split(' ')
        self.intersection = set(self.__os_init_apps)\
            .intersection(self.__query_list)

    def parse_commands(self):
        if 'youtube' in self.query:
            self.__youtube()
        elif 'google' in self.query:
            self.__google()
        elif 'amazon' in self.query:
            self.__amazon()
        elif 'stackoverflow' in self.query:
            self.__stackoverflow()
        elif 'linkedin' in self.query:
            self.__linkedin()
        elif 'github' in self.query:
            self.__github()
        elif 'twitter' in self.query:
            self.__twitter()
        elif len(self.intersection) > 0:
            app = list(self.intersection)[0]
            self.__exe_os_app(self.__os_init_apps[app])

    @staticmethod
    def __youtube():
        speak('Opening YouTube')
        webbrowser.open('http://www.youtube.com/')

    @staticmethod
    def __google():
        speak('Opening Google')
        webbrowser.open('http://www.google.com/')

    @staticmethod
    def __amazon():
        speak('Opening Amazon')
        webbrowser.open('http://www.amazon.com/')

    @staticmethod
    def __stackoverflow():
        speak('Opening StackOverflow')
        webbrowser.open('https://stackoverflow.com/')

    @staticmethod
    def __linkedin():
        speak('Opening  LinkedIn')
        webbrowser.open("https://www.linkedin.com/")

    @staticmethod
    def __github():
        speak('Opening GitHub')
        webbrowser.open('https://github.com/')

    @staticmethod
    def __twitter():
        speak('Opening Twitter')
        webbrowser.open('https://twitter.com/')

    @staticmethod
    def __exe_os_app(app: str):
        os.system(f'start {app}')
