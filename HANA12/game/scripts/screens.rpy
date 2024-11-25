screen say(who, what, side_image=None, two_window=False):

    window:
        id "window"


        background Transform("ui/window.png",alpha=persistent.window_opacity)

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
        if len(items) == 2:
            yalign 0.4
        else:
            yalign 0.22

        vbox:
            style "menu"
            spacing 24


            for i,n in zip(items,[choice1,choice2,choice3,choice4,choice5,choice6]):

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
        background Frame("ui/choice_idle.png")
        hover_background Frame("ui/choice_hover.png")
        xpadding 16


    style menu_choice_chosen_button is menu_choice_button:
        background Frame(im.MatrixColor("ui/choice_idle.png",im.matrix.saturation(0.2)))
        hover_background Frame("ui/choice_hover.png")




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

screen main_menu():
    tag menu

    imagemap:
        ground "ui/title_ground.png"
        idle "ui/title_idle.png"
        hover "ui/title_hover.png"
        selected_idle "ui/title_selected.png"
        selected_hover "ui/title_selected.png"

        alpha False

        hotspot (630,345,150,46) action Start()
        hotspot (630,395,150,46) action ShowMenu("load")
        hotspot (630,445,150,46) action ShowMenu("extra")
        hotspot (630,495,150,46) action ShowMenu("preferences")
        hotspot (630,545,150,46) action Quit(confirm=True)

    on "replace" action Play("music","bgm/bgm01.ogg",if_changed=True)


