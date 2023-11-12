define hide_textbox = Character(None,window_background=None)

default toilet = False
default manor = False

label map:
    scene map
    show map
    show screen trackers    
    show screen gui_map_menu
    hide_textbox ""

    if year == 0:
        jump year_1
    elif year == 1:
        jump good_ending


screen trackers:
    hbox:
        xcenter 0.5 yalign 0
        text "Resources: [resources]"


screen gui_map_menu():
    hbox:
        xalign 0.425 yalign 0.15
        imagebutton:
            auto "emptyplot %s.png"
            sensitive resources >= 2 and toilet == False
            action Function(toggle_toilet)
    hbox:
        xalign 0.09 yalign 0.63
        imagebutton:
            auto "manor %s.png"
            sensitive resources >= 1 and manor == False
            action Function(toggle_manor)


init python:
    def decrement_resources(amount):
        global resources
        resources -= amount
        if resources < 0:
            resources = 0
        return


    def toggle_toilet():
        global toilet
        toilet = True
        decrement_resources(2)
        return renpy.restart_interaction()


    def toggle_manor():
        global manor
        manor = True
        decrement_resources(1)
        return renpy.restart_interaction()
