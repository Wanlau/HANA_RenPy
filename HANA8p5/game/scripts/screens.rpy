screen say(who, what, side_image=None, two_window=False):

    window:
        id "window"


        background Transform("images/ui/window.png",alpha=persistent.window_opacity)

        has vbox:
            style "say_vbox"

        if who:
            text who id "who"

        text what id "what"

    use quick_menu


screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.4

        vbox:
            style "menu"
            spacing 24

            for i,n in zip(items,[choice1,choice2]):

                button:
                    action i[1]

                    if not i[2]:
                        style "menu_choice_button"
                        text i[0] style "menu_choice"
                    else:
                        style "menu_choice_chosen_button"
                        text i[0] style "menu_choice_chosen"

                    at n


init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is say_thought clear:

        yoffset -1
        xalign 0.5
        outlines [(0,"#000000A0",2,2)]

    style menu_choice_chosen is menu_choice:
        color "#C0C0C0"

    style menu_choice_button is button clear:

        xminimum 500
        yminimum 40
        background Frame("images/ui/choice_idle.png")
        hover_background Frame("images/ui/choice_hover.png")
        xpadding 16


    style menu_choice_chosen_button is menu_choice_button:
        background Frame(im.MatrixColor("images/ui/choice_idle.png",im.matrix.saturation(0.2)))
        hover_background Frame("images/ui/choice_hover.png")




    transform choice1:
        alpha 0.0 yanchor 10
        easein 0.75 alpha 1.0 yanchor 0
    transform choice2:
        alpha 0.0 yanchor 50
        easein 0.75 alpha 1.0 yanchor 0
    transform choice3:
        alpha 0.0 yanchor 90
        easein 0.75 alpha 1.0 yanchor 0
    transform choice4:
        alpha 0.0 yanchor 130
        easein 0.75 alpha 1.0 yanchor 0
    transform choice5:
        alpha 0.0 yanchor 170
        easein 0.75 alpha 1.0 yanchor 0
    transform choice6:
        alpha 0.0 yanchor 210
        easein 0.75 alpha 1.0 yanchor 0

    style language_window is menu_window:
        align (0.5, 0.5)

screen main_menu():
    tag menu

    imagemap:
        ground "images/ui/title_ground.png"
        idle "images/ui/title_idle.png"
        hover "images/ui/title_hover.png"
        selected_idle "images/ui/title_selected_idle.png"
        selected_hover "images/ui/title_selected_hover.png"

        alpha False

        hotspot (630,345,150,46) action Start()
        hotspot (630,395,150,46) action ShowMenu("load")
        hotspot (630,445,150,46) action ShowMenu("extra")
        hotspot (630,495,150,46) action ShowMenu("options")
        hotspot (630,545,150,46) action Quit(confirm=True)

    add "images/ui/logo.png" xpos 12 ypos 16

    on "replace" action Play("music","bgm/M01.ogg",if_changed=True)


screen save():
    tag menu

    imagemap:
        ground "images/ui/file_ground_save.png"
        idle "images/ui/file_idle.png"
        hover "images/ui/file_hover.png"
        selected_idle "images/ui/file_selected_idle.png"
        selected_hover "images/ui/file_selected_hover.png"
        insensitive "images/ui/file_insensitive.png"
        alpha False


        for i in range(1,6):

            $ file_name = FileSlotName(i,10)
            $ file_time = FileTime(i, format='%Y年%m月%d日 %H:%M', empty="")
            $ save_name = FileSaveName(i)

            hotspot (20,75 + ((i-1) * 95),370,90):

                action FileAction(i)

                add FileScreenshot(i) xpos 9 ypos 9
                if not persistent.hide_savename:
                    text "\n[save_name!t]" style "save_slot"
                text "[file_name]. [file_time!t]" style "save_slot" size 16

                key "save_delete" action FileDelete(i)


        for i in range(1,6):

            $ file_name = FileSlotName(i + 5,10)
            $ file_time = FileTime(i + 5, format='%Y年%m月%d日 %H:%M', empty="")
            $ save_name = FileSaveName(i + 5)

            hotspot (410,75 + ((i-1) * 95),370,90):

                action FileAction(i + 5)

                add FileScreenshot(i + 5) xpos 9 ypos 9
                if not persistent.hide_savename:
                    text "\n[save_name!t]" style "save_slot"
                text "[file_name]. [file_time!t]" style "save_slot" size 16

                key "save_delete" action FileDelete(i + 5)


        hotspot (680,550,100,40) action Return()
        hotspot (297,25,68,32) action FilePage("auto")
        hotspot (367,25,68,32) action FilePage("quick")
        hotspot (437,25,32,32) action FilePage(1)
        hotspot (472,25,32,32) action FilePage(2)
        hotspot (507,25,32,32) action FilePage(3)
        hotspot (542,25,32,32) action FilePage(4)
        hotspot (577,25,32,32) action FilePage(5)
        hotspot (612,25,32,32) action FilePage(6)
        hotspot (647,25,32,32) action FilePage(7)
        hotspot (682,25,32,32) action FilePage(8)
        hotspot (717,25,32,32) action FilePage(9)
        hotspot (752,25,32,32) action FilePage(10)


    if persistent.controls == 0:
        key "K_ESCAPE" action Return()

