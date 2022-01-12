define d = DynamicCharacter("doc_name")
image pic1 = im.Scale("red.jpg", 1280, 720)
image hall = im.Scale("hall.jpg", 1280, 720)
image stair = im.Scale("stair.jpg", 1280, 720)
image cafe = im.Scale("cafe2.jpg", 1280, 720)
image out2 = im.Scale("out2.jpg", 1280, 720)
image doctor = im.Scale("doc2.png", 500, 680)


# The game starts here.

label start:
    scene black
    "I woke up with a severe headache."
    play music [ "<silence 2>", "Full.mp3" ]
    "It seems as if I'm in a pitched black room."
    "Where exactly am I?"
    "If I recall correctly, a black van crashed into my vehicle, knocking me out unconcious."
    "A pair of sirens went off and I was transported into a building..."
    "Which means I'm inside a hospital?"
    "I don't remember much, a sign of early amnesia, I suppose."
    "but I do recall that my name is..."
    $ y = renpy.input("Enter your name.")
    while y == "":
        "I may have amnesia, but I do know my name, it's..."
        $ y = renpy.input("Enter your name.")
    y "Right, I recall now, who would forget a name [y]?"
    scene pic1
    play sound "Shock.mp3"
    "A flash of red came over my head and it ached with severe pain."
    scene black
    y "Ack!!"
    y "Seems like the surgery effects are still residing."
    y "That being said, this is a bit eery, isn't it?"
    y "The hospital is way too quiet and no doctors are around..."
    y "What should I do?"
    "NOTICE: only the first option works, takes quite a while to come up with a story so the second choice leads to nowhere"
    menu:
        "leave the room":
            play sound "Run.mp3"
            jump leave_room
        "rest for a while longer":
            "nothing"

label leave_room:
    "I left the room, heading towards the light."
    "And I can't tell if my eyes are deceiving me, but what I saw was a sight from nightmares."
    scene hall
    play music [ "<silence 1>", "Chaos.mp3" ]
    y "W... What?"
    y "What the hell is this?"
    "My surrounding walls are of a different texture, as if human guts are glued onto it."
    "Although when I touched it, it felt the same as a normal wall."
    y "What did those surgeons do to me??"
    "I am sweating buckets right now, but I try to calm down."
    "There's no point standing idly by."
    y "First, I should try to find an exit."
    "I walked towards the end of the hallway and two routes open up."
    "(only first choice works)"
    menu:
        "walk towards the right":
            play sound "Run.mp3"
            jump right_room
        "walk towards the left":
            "nothing"

label right_room:
    scene cafe
    play music [ "<silence 1>", "Sin.mp3" ]
    "I walked into a room that seems to be a cafeteria."
    "The tables and chairs are also a sight of grotesque."
    "Upon further inspection from my sense of touch, it feels strangely normal."
    play sound "Roar.mp3"
    "A roar split the entire room from upstairs"
    "From across the room, I see multiple documents on the employee's counter."
    "And a few feet away exists a window."
    y "hmm,I can probably learn what exactly is going on, or I can escape through the windows..."
    "If I try to figure out what's going on, would it be too risky?"
    "After all, there does seem to exist something inhuman upstairs"
    y "hmm..."
    "(only first choice works)"
    menu:
        "try to escape":
            "I grabbed a chair and threw it onto the window with all my might."
            play sound "Crash.mp3"
            "My sense of sound seems to be intact as I hear regular windows breaking."
            "However, my sense of sight is still unstable."
            "The chair made a little dent before the gutsy texture bounced it right off."
            y "Well, at least the dent is big enough to force myself through."
            "I latched onto the hole and teared it apart, reaching the outside world."
            jump out
        "gather more information":
            "nothing"


label out:
    scene out2
    default doc_name = "???"
    "I finally made it out, but the scenery is still unpleasant."
    "The surgeons may have altered my sense of vision and the cure must lie inside the hospital..."
    "I planned on going back in but a voice appeared behind me."
    d "Well, what do we have here, a lost rat?"
    "I turned around and saw someone in a uniform, a doctor, perhaps?"
    show doctor
    y "Who are you?"
    "I demanded for his name."
    d "Another employee here, I guess, just call me doc."
    $ doc_name = "doc"
    y "[d] huh? Tell me, what exactly is going on? Why does everything look so grotesque?"
    d "Grotesque? Ah yes, you were part of the lab 32 experiment."
    play music [ "<silence 1>", "Insanity.mp3" ]
    y "Huh?"
    d "I am surprised that you were able to move at all, professor coded your brain chip so you cannot think."
    y "..."
    "Code? Chip? What is he going on about?"
    d "Ah, I see now, YOU there behind the screen, YOU aided this rat's escape, didn't YOU?"
    y "Behind the screen? What?"
    d "Oh, well, unluckily for YOU, YOU did not acquire enough information to defelct my code. So long then."
    "The doctor took out his phone and typed something in..."
    y "Ack!... Huh?"
    "My body became paralyzed and a thought came into my mind"
    "if 'YOU' in [y]_subconcious:"
    "index = [y]_subconcious.index(YOU)"
    "[y]_subconcious.remove(index, YOU)"
    d "Have fun being a prisoner of the ending credits"
    jump cred


## ATL for scrolling screen object. In this case, credits roll.
## Speed is the time for object to move up from initial ypos to finish ypos.

transform credits_scroll(speed):
    ypos 50
    linear speed ypos -50

## Credits screen.

screen credits():
    style_prefix "credits"

    add "#000"

    frame at credits_scroll(5.0):
        background None
        xalign 0.5

        vbox:
            label "Credits"

            null height 20

            hbox:
                text "Story: IEatCrayon"

            hbox:
                text "Programming and assistance: IEatCrayon"

            hbox:
                text "Art: Chuuou Higashiguchi"

            hbox:
                text "Music: Zizz studio, Low"

            hbox:
                text "Special thanks to: Ren'py Engine, Ren'py forums, Reddit, and YOU"


style credits_hbox:
    spacing 40
    ysize 50

style credits_label:
    xalign 0.5

style credits_text:
    xalign 0.5


## Show credits screen.

label cred:
    play music [ "<silence 1>", "Chaos.mp3" ]
    call screen credits

return
