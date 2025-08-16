


label task_two:

    
    window show
    pov "Nooo... Where is it...?"

    
    scene apartment_afternoon with dissolve 
    play music ["apartment.mp3"] fadeout 0.5 fadein 0.5
    
    

    "You pat your pockets, check the table, under the couch cushions, the kitchen counter, even in the fridge, but your phone is nowhere to be found." 



    pov "C'mon it has to be {i}somewhere{/i}"

    "And then you hear it: The sound of unholy beep-boops, beeping and booping from the other side of the apartment."       

    play sound "cheerful_beeps.mp3"
    show robovac mischief with dissolve
    show phone_off with moveinbottom

    "Your robovac sits in the doorway, smugly blinking as it holds your phone atop its head. It revs in place, as if beckoning you closer."

    pov "...Are you serious right now?"

    hide phone_off with moveoutbottom

    show robovac excited

    "The robovac's LED display lights up with irreverent excitement, and you know this is no accident- Oh no. It's messing with you now."
    "{i}It wants to play a game{/i}"

    menu:
        "Alright you rascal, you want to make a game out of this?":
            jump task_two_bond
        "You piece of junk. Let's see how {i}you{/i} like it if I take something of {i}yours{/i}...":
            jump task_two_threaten
        "Forget it. I'll get by without my phone for a few hours.":
            jump task_two_neglect




label task_two_bond:

    "The robovac lets out a series of gleeful beep-beep-beeps and dashes across the floor."

    pov "No, you don't-! C'mere!"

    "You leap after it, just narrowly missing the robovac as it swerves so sharply your phone wobbles precariously to one side."


    menu:
        "Grab at your phone!":
            "You throw yourself towards the robovac, arms outstretched to catch the falling phone!" 
            "but the little thief corrects itself at the last second. Your hands grab nothing but air as you skid across the floor."
        
        "Try to trap it in a corner!":
            "You charge ahead of the robovac, hoping to intercept it before it can turn!"
            "However, your timing is off and you overshoot. You stumble over your own coffee table and land face first into the couch cushions."



    "Your knees will remember this battle."

    #Audio - [Robovac, Happy robot beeps, high-pitched]
    play sound "cheerful_beeps.mp3"

    show robovac mischief

    "The robovac giggles delightedly, well, as much as it can in beep-boop-bweeps." 
    "Emboldened by your failures, it zooms away towards your little kitchen. The phone wobbles again- one wrong move and it's toast"


    menu:
        "Grab your broom and joust!":

            "You snatch your broom and charge at the menace. The robovac zigzags wildly, narrowly escaping each lunge."
            pov "En garde!"


        "Pretend to give up...Then attack!":

            "You freeze and then cross your arms, sighing dramatically. The robovac slows down, unsure..."

            # Audio - [Robovac, Excited robot beeps, high-pitched, like happy but rapid-fire]
            play sound "rapidfire_beeps.mp3"

            "Narration - Then, you make your move! You dive as it beeps and darts forward again, leaving you in its dust."


    
    show robovac happy
    "After several exhausting rounds of silliness, the robovac finally slows down, its battery light blinking red. It rolls to a stop, tilting forward to offer you your phone back."

    show robovac battery
    

    "With a gentle nudge, it lets out one last tired but affectionate beep. Its motor hums, purring gently."

    $ bond += 1
    jump task_two_end
    

