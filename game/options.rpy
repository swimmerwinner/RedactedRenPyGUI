## This file contains configuration and preference defaults.


## Sounds and music ############################################################

## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.
# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.
# define config.main_menu_music = "main-menu-theme.ogg"





## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.
define config.enter_transition = Dissolve(.1)
define config.exit_transition = Dissolve(.1)

## Between screens of the game menu.
define config.intra_transition = Dissolve(.1)

## A transition that is used after a game has been loaded.
define config.after_load_transition = fade

## Used when entering the main menu after the game has ended.
define config.end_game_transition = fade

## Note: A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.





## Window management ###########################################################

## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.
define config.window = "auto"

## Transitions used to show and hide the dialogue window
define config.window_show_transition = Dissolve(.1)
define config.window_hide_transition = Dissolve(.1)





## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.
default preferences.text_cps = 0

## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.
default preferences.afm_time = 15
