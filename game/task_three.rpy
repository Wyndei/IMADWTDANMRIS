





label task_three:

    window show
    "It's been a few days. The robovac practically haunts your apartment, like a dust-eating poltergeist. It has become a fixture of the apartment..."

    scene apartment_2c with dissolve 
    play music ["apartment.mp3"] fadeout 0.5 fadein 0.5

    show robovac sad
    
    "...for better or for worse. Today, though, it seems to be in rough shape...When was the last time you cleaned it?"

    play sound "sulking_beeps.mp3"

    robovac "..."
    "It rolls towards you. Its wheel motors grind audibly as it approaches, spitting up sparks. It looks pitiful, bumping gently into your foot as it stops."
    "The thing's probably stuffed with dirt."


    menu:
        "Oh no, let's do something about that! You've been working so hard...":
            jump task_three_bond
        "You aren't going to be of much use to me like that...let's get this over with.":
            jump task_three_threaten
        "I don't have time for this. Plus, you're alive now, you can take care of yourself.":
            jump task_three_neglect


define prompt = ""

define wheels = False
define tank = False
define spa = False

label task_three_bond:

    "You've got to help! Just look at it, what a mess! You gather what supplies you can and set to work..."

    $ prompt = "What should I start with?"

    show robovac sad
    jump bond_choice
    
label bond_choice:
    
    if wheels and tank and spa:

        $ bond += 1
        jump task_three_end

    menu:
        pov "[prompt]"

        "Let's start with the wheels. They sounded bad." if not wheels:
            $ wheels = True
            jump bond_wheels

        "Let's empty your tank. You're probably full by now." if not tank:
            $ tank = True
            jump bond_tank

        "You could use a wash-you're covered in dust!" if not spa:
            $ spa = True
            jump bond_spa

label bond_wheels:
    $ prompt = "Alright, my hardworking little menace, what's next?" 
    
    show robovac sad
    "You flip the robovac gently on its side. Yikes! The wheels are tangled with hair and loose carpet fibers!"
    "You are able to work them out by pulling and spinning the wheels, and after a few minutes, they are able to spin smoothly and silently again."

    # Audio - [Robovac beeps cheerfully]
    play sound "excited_beeps.mp3"

    "The robovac spins its wheels on its own a few times as if stretching them, and it beeps its relief as you turn it back over."

    jump bond_choice

label bond_tank:
    $ prompt = "Alright, my hardworking little menace, what's next?" 

    show robovac scared
    "You move to pop the robovac open. It watches you fitfully as you go, but you're able to soothe it with a pat on the chassis."
    show robovac sad
    "The collection tank is a little over-filled, packed full with loose change, scraps of paper, dust, dust, more dust, and...well, use your imagination."
    "Unless you're eating, then don't."
    "Somehow there's also an entire chicken nugget, perfectly unbroken, and a folded up sticky note that just reads \"repent.\""
    "You pop the container out, empty it, and replace it in short order. The robovac lets out a chirp and relaxes."

    jump bond_choice

label bond_spa:
    $ prompt = "Alright, my hardworking little menace, what's next?" 

    "You take up a washcloth, a sponge, and a bottle of soap."
    pov "Wait, is water still bad for you? I'm pretty sure it would have ruined you before."
    show robovac sad
    robovac "..."
    pov "...Inconclusive, I guess. I'll just be extra careful."
    "You use a gentle hand as you begin to work. You wipe the bulk of the dust off with a dry towel then work at the harder spots with a little soapy water."
    "The robovac relaxes, practically melting into the floor as it hums with satisfaction."

    show robovac spa
    "You wrap it in a soft towel like a lil robo-burrito afterwards. Once the 'spa' treatment is over, it's bouncing with joy."
    "You may have gotten a little carried away..."
    pov "Much better, eh? You enjoy a rest now, you've earned it."

    jump bond_choice


label task_three_threaten:

    show robovac scared

    $ prompt = "Alright, where should I start?"

    "This thing won't last much longer in this state. Better get it back in working shape before it craps out for good..."
    
    

    
    jump threaten_choice

label threaten_choice:

    if wheels and tank and spa:

        $ threaten += 1
        jump task_three_end


    menu:
        pov "[prompt]"
        "Your wheels must be tangled. Let's deal with that." if not wheels:
            $ wheels = True
            jump threaten_wheels

        "I hope your tank didn't fill up that quickly, but I'll check anyway." if not tank:
            $ tank = True
            jump threaten_tank

        "You're filthy. Probably tracking around as much dirt as you're sucking up." if not spa:
            $ spa = True
            jump threaten_spa

