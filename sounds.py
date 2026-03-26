"""
VerseRacer - Sound Manager
Made by KERVY NALAM

FIX: Removed crash-prone android.storage import.
     Uses app.directory for reliable asset path on all platforms.
"""

import os
from kivy.utils import platform

try:
    from kivy.core.audio import SoundLoader
    AUDIO_AVAILABLE = True
except Exception:
    AUDIO_AVAILABLE = False


def _get_asset_dir():
    """Return the correct assets directory for desktop and Android."""
    # First try: use the running app's directory (works on Android)
    try:
        from kivy.app import App
        app = App.get_running_app()
        if app and hasattr(app, 'directory') and app.directory:
            path = os.path.join(app.directory, 'assets')
            if os.path.isdir(path):
                return path
    except Exception:
        pass

    # Second try: relative to this file (works on desktop)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')


class SoundManager:
    def __init__(self):
        self.sounds  = {}
        self.music   = None
        self.enabled = True
        self._loaded = False

    def _ensure_loaded(self):
        """Lazy load — called the first time a sound is actually needed,
        so that App.get_running_app() is available."""
        if self._loaded:
            return
        self._loaded = True
        if not AUDIO_AVAILABLE:
            return

        asset_dir = _get_asset_dir()

        files = {
            "engine_rev": "engine_rev.wav",
            "key_tap":    "key_tap.wav",
            "fanfare":    "fanfare.wav",
            "error":      "error.wav",
            "countdown":  "countdown_beep.wav",
            "go":         "go_beep.wav",
        }
        for key, fn in files.items():
            path = os.path.join(asset_dir, fn)
            if os.path.exists(path):
                snd = SoundLoader.load(path)
                if snd:
                    self.sounds[key] = snd

        music_path = os.path.join(asset_dir, 'race_music.wav')
        if os.path.exists(music_path):
            self.music = SoundLoader.load(music_path)
            if self.music:
                self.music.loop   = True
                self.music.volume = 0.4

    def play(self, name):
        if not self.enabled:
            return
        self._ensure_loaded()
        snd = self.sounds.get(name)
        if snd:
            try:
                snd.play()
            except Exception:
                pass

    def start_music(self):
        self._ensure_loaded()
        if self.enabled and self.music:
            try:
                self.music.play()
            except Exception:
                pass

    def stop_music(self):
        self._ensure_loaded()
        if self.music:
            try:
                self.music.stop()
            except Exception:
                pass

    def toggle(self):
        self.enabled = not self.enabled
        if not self.enabled:
            self.stop_music()


# Global instance
sfx = SoundManager()
