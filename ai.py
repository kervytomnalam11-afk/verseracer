"""
VerseRacer - AI Opponent System
Made by KERVY NALAM
"""

import random
import time

AI_PROFILES = {
    "rookie": {"name": "ByteBot", "wpm": 25, "accuracy": 0.85, "color": (0.8, 0.2, 0.2, 1), "variance": 8},
    "amateur": {"name": "VerseViper", "wpm": 45, "accuracy": 0.92, "color": (0.2, 0.6, 0.8, 1), "variance": 5},
    "pro": {"name": "KeyKing", "wpm": 70, "accuracy": 0.97, "color": (0.9, 0.6, 0.1, 1), "variance": 3},
    "legend": {"name": "TypeTitan", "wpm": 100, "accuracy": 0.99, "color": (0.6, 0.1, 0.8, 1), "variance": 2},
}

class AIOpponent:
    def __init__(self, difficulty="rookie"):
        profile = AI_PROFILES.get(difficulty, AI_PROFILES["rookie"])
        self.name = profile["name"]
        self.base_wpm = profile["wpm"]
        self.accuracy = profile["accuracy"]
        self.color = profile["color"]
        self.variance = profile["variance"]
        self.difficulty = difficulty

        self.chars_typed = 0
        self.total_chars = 0
        self.errors = 0
        self.current_verse_len = 0
        self.verse_progress = 0
        self.verses_completed = 0
        self.finished = False
        self.finish_time = 0
        self.start_time = 0
        self._accumulated = 0.0

    def start_race(self, verse_len):
        self.start_time = time.time()
        self.current_verse_len = verse_len
        self.verse_progress = 0
        self.chars_typed = 0
        self.total_chars = 0
        self.errors = 0
        self.finished = False
        self._accumulated = 0.0

    def set_verse(self, verse_len):
        self.current_verse_len = verse_len
        self.verse_progress = 0

    def update(self, dt, player_progress=0):
        if self.finished:
            return
        current_wpm = self.base_wpm + random.uniform(-self.variance, self.variance)
        if self.difficulty == "legend":
            if player_progress > self.get_progress():
                current_wpm *= 1.15
            elif player_progress < self.get_progress() - 0.2:
                current_wpm *= 0.9
        
        chars_per_sec = (current_wpm * 5) / 60.0
        new_chars = chars_per_sec * dt
        
        if random.random() > self.accuracy:
            self.errors += 1
            new_chars *= 0.7

        self._accumulated += new_chars
        actual_new = int(self._accumulated)
        if actual_new > 0:
            self._accumulated -= actual_new
            self.verse_progress += actual_new
            self.chars_typed += actual_new
            self.total_chars += actual_new

    def is_verse_done(self):
        return self.verse_progress >= self.current_verse_len

    def finish_verse(self):
        self.verses_completed += 1
        self.verse_progress = 0

    def get_progress(self):
        if self.current_verse_len == 0:
            return 0
        return min(1.0, self.verse_progress / self.current_verse_len)

    def get_wpm(self):
        elapsed = time.time() - self.start_time if self.start_time else 1
        if elapsed < 1:
            elapsed = 1
        return (self.chars_typed / 5.0) / (elapsed / 60.0)

    def get_accuracy(self):
        total = self.chars_typed + self.errors
        if total == 0:
            return 100.0
        return (self.chars_typed / total) * 100.0

    def mark_finished(self):
        self.finished = True
        self.finish_time = time.time() - self.start_time