screen load():
    tag menu

    imagemap:
        ground "images/ui/file_ground_load.png"
        idle "images/ui/file_idle.png"
        hover "images/ui/file_hover.png"
        selected_idle "images/ui/file_selected_idle.png"
        selected_hover "images/ui/file_selected_hover.png"
        insensitive "images/ui/file_insensitive.png"
        alpha False


        for i in range(1,6):

            $ file_name = FileSlotName(i,10)
            $ file_time = FileTime(i, format='%Y年%m月%d日 %H:%M', empty="")
            $ save_name = FileSaveName(i)

            hotspot (20,75 + ((i-1) * 95),370,90):

                action FileAction(i)
                add FileScreenshot(i) xpos 9 ypos 9
                if not persistent.hide_savename:
                    text "\n[save_name!t]" style "save_slot"
                text "[file_name]. [file_time!t]" style "save_slot" size 16

                key "save_delete" action FileDelete(i)


        for i in range(1,6):

            $ file_name = FileSlotName(i + 5,10)
            $ file_time = FileTime(i + 5, format='%Y年%m月%d日 %H:%M', empty="")
            $ save_name = FileSaveName(i + 5)

            hotspot (410,75 + ((i-1) * 95),370,90):

                action FileAction(i + 5)
                add FileScreenshot(i + 5) xpos 9 ypos 9
                if not persistent.hide_savename:
                    text "\n[save_name!t]" style "save_slot"
                text "[file_name]. [file_time!t]" style "save_slot" size 16

                key "save_delete" action FileDelete(i + 5)


        hotspot (680,550,100,40) action Return()
        hotspot (297,25,68,32) action FilePage("auto")
        hotspot (367,25,68,32) action FilePage("quick")
        hotspot (437,25,32,32) action FilePage(1)
        hotspot (472,25,32,32) action FilePage(2)
        hotspot (507,25,32,32) action FilePage(3)
        hotspot (542,25,32,32) action FilePage(4)
        hotspot (577,25,32,32) action FilePage(5)
        hotspot (612,25,32,32) action FilePage(6)
        hotspot (647,25,32,32) action FilePage(7)
        hotspot (682,25,32,32) action FilePage(8)
        hotspot (717,25,32,32) action FilePage(9)
        hotspot (752,25,32,32) action FilePage(10)

    if persistent.controls == 0:
        key "K_ESCAPE" action Return()



