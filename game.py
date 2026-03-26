"""
VerseRacer - Core Game Logic
Made by KERVY NALAM
"""

import time
from verses import get_verses, get_random_verse, get_hard_verse

class GameState:
    MODES = ["classic", "time_attack", "accuracy", "hard", "endless", "vs_ai", "multiplayer"]
    
    def __init__(self, mode="classic"):
        self.mode = mode
        self.verses = []
        self.current_verse_index = 0
        self.current_verse = ""
        self.typed_text = ""
        self.correct_count = 0
        self.error_count = 0
        self.total_chars_attempted = 0
        self.start_time = 0
        self.elapsed_time = 0
        self.is_running = False
        self.is_finished = False
        self.total_distance = 0
        self.car_position = 0  # 0.0 to 1.0
        self.verses_completed = 0
        
        # Time attack
        self.time_limit = 60
        
        # Accuracy mode
        self.min_accuracy = 85.0
        
        # Hard mode
        self.hard_min_accuracy = 90.0
        self.backspace_allowed = True
        
    def setup(self):
        if self.mode == "hard":
            self.verses = get_verses("hard", 5)
            self.backspace_allowed = False
        elif self.mode in ("classic", "vs_ai", "multiplayer"):
            self.verses = get_verses("classic", 5)
        elif self.mode in ("time_attack", "accuracy", "endless"):
            self.verses = [get_random_verse()]
        
        self.current_verse_index = 0
        self.current_verse = self.verses[0] if self.verses else ""
        self.typed_text = ""
        self.correct_count = 0
        self.error_count = 0
        self.total_chars_attempted = 0
        self.start_time = time.time()
        self.elapsed_time = 0
        self.is_running = True
        self.is_finished = False
        self.total_distance = 0
        self.car_position = 0
        self.verses_completed = 0

    def on_text_change(self, text):
        if not self.is_running or self.is_finished:
            return
        
        if not self.backspace_allowed and len(text) < len(self.typed_text):
            return self.typed_text  # reject backspace
        
        self.typed_text = text
        self.total_chars_attempted = max(self.total_chars_attempted, len(text))
        
        # Count correct
        correct = 0
        for i, ch in enumerate(text):
            if i < len(self.current_verse) and ch == self.current_verse[i]:
                correct += 1
        self.correct_count = correct
        self.error_count = len(text) - correct
        
        # Update car position for current verse
        if len(self.current_verse) > 0:
            self.car_position = min(1.0, len(text) / len(self.current_verse))
        
        # Check verse completion
        if text == self.current_verse:
            self._complete_verse()
        
        # Check accuracy mode fail
        if self.mode == "accuracy" and self.get_accuracy() < self.min_accuracy and self.total_chars_attempted > 10:
            self.finish()
        
        if self.mode == "hard" and self.get_accuracy() < self.hard_min_accuracy and self.total_chars_attempted > 10:
            self.finish()
        
        return self.typed_text

    def _complete_verse(self):
        self.total_distance += len(self.current_verse)
        self.verses_completed += 1

        if self.mode in ("classic", "hard", "vs_ai", "multiplayer"):
            self.current_verse_index += 1
            if self.current_verse_index >= len(self.verses):
                self.finish()
                return
            self.current_verse = self.verses[self.current_verse_index]
        elif self.mode in ("time_attack", "accuracy", "endless"):
            # Endless/time-attack always get a fresh random verse
            new_verse = get_random_verse()
            self.verses.append(new_verse)
            self.current_verse_index += 1
            self.current_verse = new_verse

        self.typed_text = ""
        self.correct_count = 0
        self.error_count = 0
        self.total_chars_attempted = 0
        self.car_position = 0

    def update(self, dt):
        if not self.is_running or self.is_finished:
            return
        self.elapsed_time = time.time() - self.start_time
        
        if self.mode == "time_attack" and self.elapsed_time >= self.time_limit:
            self.finish()

    def get_wpm(self):
        if self.elapsed_time < 1:
            return 0
        total_chars = self.total_distance + len(self.typed_text)
        return (total_chars / 5.0) / (self.elapsed_time / 60.0)

    def get_accuracy(self):
        attempted = self.total_chars_attempted
        if attempted == 0:
            return 100.0
        return (self.correct_count / attempted) * 100.0

    def get_overall_accuracy(self):
        total = self.total_distance + self.total_chars_attempted
        if total == 0:
            return 100.0
        correct_total = self.total_distance + self.correct_count
        return (correct_total / total) * 100.0

    def finish(self):
        self.is_running = False
        self.is_finished = True
        self.elapsed_time = time.time() - self.start_time

    def get_char_statuses(self):
        """Return list of (char, status) for display. status: 'correct', 'wrong', 'pending'"""
        result = []
        for i, ch in enumerate(self.current_verse):
            if i < len(self.typed_text):
                if self.typed_text[i] == ch:
                    result.append((ch, "correct"))
                else:
                    result.append((ch, "wrong"))
            else:
                result.append((ch, "pending"))
        return result
