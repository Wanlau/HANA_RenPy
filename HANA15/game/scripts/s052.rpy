

label ending01:
    $ persistent.Ending01 = True
    scene black with None
    play music "bgm/bgm25.ogg" noloop
    show ending01

    python:
        if not _in_replay:
            _game_menu_screen = None
            _dismiss_pause = False
            _rollback = False
            renpy.pause(delay=212,hard=True)
            renpy.full_restart()
        else:
            _game_menu_screen = None
            renpy.pause(delay=212)
            _game_menu_screen = "save"
            renpy.end_replay()
