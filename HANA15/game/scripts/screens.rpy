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

    cg.button('CU01')
    cg.unlock('CU01')
    cg.image(Solid('#fff'), 'CU01')

    cg.button('CU02')
    cg.unlock('CU02')
    cg.image(Solid('#fff'), 'CU02')

    cg.button('CU03')
    cg.unlock('CU03')
    cg.image(Solid('#fff'), 'CU03')

    cg.button('CU04')
    cg.unlock('CU04')
    cg.image(Solid('#fff'), 'CU04')

    cg.button('CU05')
    cg.unlock('CU05')
    cg.image(Solid('#fff'), 'CU05')

    cg.button('CU06')
    cg.unlock('CU06')
    cg.image(Solid('#fff'), 'CU06')

    cg.button('CU07')
    cg.unlock('CU07')
    cg.image(Solid('#fff'), 'CU07')

    cg.button('CU08')
    cg.unlock('CU08', 'CU08p1')
    cg.image(Solid('#fff'), 'CU08')
    cg.image(Solid('#fff'), 'CU08p1')

    cg.button('CU09')
    cg.unlock('CU09')
    cg.image(Solid('#fff'), 'CU09')

    cg.button('CU10')
    cg.unlock('CU10')
    cg.image(Solid('#fff'), 'CU10')

    cg.button('CU11')
    cg.unlock('CU11')
    cg.image(Solid('#fff'), 'CU11')

    cg.button('CU12')
    cg.unlock('CU12')
    cg.image(Solid('#fff'), 'CU12')

    cg.button('CU13')
    cg.unlock('CU13')
    cg.image(Solid('#fff'), 'CU13')

    cg.button('CU14')
    cg.unlock('CU14')
    cg.image(Solid('#fff'), 'CU14')

    cg.button('CU15')
    cg.unlock('CU15')
    cg.image(Solid('#fff'), 'CU15')

    cg.button('CU16')
    cg.unlock('CU16')
    cg.image(Solid('#fff'), 'CU16')

    cg.button('CU17')
    cg.unlock('CU17')
    cg.image(Solid('#fff'), 'CU17')

    cg.button('CU18')
    cg.unlock('CU18')
    cg.image(Solid('#fff'), 'CU18')

    cg.button('CU19')
    cg.unlock('CU19', 'CU19p1')
    cg.image(Solid('#fff'), 'CU19')
    cg.image(Solid('#fff'), 'CU19p1')

    cg.button('CU20')
    cg.unlock('CU20')
    cg.image(Solid('#fff'), 'CU20')

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
    cg.unlock('EV06', 'EV06p1')
    cg.image('EV06')
    cg.image('EV06p1')

    cg.button('EV07')
    cg.unlock('EV07', 'EV07p1')
    cg.image('EV07')
    cg.image('EV07p1')

    cg.button('EV08')
    cg.unlock('EV08', 'EV08p1')
    cg.image('EV08')
    cg.image('EV08p1')

    cg.button('EV09')
    cg.unlock('EV09', 'EV09p1')
    cg.image('EV09')
    cg.image('EV09p1')

    cg.button('EV10')
    cg.unlock('EV10', 'EV10p1')
    cg.image('EV10')
    cg.image('EV10p1')

    cg.button('EV11')
    cg.unlock('EV11', 'EV11p1')
    cg.image('EV11')
    cg.image('EV11p1')

    cg.button('EV12')
    cg.unlock('EV12', 'EV12p1', 'EV12p2')
    cg.image('EV12')
    cg.image('EV12p1')
    cg.image('EV12p2')

    cg.button('EV13')
    cg.unlock('EV13', 'EV13p1')
    cg.image('EV13')
    cg.image('EV13p1')

    cg.button('EV14')
    cg.unlock('EV14', 'EV14p1')
    cg.image('EV14')
    cg.image('EV14p1')

    cg.button('EV15')
    cg.unlock('EV15', 'EV15p1')
    cg.image('EV15')
    cg.image('EV15p1')

    cg.button('EV16')
    cg.unlock('EV16', 'EV16p1', 'EV16p2')
    cg.image('EV16')
    cg.image('EV16p1')
    cg.image('EV16p2')

    cg.button('EV17')
    cg.unlock('EV17', 'EV17p1', 'EV17p2')
    cg.image('EV17')
    cg.image('EV17p1')
    cg.image('EV17p2')

    cg.button('EV18')
    cg.unlock('EV18', 'EV18p1', 'EV18p2')
    cg.image('EV18')
    cg.image('EV18p1')
    cg.image('EV18p2')

    cg.button('EV19')
    cg.unlock('EV19', 'EV19p1')
    cg.image('EV19')
    cg.image('EV19p1')

    cg.button('EV20')
    cg.unlock('EV20', 'EV20p1', 'EV20p2')
    cg.image('EV20')
    cg.image('EV20p1')
    cg.image('EV20p2')

    cg.button('EV21')
    cg.unlock('EV21', 'EV21p1')
    cg.image('EV21')
    cg.image('EV21p1')

    cg.button('EV22')
    cg.unlock('EV22', 'EV22p1', 'EV22p2', 'EV22p3')
    cg.image('EV22')
    cg.image('EV22p1')
    cg.image('EV22p2')
    cg.image('EV22p3')

    cg.button('EV23')
    cg.unlock('EV23', 'EV23p1', 'EV23p2')
    cg.image('EV23')
    cg.image('EV23p1')
    cg.image('EV23p2')

    cg.button('EV24')
    cg.unlock('EV24', 'EV24p1')
    cg.image('EV24')
    cg.image('EV24p1')

    cg.button('EV25')
    cg.unlock('EV25', 'EV25p1', 'EV25p2')
    cg.image('EV25')
    cg.image('EV25p1')
    cg.image('EV25p2')

    cg.button('EV26')
    cg.unlock('EV26')
    cg.image('EV26')

    cg.button('EV27')
    cg.unlock('EV27', 'EV27p1')
    cg.image('EV27')
    cg.image('EV27p1')

    cg.button('EV28')
    cg.unlock('EV28', 'EV28p1')
    cg.image('EV28')
    cg.image('EV28p1')

    cg.button('EV29')
    cg.unlock('EV29', 'EV29p1')
    cg.image('EV29')
    cg.image('EV29p1')

    cg.button('EV30')
    cg.unlock('EV30', 'EV30p1', 'EV30p2')
    cg.image('EV30')
    cg.image('EV30p1')
    cg.image('EV30p2')

    cg.button('EV31')
    cg.unlock('EV31', 'EV31p1', 'EV31p2')
    cg.image('EV31')
    cg.image('EV31p1')
    cg.image('EV31p2')

    cg.button('EV32')
    cg.unlock('EV32', 'EV32p1', 'EV32p2')
    cg.image('EV32')
    cg.image('EV32p1')
    cg.image('EV32p2')

    cg.button('EV33')
    cg.unlock('EV33', 'EV33p1')
    cg.image('EV33')
    cg.image('EV33p1')

    cg.button('EV34')
    cg.unlock('EV34', 'EV34p1', 'EV34p2')
    cg.image('EV34')
    cg.image('EV34p1')
    cg.image('EV34p2')

    cg.button('EV35')
    cg.unlock('EV35', 'EV35p1')
    cg.image('EV35')
    cg.image('EV35p1')

    cg.button('EV36')
    cg.unlock('EV36', 'EV36p1')
    cg.image('EV36')
    cg.image('EV36p1')

    cg.button('EV37')
    cg.unlock('EV37', 'EV37p1', 'EV37p2')
    cg.image('EV37')
    cg.image('EV37p1')
    cg.image('EV37p2')

    cg.button('EV38')
    cg.unlock('EV38', 'EV38p1')
    cg.image('EV38')
    cg.image('EV38p1')

    cg.button('EV39')
    cg.unlock('EV39', 'EV39p1', 'EV39p2')
    cg.image('EV39')
    cg.image('EV39p1')
    cg.image('EV39p2')

    cg.button('EV40')
    cg.unlock('EV40', 'EV40p1')
    cg.image('EV40')
    cg.image('EV40p1')

    cg.button('EV41')
    cg.unlock('EV41', 'EV41p1')
    cg.image('EV41')
    cg.image('EV41p1')

    cg.button('EV42')
    cg.unlock('EV42')
    cg.image('EV42')

    cg.button('EV43')
    cg.unlock('EV43')
    cg.image('EV43')

    cg.button('EV44')
    cg.unlock('EV44', 'EV44p1')
    cg.image('EV44')
    cg.image('EV44p1')

    cg.button('EV45')
    cg.unlock('EV45', 'EV45p1', 'EV45p2')
    cg.image('EV45')
    cg.image('EV45p1')
    cg.image('EV45p2')

    cg.button('EV46')
    cg.unlock('EV46', 'EV46p1')
    cg.image('EV46')
    cg.image('EV46p1')

    cg.button('EV47')
    cg.unlock('EV47', 'EV47p1')
    cg.image('EV47')
    cg.image('EV47p1')

    cg.button('EV48')
    cg.unlock('EV48', 'EV48p1')
    cg.image('EV48')
    cg.image('EV48p1')

    cg.button('EV49')
    cg.unlock('EV49', 'EV49p1')
    cg.image('EV49')
    cg.image('EV49p1')

    cg.button('EV50')
    cg.unlock('EV50', 'EV50p1', 'EV50p2')
    cg.image('EV50')
    cg.image('EV50p1')
    cg.image('EV50p2')

    cg.button('EV51')
    cg.unlock('EV51', 'EV51p1', 'EV51p2')
    cg.image('EV51')
    cg.image('EV51p1')
    cg.image('EV51p2')

    cg.button('EV52')
    cg.unlock('EV52', 'EV52p1')
    cg.image('EV52')
    cg.image('EV52p1')

    cg.button('EV53')
    cg.unlock('EV53', 'EV53p1')
    cg.image('EV53')
    cg.image('EV53p1')

    cg.button('EV54')
    cg.unlock('EV54', 'EV54p1', 'EV54p2')
    cg.image('EV54')
    cg.image('EV54p1')
    cg.image('EV54p2')

    cg.button('EV55')
    cg.unlock('EV55', 'EV55p1')
    cg.image('EV55')
    cg.image('EV55p1')

    cg.button('EV56')
    cg.unlock('EV56', 'EV56p1', 'EV56p2')
    cg.image('EV56')
    cg.image('EV56p1')
    cg.image('EV56p2')

    cg.button('EV57')
    cg.unlock('EV57', 'EV57p1', 'EV57p2')
    cg.image('EV57')
    cg.image('EV57p1')
    cg.image('EV57p2')

    cg.button('EV58')
    cg.unlock('EV58', 'EV58p1', 'EV58p2')
    cg.image('EV58')
    cg.image('EV58p1')
    cg.image('EV58p2')

    cg.button('EV59')
    cg.unlock('EV59', 'EV59p1')
    cg.image('EV59')
    cg.image('EV59p1')

    cg.button('EV60')
    cg.unlock('EV60', 'EV60p1')
    cg.image('EV60')
    cg.image('EV60p1')

    cg.button('EV61')
    cg.unlock('EV61', 'EV61p1', 'EV61p2')
    cg.image('EV61')
    cg.image('EV61p1')
    cg.image('EV61p2')

    cg.button('EV62')
    cg.unlock('EV62', 'EV62p1')
    cg.image('EV62')
    cg.image('EV62p1')

    cg.button('EV63')
    cg.unlock('EV63', 'EV63p1')
    cg.image('EV63')
    cg.image('EV63p1')

    cg.button('EV64')
    cg.unlock('EV64', 'EV64p1', 'EV64p2', 'EV64p3')
    cg.image('EV64')
    cg.image('EV64p1')
    cg.image('EV64p2')
    cg.image('EV64p3')

    cg.button('EV65')
    cg.unlock('EV65', 'EV65p1', 'EV65p2')
    cg.image('EV65')
    cg.image('EV65p1')
    cg.image('EV65p2')

    cg.button('EV66')
    cg.unlock('EV66', 'EV66p1')
    cg.image('EV66')
    cg.image('EV66p1')

    cg.button('EV67')
    cg.unlock('EV67', 'EV67p1')
    cg.image('EV67')
    cg.image('EV67p1')

    cg.button('EV68')
    cg.unlock('EV68', 'EV68p1')
    cg.image('EV68')
    cg.image('EV68p1')

    cg.button('EV69')
    cg.unlock('EV69', 'EV69p1', 'EV69p2')
    cg.image('EV69')
    cg.image('EV69p1')
    cg.image('EV69p2')

    cg.button('EV70')
    cg.unlock('EV70', 'EV70p1')
    cg.image('EV70')
    cg.image('EV70p1')

    cg.button('EV71')
    cg.unlock('EV71', 'EV71p1', 'EV71p2')
    cg.image('EV71')
    cg.image('EV71p1')
    cg.image('EV71p2')

    cg.button('EV72')
    cg.unlock('EV72', 'EV72p1', 'EV72p2')
    cg.image('EV72')
    cg.image('EV72p1')
    cg.image('EV72p2')

    cg.button('EV73')
    cg.unlock('EV73', 'EV73p1')
    cg.image('EV73')
    cg.image('EV73p1')

    cg.button('EV74')
    cg.unlock('EV74', 'EV74p1')
    cg.image('EV74')
    cg.image('EV74p1')

    cg.button('EV75')
    cg.unlock('EV75', 'EV75p1')
    cg.image('EV75')
    cg.image('EV75p1')

    cg.button('EV76')
    cg.unlock('EV76', 'EV76p1')
    cg.image('EV76')
    cg.image('EV76p1')

    cg.button('EV77')
    cg.unlock('EV77', 'EV77p1')
    cg.image('EV77')
    cg.image('EV77p1')

    cg.button('EV78')
    cg.unlock('EV78', 'EV78p1')
    cg.image('EV78')
    cg.image('EV78p1')

    cg.button('EV79')
    cg.unlock('EV79', 'EV79p1')
    cg.image('EV79')
    cg.image('EV79p1')

    cg.button('EV80')
    cg.unlock('EV80', 'EV80p1')
    cg.image('EV80')
    cg.image('EV80p1')


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
    mr.add("bgm/bgm25.ogg",always_unlocked=True) 
    



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
                hotspot (50,408,340,40) action Play("music","bgm/bgm25.ogg",fadeout=0)

                hotspot (410,108,340,40) action Play("music","bgm/bgm16.ogg",fadeout=0)
                hotspot (410,168,340,40) action Play("music","bgm/bgm18.ogg",fadeout=0)
                hotspot (410,228,340,40) action Play("music","bgm/bgm20.ogg",fadeout=0)
                hotspot (410,288,340,40) action Play("music","bgm/bgm22.ogg",fadeout=0)
                hotspot (410,348,340,40) action Play("music","bgm/bgm24.ogg",fadeout=0)


