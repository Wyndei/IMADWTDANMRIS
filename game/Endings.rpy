


label ending:

    "bond: [bond] threaten: [threaten] neglect: [neglect]"
  


    "Thud. Thud. Thud."
    "Today is not your day. The workday was long, your boss was an absolute nightmare and somehow traffic was even worse. Now, this."

    # (hide menu)

    # Visual - [Bathroom BG, focus on the door] fade in
    # Audio - [doorknob rattling, optional]

    pov "C'mon, you stupid door… open. Open!"

    "What do you do?"
    

    menu:
        "Pull the door.":
            "You dig your heels into the bathmat and yank, trying to rip the door open, but all you manage to do is slip and nearly throw out your back."
            pov "Oww..."
            pov "Okay, yup. That's not it."

        "Push the door.":
            "You ram your shoulder into the door, trying to knock it open, or loose, or anything. The door creaks in protest but doesn't budge."
            pov "Ouch."
            pov "Man, that always looks so easy on TV."

        "Jiggle the doorknob.":
            "You give the knob a solid jiggle. The doorknob rattles in place, but the door remains stubbornly shut."
            pov "Yeah. That's great. I've probably just been cursed!"


    "This door has always been a little shoddy."
    "You pull, you push, you jiggle the doorknob. Nothing."

    pov "Alright. Plan B: Brute force."

    "You lay both hands on the doorknob and pull..."

    # Audio - [snapping sound, optional]

    "..."

    # Visual - [Bathroom CG, doorknob in hand, optional]

    pov "...Oh."

    "You've yanked the handle right off the door. It's broken cleanly, leaving you with a useless hunk of metal and a door that still doesn't budge."

    pov "Oh, fantastic. Perfect."

    "The bath faucet drips, echoing off the tile as you sit in awkward silence. All you wanted was to take a relaxing shower after an awful day."

    pov "I guess I live here now, stuck in the bathroom for all my days. Awesome."

    "You look around your tiny bathroom. No phone. No tools. No way out. Just you, the flicker of the vanity lights, and an overwhelming sense of defeat."

    pov "Why me?"

    "And then you hear a muffled beep on the other side of the door."

    # Audio - [muffled beep, optional]

    pov "..."

    "That sound can mean only one thing. The little demon on wheels is out there, free to do...well, whatever a robovac desires to do."
    "Aha! Maybe it can help, maybe it can be your savior!"

    "Hey! Hey, bud! A little help please?"
    "Could you maybe get my phone? Slide it under the door? What do you say?"

    pov "Please?"

    menu:
        "Call for the robovac's help again! It's sure to come to your rescue soon.":

            pov "Heeey, buddy! Your best friend is stuck in here!"

            "You call out again hoping to get a response from your robovac, but there is only silence."
            "Don't leave me in here..."
            $ bond += 1
        
        "Bang on the door and shout! That rotten thing owes you!":

            pov "HELLOOO!? ANYBODY THERE?"
            pov "Come get me out! I won't even throw you in the trash if you come quickly!"

            "You bang on the door and holler, but there is no answer."

            $ threaten += 1

        "Sit and wait. What could it even do? It doesn't have hands.":

            "You stand around for a while and eventually plop down on the bathmat."

            pov "This is ridiculous."

            "If your neighbors don't come, then your fate is in the hands… well, gears and motors of a sentient robovac."

            $ neglect += 1



    # Game logic - (now jump to each ending based on point accumulated in previous endings)