init python:


    cg = Gallery()
    cg.transition = dissolve

    cg.locked_button = Solid((70, 6, 255, 75))
    cg.idle_border = Solid((0, 0, 0, 100))
    cg.locked = False

    cg.button('CU01')
    cg.unlock('CU01')
    cg.image(Solid('#fff'), 'CU01')

    cg.button('CU02')
    cg.unlock('CU02')
    cg.image(Solid('#fff'), 'CU02')

    cg.button('CU03')
    cg.unlock('CU03', 'CU03p1')
    cg.image(Solid('#fff'), 'CU03')
    cg.image(Solid('#fff'), 'CU03p1')

    cg.button('EV01')
    cg.unlock('EV01', 'EV01p1')
    cg.image('EV01')
    cg.image('EV01p1')

    cg.button('EV02')
    cg.unlock('EV02', 'EV02p1')
    cg.image('EV02')
    cg.image('EV02p1')

    cg.button('EV03')
    cg.unlock('EV03')
    cg.image('EV03')

    cg.button('EV04')
    cg.unlock('EV04', 'EV04p1')
    cg.image('EV04')
    cg.image('EV04p1')

    cg.button('EV05')
    cg.unlock('EV05', 'EV05p1')
    cg.image('EV05')
    cg.image('EV05p1')

    cg.button('EV06')
    cg.unlock('EV06')
    cg.image('EV06')

    cg.button('EV07')
    cg.unlock('EV07', 'EV07p1')
    cg.image('EV07')
    cg.image('EV07p1')

    cg.button('EV08')
    cg.unlock('EV08', 'EV08p1')
    cg.image('EV08')
    cg.image('EV08p1')

    cg.button('EV09')
    cg.unlock('EV09')
    cg.image('EV09')

    cg.button('EV10')
    cg.unlock('EV10')
    cg.image('EV10')

    cg.button('EV11')
    cg.unlock('EV11')
    cg.image('EV11')

    cg.button('EV12')
    cg.unlock('EV12', 'EV12p1')
    cg.image('EV12')
    cg.image('EV12p1')

    cg.button('EV13')
    cg.unlock('EV13', 'EV13p1')
    cg.image('EV13')
    cg.image('EV13p1')

    cg.button('EV14')
    cg.unlock('EV14')
    cg.image('EV14')

    cg.button('EV15')
    cg.unlock('EV15')
    cg.image('EV15')

    cg.button('EV16')
    cg.unlock('EV16', 'EV16p1')
    cg.image('EV16')
    cg.image('EV16p1')

    cg.button('EV17')
    cg.unlock('EV17', 'EV17p1')
    cg.image('EV17')
    cg.image('EV17p1')

    cg.button('EV18')
    cg.unlock('EV18')
    cg.image('EV18')

    cg.button('EV19')
    cg.unlock('EV19')
    cg.image('EV19')

    cg.button('EV20')
    cg.unlock('EV20')
    cg.image('EV20')

    playerList = [
        ("bgm/M01.ogg", "images/ui/bgm/M01.png"),
        ("bgm/M02.ogg", "images/ui/bgm/M02.png"),
        ("bgm/M03.ogg", "images/ui/bgm/M03.png"),
        ("bgm/M04.ogg", "images/ui/bgm/M04.png"),
        ("bgm/M05.ogg", "images/ui/bgm/M05.png"),
        ("bgm/M06.ogg", "images/ui/bgm/M06.png"),
        ("bgm/M07.ogg", "images/ui/bgm/M07.png"),
        ("bgm/M08.ogg", "images/ui/bgm/M08.png"),
        ("bgm/M09.ogg", "images/ui/bgm/M09.png"),
        ("bgm/M10.ogg", "images/ui/bgm/M10.png"),
        ("bgm/M11.ogg", "images/ui/bgm/M11.png"),
        ("bgm/M12.ogg", "images/ui/bgm/M12.png"),
        ("bgm/M13.ogg", "images/ui/bgm/M13.png"),
        ("bgm/M14.ogg", "images/ui/bgm/M14.png"),
        ("bgm/M15.ogg", "images/ui/bgm/M15.png"),
        ("bgm/M16.ogg", "images/ui/bgm/M16.png"),
        ("bgm/M17.ogg", "images/ui/bgm/M17.png"),
        ("bgm/M18.ogg", "images/ui/bgm/M18.png"),
        ("bgm/M19.ogg", "images/ui/bgm/M19.png"),
        ("bgm/M20.ogg", "images/ui/bgm/M20.png"),
        ("bgm/M21.ogg", "images/ui/bgm/M21.png"),
    ]

    mr = MusicRoom(fadeout=0.0, shuffle=False)

    for (track, image) in playerList:
        mr.add(track, always_unlocked=True, action=SetVariable("my_image", image))

init:
    default my_image = "images/ui/bgm/M01.png"
    


