# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define me = Character("Me")
define narrator = Character("Narrator")
define earnest = Character("Earnest")
define eucie = Character("Eucie")

default resources = 10
default money = 1000
default year = 0

# def swapemote(newemote):
#     hide oldemote
#     show newemote

# The game starts here.

label start:

    scene woodsout

    jump prologue


label prologue:
    narrator "Society has become too oppressive for you to continue living there. Travelling among the mountain’s valleys you’ve come searching for a life apart from the hellscapes you’ve known. "
    narrator "Suddenly, you hear a scream coming from the forest."

    menu:
        "Investigate":
            jump investigate
        "Ignore":
            jump ignore


label investigate:
    narrator "Chasing the sounds, you find a man, clutched loosely by the quickly closing jaws of a pair of wolves. Their growling and howling echoing into the hollow woodlands around.."
    
    show earnestsad

    earnest "Please oh gods above, I pray grant me a miracle"
    
    menu:
        "Ignore him":
            jump ignore_him
        "Help him":
            jump help_him


label ignore_him:

    hide earnestsad
    show earnestdead
    narrator "The miracle never happen. Meanwhile, you continue preparing breakfast. The rest of your life is uneventful. Eventually, you die. The end."

    jump bad_ending


label help_him:

    hide earnestsad
    show kick
    earnest "What strength! You saved my life, and the lives of my people. A whole village is in your debt. Perhaps my faith blinds my judgement, but I see you as a miracle."
    hide kick
    show earnesthappy
    earnest "Oh great lord, won’t you please, please lend your leadership to my town. I struggle to be their guiding voice, but you, you are so bold. Please lead us forward"

    menu:
        "Nah":
            jump reject_town
        "Yes":
            jump accept_town


label reject_town:
    hide earnesthappy
    narrator "You go back to your camp in the mountains and continue preparing breakfast. The rest of your life is uneventful. Eventually, you die. The end."

    jump bad_ending


label accept_town:
    earnest "It's my greatest pleasure to pass on my role to you. Under you, our town shall become the richest and most plentiful in all the land. Follow me, I'll lead you there."
    hide earnesthappy
    scene bg room

    narrator "The townsfolk cheer as you are crowned their new leader. "
    show eucieeager
    eucie "We all heard of your heroic deed! I know our town will prosper under your reign."
    hide eucieeager

    scene map
    show earnestneutral
    earnest "Here's the town's resources. Use them wisely, and our town will grow rich."
    hide earnestneutral
    menu:
        "Continue":
            jump map


label ignore:
    narrator "You continue preparing breakfast. The rest of your life is uneventful. Eventually, you die. The end."

    jump bad_ending
