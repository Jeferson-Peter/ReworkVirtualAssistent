import pywhatkit as kit
from helpers import speak


class PlayThings:
    def __init__(self, query: str):
        self.query = query.lower()
        self.parse_commands()

    def parse_commands(self):
        if 'youtube' in self.query:
            self.play_youtube()

    def play_youtube(self):
        video = self.query.split(' ')
        try:
            index_yt = video.index('youtube')
            index_yt += 1
            video = ' '.join(map(str, video[index_yt:]))
        except ValueError:
            pass
        kit.playonyt(self.query)
        speak(f'Playing on YouTube {video}')
