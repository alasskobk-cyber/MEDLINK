[app]

# Nom de l'application
title = MEDLINK

# Nom technique du package
package.name = medlink

# Identifiant unique de l'application
package.domain = org.medlink

# Dossier contenant main.py
source.dir = .

# Fichiers à inclure dans l'application
source.include_exts = py,png,jpg,jpeg,kv,json

# Version de MEDLINK
version = 1.0

# Dépendances Python
requirements = python3,kivy

# Orientation de l'application
orientation = portrait

# Ne pas utiliser le plein écran
fullscreen = 0

# Configuration Android
android.api = 35
android.minapi = 23
android.arch = arm64-v8a

# Accepter les licences Android
android.accept_sdk_license = True


[buildozer]

# Niveau des journaux
log_level = 2

# Avertissement si Buildozer est exécuté avec les privilèges root
warn_on_root = 1