screen extra_cg():
    tag menu

    default cg_char = 1
    default cg_page = 1

    imagemap:
        ground "ui/extra_cg_ground.png"
        idle "ui/cg_idle.png"
        hover "ui/cg_hover.png"
        selected_idle "ui/cg_selected_idle.png"
        selected_hover "ui/cg_selected_hover.png"
        alpha False

        hotspot (10,84,180,40)  action SetScreenVariable("cg_char",1)
        hotspot (10,124,180,40) action SetScreenVariable("cg_char",2)
        hotspot (10,164,180,40) action SetScreenVariable("cg_char",3)
        hotspot (10,204,180,40) action SetScreenVariable("cg_char",4)
        hotspot (10,244,180,40) action SetScreenVariable("cg_char",5)
        hotspot (10,284,180,40) action SetScreenVariable("cg_char",6)
        hotspot (10,324,180,40) action SetScreenVariable("cg_char",7)
        hotspot (637,558,120,30) action ShowMenu("extra")

    if cg_char == 1:
        
        imagemap:
            ground Null()
            idle "ui/page_idle.png"
            hover "ui/page_hover.png"
            selected_idle "ui/page_selected_idle.png"
            selected_hover "ui/page_selected_hover.png"
            alpha False

            hotspot (43,558,30,30) action SetScreenVariable("cg_page",1)
            hotspot (73,558,30,30) action SetScreenVariable("cg_page",2)
            hotspot (103,558,30,30) action SetScreenVariable("cg_page",3)

        if cg_page == 1:
            add cg.make_button("EV01", "ui/thumbs/cg_p_01.png",xpos=231,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV02", "ui/thumbs/cg_p_02.png",xpos=410,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV04", "ui/thumbs/cg_p_04.png",xpos=588,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV11", "ui/thumbs/cg_p_11.png",xpos=231,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV12", "ui/thumbs/cg_p_12.png",xpos=410,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV13", "ui/thumbs/cg_p_13.png",xpos=588,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV14", "ui/thumbs/cg_p_14.png",xpos=231,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV15", "ui/thumbs/cg_p_15.png",xpos=410,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV16", "ui/thumbs/cg_p_16.png",xpos=588,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)



        elif cg_page == 2:
            add cg.make_button("EV17", "ui/thumbs/cg_p_17.png",xpos=231,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV18", "ui/thumbs/cg_p_18.png",xpos=410,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV19", "ui/thumbs/cg_p_19.png",xpos=588,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV20", "ui/thumbs/cg_p_20.png",xpos=231,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV21", "ui/thumbs/cg_p_21.png",xpos=410,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV22", "ui/thumbs/cg_p_22.png",xpos=588,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV23", "ui/thumbs/cg_p_23.png",xpos=231,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV24", "ui/thumbs/cg_p_24.png",xpos=410,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV25", "ui/thumbs/cg_p_25.png",xpos=588,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)

        elif cg_page == 3:
            add cg.make_button("EV26", "ui/thumbs/cg_p_26.png",xpos=231,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)

    elif cg_char == 2:
        
        imagemap:
            ground Null()
            idle "ui/page_idle.png"
            hover "ui/page_hover.png"
            selected_idle "ui/page_selected_idle.png"
            selected_hover "ui/page_selected_hover.png"
            alpha False

            hotspot (43,558,30,30) action SetScreenVariable("cg_page",1)
            hotspot (73,558,30,30) action SetScreenVariable("cg_page",2)

        if cg_page == 1:
            add cg.make_button("EV03", "ui/thumbs/cg_p_03.png",xpos=231,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV10", "ui/thumbs/cg_p_10.png",xpos=410,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV27", "ui/thumbs/cg_p_27.png",xpos=588,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV28", "ui/thumbs/cg_p_28.png",xpos=231,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV29", "ui/thumbs/cg_p_29.png",xpos=410,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV30", "ui/thumbs/cg_p_30.png",xpos=588,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV31", "ui/thumbs/cg_p_31.png",xpos=231,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV32", "ui/thumbs/cg_p_32.png",xpos=410,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV33", "ui/thumbs/cg_p_33.png",xpos=588,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)



        elif cg_page == 2:
            add cg.make_button("EV34", "ui/thumbs/cg_p_34.png",xpos=231,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV35", "ui/thumbs/cg_p_35.png",xpos=410,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV36", "ui/thumbs/cg_p_36.png",xpos=588,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV37", "ui/thumbs/cg_p_37.png",xpos=231,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV38", "ui/thumbs/cg_p_38.png",xpos=410,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV39", "ui/thumbs/cg_p_39.png",xpos=588,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV40", "ui/thumbs/cg_p_40.png",xpos=231,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)

    elif cg_char == 3:
        
        imagemap:
            ground Null()
            idle "ui/page_idle.png"
            hover "ui/page_hover.png"
            selected_idle "ui/page_selected_idle.png"
            selected_hover "ui/page_selected_hover.png"
            alpha False

            hotspot (43,558,30,30) action SetScreenVariable("cg_page",1)
            hotspot (73,558,30,30) action SetScreenVariable("cg_page",2)

        if cg_page == 1:
            add cg.make_button("EV07", "ui/thumbs/cg_p_07.png",xpos=231,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV41", "ui/thumbs/cg_p_41.png",xpos=410,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV42", "ui/thumbs/cg_p_42.png",xpos=588,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV43", "ui/thumbs/cg_p_43.png",xpos=231,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV44", "ui/thumbs/cg_p_44.png",xpos=410,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV45", "ui/thumbs/cg_p_45.png",xpos=588,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV46", "ui/thumbs/cg_p_46.png",xpos=231,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV47", "ui/thumbs/cg_p_47.png",xpos=410,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV48", "ui/thumbs/cg_p_48.png",xpos=588,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)



        elif cg_page == 2:
            add cg.make_button("EV49", "ui/thumbs/cg_p_49.png",xpos=231,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV50", "ui/thumbs/cg_p_50.png",xpos=410,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV51", "ui/thumbs/cg_p_51.png",xpos=588,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV52", "ui/thumbs/cg_p_52.png",xpos=231,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV53", "ui/thumbs/cg_p_53.png",xpos=410,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)

    elif cg_char == 4:
        
        imagemap:
            ground Null()
            idle "ui/page_idle.png"
            hover "ui/page_hover.png"
            selected_idle "ui/page_selected_idle.png"
            selected_hover "ui/page_selected_hover.png"
            alpha False

            hotspot (43,558,30,30) action SetScreenVariable("cg_page",1)
            hotspot (73,558,30,30) action SetScreenVariable("cg_page",2)

        if cg_page == 1:
            add cg.make_button("EV08", "ui/thumbs/cg_p_08.png",xpos=231,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV54", "ui/thumbs/cg_p_54.png",xpos=410,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV55", "ui/thumbs/cg_p_55.png",xpos=588,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV56", "ui/thumbs/cg_p_56.png",xpos=231,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV57", "ui/thumbs/cg_p_57.png",xpos=410,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV58", "ui/thumbs/cg_p_58.png",xpos=588,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV59", "ui/thumbs/cg_p_59.png",xpos=231,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV60", "ui/thumbs/cg_p_60.png",xpos=410,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV61", "ui/thumbs/cg_p_61.png",xpos=588,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)



        elif cg_page == 2:
            add cg.make_button("EV62", "ui/thumbs/cg_p_62.png",xpos=231,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV63", "ui/thumbs/cg_p_63.png",xpos=410,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV64", "ui/thumbs/cg_p_64.png",xpos=588,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV65", "ui/thumbs/cg_p_65.png",xpos=231,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV66", "ui/thumbs/cg_p_66.png",xpos=410,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)

    elif cg_char == 5:
        
        imagemap:
            ground Null()
            idle "ui/page_idle.png"
            hover "ui/page_hover.png"
            selected_idle "ui/page_selected_idle.png"
            selected_hover "ui/page_selected_hover.png"
            alpha False

            hotspot (43,558,30,30) action SetScreenVariable("cg_page",1)
            hotspot (73,558,30,30) action SetScreenVariable("cg_page",2)

        if cg_page == 1:
            add cg.make_button("EV09", "ui/thumbs/cg_p_09.png",xpos=231,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV67", "ui/thumbs/cg_p_67.png",xpos=410,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV68", "ui/thumbs/cg_p_68.png",xpos=588,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV69", "ui/thumbs/cg_p_69.png",xpos=231,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV70", "ui/thumbs/cg_p_70.png",xpos=410,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV71", "ui/thumbs/cg_p_71.png",xpos=588,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV72", "ui/thumbs/cg_p_72.png",xpos=231,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV73", "ui/thumbs/cg_p_73.png",xpos=410,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV74", "ui/thumbs/cg_p_74.png",xpos=588,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)



        elif cg_page == 2:
            add cg.make_button("EV75", "ui/thumbs/cg_p_75.png",xpos=231,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV76", "ui/thumbs/cg_p_76.png",xpos=410,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV77", "ui/thumbs/cg_p_77.png",xpos=588,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV78", "ui/thumbs/cg_p_78.png",xpos=231,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV79", "ui/thumbs/cg_p_79.png",xpos=410,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV80", "ui/thumbs/cg_p_80.png",xpos=588,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)

    elif cg_char == 6:
        
        imagemap:
            ground Null()
            idle "ui/page_idle.png"
            hover "ui/page_hover.png"
            selected_idle "ui/page_selected_idle.png"
            selected_hover "ui/page_selected_hover.png"
            alpha False

            hotspot (43,558,30,30) action SetScreenVariable("cg_page",1)

        if cg_page == 1:
            add cg.make_button("EV05", "ui/thumbs/cg_p_05.png",xpos=231,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("EV06", "ui/thumbs/cg_p_06.png",xpos=410,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)

    elif cg_char == 7:
        
        imagemap:
            ground Null()
            idle "ui/page_idle.png"
            hover "ui/page_hover.png"
            selected_idle "ui/page_selected_idle.png"
            selected_hover "ui/page_selected_hover.png"
            alpha False

            hotspot (43,558,30,30) action SetScreenVariable("cg_page",1)
            hotspot (73,558,30,30) action SetScreenVariable("cg_page",2)
            hotspot (103,558,30,30) action SetScreenVariable("cg_page",3)

        if cg_page == 1:
            add cg.make_button("CU01", "ui/thumbs/cg_p_cu01.png",xpos=231,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("CU02", "ui/thumbs/cg_p_cu02.png",xpos=410,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("CU03", "ui/thumbs/cg_p_cu03.png",xpos=588,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("CU04", "ui/thumbs/cg_p_cu04.png",xpos=231,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("CU05", "ui/thumbs/cg_p_cu05.png",xpos=410,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("CU06", "ui/thumbs/cg_p_cu06.png",xpos=588,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("CU07", "ui/thumbs/cg_p_cu07.png",xpos=231,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("CU08", "ui/thumbs/cg_p_cu08.png",xpos=410,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("CU09", "ui/thumbs/cg_p_cu09.png",xpos=588,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)



        elif cg_page == 2:
            add cg.make_button("CU10", "ui/thumbs/cg_p_cu10.png",xpos=231,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("CU11", "ui/thumbs/cg_p_cu11.png",xpos=410,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("CU12", "ui/thumbs/cg_p_cu12.png",xpos=588,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("CU13", "ui/thumbs/cg_p_cu13.png",xpos=231,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("CU14", "ui/thumbs/cg_p_cu14.png",xpos=410,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("CU15", "ui/thumbs/cg_p_cu15.png",xpos=588,ypos=249,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("CU16", "ui/thumbs/cg_p_cu16.png",xpos=231,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("CU17", "ui/thumbs/cg_p_cu17.png",xpos=410,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("CU18", "ui/thumbs/cg_p_cu18.png",xpos=588,ypos=388,xysize=(160,120),xpadding=0,ypadding=0)

        elif cg_page == 3:
            add cg.make_button("CU19", "ui/thumbs/cg_p_cu19.png",xpos=231,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)
            add cg.make_button("CU20", "ui/thumbs/cg_p_cu20.png",xpos=410,ypos=110,xysize=(160,120),xpadding=0,ypadding=0)




screen extra_scene():
    tag menu

    default scene_char = 1

    imagemap:
        ground "ui/extra_scene_ground.png"
        idle "ui/scene_idle.png"
        hover "ui/scene_hover.png"
        selected_idle "ui/scene_selected_idle.png"
        selected_hover "ui/scene_selected_hover.png"
        alpha False

        hotspot (10,84,180,40) action SetScreenVariable("scene_char",1)
        hotspot (10,124,180,40) action SetScreenVariable("scene_char",2)
        hotspot (10,164,180,40) action SetScreenVariable("scene_char",3)
        hotspot (10,204,180,40) action SetScreenVariable("scene_char",4)
        hotspot (10,244,180,40) action SetScreenVariable("scene_char",5)
        hotspot (637,558,120,30) action ShowMenu("extra")

    if scene_char == 1:

        imagebutton:
            insensitive "ui/extra_cg_locked.png"
            idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_16.png",(0,0),"ui/extra_cg_idle.png")
            hover "ui/thumbs/cg_p_16.png"
            action Replay("Replay01_01",locked=not persistent.Replay01_01)
            xpos 231
            ypos 110
            xpadding 0
            ypadding 0

        imagebutton:
            insensitive "ui/extra_cg_locked.png"
            idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_18.png",(0,0),"ui/extra_cg_idle.png")
            hover "ui/thumbs/cg_p_18.png"
            action Replay("Replay01_02",locked=not persistent.Replay01_02)
            xpos 410
            ypos 110
            xpadding 0
            ypadding 0

        imagebutton:
            insensitive "ui/extra_cg_locked.png"
            idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_21.png",(0,0),"ui/extra_cg_idle.png")
            hover "ui/thumbs/cg_p_21.png"
            action Replay("Replay01_03",locked=not persistent.Replay01_03)
            xpos 588
            ypos 110
            xpadding 0
            ypadding 0

        imagebutton:
            insensitive "ui/extra_cg_locked.png"
            idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_23.png",(0,0),"ui/extra_cg_idle.png")
            hover "ui/thumbs/cg_p_23.png"
            action Replay("Replay01_04",locked=not persistent.Replay01_04)
            xpos 231
            ypos 249
            xpadding 0
            ypadding 0

        imagebutton:
            insensitive "ui/extra_cg_locked.png"
            idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_25.png",(0,0),"ui/extra_cg_idle.png")
            hover "ui/thumbs/cg_p_25.png"
            action Replay("Replay01_05",locked=not persistent.Replay01_05)
            xpos 410
            ypos 249
            xpadding 0
            ypadding 0

    elif scene_char == 2:

        imagebutton:
            insensitive "ui/extra_cg_locked.png"
            idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_28.png",(0,0),"ui/extra_cg_idle.png")
            hover "ui/thumbs/cg_p_28.png"
            action Replay("Replay02_01",locked=not persistent.Replay02_01)
            xpos 231
            ypos 110
            xpadding 0
            ypadding 0

        imagebutton:
            insensitive "ui/extra_cg_locked.png"
            idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_30.png",(0,0),"ui/extra_cg_idle.png")
            hover "ui/thumbs/cg_p_30.png"
            action Replay("Replay02_02",locked=not persistent.Replay02_02)
            xpos 410
            ypos 110
            xpadding 0
            ypadding 0

        imagebutton:
            insensitive "ui/extra_cg_locked.png"
            idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_37.png",(0,0),"ui/extra_cg_idle.png")
            hover "ui/thumbs/cg_p_37.png"
            action Replay("Replay02_03",locked=not persistent.Replay02_03)
            xpos 588
            ypos 110
            xpadding 0
            ypadding 0

        imagebutton:
            insensitive "ui/extra_cg_locked.png"
            idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_39.png",(0,0),"ui/extra_cg_idle.png")
            hover "ui/thumbs/cg_p_39.png"
            action Replay("Replay02_04",locked=not persistent.Replay02_04)
            xpos 231
            ypos 249
            xpadding 0
            ypadding 0

    elif scene_char == 3:

        imagebutton:
            insensitive "ui/extra_cg_locked.png"
            idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_44.png",(0,0),"ui/extra_cg_idle.png")
            hover "ui/thumbs/cg_p_44.png"
            action Replay("Replay03_01",locked=not persistent.Replay03_01)
            xpos 231
            ypos 110
            xpadding 0
            ypadding 0

        imagebutton:
            insensitive "ui/extra_cg_locked.png"
            idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_47.png",(0,0),"ui/extra_cg_idle.png")
            hover "ui/thumbs/cg_p_47.png"
            action Replay("Replay03_02",locked=not persistent.Replay03_02)
            xpos 410
            ypos 110
            xpadding 0
            ypadding 0

        imagebutton:
            insensitive "ui/extra_cg_locked.png"
            idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_49.png",(0,0),"ui/extra_cg_idle.png")
            hover "ui/thumbs/cg_p_49.png"
            action Replay("Replay03_03",locked=not persistent.Replay03_03)
            xpos 588
            ypos 110
            xpadding 0
            ypadding 0

        imagebutton:
            insensitive "ui/extra_cg_locked.png"
            idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_51.png",(0,0),"ui/extra_cg_idle.png")
            hover "ui/thumbs/cg_p_51.png"
            action Replay("Replay03_04",locked=not persistent.Replay03_04)
            xpos 231
            ypos 249
            xpadding 0
            ypadding 0

    elif scene_char == 4:

        imagebutton:
            insensitive "ui/extra_cg_locked.png"
            idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_57.png",(0,0),"ui/extra_cg_idle.png")
            hover "ui/thumbs/cg_p_57.png"
            action Replay("Replay04_01",locked=not persistent.Replay04_01)
            xpos 231
            ypos 110
            xpadding 0
            ypadding 0

        imagebutton:
            insensitive "ui/extra_cg_locked.png"
            idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_60.png",(0,0),"ui/extra_cg_idle.png")
            hover "ui/thumbs/cg_p_60.png"
            action Replay("Replay04_02",locked=not persistent.Replay04_02)
            xpos 410
            ypos 110
            xpadding 0
            ypadding 0

        imagebutton:
            insensitive "ui/extra_cg_locked.png"
            idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_63.png",(0,0),"ui/extra_cg_idle.png")
            hover "ui/thumbs/cg_p_63.png"
            action Replay("Replay04_03",locked=not persistent.Replay04_03)
            xpos 588
            ypos 110
            xpadding 0
            ypadding 0

    elif scene_char == 5:

        imagebutton:
            insensitive "ui/extra_cg_locked.png"
            idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_69.png",(0,0),"ui/extra_cg_idle.png")
            hover "ui/thumbs/cg_p_69.png"
            action Replay("Replay05_01",locked=not persistent.Replay05_01)
            xpos 231
            ypos 110
            xpadding 0
            ypadding 0

        imagebutton:
            insensitive "ui/extra_cg_locked.png"
            idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_71.png",(0,0),"ui/extra_cg_idle.png")
            hover "ui/thumbs/cg_p_71.png"
            action Replay("Replay05_02",locked=not persistent.Replay05_02)
            xpos 410
            ypos 110
            xpadding 0
            ypadding 0

        imagebutton:
            insensitive "ui/extra_cg_locked.png"
            idle LiveComposite((160,120),(0,0),"ui/thumbs/cg_p_77.png",(0,0),"ui/extra_cg_idle.png")
            hover "ui/thumbs/cg_p_77.png"
            action Replay("Replay05_03",locked=not persistent.Replay05_03)
            xpos 588
            ypos 110
            xpadding 0
            ypadding 0




screen preferences():
    tag menu

    modal True

    imagemap:
        auto "ui/option_%s.png"
        alpha False

        hotspot (121,136,100,25) action [Preference("display", "window"),SelectedIf(not _preferences.fullscreen)]
        hotspot (227,136,100,25) action Preference("display", "fullscreen")
        hotspot (121,186,100,25) action Preference("skip", "seen")
        hotspot (227,186,100,25) action Preference("skip", "all")

        hotspot (205,325,70,25) action StylePreference("shadow","on")
        hotspot (275,325,70,25) action StylePreference("shadow","off")

        hotspot (173,411,40,25) action Preference("music mute", "enable")
        hotspot (213,411,40,25) action Preference("music mute", "disable")
        hotspot (173,461,40,25) action Preference("sound mute", "enable")
        hotspot (213,461,40,25) action Preference("sound mute", "disable")
        hotspot (253,461,40,25) action Play("sound","se/se001.ogg")
        hotspot (173,511,40,25) action Preference("voice mute", "enable")
        hotspot (213,511,40,25) action Preference("voice mute", "disable")
        hotspot (253,511,40,25) action Play("voice","voice/Sayuki0835.ogg")

        hotspot (471,400,100,25) action ChangeControl(0)
        hotspot (571,400,100,25) action ChangeControl(1)
        hotspot (663,525,60,30) action Return()

        hotspot (443,242,256,24) action OpenURL("https://www.renpy.org/doc/html/license.html")

        bar:
            #style "bar"
            value FieldValue(preferences,"afm_time",12.0,offset=3) 
            bar_invert True 
            xpos 80 
            ypos 239

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
            ypos 294

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
            ypos 352

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
            ypos 436

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
            ypos 486

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
            ypos 536

            base_bar "ui/bar_idle.png"
            hover_base_bar "ui/bar_hover.png"
            ymaximum 20
            xmaximum 290
            unscrollable "insensitive"    
            thumb "ui/thumb.png"
            thumb_offset 9
            thumb_shadow None


    add "ui/option_text.png"

    add ConditionSwitch("(persistent.controls == 0)","ui/control_classical.png","(persistent.controls == 1)","ui/control_renpy.png") xpos 420 ypos 440



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