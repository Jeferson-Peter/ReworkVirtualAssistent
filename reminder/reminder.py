import os
from helpers import takeCommand, speak

ALL_MONTHS = ('january', 'february', 'april', 'may', 'june',
              'july', 'august', 'september', 'october', 'november', 'december')

SHORT_TASKS = {
    'tomorrow': 1,
    'in a week': 7,
    'in a month': 30,
}

class Reminder:
    def __init__(self, query: str):
        self.query = query
        self.create_directories()

    @staticmethod
    def create_directories() -> None:
        reminder_dir = os.path.abspath(r'')
        data_dir = os.path.join(reminder_dir, 'data')
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

    def parse_reminder(self):
        if 'reminder' in self.query or \
                'remember me' in self.query:
            pass

    def get_reminder_content(self):
        splitted_query = self.query.split(' ')
        if 'reminder' in self.query:
            phrase_identifier = 'reminder'
        elif 'remember me' in self.query:
            phrase_identifier = 'remember me'
        index_identifier = splitted_query.index(phrase_identifier)
        reminder_content = ' '.join(map(str, splitted_query[index_identifier + 1:]))
        return reminder_content

    def create_reminder(self):
        reminder_content = self.get_reminder_content()
        speak("Confirm your reminder content is correct.")
        speak(reminder_content)
        yes_or_no = takeCommand()
        if 'yes' in yes_or_no:
            pass
        elif 'no' in yes_or_no:
            reminder_content = takeCommand()
            reminder_content = self.get_reminder_content()
            pass

    def get_reminder_date(self):
        speak("What Date do you want to set the reminder")
        query = takeCommand()
        splitted_date = query.split(' ')



# October 24th 2012


if __name__ == '__main__':
    print(os.path.abspath(r''))
