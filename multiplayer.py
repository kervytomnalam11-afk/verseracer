"""
VerseRacer - Local Multiplayer System
Made by KERVY NALAM
"""

class PlayerSession:
    def __init__(self, name, color, player_id):
        self.name = name
        self.color = color
        self.player_id = player_id
        self.chars_typed = 0
        self.correct_chars = 0
        self.total_chars_attempted = 0
        self.verses_completed = 0
        self.current_input = ""
        self.finished = False
        self.finish_time = 0
        self.place = 0
        self.start_time = 0
        self.wants_to_quit = False

    def get_wpm(self, current_time):
        elapsed = current_time - self.start_time if self.start_time else 1
        if elapsed < 1:
            elapsed = 1
        return (self.chars_typed / 5.0) / (elapsed / 60.0)

    def get_accuracy(self):
        if self.total_chars_attempted == 0:
            return 100.0
        return (self.correct_chars / self.total_chars_attempted) * 100.0

    def reset(self):
        self.chars_typed = 0
        self.correct_chars = 0
        self.total_chars_attempted = 0
        self.verses_completed = 0
        self.current_input = ""
        self.finished = False
        self.finish_time = 0
        self.place = 0
        self.wants_to_quit = False


PLAYER_COLORS = [
    (0.2, 0.7, 0.3, 1),   # Green
    (0.9, 0.3, 0.2, 1),   # Red
    (0.2, 0.5, 0.9, 1),   # Blue
    (0.9, 0.8, 0.1, 1),   # Yellow
]

COLOR_NAMES = ["Green", "Red", "Blue", "Yellow"]