screen extra():
    tag menu

    default cg_page = 1

    on "replaced" action Play("music", "bgm/M01.ogg")

    imagemap:
        ground "images/ui/extra_ground.png"
        idle "images/ui/extra_idle.png"
        hover "images/ui/extra_hover.png"
        selected_idle "images/ui/extra_selected_idle.png"
        selected_hover "images/ui/extra_selected_hover.png"
        alpha False

        hotspot (302, 53, 31, 27) action mr.Previous()
        hotspot (358, 53, 25, 27) action mr.Play() selected renpy.music.is_playing()
        hotspot (406, 53, 27, 27) action mr.Stop()
        hotspot (454, 53, 32, 27) action mr.Next()
        hotspot (687, 117, 32, 32) action SetScreenVariable("cg_page", 1)
        hotspot (729, 117, 32, 32) action SetScreenVariable("cg_page", 2)
        hotspot (25, 534, 149, 40) action Return()

    add my_image pos (509, 43)

    if cg_page == 1:
        add cg.make_button("EV01", im.Scale("images/cg/EV01.png", 120, 90), xysize=(120,90)) pos (220, 170)
        add cg.make_button("EV02", im.Scale("images/cg/EV02.png", 120, 90), xysize=(120,90)) pos (360, 170)
        add cg.make_button("EV03", im.Scale("images/cg/EV03.png", 120, 90), xysize=(120,90)) pos (500, 170)
        add cg.make_button("EV04", im.Scale("images/cg/EV04.png", 120, 90), xysize=(120,90)) pos (640, 170)
        add cg.make_button("EV05", im.Scale("images/cg/EV05.png", 120, 90), xysize=(120,90)) pos (220, 270)
        add cg.make_button("EV06", im.Scale("images/cg/EV06.png", 120, 90), xysize=(120,90)) pos (360, 270)
        add cg.make_button("EV07", im.Scale("images/cg/EV07.png", 120, 90), xysize=(120,90)) pos (500, 270)
        add cg.make_button("EV08", im.Scale("images/cg/EV08.png", 120, 90), xysize=(120,90)) pos (640, 270)
        add cg.make_button("EV09", im.Scale("images/cg/EV09.png", 120, 90), xysize=(120,90)) pos (220, 370)
        add cg.make_button("EV10", im.Scale("images/cg/EV10.png", 120, 90), xysize=(120,90)) pos (360, 370)
        add cg.make_button("EV11", im.Scale("images/cg/EV11.png", 120, 90), xysize=(120,90)) pos (500, 370)
        add cg.make_button("EV12", im.Scale("images/cg/EV12.png", 120, 90), xysize=(120,90)) pos (640, 370)
        add cg.make_button("EV13", im.Scale("images/cg/EV13.png", 120, 90), xysize=(120,90)) pos (220, 470)
        add cg.make_button("EV14", im.Scale("images/cg/EV14.png", 120, 90), xysize=(120,90)) pos (360, 470)
        add cg.make_button("EV15", im.Scale("images/cg/EV15.png", 120, 90), xysize=(120,90)) pos (500, 470)
        add cg.make_button("EV16", im.Scale("images/cg/EV16.png", 120, 90), xysize=(120,90)) pos (640, 470)

    if cg_page == 2:
        add cg.make_button("EV17", im.Scale("images/cg/EV17.png", 120, 90), xysize=(120,90)) pos (220, 170)
        add cg.make_button("EV18", im.Scale("images/cg/EV18.png", 120, 90), xysize=(120,90)) pos (360, 170)
        add cg.make_button("EV19", im.Scale("images/cg/EV19.png", 120, 90), xysize=(120,90)) pos (500, 170)
        add cg.make_button("EV20", im.Scale("images/cg/EV20.png", 120, 90), xysize=(120,90)) pos (640, 170)





