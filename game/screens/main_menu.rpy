## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu


screen main_menu():

    tag menu

    vbox:

        text config.name

        textbutton _("Start") action Start()
        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("About") action ShowMenu("about")
        textbutton _("Help") action ShowMenu("help")
        textbutton _("Quit") action Quit(confirm=not main_menu)
