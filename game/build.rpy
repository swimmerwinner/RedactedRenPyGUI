## This file contains settings that can be changed to customize your final build.


## Build Images ##################################################################
##
## A checklist of images you should include in your final build.
## These go *outside* the game folder.

## Desktop icons.
##
## https://iconifypng.com/
# ▢ icon.ico
# ▢ icon.icns

## Android app icon.
##
## https://www.renpy.org/doc/html/android.html#icon
# ▢ android-icon_foreground.png
# ▢ android-icon_background.png

## Android pre-splash.
##
## https://www.renpy.org/doc/html/android.html#presplash
# ▢ android-presplash.jpg

## Web pre-splash.
##
## https://www.renpy.org/doc/html/web.html#presplash
# ▢ web-presplash.png





## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.
define config.name = _("Redacted Ren'Py GUI")


## The version of the game.
define config.version = "1.0"


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.
define build.name = "RedactedGUI"





## Save directory ##############################################################

## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.
define config.save_directory = "DeleteThis-1775640010"





## Icon ########################################################################

## The icon displayed on the taskbar or dock.
define config.window_icon = "gui/window_icon.png"





## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Do not include in the final build.
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.psd', None)
    build.classify('game/**.rpy', None)

    ## Archive folders.
    build.archive("images","all")
    build.archive("audio", "all")
    build.archive("game", "all")
    
    # Images.
    build.classify('game/**.png', 'images')
    build.classify('game/**.jpg', 'images')
    build.classify('game/**.webp', 'images')
    build.classify('game/**.webm', 'images')
    
    # Audio.
    build.classify('game/**.ogg', 'audio')
    build.classify('game/**.mp3', 'audio')
    build.classify('game/**.wav', 'audio')

    # Game.
    build.classify("game/**.rpyc", "game")
    build.classify("game/**.py", "game")
    build.classify("game/**.ttf", "game")
    build.classify("game/**.otf", "game")

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.
    build.documentation('*.html')
    build.documentation('*.txt')





## Google Play #################################################################

## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".
# define build.google_play_key = "..."





## Itch.io #####################################################################

## The username and project name associated with an itch.io project, separated
## by a slash.
# define build.itch_project = "renpytom/test-project"