screen options():
    tag menu

    modal True

    imagemap:
        ground "images/ui/option_ground.png"
        idle "images/ui/option_idle.png"
        hover "images/ui/option_hover.png"
        selected_idle "images/ui/option_selected_idle.png"
        selected_hover "images/ui/option_selected_hover.png"
        alpha False

        hotspot (60,145,125,35) action [Preference("display", "window"),SelectedIf(not _preferences.fullscreen)]
        hotspot (215,145,125,35) action Preference("display", "fullscreen")
        hotspot (60,265,125,35) action Preference("skip", "seen")
        hotspot (215,265,125,35) action Preference("skip", "all")
        hotspot (530,115,65,30) action Preference("music mute", "disable")
        hotspot (615,115,65,30) action Preference("music mute", "enable")
        hotspot (530,235,65,30) action Preference("sound mute", "disable")
        hotspot (615,235,65,30) action Preference("sound mute", "enable")
        hotspot (680,235,65,30) action Play("sound","se/SE001.ogg")
        hotspot (530,355,65,30) action Preference("voice mute", "disable")
        hotspot (615,355,65,30) action Preference("voice mute", "enable")
        hotspot (680,355,65,30) action Play("voice","voice/Amane_1256.ogg")

        hotspot (425,489,181,40) action [Show("language_menu", transition=Dissolve(0.3)), Hide("options")]
        hotspot (636,489,101,40) action Return()

    bar pos (55, 403) value Preference("auto-forward time") style "slider"
    bar pos (55, 523) value Preference("text speed") style "slider"
    bar pos (455, 163) value Preference("music volume") style "slider"
    bar pos (455, 283) value Preference("sound volume") style "slider"
    bar pos (455, 403) value Preference("voice volume") style "slider"

    add "images/ui/option_text.png"

style slider:
    base_bar "images/ui/slider_idle.png"
    hover_base_bar "images/ui/slider_hover.png"
    left_gutter 6
    right_gutter 6
    unscrollable "insensitive"
    xsize 290
    ysize 20
    thumb "images/ui/thumb.png"


init python:

    class ChangeControl(Action):
        """Action to change controls between two choices."""
        
        def __init__(self,set):
            self.set = set
        def __call__(self):
            
            
            if self.set == 0 and not persistent.controls == 0:
                persistent.controls = 0
                
                if 'mouseup_3' in config.keymap['game_menu']:
                    config.keymap['game_menu'].remove('mouseup_3')
                config.keymap['hide_windows'].append('mouseup_3')
                if 'K_ESCAPE' in config.keymap['game_menu']:
                    config.keymap['game_menu'].remove('K_ESCAPE')
                config.keymap['hide_windows'].append('K_ESCAPE')
                
                                                
                config.keymap['toggle_skip'].append('mousedown_2')
                config.keymap['toggle_skip'].append('mouseup_2')
            
            
            if self.set == 1 and not persistent.controls == 1:
                persistent.controls = 1
                
                config.keymap['game_menu'].append('mouseup_3')
                if 'mouseup_3' in config.keymap['hide_windows']:
                    config.keymap['hide_windows'].remove('mouseup_3')
                
                config.keymap['game_menu'].append('K_ESCAPE')
                if 'K_ESCAPE' in config.keymap['hide_windows']:
                    config.keymap['hide_windows'].remove('K_ESCAPE')
                
                if 'mousedown_2' in config.keymap['toggle_skip']:
                    config.keymap['toggle_skip'].remove('mousedown_2')
                if 'mouseup_2' in config.keymap['toggle_skip']:
                    config.keymap['toggle_skip'].remove('mouseup_2')
            
            
            renpy.clear_keymap_cache()            
            
            renpy.restart_interaction()
        
        def get_selected(self):
            
            if self.set == 0 and persistent.controls == 0:
                self.changed = True
                return True
            elif self.set == 1 and persistent.controls == 1:
                self.changed = True
                return True
            else:
                return False



