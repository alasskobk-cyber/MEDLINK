[app]

# ==================================================
# INFORMATIONS DE L'APPLICATION
# ==================================================

title = MEDLINK
package.name = medlink
package.domain = org.medlink

version = 1.0

# ==================================================
# CODE SOURCE
# ==================================================

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json

# ==================================================
# DEPENDANCES PYTHON
# ==================================================

requirements = python3,kivy

# ==================================================
# INTERFACE
# ==================================================

orientation = portrait
fullscreen = 0

# ==================================================
# ANDROID
# ==================================================

android.api = 34
android.minapi = 23
android.arch = arm64-v8a

android.accept_sdk_license = True

# ==================================================
# PERMISSIONS
# ==================================================

android.permissions = INTERNET

# ==================================================
# BUILD
# ==================================================

[buildozer]

log_level = 2
warn_on_root = 1
