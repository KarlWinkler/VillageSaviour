define connor = Character("Connor Manuel")
define hunter = Character("Hunter")
define ghost = Character("Ghost")
default conman = False
default wolves = False
default flu = False

label year_1:
    scene town_square
    hide screen trackers    
    hide screen gui_map_menu

    jump the_conman


label the_conman:
    narrator "Content with your decisions or not, time marches on. You find yourself walking the streets of your new home."
    narrator "The air is peaceful, the skies above dripping with the dew of fresh spring day. It’s in this fresh air you find your pondering rudely interrupted by a sudden commotion."

    scene town_square

    narrator "Rushing to the market stalls you’ve only recently become acquainted with, you approach a booming, cunning voice erupting from a crate tossed out into the middle."
    
    connor "Ay! Hear my pleas all ye who live amongst the hills. The eras or steam and fire have come to an end before beginning."
    connor "I speak of solar magicks. The wrath of the sun in a bottle. Believe ye not in chloro-energie?"

    earnest "What ruckus is this? Oh, my leader, pay no to this riff raff. You may expel them from our walls."

    connor "Ye lead this wondrous hamlet? Please, hear out my case. A small fee is all I need, and then ohoho."
    connor "And then my friend the world will be swarming with little green men. Photo automatons! The future is now. I will bring it. What say you?"

    menu:
        "Yes":
            jump yes_donate
        "No":
            jump no_donate


label yes_donate:
    $ conman = True
    connor "Oh my, you are too kind! And far too trusting, sucker! Automatons? Little green men? Ohoho- What a goof!"

    earnest "Well, can’t say I didn’t warn you. Did I not tell you, look out for yourself first my lord, we are all in your debt, and will stand by you." 

    jump the_wolves


label no_donate:
    $ conman = False
    connor "You fail to see my genius! I- I **kicks you** You buffoon!"

    earnest "Hunter! Take this scum away! Let him not harm our lord!"

    hunter "Huh? Me? Ok!"

    jump the_wolves



label the_wolves:
    narrator "Resting atop a bench, watching the autumn leaves fall for the first time since you’ve taken power, you breathe."
    narrator "It’s a cool breeze that rushes to fill your nostrils as you see the streets and skies painted a beautiful orange hue."
    narrator "You’ve made decisions, decisions that have helped bring about this peaceful serenity."
    narrator "Soon the villagers must prepare for the fall festival."
    narrator "And as you sigh, you assume that’s why Hunter approaches you, as you recall that village hunters must soon gather food for the supply." 

    hunter "Leader! It’s an honour to meet with you properly at last!"

    hunter "The hunt? Oh yeah, that should go smoothly without your help, really don’t sweat it! No actually, I’ve got to talk to you about something else."

    narrator "Before he can get another word out you hear a flustered scatter of footfall as Earnest bursts past flailing leaves to interrupt."

    earnest "HUNTER! What did I tell you about consulting with the leader?"

    hunter "Huh but no no, it’s not about that Sir Trudeau! The Hunting party is all prepared."

    earnest "Oh? Now I’m curious, what do you need our leader’s consultation on?"

    hunter "Well, see, I was thinking about those wolves, the one’s what gave you a proper hurt earlier this year?"

    earnest "Yes? What of them?"

    hunter "I knows where their den is."

    narrator "By this point a sizable crowd had gathered around you, the booming words of Hunter a beacon to all wandering villagers."

    hunter "I don’t really likes the idea of those wolves getting another shot on us good peoples. So leader, I was thinking."

    eucie "Always a dangerous thing."

    hunter "Shut up! I was thinking, thinking we could takes em out."

    earnest "Now there’s using your noggin! Aha, Hunter, you really know your craft. Dear leader, this is a perfect opportunity! Think of all the money those pelts might make. "
    earnest "Those beasts really have it coming for messing with us, and on top of our revenge, we’ll make out with money on money to help our people and better your situation."

    eucie "Umm, excuse me?"

    earnest "Oh yes? Remind me again, who are you?"

    eucie "I’m not much of note to be honest, a layperson by trade. But I was thinking, would improving the wall not also help keep us safe?"
    eucie "We’ve let it slack for so long now, the gate barely operates, and even common thugs could leap upon it." 

    earnest "Hmm, suppose that is an option leader. Though the costs would be measurable. Don’t force yourself, make the choice that feels best to you."

    menu:
        "Hunt":
            jump hunt
        "Build":
            jump build



label hunt:
    $ wolves = True
    narrator "You hear tell of the hunt on the eve of the festival. The wolves that had attacked Earnest so long ago would never hurt another soul."
    narrator "Perhaps you didn’t need all the gruesome details, but Hunter was a bit too eager to share his bold exploits, and you feel as though you’ve grown closer."
    # //-wolf points +1000 gold

    jump the_flu


label build:
    $ wolves = False
    narrator "While Hunter is initially disappointed by the decision, the hunt quickly takes the thoughts off his mind."
    narrator "And the town quickly bustles to life after the festivities, working hard to repair the wall."
    # //-300 gold -little energy

    jump the_flu


