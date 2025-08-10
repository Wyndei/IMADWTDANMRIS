



label init_scene:

    scene black

    stop music


    python:
        name = renpy.input("What is my name?", length = 32) 
        name = name.strip()

        if not name:
            name = "Fard"
    

    jump intro_scene