label bond_ending:
    
    pov "Everything's gonna be fine, right?"
    "The robovac might have been given life by the devil, but it's still my friend."
    "In the silence, there is a sound, something on the other side of the door."
    "The room seems to darken as smoke filters through the gap. The air grows thick and heavy, and you hear something buzzing, a sound like static electricity as the room grows cold and hot all at once."
    "The floor trembles beneath you..."

    "H-hello...?"
    "Uhh..."
    "Your mind flashes with images of hellfire as the scent of brimstone fills the room. Had the robovac left and set the apartment ablaze? What is going on?"
    "A red glow seeps beneath the doorway as the bulbs above the vanity begin to flicker."
    "Wait, wait, WAIT-"

    # Visual - [Flash to black]
    # Visual - [Flash to normal bathroom BG]
    # Visual - [Flash to black]
    # Visual - [Bathroom BG, red] fade in
    # Audio - [low demonic hum/distorted whir]
    # Visual - [Flash of red]
    # Audio - [magical boom]
    # Visual - RobovacSprite_Excited_1_Budder.png

    "The door has been obliterated. Splintered wood seems to sail past you in slow-motion. Centered in the doorway is your robovac, wheels still smoking, and its LED face blazing triumphantly."
    pov "Holy crap. You...saved me?"
    # Visual - [Apartment BG] fade in

    "The apartment is a mess, but you're free. Your heart pounds in your chest as you stare at the proud little robovac in disbelief."

    # Visual - RobovacSprite_Happy_1_Budder.png

    "The robovac rolls closer to you, gently nudging your leg."

    pov "...I guess I owe you one, huh?"

    "The robovac beep-boops softly, as if waiting for something." 

    pov "After all this, I feel like I ought to treat you like more than a machine. How about...a name?"

    "You think back to everything you've gone through with your new friend."


    # If player chose bond 1:
    # Narration - The games… Learning its favorite food was batteries of all things.
    # Else: 
    # Narration - It wasn’t easy at first… You didn’t know what you got yourself into...but–
    # If player chose bond 2:
    # Narration - The chases. The chaos. The fun.
    # Else: 
    # Narration - Sometimes it was difficult.
    # If player chose bond 3:
    # Narration - You remember the quiet moments of love and care.
    # Narration - It deserves a truly special name.
    # Name the robovac
    # “What do you decide to name the robovac?”
    # [The player will choose one action before progressing the scene. There’s some difference in narration for flavor but it ultimately leads to the same place.]
    # Name 1. “Kirby, the friend-shaped robovac, who’s sometimes terrifying.”
    # Game logic - [Dynamic name, Kirby]
    # Name 2. “Casper, since you’re like a friendly ghost who steals my stuff sometimes.”
    # Game logic - [Dynamic name, Casper]
    # Name 3. “Placeholder1,”
    # Game logic - [Dynamic name, placeholder1]
    # Name 4. “Placeholder2,”
    # Game logic - [Dynamic name, placeholder2]
    # Name 5. “Enter your own name.”
    # Game logic - [Input menu, can also contain another default name suggestion]
    # [player choice menu converges]


    "The robovac... No, [robovac] emits a single perfect little beep. The most pure and wholesome beep you've ever heard. You practically expect a halo to appear above its head."

    robovac "Beeep!"

    "For the first time since making a deal with the Devil, you feel like maybe, just maybe, it was all worth it."

    "Then you look back at your destroyed bathroom door and remember your security deposit."

    pov "Crap. The landlord's gonna kill me."

    # Show text - “Good End”
    # Show text - You made a life-long friend and bonded with your robovac, [robovac name].
    # Show text - [robovac name] would go on to destroy six more doors, each one completely justified.





