"""
VerseRacer - Leaderboard System
Made by KERVY NALAM
"""

import json
import os
from datetime import datetime

LEADERBOARD_FILE = "leaderboard.json"

def _get_path():
    """Return a writable path for the leaderboard file on all platforms."""
    try:
        from kivy.app import App
        app = App.get_running_app()
        if app and hasattr(app, 'user_data_dir'):
            return os.path.join(app.user_data_dir, "leaderboard.json")
    except Exception:
        pass
    return LEADERBOARD_FILE

def _load():
    path = _get_path()
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return []
    return []

def _save(data):
    path = _get_path()
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
    except OSError:
        pass

def add_entry(name, score, wpm, accuracy, mode):
    data = _load()
    data.append({
        "name": name,
        "score": round(score),
        "wpm": round(wpm, 1),
        "accuracy": round(accuracy, 1),
        "mode": mode,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })
    _save(data)

def get_top(mode=None, limit=10):
    data = _load()
    if mode:
        data = [e for e in data if e.get("mode") == mode]
    data.sort(key=lambda x: x.get("score", 0), reverse=True)
    return data[:limit]

def calculate_score(wpm, accuracy, time_seconds):
    acc_factor = (accuracy / 100.0) ** 2
    speed_factor = wpm
    time_bonus = max(0, 300 - time_seconds) / 10
    return max(0, (speed_factor * acc_factor * 10) + time_bonus)
