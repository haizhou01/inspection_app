[app]
title = 验房记录
package.name = inspection
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,ttf
version = 0.1
requirements = python3==3.11.7,hostpython3==3.11.7,kivy,openpyxl,pillow
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 34
android.minapi = 21
android.ndk = 25b
android.sdk = 34
android.permissions = CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.arch = armeabi-v7a, arm64-v8a