"""
VerseRacer - Main Entry Point
A typing racing game by KERVY NALAM

Type song lyrics, poem verses, or Bible verses to race your car!
"""

from kivy.app import App
from kivy.core.window import Window
from kivy.utils import platform

# Set a mobile-like window size for desktop testing only
if platform not in ('android', 'ios'):
    Window.size = (400, 750)

from ui import build_app


class VerseRacerApp(App):
    title = "VerseRacer"
    player_name = ""

    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.18, 1)
        return build_app()


if __name__ == "__main__":
    VerseRacerApp().run()
