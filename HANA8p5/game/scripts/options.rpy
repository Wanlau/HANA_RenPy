init -1 python hide:
    
    config.developer = True
    config.screen_width = 800
    config.screen_height = 600
    
    config.window_title = u"花瓣！"
    config.name = "Hanahira!"
    config.version = "1.00"
    
    #config.windows_icon = "ui/icon.png"
    
    config.has_sound = True
    config.has_music = True
    config.has_voice = True
    config.voice_filename_format = "voice/{filename}.ogg"
    config.main_menu_music = "bgm/M01.ogg"
    config.help = None
    config.fade_music = 1.0
    
    config.skip_indicator = False
    config.autosave_slots = 10
    config.quicksave_slots = 10
        
    config.enter_transition = dissolve
    config.exit_transition = dissolve
    config.intra_transition = dissolve
    config.main_game_transition = fade2
    config.game_main_transition = fade2
    config.end_splash_transition = Dissolve(1)
    config.end_game_transition = fade2
    config.after_load_transition = fade2
    config.window_show_transition = windowin
    config.window_hide_transition = windowout
    config.enter_yesno_transition = dissolve
    config.exit_yesno_transition = dissolve
    config.enter_replay_transition = fade2
    config.exit_replay_transition = fade2
    config.say_attribute_transition = None

    config.thumbnail_width = 96
    config.thumbnail_height = 72
    config.default_music_volume = 0.5
    config.default_sfx_volume = 0.75
    config.default_voice_volume = 0.7
    config.default_fullscreen = False
    config.default_afm_time = 9.0
    config.default_emphasize_audio = False
    config.default_text_cps = 100

    persistent.window_opacity = 0.8
    persistent.controls = 0
    
    
    theme.roundrect(
            widget = "#0000",
            widget_hover = "#0000",
            widget_text = "#0000",
            disabled = "#0000",
            disabled_text = "#0000",
            label = "#0000",
            frame = "#0000",
            mm_root = "#0000",
            gm_root = "#0000",
            rounded_window = False,
            )

define config.window_icon = "images/ui/icon.png"
default lily_rank = 0

##for mobile phone 
define config.dispatch_gesture = None
define config.gestures = { "e_s" : "hide_windows", "e_n" : "hide_windows"}

python early:
    config.save_directory = "HANA08p5"


init python:
    build.directory_name = "HANA08p5"
    build.executable_name = "HANA08p5"
    build.include_update = False
    build.documentation('*.html')
    build.documentation('*.txt')
    build.documentation('*.md')

    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("voice", "all")
    build.archive("bgm", "all")
    build.archive("se", "all")
    build.archive("fonts", "all")

    build.classify("game/**.rpy", None)
    build.classify("game/**.rpyc", "scripts")
    build.classify("game/images/**.png", "images")
    build.classify("game/voice/*.ogg", "voice")
    build.classify("game/bgm/*.ogg", "bgm")
    build.classify("game/se/*.ogg", "se")
    build.classify("game/fonts/*", "fonts")

    build.classify("game/cache/**", None)
    build.classify("game/saves/**", None)
