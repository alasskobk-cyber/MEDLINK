[app]

# Nom affiché de l'application
title = MEDLINK

# Nom technique du package
package.name = medlink

# Identifiant unique
package.domain = org.medlink

# Dossier contenant main.py
source.dir = .

# Extensions incluses
source.include_exts = py,png,jpg,jpeg,kv,json

# Version
version = 1.0

# Dépendances
requirements = python3,kivy

# Orientation
orientation = portrait

# Mode fenêtre
fullscreen = 0


# --------------------------------------------------
# ANDROID
# --------------------------------------------------

# Version Android utilisée pour la compilation
android.api = 34

# Version Android minimale
android.minapi = 23

# Architecture
android.arch = arm64-v8a

# Accepter automatiquement les licences
android.accept_sdk_license = True

# Nom de l'APK
android.add_src =


# --------------------------------------------------
# BUILD
# --------------------------------------------------

[buildozer]

# Niveau des logs
log_level = 2

# Avertissement si exécuté avec root
warn_on_root = 1
