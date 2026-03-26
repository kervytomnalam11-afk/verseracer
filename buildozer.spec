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
# All relevant extensions — py, kivy, images, audio, fonts, data
source.include_exts = py,png,jpg,jpeg,gif,wav,ogg,mp3,json,kv,ttf,otf,atlas,xml

# FIX 1: Use ** to recursively include ALL subfolders inside assets/
# Without **, only the top-level assets/ files are bundled — subfolders are skipped.
source.include_patterns = assets/**,assets/**/*

# Application version
version = 1.0.0

# FIX 2: Add kivy_deps and kivy_garden for audio/video support.
# kivy==2.3.0 needs sdl2, sdl2_mixer for sound to work on Android.
# Also add kivy_deps.sdl2 if you use Kivy's SoundLoader.
# ── ADD any extra libraries your game uses after the comma, e.g.:
#    ...,requests,  (if you fetch data from the internet)
#    ...,kivymd,    (if you use Material Design widgets)
requirements = python3,kivy==2.3.0,sdl2,sdl2_ttf,sdl2_mixer,sdl2_image

# Orientation
orientation = portrait

# Android-specific
android.permissions = INTERNET, MODIFY_AUDIO_SETTINGS
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

# FIX 3: Uncomment and set these if you have icon/presplash in assets/
# Recommended: icon should be 512x512 PNG, presplash 1080x1920 PNG
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
