



label init_scene:

    scene black

    stop music fadeout 0.5


    python:
        name = renpy.input("What is my name?", length = 10) 
        name = name.strip()

        if not name:
            name = "Awbee"
    

    jump intro_scene