from helpers import speak
from helpers import takeCommand
import webbrowser
import urllib.parse


class SearchThings:
    def __init__(self, query:str):
        self.query = query.lower()
        self.search = ('google', 'youtube',)
        self.check_possibilities()

    def check_possibilities(self):
        query_res = self.query.split(' ')
        result = list(set(query_res).intersection(self.search))
        if len(result) <= 0:
            speak('What do you want to search for?')
            self.query = takeCommand().lower()
        # if self.query not in self.search:
        if 'youtube' in self.query: self.youtube()
        if 'google' in self.query: self.google()

    @staticmethod
    def google():
        speak('What you want to search on Google?')
        search = takeCommand()
        url = 'https://google.com/search?q=' + search
        webbrowser.open_new_tab(url)
        speak('Here is What I found for' + search)

    @staticmethod
    def youtube():
        speak('What you want to search on Youtube?')
        search = takeCommand()
        query = urllib.parse.quote(search)
        url = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open_new_tab(url)
