label splashscreen:

    python:

        if persistent.controls == 0:
            
            config.keymap['game_menu'].remove('mouseup_3')
            config.keymap['hide_windows'].append('mouseup_3')
            
            config.keymap['game_menu'].remove('K_ESCAPE')
            config.keymap['hide_windows'].append('K_ESCAPE')
            
            config.keymap['toggle_skip'].append('mousedown_2')
            config.keymap['toggle_skip'].append('mouseup_2')
            
            renpy.clear_keymap_cache()

    $ renpy.pause(delay=0.1,hard=True)
    show stmichael with dissolve
    pause 3
    #show stmadoca with dissolve
    #pause 3
    $ renpy.pause(delay=0.1,hard=True)
    scene white with dissolve
    $ renpy.pause(delay=0.1)
    $ renpy.movie_cutscene("videos/op.mpg")
    scene black with fade
    $ renpy.pause(delay=0.1,hard=True)
    return

label before_main_menu:

    if renpy.get_game_runtime() > 0:
        stop music fadeout 1.0
        play music "bgm/bgm01.ogg" fadein 1.0
        scene black

        show expression "ui/title_ground.png" with Dissolve(1.5)
        show expression "ui/title_idle.png" with Dissolve(1.5)
