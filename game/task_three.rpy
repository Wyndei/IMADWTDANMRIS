


label task_three:

    hide robovac

    window hide dissolve


    # Visual - [The main apartment bg] image fades in

    "It's been a few days. The robovac practically haunts your apartment, like a dust-eating poltergeist. It has become a fixture of the apartment..."

    show robovac sad
    
    "...for better or for worse. Today, though, it seems to be in rough shape...When was the last time you cleaned it?"

    # Audio - [Robovac beeps sadly]

    robovac - "..."
    "It rolls towards you. Its wheel motors grind audibly as it approaches, spitting up sparks. It looks pitiful, bumping gently into your foot as it stops."
    "The thing's probably stuffed with dirt."

    "choice here fard"




label task_three_bond:



    $ bond += 1
    jump task_three_end

label task_three_threaten:



    $ threaten += 1
    jump task_three_end


label task_three_neglect:




    $ neglect += 1
    jump task_three_end


label task_three_end:

    