label task_two_threaten:
    pov "Enough is enough, if you wanna keep messing with me, fine."

    "You march over to its charging dock and yank the cord free. The robovac freezes, LED eyes flickering in fear."

    pov "Two can play at this game."

    menu:
        "Wave the charger {i}menacingly{/i}.":
            "You dangle the charger cord in front of the robovac, spinning it up in the air a bit like a cowboy with a lasso. Its little wheels jitter nervously as it backs up a few inches."
            
            # Audio - [Scared/anxious robot beeps, low pitched]
            play sound "anxious_beeps.mp3"
            
            show robovac scared 
            
            pov "What? Now you don't want to play?"

        "Drag the charging dock closer to you.":
            show robovac scared 

            #Audio - [Scared/anxious robot beeps, low pitched]
            play sound "anxious_beeps.mp3"

            "You crouch down and pull the dock across the floor, keeping your eyes locked onto the robovac. The robovac creeps forward cautiously, almost pleadingly."
            pov "No, you don't! It's mine now. You take my phone; I take your charger."

        "The tension in the air could be cut with a knife."
        "Your phone still rests on the little robot's head, but the robovac refuses to move closer, caught between loyalty to its new treasure and its precious charger."


    show robovac angry

    # Audio - [Angy robot beeps, low droning sound]
    play sound "sulking_beeps.mp3"

    "Sparks of unnatural energy crackle faintly around its wheels. It seems to be glaring at you now."


    menu:
        "Pretend to plug it in, then snatch the phone away.":

            pov "C'mere, lil guy... You want your charger, don't you?"

            "You kneel down and slowly slide the cord towards the wall. The robovac inches closer, appearing hopeful..."
            "But at the last second you yank it back, dazing the little thief."

            show robovac dazed

            pov "Ahaha! Got you!"
            
            "You snatch the device away before it can recover, and bask in your deceit."


        "Make the final ultimatum.":
            "You walk over to your drawers and rummage through them, picking up a pack of triple-A batteries. You hold up the charger and then the batteries."
            window hide dissolve


            show pentasonic_batteries with moveinbottom
            pause 1.0

            window show 


            "Last chance, buddy."
            "No charger and no batteries for you until I get my phone back."

            show robovac angry

            "The robovac lets out a long, slow beeeeep of indignation that feels a bit like a robot swear, still glaring your way."
            "Ultimately, it relents. It turns around sharply, flinging your phone away and onto the floor."


    "The robovac rolls away slowly, sulking in a dark corner. Its low pitiful bweeps sound both resentful and now slightly demonic. You got your phone back, but at what cost?"

    

    hide pentasonic_batteries with moveoutbottom

    $ threaten += 1
    jump task_two_end


label task_two_neglect:

    "I have plenty else I can do."

    "You plop down onto the couch, arms crossed. Your phone remains perched on the little robo thief's head like a crown, but you refuse to give it the satisfaction of a chase."
    
    show robovac mischief

    # Audio - [Robovac, Excited robot beeps, high-pitched, like happy but rapid-fire]
    play sound "excited_beeps.mp3"


    "The robovac bweep-boops playfully as it tries again to get your attention."


    menu:
        "Try to relax on the couch.":

            "You lean back and take a deep breath, trying to relax. You will not be baited."

            show robovac neutral

            "The robovac zooms closer, giving a hopeful little beep. But you stay stone-faced."



        "Pick up a book.":

            "You grab the nearest book and pretend to be engrossed in it. The words blur together as you stare blankly at the page."

            show robovac neutral

            "The robot spins around in a circle, bumps your foot once, twice, and then three times, trying to provoke a reaction."
            "You flip a page of your book with exaggerated calm, taking in a deep breath."


    "The robot's cheerful beeping grows louder and more desperate, before slowing to a halt. Finally, it spins around and zips away, letting your phone clatter down to the floor."
    
    show robovac angry
    
    "Victory?"

    menu:
        "Pick up your phone.":
            "You wait about ten seconds after the robovac has left just to see if it comes back before sauntering over to scoop up your phone."

        "Call after it...?":
            pov "Hey, come back!"

            "Your words echo through the apartment, and you wait a few seconds to see if the little robovac will return. It doesn't."

            pov "Hmm."
    

    "With your phone in hand, you poke around on some of your apps for a minute before getting bored. You call out to the little robot again."
    "Hey, sorry I didn't want to play."
    
    # Audio - [Sulking or disappointed robot beeps, like a sad kazoo]
    play sound "sad_kazoo.mp3"
    
    "A single, sulking beep echoes out from the kitchen in reply."
    
    $ neglect += 1
    jump task_two_end




label task_two_end:
    
    window hide
    scene black with dissolve
    stop music fadeout 0.5
    
    pause 2.0
    
    jump task_three