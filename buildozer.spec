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
source.include_exts = py,png,jpg,jpeg,wav,ogg,mp3,json,kv,ttf

# FIX 1: Explicitly include the assets folder — the old assets/* was unreliable
source.include_patterns = assets/

# Application version
version = 1.0.0

# FIX 2: Added sdl2_mixer — this is what powers audio on Android with Kivy.
# Without it, SoundLoader builds fine but produces silence on device.
requirements = python3,kivy==2.3.0,sdl2,sdl2_ttf,sdl2_mixer,sdl2_image

# Orientation
orientation = portrait

# Android-specific
android.permissions = INTERNET, MODIFY_AUDIO_SETTINGS
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

# Icon and presplash (uncomment and set path if you have these files)
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
