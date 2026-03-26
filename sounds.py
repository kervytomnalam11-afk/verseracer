"""
VerseRacer - Sound Manager
Made by KERVY NALAM
"""

import os

try:
    from kivy.core.audio import SoundLoader
    AUDIO_AVAILABLE = True
except Exception:
    AUDIO_AVAILABLE = False

ASSET_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

class SoundManager:
    def __init__(self):
        self.sounds = {}
        self.music = None
        self.enabled = True
        self._load()

    def _load(self):
        if not AUDIO_AVAILABLE:
            return
        files = {
            "engine_rev": "engine_rev.wav",
            "key_tap": "key_tap.wav",
            "fanfare": "fanfare.wav",
            "error": "error.wav",
            "countdown": "countdown_beep.wav",
            "go": "go_beep.wav",
        }
        for key, fn in files.items():
            path = os.path.join(ASSET_DIR, fn)
            if os.path.exists(path):
                self.sounds[key] = SoundLoader.load(path)

        music_path = os.path.join(ASSET_DIR, "race_music.wav")
        if os.path.exists(music_path):
            self.music = SoundLoader.load(music_path)
            if self.music:
                self.music.loop = True
                self.music.volume = 0.4

    def play(self, name):
        if not self.enabled:
            return
        snd = self.sounds.get(name)
        if snd:
            snd.play()

    def start_music(self):
        if self.enabled and self.music:
            self.music.play()

    def stop_music(self):
        if self.music:
            self.music.stop()

    def toggle(self):
        self.enabled = not self.enabled
        if not self.enabled:
            self.stop_music()


# Global instance
sfx = SoundManager()
