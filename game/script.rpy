# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define me = Character("me")
define advisor = Character("advisor")

define hide_textbox = Character(None,window_background=None)

default resources = 10

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "Alex happy.png" to the images
    # directory.

    show alex happy

    # These display lines of dialogue.

    advisor "You've created a new Ren'Py game."

    advisor "Once you add a story, pictures, and music, you can release it to the world!"

    me "Thank you, Ren'Py!"

    jump map


label map:

    show map
    show screen gui_game_menu

    hide_textbox ""


screen gui_game_menu():
    hbox:
        imagebutton:
            auto "house %s.png"
            action Function(decrement_resources(1))
        text "Resources: [resources]"


init python:
    def decrement_resources(amount):
        global resources
        resources -= amount
        if resources < 0:
            resources = 0
        return Jump("map")
