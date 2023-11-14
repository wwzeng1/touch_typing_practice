import datetime
from typing import Dict

class Session:
    def __init__(self, text: str):
        self.text = text
        self.start_time = None
        self.end_time = None
        self.typed_text = ""

    def start(self):
        self.start_time = datetime.datetime.now()

    def end(self, typed_text: str):
        self.end_time = datetime.datetime.now()
        self.typed_text = typed_text

    def calculate_statistics(self) -> Dict:
        time_taken = (self.end_time - self.start_time).total_seconds()
        characters_typed = len(self.typed_text)
        words_typed = len(self.typed_text.split())
        speed = words_typed / (time_taken / 60)  # Words per minute
        accuracy = sum(t == o for t, o in zip(self.typed_text, self.text)) / len(self.text) * 100  # percentage

        return {
            'start_time': self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            'end_time': self.end_time.strftime("%Y-%m-%d %H:%M:%S"),
            'time_taken': time_taken,
            'characters_typed': characters_typed,
            'words_typed': words_typed,
            'speed': speed,
            'accuracy': accuracy
        }
