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

    if not persistent.language_set:
        call screen language_menu
        $ persistent.language_set = True

    $ renpy.pause(delay=0.1,hard=True)
    show fuguriya with dissolve
    pause 3
    scene black with fade
    $ renpy.pause(delay=0.1,hard=True)
    return

label before_main_menu:

    if renpy.get_game_runtime() > 0:
        stop music fadeout 1.0
        play music "bgm/M01.ogg" fadein 1.0
        scene black

        show expression "images/ui/title_ground.png" with Dissolve(1.5)
        show expression "images/ui/title_idle.png" with Dissolve(1.5)
        show expression "images/ui/logo.png" with Dissolve(1.5):
            xpos 12 
            ypos 16