screen save():
    tag menu

    imagemap:
        ground "ui/file_ground_save.png"
        idle "ui/file_idle.png"
        hover "ui/file_hover.png"
        selected_idle "ui/file_selected_idle.png"
        selected_hover "ui/file_selected_hover.png"
        insensitive "ui/file_insensitive.png"
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
        ground "ui/file_ground_load.png"
        idle "ui/file_idle.png"
        hover "ui/file_hover.png"
        selected_idle "ui/file_selected_idle.png"
        selected_hover "ui/file_selected_hover.png"
        insensitive "ui/file_insensitive.png"
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

    cg.locked_button = "ui/extra_cg_locked.png"
    cg.idle_border = "ui/extra_cg_idle.png"
    cg.locked = False

    cg.button("ev01")
    cg.unlock("ev01","ev01p1","ev01p2")
    cg.image("ev01")
    cg.image("ev01p1")
    cg.image("ev01p2")

    cg.button("ev02")
    cg.unlock("ev02","ev02p1","ev02p2")
    cg.image("ev02")
    cg.image("ev02p1")
    cg.image("ev02p2")

    cg.button("ev03")
    cg.unlock("ev03","ev03p1")
    cg.image("ev03")
    cg.image("ev03p1")
    cg.image("ev03p2")

    cg.button("ev04")
    cg.unlock("ev04","ev04p1","ev04p2")
    cg.image("ev04")
    cg.image("ev04p1")
    cg.image("ev04p2")

    cg.button("ev05")
    cg.unlock("ev05","ev05p1","ev05p2")
    cg.image("ev05")
    cg.image("ev05p1")
    cg.image("ev05p2")

    cg.button("ev06")
    cg.unlock("ev06","ev06p1","ev06p2")
    cg.image("ev06")
    cg.image("ev06p1")
    cg.image("ev06p2")

    cg.button("ev07")
    cg.unlock("ev07","ev07p1","ev07p2")
    cg.image("ev07")
    cg.image("ev07p1")
    cg.image("ev07p2")

    cg.button("ev08")
    cg.unlock("ev08","ev08p1","ev08p2")
    cg.image("ev08")
    cg.image("ev08p1")
    cg.image("ev08p2")

    cg.button("ev09")
    cg.unlock("ev09","ev09p1","ev09p2")
    cg.image("ev09")
    cg.image("ev09p1")
    cg.image("ev09p2")

    cg.button("ev10")
    cg.unlock("ev10","ev10p1","ev10p2")
    cg.image("ev10")
    cg.image("ev10p1")
    cg.image("ev10p2")

    cg.button("ev11")
    cg.unlock("ev11","ev11p1")
    cg.image("ev11")
    cg.image("ev11p1")

    cg.button("ev12")
    cg.unlock("ev12","ev12p1")
    cg.image("ev12")
    cg.image("ev12p1")

    cg.button("ev13")
    cg.unlock("ev13","ev13p1")
    cg.image("ev13")
    cg.image("ev13p1")

    cg.button("ev14")
    cg.unlock("ev14","ev14p1","ev14p2")
    cg.image("ev14")
    cg.image("ev14p1")
    cg.image("ev14p2")

    cg.button("ev15")
    cg.unlock("ev15","ev15p1")
    cg.image("ev15")
    cg.image("ev15p1")

    cg.button("ev16")
    cg.unlock("ev16","ev16p1")
    cg.image("ev16")
    cg.image("ev16p1")

    cg.button("ev17")
    cg.unlock("ev17","ev17p1")
    cg.image("ev17")
    cg.image("ev17p1")

    cg.button("ev18")
    cg.unlock("ev18","ev18p1")
    cg.image("ev18")
    cg.image("ev18p1")

    cg.button("ev19")
    cg.unlock("ev19","ev19p1")
    cg.image("ev19")
    cg.image("ev19p1")

    cg.button("ev20")
    cg.unlock("ev20")
    cg.image("ev20")


    mr = MusicRoom(single_track=True)

    mr.add("bgm/bgm01.ogg",always_unlocked=True)
    mr.add("bgm/bgm02.ogg",always_unlocked=True)
    mr.add("bgm/bgm03.ogg",always_unlocked=True)
    mr.add("bgm/bgm04.ogg",always_unlocked=True)
    mr.add("bgm/bgm05.ogg",always_unlocked=True)
    mr.add("bgm/bgm06.ogg",always_unlocked=True)
    mr.add("bgm/bgm07.ogg",always_unlocked=True)
    mr.add("bgm/bgm08.ogg",always_unlocked=True)
    mr.add("bgm/bgm09.ogg",always_unlocked=True)
    mr.add("bgm/bgm10.ogg",always_unlocked=True)
    mr.add("bgm/bgm11.ogg",always_unlocked=True)
    mr.add("bgm/bgm12.ogg",always_unlocked=True)
    mr.add("bgm/bgm13.ogg",always_unlocked=True)
    mr.add("bgm/bgm14.ogg",always_unlocked=True)
    mr.add("bgm/bgm15.ogg",always_unlocked=True)
    mr.add("bgm/bgm16.ogg",always_unlocked=True)
    mr.add("bgm/bgm17.ogg",always_unlocked=True)
    mr.add("bgm/bgm18.ogg",always_unlocked=True)
    mr.add("bgm/bgm19.ogg",always_unlocked=True)
    mr.add("bgm/bgm20.ogg",always_unlocked=True)
    mr.add("bgm/bgm21.ogg",always_unlocked=True)
    mr.add("bgm/bgm22.ogg",always_unlocked=True)
    mr.add("bgm/bgm23.ogg",always_unlocked=True)
    mr.add("bgm/bgm24.ogg",always_unlocked=True) 
    



screen extra():
    tag menu

    imagemap:
        ground "ui/title_ground.png"
        idle "ui/extra_idle.png"
        hover "ui/extra_hover.png"
        selected_idle "ui/extra_selected.png"
        selected_hover "ui/extra_selected.png"

        hotspot (630,395,150,46) action ShowMenu("extra_bgm")
        hotspot (630,445,150,46) action ShowMenu("extra_cg")
        hotspot (630,495,150,46) action ShowMenu("extra_scene")
        hotspot (630,545,150,46) action Return()


