# The script of the game goes in this file.

# Declare characters used by this game.
define e = Character("Eileen")


# The game starts here.

label start:

    scene bg room 
    show eileen happy
    with fade

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    return
