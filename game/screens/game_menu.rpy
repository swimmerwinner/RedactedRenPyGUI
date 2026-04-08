default _game_menu_screen = "saves"

screen game_menu(label=""):

    style_prefix "game_menu"

    frame style "game_menu_label_frame":
        label label

    frame style "game_menu_content_frame":
        transclude

    frame style "game_menu_navigation_frame":
        use game_menu_navigation

style game_menu_label_frame:
    background Transform(gui.black, alpha=0.85)
    xfill True
    ysize 0.1  # top ribbon
    yalign 0.0

style game_menu_content_frame:
    background Transform(gui.black, alpha=0.5)
    xfill True
    ysize 0.8  # middle content
    yalign 0.5

style game_menu_navigation_frame:
    background Transform(gui.black, alpha=0.95)
    xfill True
    ysize 0.1  # bottom ribbon
    yalign 1.0

style game_menu_label:
    xpos 20
    yalign 0.5

style game_menu_label_text:
    size 80


screen game_menu_navigation():

    style_prefix "navigation"

    hbox:
        textbutton _("Saves") action ShowMenu("saves")

        textbutton _("Preferences") action ShowMenu("preferences")

        if not main_menu:
            textbutton _("Title") action MainMenu()
        else:
            textbutton _("About") action ShowMenu("about")

        textbutton _("Help") action ShowMenu("help")

    textbutton _("Return") action Return() keysym "game_menu" style "navigation_return"

style navigation_hbox:
    xalign 0.0 xoffset 20
    yalign 0.5
    spacing 50

style navigation_button_text:
    is button_text
    size 40

style navigation_return:
    xalign 1.0 xoffset -20
    yalign 0.5

style navigation_return_text:
    is button_text
    size 40
