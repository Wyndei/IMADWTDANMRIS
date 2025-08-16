




define devil = DynamicCharacter("[devil_name]", image = "devil")

define robovac = DynamicCharacter("[robovac_name]", image = "robovac")

label intro_scene:


    $ devil_name = "???"

    $ robovac_name = "robovac"

    
    play sound "footsteps_enter.mp3"

    window hide dissolve
    pause 5.0
    window show dissolve

    pov "What a day, work really took it out of me."


    stop sound
    play music ["apartment.mp3"] fadeout 0.5 fadein 0.5

    "Your apartment is quiet, save for the distant drone of traffic." 
    "The gentle glow of the setting sun begins to fade through the doorway window, leaving only the soft, flat artificial lighting of your apartment."

    scene apartment_2b with fade

    "Your shoes squeak against the spotless floor, reminding you to take them off"

    pov "Thank goodness I've got that robovac. I just wish I had someone to hang out with too."
    
    
    devil "I think I could be of assistance then."

    stop music fadeout 0.5

    play sound "demonic_hum.mp3"
    scene devil_shadow with fade

    "A silhouette stretches unnaturally across the wall, jagged edges curl and loom upwards. It suddenly feels too hot and too cold all at once."

    pov "Wha—what? Who are you? How did you get into my apartment?"

    devil "Huh? No, that's my shadow. I'm down here."

    "{i}You look down.{/i}"

    stop sound
    play music ["apartment.mp3"] fadeout 0.5 fadein 0.5
    scene devil_reveal with fade


    devil "Thank you."

    pov "..."

    devil "..."

    pov "...well?"

    devil "Oh, right!" 
    devil "You want a friend, and I can help!"

    scene apartment_2b with fade
    show devil normal

    menu:
        "..."
        "Are you some kind of bug?":
            show devil angry
            devil "No! How can you not see it, I'm The Devil! From Hell? You know, Satan."
            "The tiny demon emphasizes their name, crossing their arms indignantly"
            

        "What are you":
            show devil happy
            devil "Isn't it obvious? I'm the Devil!"
            "They strike a pose, drawing attention to their horns and glowing eyes. Their little demon's tail flicks with amusement"
            

        "...Is there a gas leak in here?":
            show devil happy
            devil "No, silly goose! I'm The Devil!"
            "The little devil giggles, apparently delighted by your confusion."
            

    $ devil_name = "Devil"

    pov "...Okay."

    show devil happy

    devil "That's it? 'Okay?' I can help you out, watch this!"

    "Suddenly, the devil breathes in deeply while raising their little arms. They close their eyes in concentration."

    devil "You want a friend to hang out with?"

    pov "...Yes?"

    devil "Alright, deal!"

    hide devil


    "The tiny demon snaps their fingers and vanishes in a plume of smoke. The air still tingles with static electricity as the temperature suddenly returns to normal."

    pov "What? I didn't agree to anything."

    "There is no further sign of the creature. You don't feel any different. You pat your own chest and then the wall as if checking you're still real."
    
    pov "Did you take my soul"
    pov "You didn't take my soul, right"

    
    play sound "cheerful_beeps.mp3"
    "A cheerful beeping emits from the other side of your apartment, and something comes rolling around the corner..."

    show robovac happy with moveinleft 

    pov "Oh. {i}Oh no{/i}"

    "The machine slows to a stop at your feet. Its LED display lights come on by themselves, and then it blinks twice. It feels like it's...watching you."

    pov "...Are you...alive?"

    play sound "excited_beeps.mp3"
    robovac "{i}Beeps cheerfully{/i}"
    
    window hide
    scene black with dissolve
    stop music fadeout 0.5
   
    pause 2.0

    jump task_one