screen extra_bgm():
    tag menu

    default bgm_page = 1

    imagemap:
        ground "ui/extra_bgm_ground.png"
        idle "ui/bgm_idle.png"
        hover "ui/bgm_hover.png"
        selected_idle "ui/bgm_selected_idle.png"
        selected_hover "ui/bgm_selected_hover.png"
        alpha False

        hotspot (43,558,30,30) action SetScreenVariable("bgm_page",1)
        hotspot (73,558,30,30) action SetScreenVariable("bgm_page",2)
        hotspot (637,558,120,30) action ShowMenu("extra")


    if bgm_page == 1:
            imagemap:
                ground Null()
                idle "ui/bgm1_idle.png"
                hover "ui/bgm1_hover.png"
                selected_idle "ui/bgm1_selected_idle.png"
                selected_hover "ui/bgm1_selected_hover.png"
                alpha False
                hotspot (50,108,340,40) action Play("music","bgm/bgm01.ogg",fadeout=0)
                hotspot (50,168,340,40) action Play("music","bgm/bgm03.ogg",fadeout=0)
                hotspot (50,228,340,40) action Play("music","bgm/bgm05.ogg",fadeout=0)
                hotspot (50,288,340,40) action Play("music","bgm/bgm07.ogg",fadeout=0)
                hotspot (50,348,340,40) action Play("music","bgm/bgm09.ogg",fadeout=0)
                hotspot (50,408,340,40) action Play("music","bgm/bgm11.ogg",fadeout=0)
                hotspot (50,468,340,40) action Play("music","bgm/bgm13.ogg",fadeout=0)

                hotspot (410,108,340,40) action Play("music","bgm/bgm02.ogg",fadeout=0)
                hotspot (410,168,340,40) action Play("music","bgm/bgm04.ogg",fadeout=0)
                hotspot (410,228,340,40) action Play("music","bgm/bgm06.ogg",fadeout=0)
                hotspot (410,288,340,40) action Play("music","bgm/bgm08.ogg",fadeout=0)
                hotspot (410,348,340,40) action Play("music","bgm/bgm10.ogg",fadeout=0)
                hotspot (410,408,340,40) action Play("music","bgm/bgm12.ogg",fadeout=0)
                hotspot (410,468,340,40) action Play("music","bgm/bgm14.ogg",fadeout=0)
                
                
    elif bgm_page == 2:
            imagemap:
                ground Null()
                idle "ui/bgm2_idle.png"
                hover "ui/bgm2_hover.png"
                selected_idle "ui/bgm2_selected_idle.png"
                selected_hover "ui/bgm2_selected_hover.png"
                alpha False
                hotspot (50,108,340,40) action Play("music","bgm/bgm15.ogg",fadeout=0)
                hotspot (50,168,340,40) action Play("music","bgm/bgm17.ogg",fadeout=0)
                hotspot (50,228,340,40) action Play("music","bgm/bgm19.ogg",fadeout=0)
                hotspot (50,288,340,40) action Play("music","bgm/bgm21.ogg",fadeout=0)
                hotspot (50,348,340,40) action Play("music","bgm/bgm23.ogg",fadeout=0)

                hotspot (410,108,340,40) action Play("music","bgm/bgm16.ogg",fadeout=0)
                hotspot (410,168,340,40) action Play("music","bgm/bgm18.ogg",fadeout=0)
                hotspot (410,228,340,40) action Play("music","bgm/bgm20.ogg",fadeout=0)
                hotspot (410,288,340,40) action Play("music","bgm/bgm22.ogg",fadeout=0)
                hotspot (410,348,340,40) action Play("music","bgm/bgm24.ogg",fadeout=0)


