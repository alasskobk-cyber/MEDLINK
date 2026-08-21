[app]

title = MEDLINK
package.name = medlink
package.domain = org.medlink

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Android
android.api = 35
android.minapi = 23
android.accept_sdk_license = True
android.arch = arm64-v8a

[buildozer]

log_level = 2
warn_on_root = 1
