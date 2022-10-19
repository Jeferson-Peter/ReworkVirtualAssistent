import os

from googletrans import Translator
from googletrans.constants import LANGUAGES
from gtts import gTTS
from playsound import playsound

from helpers import speak, takeCommand



class Translate:
    def __init__(self, query: str):
        self.query = query.lower()
        self.translator = Translator()
        self._translate()

    def _parse_dest_lang(self, dest_lang):
        if dest_lang not in LANGUAGES.values():
            return None
        else:
            result = dict((new_val, new_k) for new_k, new_val in LANGUAGES.items()).get(dest_lang)
            return result


    def _translate(self):
        if 'translate' in self.query:
            phrase_list = self.query.split(' ')
            index_translate = phrase_list.index('translate')
            phrase_to_translate = ' '.join(map(str, phrase_list[index_translate+1:]))
            speak("which language do you want to translate?")
            dest_language = takeCommand().lower()
            min_dest_language = self._parse_dest_lang(dest_language)
            while min_dest_language is None:
                dest_language = takeCommand().lower()
                min_dest_language = self._parse_dest_lang(dest_language)
            if min_dest_language is not None:
                try:
                    translated = self.translator.translate(phrase_to_translate, dest=min_dest_language).text
                    speak(f"You asked me to translate the following phrase {phrase_to_translate}")
                    # speak(f"The phrase translate to {dest_language} is {translated}")
                    translated_speak = gTTS(text=translated, lang=min_dest_language, slow=False)

                    # speech in capture_voice.mp3
                    translated_speak.save("captured_voice.mp3")

                    # Using OS module to run the translated voice.
                    playsound(f"captured_voice.mp3")
                    os.remove('captured_voice.mp3')
                except:
                    speak("Could not translate, Internal error")