screen extra_cg():
    tag menu

    default cg_page = 1

    imagemap:
        ground "ui/extra_cg_ground.png"
        idle "ui/cg_idle.png"
        hover "ui/cg_hover.png"
        selected_idle "ui/cg_selected_idle.png"
        selected_hover "ui/cg_selected_hover.png"
        alpha False

        hotspot (43,558,30,30) action SetScreenVariable("cg_page",1)
        hotspot (73,558,30,30) action SetScreenVariable("cg_page",2)
        hotspot (637,558,120,30) action ShowMenu("extra")


    if cg_page == 1:
        add cg.make_button("ev01", "ui/thumbs/cg_p_01.png",xpos=52,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
        add cg.make_button("ev02", "ui/thumbs/cg_p_02.png",xpos=230,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
        add cg.make_button("ev03", "ui/thumbs/cg_p_03.png",xpos=410,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
        add cg.make_button("ev04", "ui/thumbs/cg_p_04.png",xpos=588,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
        add cg.make_button("ev05", "ui/thumbs/cg_p_05.png",xpos=52,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
        add cg.make_button("ev06", "ui/thumbs/cg_p_06.png",xpos=230,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
        add cg.make_button("ev07", "ui/thumbs/cg_p_07.png",xpos=410,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
        add cg.make_button("ev08", "ui/thumbs/cg_p_08.png",xpos=588,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
        add cg.make_button("ev09", "ui/thumbs/cg_p_09.png",xpos=52,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)
        add cg.make_button("ev10", "ui/thumbs/cg_p_10.png",xpos=230,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)
        add cg.make_button("ev11", "ui/thumbs/cg_p_11.png",xpos=410,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)
        add cg.make_button("ev12", "ui/thumbs/cg_p_12.png",xpos=588,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)



    elif cg_page == 2:
        add cg.make_button("ev13", "ui/thumbs/cg_p_13.png",xpos=52,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
        add cg.make_button("ev14", "ui/thumbs/cg_p_14.png",xpos=230,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
        add cg.make_button("ev15", "ui/thumbs/cg_p_15.png",xpos=410,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
        add cg.make_button("ev16", "ui/thumbs/cg_p_16.png",xpos=588,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
        add cg.make_button("ev17", "ui/thumbs/cg_p_17.png",xpos=52,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
        add cg.make_button("ev18", "ui/thumbs/cg_p_18.png",xpos=230,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
        add cg.make_button("ev19", "ui/thumbs/cg_p_19.png",xpos=410,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
        add cg.make_button("ev20", "ui/thumbs/cg_p_20.png",xpos=588,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)




screen extra_scene():
    tag menu

    imagemap:
        ground "ui/extra_scene_ground.png"
        idle "ui/scene_idle.png"
        hover "ui/scene_hover.png"
        selected_idle "ui/scene_selected_idle.png"
        selected_hover "ui/scene_selected_hover.png"
        alpha False

        hotspot (637,558,120,30) action ShowMenu("extra")

    imagebutton:
        insensitive "ui/extra_cg_locked.png"
        idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_01.png",(0,0),"ui/extra_cg_idle.png")
        hover "ui/thumbs/cg_p_01.png"
        action Replay("Replay01",locked=not persistent.Replay01)
        xpos 52
        ypos 110
        xpadding 0
        ypadding 0

    imagebutton:
        insensitive "ui/extra_cg_locked.png"
        idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_03.png",(0,0),"ui/extra_cg_idle.png")
        hover "ui/thumbs/cg_p_03.png"
        action Replay("Replay02",locked=not persistent.Replay02)
        xpos 230
        ypos 110
        xpadding 0
        ypadding 0

    imagebutton:
        insensitive "ui/extra_cg_locked.png"
        idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_04.png",(0,0),"ui/extra_cg_idle.png")
        hover "ui/thumbs/cg_p_04.png"
        action Replay("Replay03",locked=not persistent.Replay03)
        xpos 410
        ypos 110
        xpadding 0
        ypadding 0

    imagebutton:
        insensitive "ui/extra_cg_locked.png"
        idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_06.png",(0,0),"ui/extra_cg_idle.png")
        hover "ui/thumbs/cg_p_06.png"
        action Replay("Replay04",locked=not persistent.Replay04)
        xpos 588
        ypos 110
        xpadding 0
        ypadding 0

    imagebutton:
        insensitive "ui/extra_cg_locked.png"
        idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_09.png",(0,0),"ui/extra_cg_idle.png")
        hover "ui/thumbs/cg_p_09.png"
        action Replay("Replay05",locked=not persistent.Replay05)
        xpos 52
        ypos 249
        xpadding 0
        ypadding 0

    imagebutton:
        insensitive "ui/extra_cg_locked.png"
        idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_11.png",(0,0),"ui/extra_cg_idle.png")
        hover "ui/thumbs/cg_p_11.png"
        action Replay("Replay06",locked=not persistent.Replay06)
        xpos 230
        ypos 249
        xpadding 0
        ypadding 0

    imagebutton:
        insensitive "ui/extra_cg_locked.png"
        idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_16.png",(0,0),"ui/extra_cg_idle.png")
        hover "ui/thumbs/cg_p_16.png"
        action Replay("Replay07",locked=not persistent.Replay07)
        xpos 410
        ypos 249
        xpadding 0
        ypadding 0

    imagebutton:
        insensitive "ui/extra_cg_locked.png"
        idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_17.png",(0,0),"ui/extra_cg_idle.png")
        hover "ui/thumbs/cg_p_17.png"
        action Replay("Replay08",locked=not persistent.Replay08)
        xpos 588
        ypos 249
        xpadding 0
        ypadding 0


screen preferences():
    tag menu

    modal True

    imagemap:
        auto "ui/option_%s.png"
        alpha False

        hotspot (121,106,100,25) action [Preference("display", "window"),SelectedIf(not _preferences.fullscreen)]
        hotspot (227,106,100,25) action Preference("display", "fullscreen")
        hotspot (121,156,100,25) action Preference("skip", "seen")
        hotspot (227,156,100,25) action Preference("skip", "all")

        hotspot (205,295,70,25) action StylePreference("shadow","on")
        hotspot (275,295,70,25) action StylePreference("shadow","off")

        hotspot (173,381,40,25) action Preference("music mute", "enable")
        hotspot (213,381,40,25) action Preference("music mute", "disable")
        hotspot (173,431,40,25) action Preference("sound mute", "enable")
        hotspot (213,431,40,25) action Preference("sound mute", "disable")
        hotspot (253,431,40,25) action Play("sound","se/se001.ogg")
        hotspot (173,481,40,25) action Preference("voice mute", "enable")
        hotspot (213,481,40,25) action Preference("voice mute", "disable")
        hotspot (253,481,40,25) action Play("voice","voice/miya_0017.ogg")

        hotspot (471,370,100,25) action ChangeControl(0)
        hotspot (571,370,100,25) action ChangeControl(1)
        hotspot (663,495,60,30) action Return()

        hotspot (443,212,256,24) action OpenURL("https://www.renpy.org/doc/html/license.html")

        bar:
            #style "bar"
            value FieldValue(preferences,"afm_time",12.0,offset=3) 
            bar_invert True 
            xpos 80 
            ypos 209

            base_bar "ui/bar_idle.png"
            hover_base_bar "ui/bar_hover.png"
            ymaximum 20
            xmaximum 290
            unscrollable "insensitive"    
            thumb "ui/thumb.png"
            thumb_offset 9
            thumb_shadow None


        bar:
            #style "bar" 
            value Preference("text speed") 
            xpos 80 
            ypos 264

            base_bar "ui/bar_idle.png"
            hover_base_bar "ui/bar_hover.png"
            ymaximum 20
            xmaximum 290
            unscrollable "insensitive"    
            thumb "ui/thumb.png"
            thumb_offset 9
            thumb_shadow None

        bar:
            #style "bar" 
            value FieldValue(persistent,"window_opacity",1.0) 
            xpos 80 
            ypos 322

            base_bar "ui/bar_idle.png"
            hover_base_bar "ui/bar_hover.png"
            ymaximum 20
            xmaximum 290
            unscrollable "insensitive"    
            thumb "ui/thumb.png"
            thumb_offset 9
            thumb_shadow None

        bar:
            #style "bar" 
            value Preference("music volume") 
            xpos 80 
            ypos 406

            base_bar "ui/bar_idle.png"
            hover_base_bar "ui/bar_hover.png"
            ymaximum 20
            xmaximum 290
            unscrollable "insensitive"    
            thumb "ui/thumb.png"
            thumb_offset 9
            thumb_shadow None

        bar:
            #style "bar" 
            value Preference("sound volume") 
            xpos 80 
            ypos 456

            base_bar "ui/bar_idle.png"
            hover_base_bar "ui/bar_hover.png"
            ymaximum 20
            xmaximum 290
            unscrollable "insensitive"    
            thumb "ui/thumb.png"
            thumb_offset 9
            thumb_shadow None


        bar:
            #style "bar" 
            value Preference("voice volume") 
            xpos 80 
            ypos 506

            base_bar "ui/bar_idle.png"
            hover_base_bar "ui/bar_hover.png"
            ymaximum 20
            xmaximum 290
            unscrollable "insensitive"    
            thumb "ui/thumb.png"
            thumb_offset 9
            thumb_shadow None


    add "ui/option_text.png"

    add ConditionSwitch("(persistent.controls == 0)","ui/control_classical.png","(persistent.controls == 1)","ui/control_renpy.png") xpos 420 ypos 400



init -2:
    style bar:
        base_bar "ui/bar_idle.png"
        hover_base_bar "ui/bar_hover.png"
        ymaximum 20
        xmaximum 290
        unscrollable "insensitive"

        thumb "ui/thumb.png"
        thumb_offset 9
        thumb_shadow None


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
    add "ui/yesno_ground.png" xpos 206 ypos 221
    imagemap:
        ground Fixed()
        idle "ui/yesno_idle.png"
        hover "ui/yesno_hover.png"
        insensitive "ui/yesno_hover.png"
        xpos 206
        ypos 221
        alpha False
        hotspot (26,88,140,50) action yes_action
        hotspot (220,88,140,50) action no_action


    if (message==layout.ARE_YOU_SURE):
        add "ui/yesno_areyousure.png" xcenter 400 ypos 263
    if (message==layout.DELETE_SAVE):
        add "ui/yesno_delete.png" xcenter 400 ypos 263
    if (message==layout.OVERWRITE_SAVE):
        add "ui/yesno_save.png" xcenter 400 ypos 263
    if (message==layout.LOADING):
        add "ui/yesno_load.png" xcenter 400 ypos 263
    if (message==layout.QUIT):
        add "ui/yesno_quit.png" xcenter 400 ypos 263
    if (message==layout.MAIN_MENU):
        add "ui/yesno_mainmenu.png" xcenter 400 ypos 263
    if (message==layout.END_REPLAY):
        add "ui/yesno_extra.png" xcenter 400 ypos 263


    key "K_RETURN" action If(renpy.focus_coordinates() == (None,None,None,None),true=yes_action,false=NullAction())
    key "K_SPACE" action If(renpy.focus_coordinates() == (None,None,None,None),true=yes_action,false=NullAction())
    key "K_KP_ENTER" action If(renpy.focus_coordinates() == (None,None,None,None),true=yes_action,false=NullAction())
    key "hide_windows" action no_action
    key "K_ESCAPE" action no_action



screen quick_menu():



    imagemap:
        ground Fixed()
        idle "ui/quickmenu_idle.png"
        hover "ui/quickmenu_hover.png"
        selected_idle "ui/quickmenu_selected_idle.png"
        selected_hover "ui/quickmenu_selected_hover.png"
        insensitive "ui/quickmenu_insensitive.png"
        alpha False


        hotspot (49,572,69,28) action QuickSave()
        hotspot (118,572,69,28) action QuickLoad()
        hotspot (187,572,69,28) action ShowMenu("save")
        hotspot (256,572,69,28) action [ShowMenu("load"),SensitiveIf(not _in_replay)]
        hotspot (325,572,69,28) action Preference("auto-forward", "toggle")
        hotspot (394,572,69,28) action Skip()
        hotspot (463,572,69,28) action ShowMenu("preferences")
        if not _in_replay:
            hotspot (532,572,69,28) action MainMenu()
        else:
            hotspot (532,572,69,28) action EndReplay()

        hotspot (630,572,69,28) action VoiceReplay()
        hotspot (699,572,26,28) action Rollback()
        hotspot (725,572,26,28) action RollForward()