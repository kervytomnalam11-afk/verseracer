[app]

# Title of your application
title = VerseRacer

# Package name (must be unique, no spaces)
package.name = verseracer

# Package domain (reverse DNS style)
package.domain = com.kervynalam

# Source directory (relative to this file)
source.dir = .

# Source files to include
source.include_exts = py,png,jpg,wav,ogg,mp3,json,kv,ttf
source.include_patterns = assets/*,assets/*.wav,assets/*.mp3,assets/*.ogg

# Application version
version = 1.0.0

# Python requirements
requirements = python3,kivy==2.3.0

# Orientation
orientation = portrait

# Android-specific
# READ/WRITE_EXTERNAL_STORAGE: needed for leaderboard.json on older Android
# MODIFY_AUDIO_SETTINGS + READ/WRITE access for audio playback
android.permissions = INTERNET, MODIFY_AUDIO_SETTINGS, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

# Keep screen on during race
android.wakelock = True

# Soft keyboard behaviour — IMPORTANT for layout fix:
# adjustResize causes the window to shrink when the soft keyboard appears,
# so layout.height = Window.height always gives the usable area above the keyboard.
android.manifest.intent_filters =
android.add_activities =

# Icon and presplash (place files in assets/)
#icon.filename = %(source.dir)s/assets/icon.png
#presplash.filename = %(source.dir)s/assets/presplash.png

# Fullscreen
fullscreen = 0

# Log level (0=error, 1=info, 2=debug)
log_level = 1

[buildozer]

# Buildozer working directory
build_dir = ./.buildozer

# Binaries directory
bin_dir = ./bin

# Warn on remote package fetching
warn_on_root = 0