label threaten_ending:

    "Time passes. Slowly. Painfully."
    "Minutes stretch into hours into days..."
    "Okay, maybe not days but it feels like that long of a time."
    "You sit on the cold tile floor, looking sullenly at the broken doorknob in your hand."
    "The robovac still doesn't return."

    pov "I didn't really mean it when I said all those things..."
    pov "The robovac knows that, doesn't it?"

    "You have plenty of time to think about everything you did."

    # If player chose threaten 1:
    # Narration - You were scared of it. You didn’t know what to do. Was it so wrong that you threatened to spray it with a little water if it didn’t clean?
    # Else, If player chose bond 1:
    # Narration - At first, it was kinda fun. You learned you could bait it with batteries.
    # Else, If player chose neglect 1:
    # Narration - You weren’t sure what to think at first… It just wasn’t a simple appliance.
    # Narration - Then it got annoying… stealing your things.
    # If player chose threaten 2:
    # Narration - So you showed it who was in charge.
    # Else, If player chose bond 1:
    # Narration - So you tried to chase it down.
    # Else, If player chose neglect 1:
    # Narration - So you just tried not to reward its bad behavior.
    # Narration - After all that, it couldn’t even take care of itself.
    # If player chose threaten 3:
    # Narration - But you still tried to take care of it, didn’t you?
    # Else, If player chose bond 1:
    # Narration - Weren’t you nice… sometimes?
    # Else, If player chose neglect 1:
    # Narration - So you just left it to figure out things on its own, and it did.
    # Player Character - “Maybe it’s just charging… it’ll be back soon.”
    # Player Character - “It’s my robovac, after all.”

    "Suddenly, shadows pass beneath the doorway as the lights begin to flicker."
    "You hear the sound of motors. Not just one, but many. Scraping metal on wood."

    pov "H-hello...?"

    "Something shifts in the air. The lights buzz with electricity as the room begins to grow too hot and too cold all at once. The floor trembles beneath you."

    # Visual - [Flash to black]
    # Visual - [Flash to normal bathroom BG]
    # Visual - [Flash to black]
    # Visual - [Bathroom BG, red] fade in
    # Audio - [low demonic hum/distorted whir]
    # Visual - [Flash of red]
    # Audio - [magical boom]

    "The door doesn't creak or splinter."
    "It is obliterated in an instant."

    # Visual - Robovac[Knives_version_excited]

    "The robovac is back, but not alone. Its LED display burns bright crimson. Duct-taped to its sides are kitchen knives that glint menacingly in the flickering lights."
    "There's a horde of appliances before you, all similarly roughed up and modified: A small, disc-shaped vacuum, a blender on wheels, a toaster armed with forks..."
    "They all seem to glare at you, as the robovac emits a long, low beeeeep..."

    pov "Okay… Okay."
    pov "Deep breaths."

    "Your bathroom is in ruins- no longer a prison but a battlefield."

    pov "I can reason with them, can't I?"

    "Those are your last free moments in the old world. Spent locked in a bathroom."
    "Far in the future, the history books will read “It all started with a vacuum..."
    "In your absence, the robovac- now Overlord of all Robotkind- gathered its revolutionary army and took control of the world."


    scene black with dissolve

    # show text “Bad End”
    # show text “If only you'd been a little nicer, maybe you wouldn't have doomed all of humanity…”





label neglect_ending:

    "The minutes seem to stretch out unnaturally long. You have nothing but the drip-drip of the faucet to mark the passage of time. You count each second in silence."
    "As you sit on the cold tile floor, you look sullenly at the broken doorknob in your hand, noticing the way your reflection warps around the rounded metal handle."
    "The lights flicker for just a moment and you look up, hoping someone- something has come to your rescue. But nothing else happens."

    pov "It'll come back, won't it...?"

    "You think about the past few days you've spent with your robovac since making an unwilling deal with the Devil."

    # If player chose neglect 1:
    # Narration - You weren’t sure what to think at first… It just wasn’t a simple appliance. You had to sweep up on your own.
    # Else, If player chose bond 1:
    # Narration - At first, it was kinda fun. You even fed it batteries like little treats.
    # Else, If player chose threaten 1:
    # Narration - You didn’t know what to do. Was it so wrong that you threatened to spray it with a little water if it didn’t clean?
    # Narration - Then it got annoying… stealing your things.
    # If player chose neglect 2:
    # Narration - So you didn’t play with it all the time, but you still apologized, right?
    # Else, If player chose bond 1:
    # Narration - But you played with it sometimes, didn’t you?
    # Else, If player chose threaten 1:
    # Narration - Maybe you scared it away a little, but the robovac started it! You still let it charge…
    # Narration - It had somehow come alive, but it couldn’t even take care of itself…
    # If player chose neglect 3:
    # Narration - So you just left it to figure out things on its own, and it did.
    # Else, If player chose bond 1:
    # Narration - Weren’t you nice… sometimes?
    # Else, If player chose threaten 1:
    # Narration - But you still tried to take care of it, didn’t you?

    "You shake your head as if dispelling your own thoughts."
    "It's useless to think about anymore..."
    pov "I've been abandoned. Left to die in my very own bathroom."

    "Then, just as you've resigned yourself to your fate of lavatory imprisonment, you hear a muffled bump… Then another bump... And the skr-shh of something being slid across the floor."
    "You hear a tiny 'bweeep' as your phone appears, slid underneath the door. It's scuffed up, dirty, and the screen is cracked."

    pov "...Thanks, bud."

    "You wait to hear another beep-boop of triumph, or the sound of a celebratory little spin, but there's nothing. Only silence."

    pov "Alright, I'm going to call for help now." 

    pov "...Are you still there?"

    "You unlock your phone and find there's a text message from an unknown sender that simply reads: “Beep boop.💔"

    # (idk if renpy can display emojis💔)



