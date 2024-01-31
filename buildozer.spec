[app]

# (str) Title of your application
title = Link Solution

# (str) Package name
package.name = linksolution

# (str) Package domain (needed for android/ios packaging)
package.domain = org.linksolution

# (str) Source code where the main.py live
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = assets/*,images/*.png

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,kivymd

# (str) Application versioning (method 1)
version = 0.1

# (list) Application source code
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = assets/*,images/*.png

# (list) Garden requirements
#garden_requirements = 

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Presplash background color (for new android toolchain)
presplash.color = #FFFFFF

# (str) Presplash image (if none present, the app will remain fullscreen during loading)
#presplash.filename = 

# (str) Icon of the application
#icon.filename = %(source.dir)s/icon.png

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# (bool) Indicate to include sqlite in the application package
# Uncomment and change to 1 to activate
# require.sdl2 = 1

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# (str) Application build settings
[buildozer]

# (int) Log level (1 = debug, 2 = info, 3 = warning, 4 = error, 5 = critical)
log_level = 2

# (int) Display warning if build settings are missing
warn_on_missing_build_dep = True

# (str) Path to directory to save build artifacts
# build_dir = /path/to/build/directory

# (int) Commit before switching back to the develop branch (you may want to do
# this manually)
#commit_before = True

# (int) Automatically build and package an apk
android.build = 1

# (int) Punctuation of the version, needed by android's packager.
# Should be a single int or a list of int.
# If you want the version to end with a dot, add a '.', or add a 'c' for
# release candidates, e.g. 3.5.3c
#version.regex = __version__ = ['"v'](.*)['"]
# version.filename = %(source.dir)s/main.py

# (int) Application version code
# version.code = 1

# (str) Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
#arch = armeabi-v7a

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.renpy.android.PythonActivity

# (str) Android app theme, default is okay for Kivy-based app
#android.app_theme = @android:style/Theme.NoTitleBar

# (list) Pattern to whitelist for globbing
#source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_exts = py,png,jpg,kv,atlas

# (list) List of exclusions using pattern matching
#source.exclude_exts = spec, yml, yaml, pyo, pyc, json, kivy, git, sqlite3, inv

# (list) List of framework imports (include only what you need)
#python3_modules = sqlite3,kivy

# (str) Application icon
# icon.filename = %(source.dir)s/icon.png

# (str) If source.root is given, consider as a directory, and look for main.py in this directory
# source.root = 

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
#requirements = python3,kivy

# (str) Inclusions
# include_exts = py,png,jpg,kv,atlas

# (str) All the path added to Python path (I added the one for testings and for
# python-for-android
# p4a.source_dir = /home/tito/work/p4a-sandbox
# p4a.local_recipes = /home/tito/work/p4a-venv/build/python-install/lib/python3.6/site-packages/kivy/recipes
# p4a.local_recipes = /home/tito/work/p4a-venv/build/python-install/lib/python3.7/site-packages/kivy/recipes
# p4a.sysroot_cython_args = --exclude=TestUnpickling

# (list) List of all the modules to include (python-for-android)
#p4a.modules_dir = %(source.dir)s/_modules/

# (str) The path of the python-for-android git checkout
#p4a.source_dir = /home/tito/work/python-for-android

# (str) The path of the p4a git checkout
#p4a.source_dir = /home/tito/work/python-for-android/pythonforandroid

# (list) Include patterns (and files) that are not in the python-for-android
# default blacklists
#p4a.include_exts = .gitignore,gradlew.bat,build.gradle

# (list) Exclude patterns (and files) that are in the python-for-android default
# blacklists
#p4a.exclude_exts = 

# (str) Application entry point
#p4a.entry_point = /home/tito/code/kivy/examples/demo/pictures/main.py

# (str) Specify the root python-for-android directory (if not in same dir as
# buildozer.spec)
#p4a.source_dir = /home/tito/work/p/python-for-android

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process.
#android.add_jars = foo.jar,bar.jar,path/to/more/jars.jar

# (list) List of Java files to add to the