screen confirm(message, yes_action, no_action):

    modal True
    if main_menu:
        add Solid("#ffbffb")
    add "images/ui/yesno_ground.png" 
    imagemap:
        ground Fixed()
        idle "images/ui/yesno_idle.png"
        hover "images/ui/yesno_hover.png"
        xpos 206
        ypos 198
        alpha False
        hotspot (26,88,140,50) action yes_action
        hotspot (220,88,140,50) action no_action


    if (message==layout.ARE_YOU_SURE):
        add "images/ui/yesno_areyousure.png" xcenter 400 ypos 233
    if (message==layout.DELETE_SAVE):
        add "images/ui/yesno_delete.png" xcenter 400 ypos 233
    if (message==layout.OVERWRITE_SAVE):
        add "images/ui/yesno_save.png" xcenter 400 ypos 233
    if (message==layout.LOADING):
        add "images/ui/yesno_load.png" xcenter 400 ypos 233
    if (message==layout.QUIT):
        add "images/ui/yesno_quit.png" xcenter 400 ypos 233
    if (message==layout.MAIN_MENU):
        add "images/ui/yesno_mainmenu.png" xcenter 400 ypos 233
    if (message==layout.END_REPLAY):
        add "images/ui/yesno_extra.png" xcenter 400 ypos 233


    key "K_RETURN" action If(renpy.focus_coordinates() == (None,None,None,None),true=yes_action,false=NullAction())
    key "K_SPACE" action If(renpy.focus_coordinates() == (None,None,None,None),true=yes_action,false=NullAction())
    key "K_KP_ENTER" action If(renpy.focus_coordinates() == (None,None,None,None),true=yes_action,false=NullAction())
    key "hide_windows" action no_action
    key "K_ESCAPE" action no_action



screen quick_menu():



    imagemap:
        ground Fixed()
        idle "images/ui/quickmenu_idle.png"
        hover "images/ui/quickmenu_hover.png"
        selected_idle "images/ui/quickmenu_selected_idle.png"
        selected_hover "images/ui/quickmenu_selected_hover.png"
        insensitive "images/ui/quickmenu_insensitive.png"
        alpha False


        hotspot (49,572,69,28) action QuickSave()
        hotspot (118,572,69,28) action QuickLoad()
        hotspot (187,572,69,28) action ShowMenu("save")
        hotspot (256,572,69,28) action [ShowMenu("load"),SensitiveIf(not _in_replay)]
        hotspot (325,572,69,28) action Preference("auto-forward", "toggle")
        hotspot (394,572,69,28) action Skip()
        hotspot (463,572,69,28) action ShowMenu("options")
        if not _in_replay:
            hotspot (532,572,69,28) action MainMenu()
        else:
            hotspot (532,572,69,28) action EndReplay()

        hotspot (630,572,69,28) action VoiceReplay()
        hotspot (699,572,26,28) action Rollback()
        hotspot (725,572,26,28) action RollForward()



screen language_menu():
    tag menu
    add "images/ui/menu_ground.png"

    window:
        style "language_window"

        has vbox
        style "menu"
        spacing 20

        button:
            action If(persistent.language_set, true = Language(None), false = [Language(None), Hide('language_menu', transition=dissolve), Return()])
            text '{font=fonts/Tuffy-Regular.ttf}中文{/font}' size 22 pos (250, 19) style 'lang_text'
            style 'lang_button'

            if persistent.language_set:
                selected_background 'images/ui/choice_hover.png'

        button:
            action If(persistent.language_set, true = Language('Japanese'), false = [Language('Japanese'), Hide('language_menu', transition=dissolve), Return()])
            text '{font=fonts/NudMotoyMaru.ttf}日本語{/font}' size 22 pos (250, 20) style 'lang_text'
            style 'lang_button'

            if persistent.language_set:
                selected_background 'images/ui/choice_hover.png'

        button:
            action If(persistent.language_set, true = Language('English'), false = [Language('English'), Hide('language_menu', transition=dissolve), Return()])
            text '{font=fonts/Tuffy-Regular.ttf}English{/font}' size 22 pos (250, 19) style 'lang_text'
            style 'lang_button'

            if persistent.language_set:
                selected_background 'images/ui/choice_hover.png'

    if persistent.language_set:
        imagebutton:
            auto "images/ui/back_%s.png"
            action Show("options", transition=Dissolve(0.3))
            pos (660, 500)

        key "K_ESCAPE" action Return()
        key "mouseup_3" action Return()


style lang_text:
    anchor(0.5, 0.5)
    color '#FFF'
    outlines [(0, (0, 0, 0, 90), 1.5, 1), (0, (0, 0, 0, 45), 2, 1), (0, (0, 0, 0, 45), 2, 1.5)]

style lang_button:
    idle_background 'images/ui/choice_idle.png'
    hover_background 'images/ui/choice_hover.png'
    xysize(500, 40)