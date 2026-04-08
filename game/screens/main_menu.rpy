## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu


screen main_menu():

    tag menu

    style_prefix "main_menu"

    add gui.black

    vbox:

        label config.name

        null height 50

        textbutton _("Start") action Start()
        textbutton _("Saves") action ShowMenu("saves") keysym "game_menu"
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("About") action ShowMenu("about")
        textbutton _("Help") action ShowMenu("help")
        textbutton _("Quit") action Quit(confirm=False)


style main_menu_vbox:
    xalign 0.5
    ypos 80
    spacing 20

style main_menu_label:
    xalign 0.5

style main_menu_label_text:
    color gui.white
    size 180
    xalign 0.5

style main_menu_button:
    hover_background gui.darkgrey
    size_group "main_menu"
    xalign 0.5

style main_menu_button_text:
    size 60
    xalign 0.5
