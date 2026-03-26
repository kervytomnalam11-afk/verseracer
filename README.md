# 🏎️ VerseRacer
**Made by KERVY NALAM**

A mobile typing racing game built with Python + Kivy.  
Type song lyrics, poem verses, and Bible verses to race your car — the faster and more accurately you type, the faster you go!

---

## 🎮 Game Modes

| Mode            | Description |
|-----------------|-------------|
| 🏁 Classic       | Type 5 verses. First to finish wins. |
| ⏱️ Time Attack   | Type as many verses as possible in 60 seconds. |
| 🎯 Accuracy      | Type forever — but drop below 85% accuracy and you're out. |
| 💀 Hard          | Longer verses, no backspace, must maintain 90% accuracy. |
| ♾️ Endless        | Never ends — tap **End Race** when you want to stop. |
| 🤖 VS AI         | Race against 1–3 AI opponents at 4 difficulty levels. |
| 👥 Multiplayer   | 2–4 players on one device, split-screen. |

---

## 🤖 AI Difficulties

| Level    | ~WPM | Accuracy | Behaviour |
|----------|------|----------|-----------|
| Rookie   | 25   | 85%      | Frequent slowdowns and typos |
| Amateur  | 45   | 92%      | Moderate consistency |
| Pro      | 70   | 97%      | Rarely slows down |
| Legend   | 100  | 99%      | Adapts to player — speeds up if you lead |

---

## 👥 Local Multiplayer (2–4 players)

- **2 players** → stacked split-screen (top / bottom)
- **3–4 players** → 2×2 grid, each player gets their own panel
- All players see their own car, verse, live WPM and accuracy
- Each player taps their own text field to type
- In **Endless** mode each player has their own "End" button
- Podium results screen with 🥇🥈🥉 medals

---

## 📦 Project Structure

```
verseracer/
├── main.py           Entry point — runs the Kivy app
├── ui.py             All screens, widgets, countdown overlay
├── game.py           Core typing/race logic (GameState)
├── ai.py             AI opponent simulation
├── multiplayer.py    PlayerSession + colour constants
├── leaderboard.py    JSON leaderboard + score formula
├── sounds.py         SoundManager (graceful if no audio files)
├── verses.py         100+ verses across Bible / poems / songs
├── requirements.txt  Python dependencies
├── buildozer.spec    Android APK build config
└── assets/           (optional) .wav sound files
```

---

## 🖥️ Running on Desktop (for testing)

### 1. Install dependencies
```bash
pip install kivy==2.3.0
```

### 2. Run
```bash
python main.py
```

---

## 📱 Building the Android APK

### Prerequisites (Linux recommended — Ubuntu 20.04+)
```bash
# Install system dependencies
sudo apt update
sudo apt install -y python3-pip build-essential git \
    libssl-dev libffi-dev python3-dev \
    zlib1g-dev libncurses5-dev libbz2-dev \
    openjdk-17-jdk autoconf libtool

# Install buildozer
pip install buildozer cython

# Android SDK tools (buildozer downloads these automatically)
```

### Build APK
```bash
cd verseracer/

# First build (downloads Android SDK/NDK — takes 10–30 min)
buildozer android debug

# Your APK will be in:
#   bin/verseracer-1.0.0-debug.apk
```

### Install to device
```bash
# Via USB (with USB debugging enabled)
buildozer android deploy run

# Or copy the APK manually to your phone and open it
```

---

## 🔊 Sound Files (optional)

Place these `.wav` files in the `assets/` folder for full audio:

| File               | Plays when…             |
|--------------------|-------------------------|
| `engine_rev.wav`   | Race starts             |
| `key_tap.wav`      | Each keystroke          |
| `fanfare.wav`      | Race finishes           |
| `error.wav`        | Wrong key               |
| `countdown_beep.wav` | 3-2-1 countdown      |
| `go_beep.wav`      | GO!                     |
| `race_music.wav`   | Background loop         |

The game runs fine without them — it silently skips missing audio files.

---

## 🏆 Leaderboard

- Stored locally in `leaderboard.json`
- Tracks: Name, Score, WPM, Accuracy, Mode, Date
- Filterable by game mode
- Score formula: `(WPM × accuracy² × 10) + time_bonus`
  - Low accuracy = heavy score penalty
  - Finishing faster gives a bonus (up to +30)

---

## 📝 Notes

- The countdown overlay (3-2-1-GO) appears before every race and does **not** count toward your time.
- Hard mode disables the backspace key.
- In VS AI mode the AI position is shown on the shared race track above your car.
- Multiplayer saves a leaderboard entry for **every** human player after the race.