label the_flu:
    narrator "You're taking a walk with Earnest, admiring the softly falling snow and lack of wolves."
    narrator "It's quiet, most of the townsfolk are inside their homes, presumably preparing for the holidays."

    eucie "Glorious leader! H-hachoooow goes your day?"

    earnest "Hey! Are you sick? Stay away, we don't want our leader to catch whatever you've got!"

    eucie "Sure, surachoo! But it’s nothing big, just the yearly flu. Half the town has it. Sniff." 

    earnest "you should go back home so you don't risk catching it. we don't want you to suffer. There's nothing we can do about it other than try our best to avoid it."

    eucie "I heard the neighbouring town has an expert that can cure the flu! Their people no longer get sick every year. I hear their apothecary is a real miracle worker."
    eucie "I wonder sir, if you might be able to hire their skills for our own healthcare."

    earnest "You don't need to trouble about this, leader. It's just a little inconvenience, really it happens every year."
        
    menu:
        "Ignore Eucie and take Earnest’s advice of going home":
            jump ignore_eucie
        "Visit the neighbouring town":
            jump visit_neighbouring_town
      

label ignore_eucie:
    $ flu = True
    # // Health infrastructure not improved
    narrator "Heeding Earnest’s advice brings you on a direct path home, care."
    narrator "The days of winter pass slowly in your isolation, but you keep your health. Within 2 weeks, Earnest knocks upon your door."
    narrator "The coast clear, the villagers again healthy, you resume your duties as usual."

    jump the_ghost


label visit_neighbouring_town:
    $ flu = False
    # // -500 gold +1 health -a lot of energy
    narrator "After a day’s hike, you make it to the other town."
    narrator "The apothecary is a jovial spirit, in fact it hardly takes a moment’s hesitation, and a small sack of gold before he gladly spills all his secrets of medicine."
    narrator "The most trying task of all remains at home however."
    narrator "The medicine is difficult to produce, it takes a full week of effort before the infrastructure is in place to start curing the citizens,"
    narrator "by which point most of the town has recovered anyway, but oh well it might help in future years."

    jump the_ghost


label the_ghost:
    narrator "And as winter winds give way to spring dews once again, you approach a full year passed in the village."
    narrator "Before the anniversary of your appointment arrives, you spend an evening surrounded in the warm embrace of all you’ve come to know."
    narrator "Hunter, Eucie, Earnest, and even more warm faces greet you in warm rejoice. You’ve made an impression on them all, and they’ve grown to rely on your guidance."
    narrator "As the firelight of the ceremony grows dim, you return home. Comforted by the warm darkness, you drift into nothingness."

    narrator "Suddenly, a figure appears before you, somewhere in the endless expanse of the void."

    ghost "Oh being of fate. The bonds of hell, shackle themselves to you. Lives countless, rest."
    ghost "Rest in blazing agony, awaiting the fate you choose. Bold are you to take lives in your hands. Your wrists, already lashed with the embers of mistakes." 

    if conman:
        ghost "Your kindness, it’s violent unyielding naivety. You err and trust."
        ghost "You err and put your lives in other’s hands. And in these blazing mistakes, you take a leap, one you will live to see paid back in full."
    else:
        ghost "Your shrewdness, it pays. It pays in pain, it pays in broken trust. It’s wrathful hate burns within you."
        ghost "Yet no loss is the greatest loss of all. You prosper, but wilt. You suffer. You will always suffer."

    if wolves:
        ghost "Hunt. Hunt and kill. Revenge, it is not folly, but sabotage. You must kill. You will always kill."
        ghost "If lives are in their hands they must take them too. You chose the path of hell, it lashes at you with great flames."
        ghost "Kill your children too. Take all with you on the path."
    else:
        ghost "You build a future you will never see. When hellhounds bark from heaven’s gate, then crimson embers tear down your walls."
        ghost "What use is there? You fight for life you’ve damned already, taking upon your shoulders an endless fight. And yet they will thank you."

    if flu:
        ghost "Plague. Plague. You will rot. They will rot. They pass with coughs, they leave in coffins."
        ghost "You dug the grave. You brought them hell. The hell you always walk. The future you never see."
    else:
        ghost "Your burning kindness brings them close. Their burning hate tears your skin."
        ghost "Their coughs on you, your plague is spite. In truth, the burning love shines through."

    # # TODO: add optional events

    # # ghost(OP1-1) (Very Angry) In filth they bathe the filth that bathe. And rot, your children will rot, and feed yours with rot. From rot the filth will breed, and hell’s gates will open. Famine, disease and death. It joins with you.

    # # ghost(OP1-2) (Contemplative) You built a toilet.

    # # ghost(OP2) (Very Angry) In decadence you sour, like rotting ale, like dying fruit. You are the disease that breeds within these walls. You rot away the woods beside, kill beast and bird alike. Your joys are hollow. Your suffering eternal.

    jump map
    