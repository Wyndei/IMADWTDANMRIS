


label task_one:
    
    

    play music ["apartment.mp3"] fadeout 0.5 fadein 0.5
    scene apartment_dirty with dissolve

    window show

    "The tiny robot sits in the center of the room, spinning in circles as if thinking deeply about life with its newfound consciousness."
    "For now, it isn't paying you much mind."
    
    show robovac neutral with dissolve

    "The floor is covered in crumbs and dust. You could clean it yourself... but isn't that why you got a robovac in the first place?"

    pov "Alright, little guy, time to earn your keep."

    "You take a step forward and lean down to pick up the robot..."

    hide robovac happy with moveouttop

    "...But it spins around sharply, tires squealing as it flees"

    show robovac happy with moveinleft
    hide robovac happy with moveoutright

    play sound "excited_beeps.mp3"
    robovac "{i}Beeps playfully{/i}"

    pov "Right, you're alive now."
    pov "Not just a simple machine anymore. {i}I hope you don't bite.{/i}"
    
    show robovac mischief with moveinbottom

    "The machine stops at the other side of the room and turns around. It's staring at you again...waiting...menacing..."

    pov "You're not just going to do as I ask, are you?"

    show robovac stare

    robovac "..."


    menu:
        "I guess I'll have to get clever if I want your help then..."
        "Do you want to...play?":
            jump task_one_bond

        "You're not going to take orders from a piece of plastic! Fetch a spray bottle and see how it reacts to discipline":
            jump task_one_threaten

        "This is a waste of time, just grab the broom yourself":
            jump task_one_neglect


label task_one_bond:

    show robovac happy

    "The robot tilts slightly to the side and beeps once in anticipation. That's as good an answer as you're going to get."

    pov "Great, now...what do vacuum cleaners play with exactly?"


    show robovac low_battery
    "There is another beep, starting out high pitched and then lowering suddenly." 
    "The robovac doesn't seem to notice it, but you're familiar with the sound of a low-battery warning"
    "...That's not a bad idea actually. You grab a pack of batteries from a kitchen drawer and tear them open."

    pov "Here, little guy, come and get it!"

    show robovac excited


    show pentasonic_batteries with moveinbottom

    "The robovac perks up and its motor begins to whir loudly. It spins in circles around your feet as you dangle a triple-A battery just above it, gently bumping into your heel as it waits."
    "You set the battery down in front of the robovac. And...it..."

    play sound "battery_eat.mp3"
    hide pentasonic_batteries

    "...It ate it."

    play sound "cheerful_beeps.mp3"
    show robovac battery
    "You hear the tell-tale bleep of its battery indicator and - lo and behold - it's charged up. You can feed the robovac, and you can use that to your advantage."
    "You place batteries around your apartment, strategically luring the robovac to sweep up the most critical areas, and it races to follow you as fast as its little wheels can push it."


    "The robovac zooms around the room in a blur of enthusiasm, sweeping up everything in sight to claim its prize."

    pov "Ha, I'm a genius!"

    play sound "excited_beeps.mp3"
    robovac happy "{i}Beeps enthusiastically{/i}"

    pov "And you're not too bad yourself. Good work little guy~"




    $ bond += 1

    jump task_one_end


label task_one_threaten:

    "You're not going to take orders from a piece of plastic!"
    "You grab a spray bottle from the bathroom and fill it with water. Robots are afraid of water, right?"
    "Returning to the living room, you eye the robovac warily. It has a mind of its own; it isn't a quiet, obedient tool anymore."
    "Now it's a demonic entity that reeks of brimstone and the supernatural"


    robovac mischief "..."

    "Maybe intimidation is the only option?"

    pov "Alright, little demon...you start cleaning right now or you'll get the spray bottle!"

    show robovac angry

    "The robovac stops in place and stares, then begins a slow, menacing spin of 360 degrees as if trying to call your bluff. You wave the spray bottle and fire a warning burst into the air."

    play sound "anxious_beeps.mp3"
    show robovac scared

    "It relents."
    "With a reluctant mechanical whir, it rolls towards the nearest dust pile, sweeping up slowly, but its LED face display never looks away from you for too long."
    
    pov "That's what I thought."


    $ threaten += 1

    jump task_one_end


label task_one_neglect:


    show robovac mischief
    "You glance at the demonic robovac, its vents puffing a faint sulfur smoke as it spins in place." 
    "Maybe you could lure it with something...batteries? No, that's silly. Maybe you could try giving orders directly. Hmm, that seems cruel though. "
    
    pov "Forget it. I'll just sweep up on my own."
    
    show robovac sad
    
    "You grab a broom and start sweeping. The robovac just sits there, making slow, mocking figure-eights. Every few seconds it lets out another dramatic, self-pitying beep. It's definitely judging you."
    
    #Audio - [Sulking or disappointed robot beeps, like a sad kazoo]
    play sound "sad_kazoo.mp3"

    pov "{i}Ugh... This is humiliating...{/i}"

    "At last, the floor's mostly clean"
    "so much for the robot. Still, it rolls back to its charger and parks itself quietly, and its LED display turns dark, blank, and unreadable."
    "Somehow, it feels like you've missed an opportunity, though for what you can't say."
    "Strange. It's just a robot isn't it?"


    $ neglect += 1
    jump task_one_end


label task_one_end:

    window hide
    scene black with dissolve
    stop music fadeout 0.5
    
    pause 2.0

    jump task_two