label threaten_wheels:
    $ prompt = "Alright, let's get this over with. What next?"
    
    show robovac scared

    "You turn the robot over. The wheels are badly tangled, though it only takes a few minutes to tear the nest of hair and carpet threads free."
    "You don't waste any time."
    "As you try to clean its wheels, it growls- sounding more like a hellhound than a robot for a moment."

    show robovac angry

    "The robovac spins its wheels in place as you set it upright again. It looks none-to-pleased with your handling, and drives in a tight circle while beeping furiously."

    jump threaten_choice

label threaten_tank:
    $ prompt = "Alright, let's get this over with. What next?"

    show robovac sad

    "The robot retreats initially, but not quickly enough. You're able to hold it in place and pop the waste container out."
    "It's full! Completely full! This thing has been sucking up pennies, paperclips, ear buds...whatever it can get its vacuum on really."
    "You empty it and pop it back in."

    pov "Try eating more trash and less of my stuff from now on."
    
    show robovac scared

    play sound "anxious_beeps.mp3"

    robovac "..."

    jump threaten_choice

label threaten_spa:
    $ prompt = "Alright, let's get this over with. What next?"

    "The machine is indeed filthy. A thin layer of dust has gathered on its screen and chassis, and small stains have gathered on its edges."

    show robovac sad

    pov "This could take awhile. Let's get a move on."

    "You approach the robovac with a wet washcloth and it begins to turn away."
    "You're able to lock it in place long enough to wipe it most of the way clean, though it beeps and whines the whole time."

    show robovac dazed

    robovac "..."

    jump threaten_choice




label task_three_neglect:

    show robovac sad

    $ prompt = "Speaking of which..."

    "Yeah, you have better things to do today. It'll take care of itself if it really needs it."

    jump neglect_choice

label neglect_choice:

    if wheels and tank and spa:

        $ neglect += 1
        jump task_three_end
    
    menu:
        "I need dinner. Let's see what's in the fridge." if not wheels:
            $ wheels = True
            jump neglect_wheels

        "I've been meaning to finish a couple games...I should get on those." if not tank:
            $ tank = True
            jump neglect_tank


        " I really ought to treat myself to a nice bath or something, it's been awhile." if not spa:
            $ spa = True
            jump neglect_spa

label neglect_wheels:
    $ prompt = "Hmm. Now what should I do?"
    
    "You meander towards the kitchen area and root through the fridge."

    pov "Yogurt. Cheese. Leftover spaghetti? Eh."

    "There is a slight commotion coming from the other side of the apartment the entire time that you search, mostly shuffling and frustrated beeping."

    show robovac angry

    "By the time you return with your dinner, the robovac is driving in little circles and bweep-booping complaintively."
    "It's also sucking up little balls of hair and carpet fiber that weren't there before. Its wheels sound better at least."

    jump neglect_choice
        
label neglect_tank:
    $ prompt = "Hmm. Now what should I do?"

    "You flop on the couch and pick up a controller. Your console launches and bathes the room in bright light while a cheery boot jingle plays."

    pov "Hmm."

    "You are reminded almost immediately why you have so many unfinished games. They're either terrible or you aren't very good at them."
    "Still, you cave and load something simple."
    "The whole time you play, you can hear noises from the kitchen area, clicks and clacks, and then something being dumped into the trash."

    show robovac scared

    "Your robovac returns at some point. It seems somehow lighter, though who can say why?"
    
    jump neglect_choice

label neglect_spa:
    $ prompt = "Hmm. Now what should I do?"

    "Ah, now that's a good idea."
    "You set up in the bathroom: now it's time to get serious."
    "You run the water hot and throw in whatever you have beneath the sink. Bubble bath, epsom salt..."

    pov "...how old is this bath bomb? Do bath bombs expire?"

    "Doesn't matter, into the drink it goes. A few candles, some soothing jazz, and you're all set."
    "You let the minutes slip by, you become one with the water, with the tub. You become soup."
    "All good things must come to an end. The water has cooled down and your skin has the same texture as a bag of prunes"
    "-but you've also let go of some tension that you didn't even know you had."

    show robovac dazed

    "As you dress and return to the living room, you spot the robovac. It seems...cleaner?"
    
    "You couldn't hear a thing over the jazz, but it looks like it somehow managed to spill water on itself. Was it trying to bathe on its own?"
    pov "Well, I guess it's fine as long as you haven't left a mess."
    robovac "..."

    jump neglect_choice




label task_three_end:
    window hide
    scene black with dissolve
    stop music fadeout 0.5
    
    pause 2.0
    
    jump ending

    