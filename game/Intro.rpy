




define devil = DynamicCharacter("[devil_name]", image = "devil")

define robovac = DynamicCharacter("[robovac_name]", image = "robovac")

label intro_scene:

    $ devil_name = "???"

    $ robovac_name = "robovac"



    pov "What a day, work really took it out of me."

    "Your apartment is quiet, save for the distant drone of traffic." 
    "The gentle glow of the setting sun begins to fade through the doorway window, leaving only the soft, flat artificial lighting of your apartment."

    "Your shoes squeak against the spotless floor, reminding you to take them off"

    pov "Thank goodness I've got that robovac. I just wish I had someone to hang out with too."

    devil "I think I could be of assistance then."

    "A silhouette stretches unnaturally across the wall, jagged edges curl and loom upwards. It suddenly feels too hot and too cold all at once."

    pov "Wha—what? Who are you? How did you get into my apartment?"

    devil "Huh? No, that's my shadow. I'm down here."

    "{i}You look down.{/i}"

    #visual smol devil
    show devil normal at left with dissolve

    devil "Thank you."

    pov "..."

    "A figure steps into the overhead light of your apartment, shadow shrinking rapidly as it approaches, until you're staring at... a barely palm sized imp with stubby horns and a mischievous grin. They seem all too confident for their size."

    devil "???"

    pov "...well?"

    devil "Oh, right! You want a friend, and I can help!"

    menu:
        "Are you some kind of bug?":
            #devil mad
            devil "No! How can you not see it, I'm The Devil! From Hell? You know, Satan."
            "The tiny demon emphasizes their name, crossing their arms indignantly"
            

        "What are you":
            #devil happy
            devil "Isn't it obvious? I'm the Devil!"
            "They strike a pose, drawing attention to their horns and glowing eyes. Their little demon's tail flicks with amusement"
            

        "...Is there a gas leak in here?":
            #devil happy
            devil "No, silly goose! I'm The Devil!"
            "The little devil giggles, apparently delighted by your confusion."
            

    $ devil_name = "Devil"

    pov "...Okay."

    #devil happy

    "Suddenly, the devil breathes in deeply while raising their little arms. They close their eyes in concentration."

    devil "You want a friend to hang out with?"

    pov "...Yes?"

    #devil happy

    devil "Alright, deal!"

    hide devil

    "The tiny demon snaps their fingers and vanishes in a plume of smoke. The air still tingles with static electricity as the temperature suddenly returns to normal."
    
    pov "What? I didn't agree to anything."

    "There is no further sign of the creature. You don't feel any different. You pat your own chest and then the wall as if checking you're still real."
    
    pov "Did you take my soul"
    pov "You didn't take my soul, right"

    "A cheerful beeping emits from the other side of your apartment, and something comes rolling around the corner…"

    show robovac neutral at left with dissolve

    pov "Oh. {i}Oh no{/i}"

    "The machine slows to a stop at your feet. Its LED display lights come on by themselves, and then it blinks twice. It feels like it's...watching you."

    pov "...Are you...alive?"
    
    robovac happy "{i}Beeps cheerfully{/i}"
    
    jump task_one
