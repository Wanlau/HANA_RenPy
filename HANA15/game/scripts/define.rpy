init -2:
    image white = Solid("#fff")

    define yuuna = Character('优菜', color="#FF7609")
    define nanami = Character('七海', color="#FF0913")
    define kaede = Character('枫', color="#AA09FF")
    define sara = Character('纱良', color="#c07a3c")
    define mai = Character('麻衣', color="#0981FF")
    define reo = Character('玲绪', color="#FFC009")
    define takako = Character('贵子', color="#09FF96")
    define runa = Character('瑠奈', color="#FF8209")
    define rena = Character('丽奈', color="#FF8209")
    define erisu = Character('爱丽丝', color="#e7b621")
    define sizuku = Character('雫', color="#4224ff")
    define risa = Character('璃纱', color="#FF197A")
    define miya = Character('美夜', color="#2809FF")
    define rikka = Character('六夏', color="#168bff")
    define sayuki = Character('沙雪', color="#d417b5")

    define rie = Character('璃惠', color="#09B5FF")
    define yukino = Character('雪乃', color="#09B5FF")
    define sayuki_grandma = Character('沙雪祖母', color="#09B5FF")
    define sayuki_mother = Character('沙雪母', color="#09B5FF")
    define nanami_mother = Character('七海母', color="#09B5FF")
    define nanami_father = Character('七海父', color="#09B5FF")
    define mai_brother = Character('麻衣弟', color="#09B5FF")
    define mai_sister = Character('麻衣妹', color="#09B5FF")

    define teacher = Character('老师', color="#09B5FF")
    define girl_a = Character('女生A', color="#09B5FF")
    define girl_b = Character('女生B', color="#09B5FF")
    define girl_c = Character('女生C', color="#09B5FF")
    define girl_d = Character('女生D', color="#09B5FF")
    define girl_e = Character('女生E', color="#09B5FF")
    define member_a = Character('会员A', color="#09B5FF")
    define member_b = Character('会员B', color="#09B5FF")
    define member_c = Character('会员C', color="#09B5FF")
    define staff = Character('工作人员', color="#09B5FF")
    define camera = Character('摄影师', color="#09B5FF")
    define manager = Character('经纪人', color="#09B5FF")
    define monitor = Character('监督', color="#09B5FF")

    define unknown = Character('???', color="#09B5FF")
    define allchar = Character('全员', color="#09B5FF")

        
    image stmichael = "ui/stmichael.png"
    image stmadoca = "ui/stmadoca.png"

    style window:
        ypos 584
        top_margin 0
        bottom_margin 0
        xpadding 32
        top_padding 27
        bottom_padding -28
        yminimum 156

    style say_dialogue is say_thought:
        yanchor 52

    style say_thought:
        font "Tuffy-Regular.ttf"
        size 25

    style say_label:
        xanchor -40
        yanchor 34
        ypos -10
        outlines [(2,"#00000060",3,3),(2,"#FFFFFF",0,0)]
        font "Homizio-bold.ttf"
        size 28

    style save_slot:
        font "Homizio-bold.ttf"
        xpos 108
        ypos 6
        size 18
        xmaximum 256
        outlines [(0,"#000000A0",2,2)]

    python:
        renpy.register_style_preference("shadow","on",style.say_thought,"outlines",[(0,"#000000A0",2,2)])
        renpy.register_style_preference("shadow","off",style.say_thought,"outlines",[(3,"#000000D0",0,0)])

    transform c:
        xcenter 0.5
    transform l:
        xcenter 0.25
    transform r:
        xcenter 0.75
    transform l3:
        xcenter 0.2
    transform r3:
        xcenter 0.8
    transform u:
        yanchor 0
    transform d:
        yanchor -304
    transform sl:
        xcenter 0.1875
    transform sr:
        xcenter 0.8125

    transform f1:
        xcenter 0.1
    transform f2:
        xcenter 0.35
    transform f3:
        xcenter 0.65
    transform f4:
        xcenter 0.9

    transform q1:
        xcenter 0.25
        ycenter 0.35
    transform q2:
        xcenter 0.75
        ycenter 0.35
    transform q3:
        xcenter 0.25
        ycenter 0.72
    transform q4:
        xcenter 0.75
        ycenter 0.72

    transform quake:
        xoffset -18
        block:
            easeout_quint 0.025 xoffset 18
            easeout_quint 0.025 xoffset -18
            repeat 9
        xoffset 0

    transform eyecatch_in:
        xcenter 0.5
        xzoom 0
        pause 1
        easein 1.0 xzoom 1
    transform eyecatch_out:
        xcenter 0.5
        xzoom 1
        pause 3
        easeout 1.0 xzoom 0
    transform door:
        yalign 0.5
        yzoom 0
        easein 1.0 yzoom 1
    transform door_out:
        yalign 0.5
        yzoom 1
        easeout 1.0 yzoom 0


    define gs_en_ns = ImageDissolve("images/gs_en_ns.png",2,ramplen=256)
    define gs_en_sn = ImageDissolve("images/gs_en_sn.png",2,ramplen=256)
    define gs_udc = ImageDissolve("images/gs_udc.png",2,ramplen=256)
    define gs_cud = ImageDissolve("images/gs_cud.png",2,ramplen=256)
    define gs_clr = ImageDissolve("images/gs_clr.png",2,ramplen=256)
    define gs_hi_ns = ImageDissolve("images/gs_hi_ns.png",2,ramplen=256)
    define gs_r = ImageDissolve("images/gs_r.png",2)
    define gs_l = ImageDissolve("images/gs_l.png",2)
    define gs_rl = ImageDissolve("images/gs_rl.png",2,ramplen=256)
    define gs_lr = ImageDissolve("images/gs_lr.png",2,ramplen=256)
    define gs_du = ImageDissolve("images/gs_du.png",2,ramplen=256)
    define gs_ud = ImageDissolve("images/gs_ud.png",2,ramplen=256)
    define fade2 = Fade(1.0,0,1.0)
    define clouds = ImageDissolve("images/clouds.png",2,ramplen=256)

    define windowin = ComposeTransition(dissolve,None,MoveTransition(0.4,enter=d,leave=u,layers=['screens']))
    define windowout = ComposeTransition(dissolve,MoveTransition(0.4,enter=u,leave=d,layers=['screens']))

    image moyan = "images/moyan.png"

    image eyecatch01 = ("images/eyecatch01.png")
    image eyecatch02 = ("images/eyecatch02.png")
    image eyecatch03 = ("images/eyecatch03.png")
    image eyecatch04 = ("images/eyecatch04.png")
    image eyecatch05 = ("images/eyecatch05.png")


    image end01 = ("images/end01.png")
    image end02 = ("images/end02.png")
    image end03 = ("images/end03.png")
    image end04 = ("images/end04.png")
    image end05 = ("images/end05.png")


    image CU01 = "images/cg/CU01.png"
    image CU02 = "images/cg/CU02.png"
    image CU03 = "images/cg/CU03.png"
    image CU04 = "images/cg/CU04.png"
    image CU05 = "images/cg/CU05.png"
    image CU06 = "images/cg/CU06.png"
    image CU07 = "images/cg/CU07.png"
    image CU08 = "images/cg/CU08.png"
    image CU08p1 = "images/cg/CU08p1.png"
    image CU09 = "images/cg/CU09.png"
    image CU10 = "images/cg/CU10.png"
    image CU11 = "images/cg/CU11.png"
    image CU12 = "images/cg/CU12.png"
    image CU13 = "images/cg/CU13.png"
    image CU14 = "images/cg/CU14.png"
    image CU15 = "images/cg/CU15.png"
    image CU16 = "images/cg/CU16.png"
    image CU17 = "images/cg/CU17.png"
    image CU18 = "images/cg/CU18.png"
    image CU19 = "images/cg/CU19.png"
    image CU19p1 = "images/cg/CU19p1.png"
    image CU20 = "images/cg/CU20.png"
    image EV01 = "images/cg/EV01.png"
    image EV01p1 = "images/cg/EV01p1.png"
    image EV02 = "images/cg/EV02.png"
    image EV02p1 = "images/cg/EV02p1.png"
    image EV03 = "images/cg/EV03.png"
    image EV04 = "images/cg/EV04.png"
    image EV04p1 = "images/cg/EV04p1.png"
    image EV05 = "images/cg/EV05.png"
    image EV05p1 = "images/cg/EV05p1.png"
    image EV06 = "images/cg/EV06.png"
    image EV06p1 = "images/cg/EV06p1.png"
    image EV07 = "images/cg/EV07.png"
    image EV07p1 = "images/cg/EV07p1.png"
    image EV08 = "images/cg/EV08.png"
    image EV08p1 = "images/cg/EV08p1.png"
    image EV09 = "images/cg/EV09.png"
    image EV09p1 = "images/cg/EV09p1.png"
    image EV10 = "images/cg/EV10.png"
    image EV10p1 = "images/cg/EV10p1.png"
    image EV11 = "images/cg/EV11.png"
    image EV11p1 = "images/cg/EV11p1.png"
    image EV12 = "images/cg/EV12.png"
    image EV12p1 = "images/cg/EV12p1.png"
    image EV12p2 = "images/cg/EV12p2.png"
    image EV13 = "images/cg/EV13.png"
    image EV13p1 = "images/cg/EV13p1.png"
    image EV14 = "images/cg/EV14.png"
    image EV14p1 = "images/cg/EV14p1.png"
    image EV15 = "images/cg/EV15.png"
    image EV15p1 = "images/cg/EV15p1.png"
    image EV16 = "images/cg/EV16.png"
    image EV16p1 = "images/cg/EV16p1.png"
    image EV16p2 = "images/cg/EV16p2.png"
    image EV17 = "images/cg/EV17.png"
    image EV17p1 = "images/cg/EV17p1.png"
    image EV17p2 = "images/cg/EV17p2.png"
    image EV18 = "images/cg/EV18.png"
    image EV18p1 = "images/cg/EV18p1.png"
    image EV18p2 = "images/cg/EV18p2.png"
    image EV19 = "images/cg/EV19.png"
    image EV19p1 = "images/cg/EV19p1.png"
    image EV20 = "images/cg/EV20.png"
    image EV20p1 = "images/cg/EV20p1.png"
    image EV20p2 = "images/cg/EV20p2.png"
    image EV21 = "images/cg/EV21.png"
    image EV21p1 = "images/cg/EV21p1.png"
    image EV22 = "images/cg/EV22.png"
    image EV22p1 = "images/cg/EV22p1.png"
    image EV22p2 = "images/cg/EV22p2.png"
    image EV22p3 = "images/cg/EV22p3.png"
    image EV23 = "images/cg/EV23.png"
    image EV23p1 = "images/cg/EV23p1.png"
    image EV23p2 = "images/cg/EV23p2.png"
    image EV24 = "images/cg/EV24.png"
    image EV24p1 = "images/cg/EV24p1.png"
    image EV25 = "images/cg/EV25.png"
    image EV25p1 = "images/cg/EV25p1.png"
    image EV25p2 = "images/cg/EV25p2.png"
    image EV26 = "images/cg/EV26.png"
    image EV27 = "images/cg/EV27.png"
    image EV27p1 = "images/cg/EV27p1.png"
    image EV28 = "images/cg/EV28.png"
    image EV28p1 = "images/cg/EV28p1.png"
    image EV29 = "images/cg/EV29.png"
    image EV29p1 = "images/cg/EV29p1.png"
    image EV30 = "images/cg/EV30.png"
    image EV30p1 = "images/cg/EV30p1.png"
    image EV30p2 = "images/cg/EV30p2.png"
    image EV31 = "images/cg/EV31.png"
    image EV31p1 = "images/cg/EV31p1.png"
    image EV31p2 = "images/cg/EV31p2.png"
    image EV32 = "images/cg/EV32.png"
    image EV32p1 = "images/cg/EV32p1.png"
    image EV32p2 = "images/cg/EV32p2.png"
    image EV33 = "images/cg/EV33.png"
    image EV33p1 = "images/cg/EV33p1.png"
    image EV34 = "images/cg/EV34.png"
    image EV34p1 = "images/cg/EV34p1.png"
    image EV34p2 = "images/cg/EV34p2.png"
    image EV35 = "images/cg/EV35.png"
    image EV35p1 = "images/cg/EV35p1.png"
    image EV36 = "images/cg/EV36.png"
    image EV36p1 = "images/cg/EV36p1.png"
    image EV37 = "images/cg/EV37.png"
    image EV37p1 = "images/cg/EV37p1.png"
    image EV37p2 = "images/cg/EV37p2.png"
    image EV38 = "images/cg/EV38.png"
    image EV38p1 = "images/cg/EV38p1.png"
    image EV39 = "images/cg/EV39.png"
    image EV39p1 = "images/cg/EV39p1.png"
    image EV39p2 = "images/cg/EV39p2.png"
    image EV40 = "images/cg/EV40.png"
    image EV40p1 = "images/cg/EV40p1.png"
    image EV41 = "images/cg/EV41.png"
    image EV41p1 = "images/cg/EV41p1.png"
    image EV42 = "images/cg/EV42.png"
    image EV43 = "images/cg/EV43.png"
    image EV44 = "images/cg/EV44.png"
    image EV44p1 = "images/cg/EV44p1.png"
    image EV45 = "images/cg/EV45.png"
    image EV45p1 = "images/cg/EV45p1.png"
    image EV45p2 = "images/cg/EV45p2.png"
    image EV46 = "images/cg/EV46.png"
    image EV46p1 = "images/cg/EV46p1.png"
    image EV47 = "images/cg/EV47.png"
    image EV47p1 = "images/cg/EV47p1.png"
    image EV48 = "images/cg/EV48.png"
    image EV48p1 = "images/cg/EV48p1.png"
    image EV49 = "images/cg/EV49.png"
    image EV49p1 = "images/cg/EV49p1.png"
    image EV50 = "images/cg/EV50.png"
    image EV50p1 = "images/cg/EV50p1.png"
    image EV50p2 = "images/cg/EV50p2.png"
    image EV51 = "images/cg/EV51.png"
    image EV51p1 = "images/cg/EV51p1.png"
    image EV51p2 = "images/cg/EV51p2.png"
    image EV52 = "images/cg/EV52.png"
    image EV52p1 = "images/cg/EV52p1.png"
    image EV53 = "images/cg/EV53.png"
    image EV53p1 = "images/cg/EV53p1.png"
    image EV54 = "images/cg/EV54.png"
    image EV54p1 = "images/cg/EV54p1.png"
    image EV54p2 = "images/cg/EV54p2.png"
    image EV55 = "images/cg/EV55.png"
    image EV55p1 = "images/cg/EV55p1.png"
    image EV56 = "images/cg/EV56.png"
    image EV56p1 = "images/cg/EV56p1.png"
    image EV56p2 = "images/cg/EV56p2.png"
    image EV57 = "images/cg/EV57.png"
    image EV57p1 = "images/cg/EV57p1.png"
    image EV57p2 = "images/cg/EV57p2.png"
    image EV58 = "images/cg/EV58.png"
    image EV58p1 = "images/cg/EV58p1.png"
    image EV58p2 = "images/cg/EV58p2.png"
    image EV59 = "images/cg/EV59.png"
    image EV59p1 = "images/cg/EV59p1.png"
    image EV60 = "images/cg/EV60.png"
    image EV60p1 = "images/cg/EV60p1.png"
    image EV61 = "images/cg/EV61.png"
    image EV61p1 = "images/cg/EV61p1.png"
    image EV61p2 = "images/cg/EV61p2.png"
    image EV62 = "images/cg/EV62.png"
    image EV62p1 = "images/cg/EV62p1.png"
    image EV63 = "images/cg/EV63.png"
    image EV63p1 = "images/cg/EV63p1.png"
    image EV64 = "images/cg/EV64.png"
    image EV64p1 = "images/cg/EV64p1.png"
    image EV64p2 = "images/cg/EV64p2.png"
    image EV64p3 = "images/cg/EV64p3.png"
    image EV65 = "images/cg/EV65.png"
    image EV65p1 = "images/cg/EV65p1.png"
    image EV65p2 = "images/cg/EV65p2.png"
    image EV66 = "images/cg/EV66.png"
    image EV66p1 = "images/cg/EV66p1.png"
    image EV67 = "images/cg/EV67.png"
    image EV67p1 = "images/cg/EV67p1.png"
    image EV68 = "images/cg/EV68.png"
    image EV68p1 = "images/cg/EV68p1.png"
    image EV69 = "images/cg/EV69.png"
    image EV69p1 = "images/cg/EV69p1.png"
    image EV69p2 = "images/cg/EV69p2.png"
    image EV70 = "images/cg/EV70.png"
    image EV70p1 = "images/cg/EV70p1.png"
    image EV71 = "images/cg/EV71.png"
    image EV71p1 = "images/cg/EV71p1.png"
    image EV71p2 = "images/cg/EV71p2.png"
    image EV72 = "images/cg/EV72.png"
    image EV72p1 = "images/cg/EV72p1.png"
    image EV72p2 = "images/cg/EV72p2.png"
    image EV73 = "images/cg/EV73.png"
    image EV73p1 = "images/cg/EV73p1.png"
    image EV74 = "images/cg/EV74.png"
    image EV74p1 = "images/cg/EV74p1.png"
    image EV75 = "images/cg/EV75.png"
    image EV75p1 = "images/cg/EV75p1.png"
    image EV76 = "images/cg/EV76.png"
    image EV76p1 = "images/cg/EV76p1.png"
    image EV77 = "images/cg/EV77.png"
    image EV77p1 = "images/cg/EV77p1.png"
    image EV78 = "images/cg/EV78.png"
    image EV78p1 = "images/cg/EV78p1.png"
    image EV79 = "images/cg/EV79.png"
    image EV79p1 = "images/cg/EV79p1.png"
    image EV80 = "images/cg/EV80.png"
    image EV80p1 = "images/cg/EV80p1.png"

    image bg01a = "images/bg/bg01a.png"
    image bg01c = "images/bg/bg01c.png"
    image bg02a = "images/bg/bg02a.png"
    image bg02c = "images/bg/bg02c.png"
    image bg03a = "images/bg/bg03a.png"
    image bg04a = "images/bg/bg04a.png"
    image bg04b = "images/bg/bg04b.png"
    image bg05a = "images/bg/bg05a.png"
    image bg05b = "images/bg/bg05b.png"
    image bg06a = "images/bg/bg06a.png"
    image bg07a = "images/bg/bg07a.png"
    image bg08a = "images/bg/bg08a.png"
    image bg08b = "images/bg/bg08b.png"
    image bg08c = "images/bg/bg08c.png"
    image bg08d = "images/bg/bg08d.png"
    image bg09a = "images/bg/bg09a.png"
    image bg09c = "images/bg/bg09c.png"
    image bg10a = "images/bg/bg10a.png"
    image bg10c = "images/bg/bg10c.png"
    image bg11c = "images/bg/bg11c.png"
    image bg12a = "images/bg/bg12a.png"
    image bg12c = "images/bg/bg12c.png"
    image bg13a = "images/bg/bg13a.png"
    image bg13c = "images/bg/bg13c.png"
    image bg14a = "images/bg/bg14a.png"
    image bg14c = "images/bg/bg14c.png"
    image bg15a = "images/bg/bg15a.png"
    image bg15c = "images/bg/bg15c.png"
    image bg16a = "images/bg/bg16a.png"
    image bg16c = "images/bg/bg16c.png"
    image bg17a = "images/bg/bg17a.png"
    image bg17c = "images/bg/bg17c.png"
    image bg18a = "images/bg/bg18a.png"
    image bg18b = "images/bg/bg18b.png"
    image bg19a = "images/bg/bg19a.png"
    image bg19b = "images/bg/bg19b.png"
    image bg20a = "images/bg/bg20a.png"
    image bg20b = "images/bg/bg20b.png"
    image bg21a = "images/bg/bg21a.png"
    image bg21b = "images/bg/bg21b.png"
    image bg22a = "images/bg/bg22a.png"
    image bg22b = "images/bg/bg22b.png"
    image bg23a = "images/bg/bg23a.png"
    image bg23b = "images/bg/bg23b.png"
    image bg24a = "images/bg/bg24a.png"
    image bg24b = "images/bg/bg24b.png"
    image bg25a = "images/bg/bg25a.png"
    image bg25b = "images/bg/bg25b.png"
    image bg26a = "images/bg/bg26a.png"
    image bg26b = "images/bg/bg26b.png"
    image bg26c = "images/bg/bg26c.png"
    image bg27a = "images/bg/bg27a.png"
    image bg27c = "images/bg/bg27c.png"
    image bg28a = "images/bg/bg28a.png"
    image bg28c = "images/bg/bg28c.png"
    image bg29a = "images/bg/bg29a.png"
    image bg29b = "images/bg/bg29b.png"
    image bg29c = "images/bg/bg29c.png"
    image bg30a = "images/bg/bg30a.png"
    image bg30b = "images/bg/bg30b.png"
    image bg31a = "images/bg/bg31a.png"
    image bg31b = "images/bg/bg31b.png"
    image bg32a = "images/bg/bg32a.png"
    image bg32c = "images/bg/bg32c.png"
    image bg33a = "images/bg/bg33a.png"
    image bg33b = "images/bg/bg33b.png"
    image bg33c = "images/bg/bg33c.png"
    image bg34a = "images/bg/bg34a.png"
    image bg34c = "images/bg/bg34c.png"
    image bg35c = "images/bg/bg35c.png"
    image bg36a = "images/bg/bg36a.png"
    image bg36c = "images/bg/bg36c.png"
    image bg37a = "images/bg/bg37a.png"
    image bg37c = "images/bg/bg37c.png"
    image bg38a = "images/bg/bg38a.png"
    image bg38c = "images/bg/bg38c.png"
    image bg39a = "images/bg/bg39a.png"
    image bg39a2 = "images/bg/bg39a2.png"
    image bg39c = "images/bg/bg39c.png"
    image bg40a = "images/bg/bg40a.png"
    image bg40c = "images/bg/bg40c.png"
    image bg41a = "images/bg/bg41a.png"
    image bg41c = "images/bg/bg41c.png"
    image bg42a = "images/bg/bg42a.png"
    image bg42b = "images/bg/bg42b.png"
    image bg42c = "images/bg/bg42c.png"
    image bg43a = "images/bg/bg43a.png"
    image bg43c = "images/bg/bg43c.png"

    image erisu ter01f2 = "images/chars/ter01f2.png"
    image erisu ter01m = "images/chars/ter01m.png"
    image erisu ter01p = "images/chars/ter01p.png"
    image erisu ter01z = "images/chars/ter01z.png"
    image erisu ter02f2 = "images/chars/ter02f2.png"
    image erisu ter02m = "images/chars/ter02m.png"
    image erisu ter02p = "images/chars/ter02p.png"
    image erisu ter02z = "images/chars/ter02z.png"
    image erisu ter03f2 = "images/chars/ter03f2.png"
    image erisu ter03m = "images/chars/ter03m.png"
    image erisu ter03p = "images/chars/ter03p.png"
    image erisu ter03z = "images/chars/ter03z.png"
    image erisu ter04f2 = "images/chars/ter04f2.png"
    image erisu ter04m = "images/chars/ter04m.png"
    image erisu ter04p = "images/chars/ter04p.png"
    image erisu ter04z = "images/chars/ter04z.png"
    image erisu ter05f2 = "images/chars/ter05f2.png"
    image erisu ter05m = "images/chars/ter05m.png"
    image erisu ter05p = "images/chars/ter05p.png"
    image erisu ter05z = "images/chars/ter05z.png"
    image erisu ter06f2 = "images/chars/ter06f2.png"
    image erisu ter06m = "images/chars/ter06m.png"
    image erisu ter06p = "images/chars/ter06p.png"
    image erisu ter06z = "images/chars/ter06z.png"
    image erisu ter07f2 = "images/chars/ter07f2.png"
    image erisu ter07m = "images/chars/ter07m.png"
    image erisu ter07p = "images/chars/ter07p.png"
    image erisu ter07z = "images/chars/ter07z.png"
    image erisu ter08f2 = "images/chars/ter08f2.png"
    image erisu ter08m = "images/chars/ter08m.png"
    image erisu ter08p = "images/chars/ter08p.png"
    image erisu ter08z = "images/chars/ter08z.png"
    image erisu ter09f2 = "images/chars/ter09f2.png"
    image erisu ter09m = "images/chars/ter09m.png"
    image erisu ter09p = "images/chars/ter09p.png"
    image erisu ter09z = "images/chars/ter09z.png"
    image erisu ter10f2 = "images/chars/ter10f2.png"
    image erisu ter10m = "images/chars/ter10m.png"
    image erisu ter10p = "images/chars/ter10p.png"
    image erisu ter10z = "images/chars/ter10z.png"
    image erisu ter11f2 = "images/chars/ter11f2.png"
    image erisu ter11m = "images/chars/ter11m.png"
    image erisu ter11p = "images/chars/ter11p.png"
    image erisu ter11z = "images/chars/ter11z.png"
    image kaede tka01f2 = "images/chars/tka01f2.png"
    image kaede tka01m = "images/chars/tka01m.png"
    image kaede tka01p = "images/chars/tka01p.png"
    image kaede tka01s2 = "images/chars/tka01s2.png"
    image kaede tka01z = "images/chars/tka01z.png"
    image kaede tka02f2 = "images/chars/tka02f2.png"
    image kaede tka02m = "images/chars/tka02m.png"
    image kaede tka02p = "images/chars/tka02p.png"
    image kaede tka02s2 = "images/chars/tka02s2.png"
    image kaede tka02z = "images/chars/tka02z.png"
    image kaede tka03f2 = "images/chars/tka03f2.png"
    image kaede tka03m = "images/chars/tka03m.png"
    image kaede tka03p = "images/chars/tka03p.png"
    image kaede tka03s2 = "images/chars/tka03s2.png"
    image kaede tka03z = "images/chars/tka03z.png"
    image kaede tka04f2 = "images/chars/tka04f2.png"
    image kaede tka04m = "images/chars/tka04m.png"
    image kaede tka04p = "images/chars/tka04p.png"
    image kaede tka04s2 = "images/chars/tka04s2.png"
    image kaede tka04z = "images/chars/tka04z.png"
    image kaede tka05f2 = "images/chars/tka05f2.png"
    image kaede tka05m = "images/chars/tka05m.png"
    image kaede tka05p = "images/chars/tka05p.png"
    image kaede tka05s2 = "images/chars/tka05s2.png"
    image kaede tka05z = "images/chars/tka05z.png"
    image kaede tka06f2 = "images/chars/tka06f2.png"
    image kaede tka06m = "images/chars/tka06m.png"
    image kaede tka06p = "images/chars/tka06p.png"
    image kaede tka06s2 = "images/chars/tka06s2.png"
    image kaede tka06z = "images/chars/tka06z.png"
    image kaede tka07f2 = "images/chars/tka07f2.png"
    image kaede tka07m = "images/chars/tka07m.png"
    image kaede tka07p = "images/chars/tka07p.png"
    image kaede tka07s2 = "images/chars/tka07s2.png"
    image kaede tka07z = "images/chars/tka07z.png"
    image kaede tka08f2 = "images/chars/tka08f2.png"
    image kaede tka08m = "images/chars/tka08m.png"
    image kaede tka08p = "images/chars/tka08p.png"
    image kaede tka08s2 = "images/chars/tka08s2.png"
    image kaede tka08z = "images/chars/tka08z.png"
    image kaede tka09f2 = "images/chars/tka09f2.png"
    image kaede tka09m = "images/chars/tka09m.png"
    image kaede tka09p = "images/chars/tka09p.png"
    image kaede tka09s2 = "images/chars/tka09s2.png"
    image kaede tka09z = "images/chars/tka09z.png"
    image kaede tka10f2 = "images/chars/tka10f2.png"
    image kaede tka10m = "images/chars/tka10m.png"
    image kaede tka10p = "images/chars/tka10p.png"
    image kaede tka10s2 = "images/chars/tka10s2.png"
    image kaede tka10z = "images/chars/tka10z.png"
    image kaede tka11f2 = "images/chars/tka11f2.png"
    image kaede tka11m = "images/chars/tka11m.png"
    image kaede tka11p = "images/chars/tka11p.png"
    image kaede tka11s2 = "images/chars/tka11s2.png"
    image kaede tka11z = "images/chars/tka11z.png"
    image mai tma01f2 = "images/chars/tma01f2.png"
    image mai tma01m = "images/chars/tma01m.png"
    image mai tma01p = "images/chars/tma01p.png"
    image mai tma01s2 = "images/chars/tma01s2.png"
    image mai tma01z = "images/chars/tma01z.png"
    image mai tma02f2 = "images/chars/tma02f2.png"
    image mai tma02m = "images/chars/tma02m.png"
    image mai tma02p = "images/chars/tma02p.png"
    image mai tma02s2 = "images/chars/tma02s2.png"
    image mai tma02z = "images/chars/tma02z.png"
    image mai tma03f2 = "images/chars/tma03f2.png"
    image mai tma03m = "images/chars/tma03m.png"
    image mai tma03p = "images/chars/tma03p.png"
    image mai tma03s2 = "images/chars/tma03s2.png"
    image mai tma03z = "images/chars/tma03z.png"
    image mai tma04f2 = "images/chars/tma04f2.png"
    image mai tma04m = "images/chars/tma04m.png"
    image mai tma04p = "images/chars/tma04p.png"
    image mai tma04s2 = "images/chars/tma04s2.png"
    image mai tma04z = "images/chars/tma04z.png"
    image mai tma05f2 = "images/chars/tma05f2.png"
    image mai tma05m = "images/chars/tma05m.png"
    image mai tma05p = "images/chars/tma05p.png"
    image mai tma05s2 = "images/chars/tma05s2.png"
    image mai tma05z = "images/chars/tma05z.png"
    image mai tma06 = "images/chars/tma06.png"
    image mai tma06f2 = "images/chars/tma06f2.png"
    image mai tma06m = "images/chars/tma06m.png"
    image mai tma06p = "images/chars/tma06p.png"
    image mai tma06s2 = "images/chars/tma06s2.png"
    image mai tma06z = "images/chars/tma06z.png"
    image mai tma07f2 = "images/chars/tma07f2.png"
    image mai tma07m = "images/chars/tma07m.png"
    image mai tma07p = "images/chars/tma07p.png"
    image mai tma07s2 = "images/chars/tma07s2.png"
    image mai tma07z = "images/chars/tma07z.png"
    image mai tma08f2 = "images/chars/tma08f2.png"
    image mai tma08m = "images/chars/tma08m.png"
    image mai tma08p = "images/chars/tma08p.png"
    image mai tma08s2 = "images/chars/tma08s2.png"
    image mai tma08z = "images/chars/tma08z.png"
    image mai tma09f2 = "images/chars/tma09f2.png"
    image mai tma09m = "images/chars/tma09m.png"
    image mai tma09p = "images/chars/tma09p.png"
    image mai tma09s2 = "images/chars/tma09s2.png"
    image mai tma09z = "images/chars/tma09z.png"
    image mai tma10f2 = "images/chars/tma10f2.png"
    image mai tma10m = "images/chars/tma10m.png"
    image mai tma10p = "images/chars/tma10p.png"
    image mai tma10s2 = "images/chars/tma10s2.png"
    image mai tma10z = "images/chars/tma10z.png"
    image mai tma11f2 = "images/chars/tma11f2.png"
    image mai tma11m = "images/chars/tma11m.png"
    image mai tma11p = "images/chars/tma11p.png"
    image mai tma11s2 = "images/chars/tma11s2.png"
    image mai tma11z = "images/chars/tma11z.png"
    image miya tmi01f2 = "images/chars/tmi01f2.png"
    image miya tmi01m = "images/chars/tmi01m.png"
    image miya tmi01p = "images/chars/tmi01p.png"
    image miya tmi01s2 = "images/chars/tmi01s2.png"
    image miya tmi01z = "images/chars/tmi01z.png"
    image miya tmi02f2 = "images/chars/tmi02f2.png"
    image miya tmi02m = "images/chars/tmi02m.png"
    image miya tmi02p = "images/chars/tmi02p.png"
    image miya tmi02s2 = "images/chars/tmi02s2.png"
    image miya tmi02z = "images/chars/tmi02z.png"
    image miya tmi03f2 = "images/chars/tmi03f2.png"
    image miya tmi03m = "images/chars/tmi03m.png"
    image miya tmi03p = "images/chars/tmi03p.png"
    image miya tmi03s2 = "images/chars/tmi03s2.png"
    image miya tmi03z = "images/chars/tmi03z.png"
    image miya tmi04f2 = "images/chars/tmi04f2.png"
    image miya tmi04m = "images/chars/tmi04m.png"
    image miya tmi04p = "images/chars/tmi04p.png"
    image miya tmi04s2 = "images/chars/tmi04s2.png"
    image miya tmi04z = "images/chars/tmi04z.png"
    image miya tmi05f2 = "images/chars/tmi05f2.png"
    image miya tmi05m = "images/chars/tmi05m.png"
    image miya tmi05p = "images/chars/tmi05p.png"
    image miya tmi05s2 = "images/chars/tmi05s2.png"
    image miya tmi05z = "images/chars/tmi05z.png"
    image miya tmi06f2 = "images/chars/tmi06f2.png"
    image miya tmi06m = "images/chars/tmi06m.png"
    image miya tmi06p = "images/chars/tmi06p.png"
    image miya tmi06s2 = "images/chars/tmi06s2.png"
    image miya tmi06z = "images/chars/tmi06z.png"
    image miya tmi07f2 = "images/chars/tmi07f2.png"
    image miya tmi07m = "images/chars/tmi07m.png"
    image miya tmi07p = "images/chars/tmi07p.png"
    image miya tmi07s2 = "images/chars/tmi07s2.png"
    image miya tmi07z = "images/chars/tmi07z.png"
    image miya tmi08f2 = "images/chars/tmi08f2.png"
    image miya tmi08m = "images/chars/tmi08m.png"
    image miya tmi08p = "images/chars/tmi08p.png"
    image miya tmi08s2 = "images/chars/tmi08s2.png"
    image miya tmi08z = "images/chars/tmi08z.png"
    image miya tmi09f2 = "images/chars/tmi09f2.png"
    image miya tmi09m = "images/chars/tmi09m.png"
    image miya tmi09p = "images/chars/tmi09p.png"
    image miya tmi09s2 = "images/chars/tmi09s2.png"
    image miya tmi09z = "images/chars/tmi09z.png"
    image miya tmi10f2 = "images/chars/tmi10f2.png"
    image miya tmi10m = "images/chars/tmi10m.png"
    image miya tmi10p = "images/chars/tmi10p.png"
    image miya tmi10s2 = "images/chars/tmi10s2.png"
    image miya tmi10z = "images/chars/tmi10z.png"
    image miya tmi11f2 = "images/chars/tmi11f2.png"
    image miya tmi11m = "images/chars/tmi11m.png"
    image miya tmi11p = "images/chars/tmi11p.png"
    image miya tmi11s2 = "images/chars/tmi11s2.png"
    image miya tmi11z = "images/chars/tmi11z.png"
    image nanami tna01f2 = "images/chars/tna01f2.png"
    image nanami tna01m = "images/chars/tna01m.png"
    image nanami tna01p = "images/chars/tna01p.png"
    image nanami tna01s2 = "images/chars/tna01s2.png"
    image nanami tna01z = "images/chars/tna01z.png"
    image nanami tna02f2 = "images/chars/tna02f2.png"
    image nanami tna02m = "images/chars/tna02m.png"
    image nanami tna02p = "images/chars/tna02p.png"
    image nanami tna02s2 = "images/chars/tna02s2.png"
    image nanami tna02z = "images/chars/tna02z.png"
    image nanami tna03f2 = "images/chars/tna03f2.png"
    image nanami tna03m = "images/chars/tna03m.png"
    image nanami tna03p = "images/chars/tna03p.png"
    image nanami tna03s2 = "images/chars/tna03s2.png"
    image nanami tna03z = "images/chars/tna03z.png"
    image nanami tna04f2 = "images/chars/tna04f2.png"
    image nanami tna04m = "images/chars/tna04m.png"
    image nanami tna04p = "images/chars/tna04p.png"
    image nanami tna04s2 = "images/chars/tna04s2.png"
    image nanami tna04z = "images/chars/tna04z.png"
    image nanami tna05f2 = "images/chars/tna05f2.png"
    image nanami tna05m = "images/chars/tna05m.png"
    image nanami tna05p = "images/chars/tna05p.png"
    image nanami tna05s2 = "images/chars/tna05s2.png"
    image nanami tna05z = "images/chars/tna05z.png"
    image nanami tna06f2 = "images/chars/tna06f2.png"
    image nanami tna06m = "images/chars/tna06m.png"
    image nanami tna06p = "images/chars/tna06p.png"
    image nanami tna06s2 = "images/chars/tna06s2.png"
    image nanami tna06z = "images/chars/tna06z.png"
    image nanami tna07f2 = "images/chars/tna07f2.png"
    image nanami tna07m = "images/chars/tna07m.png"
    image nanami tna07p = "images/chars/tna07p.png"
    image nanami tna07s2 = "images/chars/tna07s2.png"
    image nanami tna07z = "images/chars/tna07z.png"
    image nanami tna08f2 = "images/chars/tna08f2.png"
    image nanami tna08m = "images/chars/tna08m.png"
    image nanami tna08p = "images/chars/tna08p.png"
    image nanami tna08s2 = "images/chars/tna08s2.png"
    image nanami tna08z = "images/chars/tna08z.png"
    image nanami tna09f2 = "images/chars/tna09f2.png"
    image nanami tna09m = "images/chars/tna09m.png"
    image nanami tna09p = "images/chars/tna09p.png"
    image nanami tna09s2 = "images/chars/tna09s2.png"
    image nanami tna09z = "images/chars/tna09z.png"
    image nanami tna10f2 = "images/chars/tna10f2.png"
    image nanami tna10m = "images/chars/tna10m.png"
    image nanami tna10p = "images/chars/tna10p.png"
    image nanami tna10s2 = "images/chars/tna10s2.png"
    image nanami tna10z = "images/chars/tna10z.png"
    image nanami tna11f2 = "images/chars/tna11f2.png"
    image nanami tna11m = "images/chars/tna11m.png"
    image nanami tna11p = "images/chars/tna11p.png"
    image nanami tna11s2 = "images/chars/tna11s2.png"
    image nanami tna11z = "images/chars/tna11z.png"
    image reo tre01f2 = "images/chars/tre01f2.png"
    image reo tre01m = "images/chars/tre01m.png"
    image reo tre01p = "images/chars/tre01p.png"
    image reo tre01s2 = "images/chars/tre01s2.png"
    image reo tre01z = "images/chars/tre01z.png"
    image reo tre02f2 = "images/chars/tre02f2.png"
    image reo tre02m = "images/chars/tre02m.png"
    image reo tre02p = "images/chars/tre02p.png"
    image reo tre02s2 = "images/chars/tre02s2.png"
    image reo tre02z = "images/chars/tre02z.png"
    image reo tre03f2 = "images/chars/tre03f2.png"
    image reo tre03m = "images/chars/tre03m.png"
    image reo tre03p = "images/chars/tre03p.png"
    image reo tre03s2 = "images/chars/tre03s2.png"
    image reo tre03z = "images/chars/tre03z.png"
    image reo tre04f2 = "images/chars/tre04f2.png"
    image reo tre04m = "images/chars/tre04m.png"
    image reo tre04p = "images/chars/tre04p.png"
    image reo tre04s2 = "images/chars/tre04s2.png"
    image reo tre04z = "images/chars/tre04z.png"
    image reo tre05f2 = "images/chars/tre05f2.png"
    image reo tre05m = "images/chars/tre05m.png"
    image reo tre05p = "images/chars/tre05p.png"
    image reo tre05s2 = "images/chars/tre05s2.png"
    image reo tre05z = "images/chars/tre05z.png"
    image reo tre06f2 = "images/chars/tre06f2.png"
    image reo tre06m = "images/chars/tre06m.png"
    image reo tre06p = "images/chars/tre06p.png"
    image reo tre06s2 = "images/chars/tre06s2.png"
    image reo tre06z = "images/chars/tre06z.png"
    image reo tre07f2 = "images/chars/tre07f2.png"
    image reo tre07m = "images/chars/tre07m.png"
    image reo tre07p = "images/chars/tre07p.png"
    image reo tre07s2 = "images/chars/tre07s2.png"
    image reo tre07z = "images/chars/tre07z.png"
    image reo tre08f2 = "images/chars/tre08f2.png"
    image reo tre08m = "images/chars/tre08m.png"
    image reo tre08p = "images/chars/tre08p.png"
    image reo tre08s2 = "images/chars/tre08s2.png"
    image reo tre08z = "images/chars/tre08z.png"
    image reo tre09f2 = "images/chars/tre09f2.png"
    image reo tre09m = "images/chars/tre09m.png"
    image reo tre09p = "images/chars/tre09p.png"
    image reo tre09s2 = "images/chars/tre09s2.png"
    image reo tre09z = "images/chars/tre09z.png"
    image reo tre10f2 = "images/chars/tre10f2.png"
    image reo tre10m = "images/chars/tre10m.png"
    image reo tre10p = "images/chars/tre10p.png"
    image reo tre10s2 = "images/chars/tre10s2.png"
    image reo tre10z = "images/chars/tre10z.png"
    image reo tre11f2 = "images/chars/tre11f2.png"
    image reo tre11m = "images/chars/tre11m.png"
    image reo tre11p = "images/chars/tre11p.png"
    image reo tre11s2 = "images/chars/tre11s2.png"
    image reo tre11z = "images/chars/tre11z.png"
    image risa tri01f2 = "images/chars/tri01f2.png"
    image risa tri01m = "images/chars/tri01m.png"
    image risa tri01p = "images/chars/tri01p.png"
    image risa tri01s2 = "images/chars/tri01s2.png"
    image risa tri01z = "images/chars/tri01z.png"
    image risa tri02f2 = "images/chars/tri02f2.png"
    image risa tri02m = "images/chars/tri02m.png"
    image risa tri02p = "images/chars/tri02p.png"
    image risa tri02s2 = "images/chars/tri02s2.png"
    image risa tri02z = "images/chars/tri02z.png"
    image risa tri03f2 = "images/chars/tri03f2.png"
    image risa tri03m = "images/chars/tri03m.png"
    image risa tri03p = "images/chars/tri03p.png"
    image risa tri03s2 = "images/chars/tri03s2.png"
    image risa tri03z = "images/chars/tri03z.png"
    image risa tri04f2 = "images/chars/tri04f2.png"
    image risa tri04m = "images/chars/tri04m.png"
    image risa tri04p = "images/chars/tri04p.png"
    image risa tri04s2 = "images/chars/tri04s2.png"
    image risa tri04z = "images/chars/tri04z.png"
    image risa tri05f2 = "images/chars/tri05f2.png"
    image risa tri05m = "images/chars/tri05m.png"
    image risa tri05p = "images/chars/tri05p.png"
    image risa tri05s2 = "images/chars/tri05s2.png"
    image risa tri05z = "images/chars/tri05z.png"
    image risa tri06f2 = "images/chars/tri06f2.png"
    image risa tri06m = "images/chars/tri06m.png"
    image risa tri06p = "images/chars/tri06p.png"
    image risa tri06s2 = "images/chars/tri06s2.png"
    image risa tri06z = "images/chars/tri06z.png"
    image risa tri07f2 = "images/chars/tri07f2.png"
    image risa tri07m = "images/chars/tri07m.png"
    image risa tri07p = "images/chars/tri07p.png"
    image risa tri07s2 = "images/chars/tri07s2.png"
    image risa tri07z = "images/chars/tri07z.png"
    image risa tri08f2 = "images/chars/tri08f2.png"
    image risa tri08m = "images/chars/tri08m.png"
    image risa tri08p = "images/chars/tri08p.png"
    image risa tri08s2 = "images/chars/tri08s2.png"
    image risa tri08z = "images/chars/tri08z.png"
    image risa tri09f2 = "images/chars/tri09f2.png"
    image risa tri09m = "images/chars/tri09m.png"
    image risa tri09p = "images/chars/tri09p.png"
    image risa tri09s2 = "images/chars/tri09s2.png"
    image risa tri09z = "images/chars/tri09z.png"
    image risa tri10f2 = "images/chars/tri10f2.png"
    image risa tri10m = "images/chars/tri10m.png"
    image risa tri10p = "images/chars/tri10p.png"
    image risa tri10s2 = "images/chars/tri10s2.png"
    image risa tri10z = "images/chars/tri10z.png"
    image risa tri11f2 = "images/chars/tri11f2.png"
    image risa tri11m = "images/chars/tri11m.png"
    image risa tri11p = "images/chars/tri11p.png"
    image risa tri11s2 = "images/chars/tri11s2.png"
    image risa tri11z = "images/chars/tri11z.png"
    image rikka trk01f2 = "images/chars/trk01f2.png"
    image rikka trk01m = "images/chars/trk01m.png"
    image rikka trk01p = "images/chars/trk01p.png"
    image rikka trk01s2 = "images/chars/trk01s2.png"
    image rikka trk01z = "images/chars/trk01z.png"
    image rikka trk02f2 = "images/chars/trk02f2.png"
    image rikka trk02m = "images/chars/trk02m.png"
    image rikka trk02p = "images/chars/trk02p.png"
    image rikka trk02s2 = "images/chars/trk02s2.png"
    image rikka trk02z = "images/chars/trk02z.png"
    image rikka trk03f2 = "images/chars/trk03f2.png"
    image rikka trk03m = "images/chars/trk03m.png"
    image rikka trk03p = "images/chars/trk03p.png"
    image rikka trk03s2 = "images/chars/trk03s2.png"
    image rikka trk03z = "images/chars/trk03z.png"
    image rikka trk04f2 = "images/chars/trk04f2.png"
    image rikka trk04m = "images/chars/trk04m.png"
    image rikka trk04p = "images/chars/trk04p.png"
    image rikka trk04s2 = "images/chars/trk04s2.png"
    image rikka trk04z = "images/chars/trk04z.png"
    image rikka trk05f2 = "images/chars/trk05f2.png"
    image rikka trk05m = "images/chars/trk05m.png"
    image rikka trk05p = "images/chars/trk05p.png"
    image rikka trk05s2 = "images/chars/trk05s2.png"
    image rikka trk05z = "images/chars/trk05z.png"
    image rikka trk06f2 = "images/chars/trk06f2.png"
    image rikka trk06m = "images/chars/trk06m.png"
    image rikka trk06p = "images/chars/trk06p.png"
    image rikka trk06s2 = "images/chars/trk06s2.png"
    image rikka trk06z = "images/chars/trk06z.png"
    image rikka trk07f2 = "images/chars/trk07f2.png"
    image rikka trk07m = "images/chars/trk07m.png"
    image rikka trk07p = "images/chars/trk07p.png"
    image rikka trk07s2 = "images/chars/trk07s2.png"
    image rikka trk07z = "images/chars/trk07z.png"
    image rikka trk08f2 = "images/chars/trk08f2.png"
    image rikka trk08m = "images/chars/trk08m.png"
    image rikka trk08p = "images/chars/trk08p.png"
    image rikka trk08s2 = "images/chars/trk08s2.png"
    image rikka trk08z = "images/chars/trk08z.png"
    image rikka trk09f2 = "images/chars/trk09f2.png"
    image rikka trk09m = "images/chars/trk09m.png"
    image rikka trk09p = "images/chars/trk09p.png"
    image rikka trk09s2 = "images/chars/trk09s2.png"
    image rikka trk09z = "images/chars/trk09z.png"
    image rikka trk10f2 = "images/chars/trk10f2.png"
    image rikka trk10m = "images/chars/trk10m.png"
    image rikka trk10p = "images/chars/trk10p.png"
    image rikka trk10s2 = "images/chars/trk10s2.png"
    image rikka trk10z = "images/chars/trk10z.png"
    image rikka trk11f2 = "images/chars/trk11f2.png"
    image rikka trk11m = "images/chars/trk11m.png"
    image rikka trk11p = "images/chars/trk11p.png"
    image rikka trk11s2 = "images/chars/trk11s2.png"
    image rikka trk11z = "images/chars/trk11z.png"
    image rena trn01f2 = "images/chars/trn01f2.png"
    image rena trn01m = "images/chars/trn01m.png"
    image rena trn01p = "images/chars/trn01p.png"
    image rena trn01z = "images/chars/trn01z.png"
    image rena trn02f2 = "images/chars/trn02f2.png"
    image rena trn02m = "images/chars/trn02m.png"
    image rena trn02p = "images/chars/trn02p.png"
    image rena trn02z = "images/chars/trn02z.png"
    image rena trn03f2 = "images/chars/trn03f2.png"
    image rena trn03m = "images/chars/trn03m.png"
    image rena trn03p = "images/chars/trn03p.png"
    image rena trn03z = "images/chars/trn03z.png"
    image rena trn04f2 = "images/chars/trn04f2.png"
    image rena trn04m = "images/chars/trn04m.png"
    image rena trn04p = "images/chars/trn04p.png"
    image rena trn04z = "images/chars/trn04z.png"
    image rena trn05f2 = "images/chars/trn05f2.png"
    image rena trn05m = "images/chars/trn05m.png"
    image rena trn05p = "images/chars/trn05p.png"
    image rena trn05z = "images/chars/trn05z.png"
    image rena trn06f2 = "images/chars/trn06f2.png"
    image rena trn06m = "images/chars/trn06m.png"
    image rena trn06p = "images/chars/trn06p.png"
    image rena trn06z = "images/chars/trn06z.png"
    image rena trn07f2 = "images/chars/trn07f2.png"
    image rena trn07m = "images/chars/trn07m.png"
    image rena trn07p = "images/chars/trn07p.png"
    image rena trn07z = "images/chars/trn07z.png"
    image rena trn08f2 = "images/chars/trn08f2.png"
    image rena trn08m = "images/chars/trn08m.png"
    image rena trn08p = "images/chars/trn08p.png"
    image rena trn08z = "images/chars/trn08z.png"
    image rena trn09f2 = "images/chars/trn09f2.png"
    image rena trn09m = "images/chars/trn09m.png"
    image rena trn09p = "images/chars/trn09p.png"
    image rena trn09z = "images/chars/trn09z.png"
    image rena trn10f2 = "images/chars/trn10f2.png"
    image rena trn10m = "images/chars/trn10m.png"
    image rena trn10p = "images/chars/trn10p.png"
    image rena trn10z = "images/chars/trn10z.png"
    image rena trn11f2 = "images/chars/trn11f2.png"
    image rena trn11m = "images/chars/trn11m.png"
    image rena trn11p = "images/chars/trn11p.png"
    image rena trn11z = "images/chars/trn11z.png"
    image runa tru01f2 = "images/chars/tru01f2.png"
    image runa tru01m = "images/chars/tru01m.png"
    image runa tru01p = "images/chars/tru01p.png"
    image runa tru01s2 = "images/chars/tru01s2.png"
    image runa tru02f2 = "images/chars/tru02f2.png"
    image runa tru02m = "images/chars/tru02m.png"
    image runa tru02p = "images/chars/tru02p.png"
    image runa tru02s2 = "images/chars/tru02s2.png"
    image runa tru03f2 = "images/chars/tru03f2.png"
    image runa tru03m = "images/chars/tru03m.png"
    image runa tru03p = "images/chars/tru03p.png"
    image runa tru03s2 = "images/chars/tru03s2.png"
    image runa tru03sc = "images/chars/tru03sc.png"
    image runa tru04f2 = "images/chars/tru04f2.png"
    image runa tru04m = "images/chars/tru04m.png"
    image runa tru04p = "images/chars/tru04p.png"
    image runa tru04s2 = "images/chars/tru04s2.png"
    image runa tru05f2 = "images/chars/tru05f2.png"
    image runa tru05m = "images/chars/tru05m.png"
    image runa tru05p = "images/chars/tru05p.png"
    image runa tru05s2 = "images/chars/tru05s2.png"
    image runa tru06f2 = "images/chars/tru06f2.png"
    image runa tru06m = "images/chars/tru06m.png"
    image runa tru06p = "images/chars/tru06p.png"
    image runa tru06s2 = "images/chars/tru06s2.png"
    image runa tru07f2 = "images/chars/tru07f2.png"
    image runa tru07m = "images/chars/tru07m.png"
    image runa tru07p = "images/chars/tru07p.png"
    image runa tru07s2 = "images/chars/tru07s2.png"
    image runa tru08f2 = "images/chars/tru08f2.png"
    image runa tru08m = "images/chars/tru08m.png"
    image runa tru08p = "images/chars/tru08p.png"
    image runa tru08s2 = "images/chars/tru08s2.png"
    image runa tru09f2 = "images/chars/tru09f2.png"
    image runa tru09m = "images/chars/tru09m.png"
    image runa tru09p = "images/chars/tru09p.png"
    image runa tru09s2 = "images/chars/tru09s2.png"
    image runa tru10f2 = "images/chars/tru10f2.png"
    image runa tru10m = "images/chars/tru10m.png"
    image runa tru10p = "images/chars/tru10p.png"
    image runa tru10s2 = "images/chars/tru10s2.png"
    image runa tru11f2 = "images/chars/tru11f2.png"
    image runa tru11m = "images/chars/tru11m.png"
    image runa tru11p = "images/chars/tru11p.png"
    image runa tru11s2 = "images/chars/tru11s2.png"
    image sara tsa01f2 = "images/chars/tsa01f2.png"
    image sara tsa01m = "images/chars/tsa01m.png"
    image sara tsa01p = "images/chars/tsa01p.png"
    image sara tsa01s2 = "images/chars/tsa01s2.png"
    image sara tsa01z = "images/chars/tsa01z.png"
    image sara tsa02f2 = "images/chars/tsa02f2.png"
    image sara tsa02m = "images/chars/tsa02m.png"
    image sara tsa02p = "images/chars/tsa02p.png"
    image sara tsa02s2 = "images/chars/tsa02s2.png"
    image sara tsa02z = "images/chars/tsa02z.png"
    image sara tsa03f2 = "images/chars/tsa03f2.png"
    image sara tsa03m = "images/chars/tsa03m.png"
    image sara tsa03p = "images/chars/tsa03p.png"
    image sara tsa03s2 = "images/chars/tsa03s2.png"
    image sara tsa03z = "images/chars/tsa03z.png"
    image sara tsa04f2 = "images/chars/tsa04f2.png"
    image sara tsa04m = "images/chars/tsa04m.png"
    image sara tsa04p = "images/chars/tsa04p.png"
    image sara tsa04s2 = "images/chars/tsa04s2.png"
    image sara tsa04z = "images/chars/tsa04z.png"
    image sara tsa05f2 = "images/chars/tsa05f2.png"
    image sara tsa05m = "images/chars/tsa05m.png"
    image sara tsa05p = "images/chars/tsa05p.png"
    image sara tsa05s2 = "images/chars/tsa05s2.png"
    image sara tsa05z = "images/chars/tsa05z.png"
    image sara tsa06f2 = "images/chars/tsa06f2.png"
    image sara tsa06m = "images/chars/tsa06m.png"
    image sara tsa06p = "images/chars/tsa06p.png"
    image sara tsa06s2 = "images/chars/tsa06s2.png"
    image sara tsa06z = "images/chars/tsa06z.png"
    image sara tsa07f2 = "images/chars/tsa07f2.png"
    image sara tsa07m = "images/chars/tsa07m.png"
    image sara tsa07p = "images/chars/tsa07p.png"
    image sara tsa07s2 = "images/chars/tsa07s2.png"
    image sara tsa07z = "images/chars/tsa07z.png"
    image sara tsa08f2 = "images/chars/tsa08f2.png"
    image sara tsa08m = "images/chars/tsa08m.png"
    image sara tsa08p = "images/chars/tsa08p.png"
    image sara tsa08s2 = "images/chars/tsa08s2.png"
    image sara tsa08z = "images/chars/tsa08z.png"
    image sara tsa09f2 = "images/chars/tsa09f2.png"
    image sara tsa09m = "images/chars/tsa09m.png"
    image sara tsa09p = "images/chars/tsa09p.png"
    image sara tsa09s2 = "images/chars/tsa09s2.png"
    image sara tsa09z = "images/chars/tsa09z.png"
    image sara tsa10f2 = "images/chars/tsa10f2.png"
    image sara tsa10m = "images/chars/tsa10m.png"
    image sara tsa10p = "images/chars/tsa10p.png"
    image sara tsa10s2 = "images/chars/tsa10s2.png"
    image sara tsa10z = "images/chars/tsa10z.png"
    image sara tsa11f2 = "images/chars/tsa11f2.png"
    image sara tsa11m = "images/chars/tsa11m.png"
    image sara tsa11p = "images/chars/tsa11p.png"
    image sara tsa11s2 = "images/chars/tsa11s2.png"
    image sara tsa11z = "images/chars/tsa11z.png"
    image sizuku tsi01f2 = "images/chars/tsi01f2.png"
    image sizuku tsi01m = "images/chars/tsi01m.png"
    image sizuku tsi01p = "images/chars/tsi01p.png"
    image sizuku tsi02f2 = "images/chars/tsi02f2.png"
    image sizuku tsi02m = "images/chars/tsi02m.png"
    image sizuku tsi02p = "images/chars/tsi02p.png"
    image sizuku tsi03f2 = "images/chars/tsi03f2.png"
    image sizuku tsi03m = "images/chars/tsi03m.png"
    image sizuku tsi03p = "images/chars/tsi03p.png"
    image sizuku tsi04f2 = "images/chars/tsi04f2.png"
    image sizuku tsi04m = "images/chars/tsi04m.png"
    image sizuku tsi04p = "images/chars/tsi04p.png"
    image sizuku tsi05f2 = "images/chars/tsi05f2.png"
    image sizuku tsi05m = "images/chars/tsi05m.png"
    image sizuku tsi05p = "images/chars/tsi05p.png"
    image sizuku tsi06f2 = "images/chars/tsi06f2.png"
    image sizuku tsi06m = "images/chars/tsi06m.png"
    image sizuku tsi06p = "images/chars/tsi06p.png"
    image sizuku tsi07f2 = "images/chars/tsi07f2.png"
    image sizuku tsi07m = "images/chars/tsi07m.png"
    image sizuku tsi07p = "images/chars/tsi07p.png"
    image sizuku tsi08f2 = "images/chars/tsi08f2.png"
    image sizuku tsi08m = "images/chars/tsi08m.png"
    image sizuku tsi08p = "images/chars/tsi08p.png"
    image sizuku tsi09f2 = "images/chars/tsi09f2.png"
    image sizuku tsi09m = "images/chars/tsi09m.png"
    image sizuku tsi09p = "images/chars/tsi09p.png"
    image sizuku tsi10f2 = "images/chars/tsi10f2.png"
    image sizuku tsi10m = "images/chars/tsi10m.png"
    image sizuku tsi10p = "images/chars/tsi10p.png"
    image sizuku tsi11f2 = "images/chars/tsi11f2.png"
    image sizuku tsi11m = "images/chars/tsi11m.png"
    image sizuku tsi11p = "images/chars/tsi11p.png"
    image sayuki tsy01f2 = "images/chars/tsy01f2.png"
    image sayuki tsy01m = "images/chars/tsy01m.png"
    image sayuki tsy01p = "images/chars/tsy01p.png"
    image sayuki tsy01s2 = "images/chars/tsy01s2.png"
    image sayuki tsy01z = "images/chars/tsy01z.png"
    image sayuki tsy02f2 = "images/chars/tsy02f2.png"
    image sayuki tsy02m = "images/chars/tsy02m.png"
    image sayuki tsy02p = "images/chars/tsy02p.png"
    image sayuki tsy02s2 = "images/chars/tsy02s2.png"
    image sayuki tsy02z = "images/chars/tsy02z.png"
    image sayuki tsy03f2 = "images/chars/tsy03f2.png"
    image sayuki tsy03m = "images/chars/tsy03m.png"
    image sayuki tsy03p = "images/chars/tsy03p.png"
    image sayuki tsy03s2 = "images/chars/tsy03s2.png"
    image sayuki tsy03z = "images/chars/tsy03z.png"
    image sayuki tsy04f2 = "images/chars/tsy04f2.png"
    image sayuki tsy04m = "images/chars/tsy04m.png"
    image sayuki tsy04p = "images/chars/tsy04p.png"
    image sayuki tsy04s2 = "images/chars/tsy04s2.png"
    image sayuki tsy04z = "images/chars/tsy04z.png"
    image sayuki tsy05f2 = "images/chars/tsy05f2.png"
    image sayuki tsy05m = "images/chars/tsy05m.png"
    image sayuki tsy05p = "images/chars/tsy05p.png"
    image sayuki tsy05s2 = "images/chars/tsy05s2.png"
    image sayuki tsy05z = "images/chars/tsy05z.png"
    image sayuki tsy06f2 = "images/chars/tsy06f2.png"
    image sayuki tsy06m = "images/chars/tsy06m.png"
    image sayuki tsy06p = "images/chars/tsy06p.png"
    image sayuki tsy06s2 = "images/chars/tsy06s2.png"
    image sayuki tsy06z = "images/chars/tsy06z.png"
    image sayuki tsy07f2 = "images/chars/tsy07f2.png"
    image sayuki tsy07m = "images/chars/tsy07m.png"
    image sayuki tsy07p = "images/chars/tsy07p.png"
    image sayuki tsy07s2 = "images/chars/tsy07s2.png"
    image sayuki tsy07z = "images/chars/tsy07z.png"
    image sayuki tsy08f2 = "images/chars/tsy08f2.png"
    image sayuki tsy08m = "images/chars/tsy08m.png"
    image sayuki tsy08p = "images/chars/tsy08p.png"
    image sayuki tsy08s2 = "images/chars/tsy08s2.png"
    image sayuki tsy08z = "images/chars/tsy08z.png"
    image sayuki tsy09f2 = "images/chars/tsy09f2.png"
    image sayuki tsy09m = "images/chars/tsy09m.png"
    image sayuki tsy09p = "images/chars/tsy09p.png"
    image sayuki tsy09s2 = "images/chars/tsy09s2.png"
    image sayuki tsy09z = "images/chars/tsy09z.png"
    image sayuki tsy10f2 = "images/chars/tsy10f2.png"
    image sayuki tsy10m = "images/chars/tsy10m.png"
    image sayuki tsy10p = "images/chars/tsy10p.png"
    image sayuki tsy10s2 = "images/chars/tsy10s2.png"
    image sayuki tsy10z = "images/chars/tsy10z.png"
    image sayuki tsy11f2 = "images/chars/tsy11f2.png"
    image sayuki tsy11m = "images/chars/tsy11m.png"
    image sayuki tsy11s2 = "images/chars/tsy11s2.png"
    image sayuki tsy11z = "images/chars/tsy11z.png"
    image takako tta01f2 = "images/chars/tta01f2.png"
    image takako tta01m = "images/chars/tta01m.png"
    image takako tta01p = "images/chars/tta01p.png"
    image takako tta01s2 = "images/chars/tta01s2.png"
    image takako tta02f2 = "images/chars/tta02f2.png"
    image takako tta02m = "images/chars/tta02m.png"
    image takako tta02p = "images/chars/tta02p.png"
    image takako tta02s2 = "images/chars/tta02s2.png"
    image takako tta03f2 = "images/chars/tta03f2.png"
    image takako tta03m = "images/chars/tta03m.png"
    image takako tta03p = "images/chars/tta03p.png"
    image takako tta03s2 = "images/chars/tta03s2.png"
    image takako tta04f2 = "images/chars/tta04f2.png"
    image takako tta04m = "images/chars/tta04m.png"
    image takako tta04p = "images/chars/tta04p.png"
    image takako tta04s2 = "images/chars/tta04s2.png"
    image takako tta05f2 = "images/chars/tta05f2.png"
    image takako tta05m = "images/chars/tta05m.png"
    image takako tta05p = "images/chars/tta05p.png"
    image takako tta05s2 = "images/chars/tta05s2.png"
    image takako tta06f2 = "images/chars/tta06f2.png"
    image takako tta06m = "images/chars/tta06m.png"
    image takako tta06p = "images/chars/tta06p.png"
    image takako tta06s2 = "images/chars/tta06s2.png"
    image takako tta07f2 = "images/chars/tta07f2.png"
    image takako tta07m = "images/chars/tta07m.png"
    image takako tta07p = "images/chars/tta07p.png"
    image takako tta07s2 = "images/chars/tta07s2.png"
    image takako tta08f2 = "images/chars/tta08f2.png"
    image takako tta08m = "images/chars/tta08m.png"
    image takako tta08p = "images/chars/tta08p.png"
    image takako tta08s2 = "images/chars/tta08s2.png"
    image takako tta09f2 = "images/chars/tta09f2.png"
    image takako tta09m = "images/chars/tta09m.png"
    image takako tta09p = "images/chars/tta09p.png"
    image takako tta09s2 = "images/chars/tta09s2.png"
    image takako tta10f2 = "images/chars/tta10f2.png"
    image takako tta10m = "images/chars/tta10m.png"
    image takako tta10p = "images/chars/tta10p.png"
    image takako tta10s2 = "images/chars/tta10s2.png"
    image takako tta11f2 = "images/chars/tta11f2.png"
    image takako tta11m = "images/chars/tta11m.png"
    image takako tta11p = "images/chars/tta11p.png"
    image takako tta11s2 = "images/chars/tta11s2.png"
    image yuuna tyu01f2 = "images/chars/tyu01f2.png"
    image yuuna tyu01m = "images/chars/tyu01m.png"
    image yuuna tyu01p = "images/chars/tyu01p.png"
    image yuuna tyu01s2 = "images/chars/tyu01s2.png"
    image yuuna tyu01z = "images/chars/tyu01z.png"
    image yuuna tyu02f2 = "images/chars/tyu02f2.png"
    image yuuna tyu02m = "images/chars/tyu02m.png"
    image yuuna tyu02p = "images/chars/tyu02p.png"
    image yuuna tyu02s2 = "images/chars/tyu02s2.png"
    image yuuna tyu02z = "images/chars/tyu02z.png"
    image yuuna tyu03f2 = "images/chars/tyu03f2.png"
    image yuuna tyu03m = "images/chars/tyu03m.png"
    image yuuna tyu03p = "images/chars/tyu03p.png"
    image yuuna tyu03s2 = "images/chars/tyu03s2.png"
    image yuuna tyu03z = "images/chars/tyu03z.png"
    image yuuna tyu04f2 = "images/chars/tyu04f2.png"
    image yuuna tyu04m = "images/chars/tyu04m.png"
    image yuuna tyu04p = "images/chars/tyu04p.png"
    image yuuna tyu04s2 = "images/chars/tyu04s2.png"
    image yuuna tyu04z = "images/chars/tyu04z.png"
    image yuuna tyu05f2 = "images/chars/tyu05f2.png"
    image yuuna tyu05m = "images/chars/tyu05m.png"
    image yuuna tyu05p = "images/chars/tyu05p.png"
    image yuuna tyu05s2 = "images/chars/tyu05s2.png"
    image yuuna tyu05z = "images/chars/tyu05z.png"
    image yuuna tyu06f2 = "images/chars/tyu06f2.png"
    image yuuna tyu06m = "images/chars/tyu06m.png"
    image yuuna tyu06p = "images/chars/tyu06p.png"
    image yuuna tyu06s2 = "images/chars/tyu06s2.png"
    image yuuna tyu06z = "images/chars/tyu06z.png"
    image yuuna tyu07f2 = "images/chars/tyu07f2.png"
    image yuuna tyu07m = "images/chars/tyu07m.png"
    image yuuna tyu07p = "images/chars/tyu07p.png"
    image yuuna tyu07s2 = "images/chars/tyu07s2.png"
    image yuuna tyu07z = "images/chars/tyu07z.png"
    image yuuna tyu08f2 = "images/chars/tyu08f2.png"
    image yuuna tyu08m = "images/chars/tyu08m.png"
    image yuuna tyu08p = "images/chars/tyu08p.png"
    image yuuna tyu08s2 = "images/chars/tyu08s2.png"
    image yuuna tyu08z = "images/chars/tyu08z.png"
    image yuuna tyu09f2 = "images/chars/tyu09f2.png"
    image yuuna tyu09m = "images/chars/tyu09m.png"
    image yuuna tyu09p = "images/chars/tyu09p.png"
    image yuuna tyu09s2 = "images/chars/tyu09s2.png"
    image yuuna tyu09z = "images/chars/tyu09z.png"
    image yuuna tyu10f2 = "images/chars/tyu10f2.png"
    image yuuna tyu10m = "images/chars/tyu10m.png"
    image yuuna tyu10p = "images/chars/tyu10p.png"
    image yuuna tyu10s2 = "images/chars/tyu10s2.png"
    image yuuna tyu10z = "images/chars/tyu10z.png"
    image yuuna tyu11f2 = "images/chars/tyu11f2.png"
    image yuuna tyu11m = "images/chars/tyu11m.png"
    image yuuna tyu11p = "images/chars/tyu11p.png"
    image yuuna tyu11s2 = "images/chars/tyu11s2.png"
    image yuuna tyu11z = "images/chars/tyu11z.png"

    image ending01:
        Solid("#FFF")
        alpha 0.0
        linear 7 alpha 1.0
        time 9
        "images/sr01.png" with Dissolve(4)
        time 19
        "images/sr02_1.png" with Fade(2,1,2,color="#FFF")
        time 30
        "images/sr03_1.png" with Fade(2,1,2,color="#FFF")
        time 41
        "images/sr04_1.png" with Fade(2,1,2,color="#FFF")
        time 52
        "images/sr05_1.png" with Fade(2,1,2,color="#FFF")
        time 63
        "images/sr06_1.png" with Fade(2,1,2,color="#FFF")
        time 74
        "images/sr07.png" with Fade(2,1,2,color="#FFF")
        time 85
        "images/sr08.png" with Fade(2,1,2,color="#FFF")
        time 96
        "images/sr11_1.png" with Fade(2,1,2,color="#FFF")
        time 107
        "images/sr12_1.png" with Fade(2,1,2,color="#FFF")
        time 118
        "images/sr13_1.png" with Fade(2,1,2,color="#FFF")
        time 129
        "images/sr14_1.png" with Fade(2,1,2,color="#FFF")
        time 140
        "images/sr15_1.png" with Fade(2,1,2,color="#FFF")
        time 151
        "images/sr16_1.png" with Fade(2,1,2,color="#FFF")
        time 162
        "images/sr17_1.png" with Fade(2,1,2,color="#FFF")
        time 173
        "images/sr18_1.png" with Fade(2,1,2,color="#FFF")
        time 184
        "images/sr19.png" with Fade(2,1,2,color="#FFF")
        time 199
        Solid("#FFF") with Dissolve(4)
        time 206
        linear 5.0 alpha 0.0


    image ending02:
        Solid("#FFF")
        alpha 0.0
        linear 7 alpha 1.0
        time 9
        "images/sr01.png" with Dissolve(4)
        time 19
        "images/sr02_2.png" with Fade(2,1,2,color="#FFF")
        time 30
        "images/sr03_2.png" with Fade(2,1,2,color="#FFF")
        time 41
        "images/sr04_2.png" with Fade(2,1,2,color="#FFF")
        time 52
        "images/sr05_2.png" with Fade(2,1,2,color="#FFF")
        time 63
        "images/sr06_2.png" with Fade(2,1,2,color="#FFF")
        time 74
        "images/sr07.png" with Fade(2,1,2,color="#FFF")
        time 85
        "images/sr08.png" with Fade(2,1,2,color="#FFF")
        time 96
        "images/sr11_2.png" with Fade(2,1,2,color="#FFF")
        time 107
        "images/sr12_2.png" with Fade(2,1,2,color="#FFF")
        time 118
        "images/sr13_2.png" with Fade(2,1,2,color="#FFF")
        time 129
        "images/sr14_2.png" with Fade(2,1,2,color="#FFF")
        time 140
        "images/sr15_2.png" with Fade(2,1,2,color="#FFF")
        time 151
        "images/sr16_2.png" with Fade(2,1,2,color="#FFF")
        time 162
        "images/sr17_2.png" with Fade(2,1,2,color="#FFF")
        time 173
        "images/sr18_2.png" with Fade(2,1,2,color="#FFF")
        time 184
        "images/sr19.png" with Fade(2,1,2,color="#FFF")
        time 199
        Solid("#FFF") with Dissolve(4)
        time 206
        linear 5.0 alpha 0.0


    image ending03:
        Solid("#FFF")
        alpha 0.0
        linear 7 alpha 1.0
        time 9
        "images/sr01.png" with Dissolve(4)
        time 19
        "images/sr02_3.png" with Fade(2,1,2,color="#FFF")
        time 30
        "images/sr03_3.png" with Fade(2,1,2,color="#FFF")
        time 41
        "images/sr04_3.png" with Fade(2,1,2,color="#FFF")
        time 52
        "images/sr05_3.png" with Fade(2,1,2,color="#FFF")
        time 63
        "images/sr06_3.png" with Fade(2,1,2,color="#FFF")
        time 74
        "images/sr07.png" with Fade(2,1,2,color="#FFF")
        time 85
        "images/sr08.png" with Fade(2,1,2,color="#FFF")
        time 96
        "images/sr11_3.png" with Fade(2,1,2,color="#FFF")
        time 107
        "images/sr12_3.png" with Fade(2,1,2,color="#FFF")
        time 118
        "images/sr13_3.png" with Fade(2,1,2,color="#FFF")
        time 129
        "images/sr14_3.png" with Fade(2,1,2,color="#FFF")
        time 140
        "images/sr15_3.png" with Fade(2,1,2,color="#FFF")
        time 151
        "images/sr16_3.png" with Fade(2,1,2,color="#FFF")
        time 162
        "images/sr17_3.png" with Fade(2,1,2,color="#FFF")
        time 173
        "images/sr18_3.png" with Fade(2,1,2,color="#FFF")
        time 184
        "images/sr19.png" with Fade(2,1,2,color="#FFF")
        time 199
        Solid("#FFF") with Dissolve(4)
        time 206
        linear 5.0 alpha 0.0

    image ending04:
        Solid("#FFF")
        alpha 0.0
        linear 7 alpha 1.0
        time 9
        "images/sr01.png" with Dissolve(4)
        time 19
        "images/sr02_4.png" with Fade(2,1,2,color="#FFF")
        time 30
        "images/sr03_4.png" with Fade(2,1,2,color="#FFF")
        time 41
        "images/sr04_4.png" with Fade(2,1,2,color="#FFF")
        time 52
        "images/sr05_4.png" with Fade(2,1,2,color="#FFF")
        time 63
        "images/sr06_4.png" with Fade(2,1,2,color="#FFF")
        time 74
        "images/sr07.png" with Fade(2,1,2,color="#FFF")
        time 85
        "images/sr08.png" with Fade(2,1,2,color="#FFF")
        time 96
        "images/sr11_4.png" with Fade(2,1,2,color="#FFF")
        time 107
        "images/sr12_4.png" with Fade(2,1,2,color="#FFF")
        time 118
        "images/sr13_4.png" with Fade(2,1,2,color="#FFF")
        time 129
        "images/sr14_4.png" with Fade(2,1,2,color="#FFF")
        time 140
        "images/sr15_4.png" with Fade(2,1,2,color="#FFF")
        time 151
        "images/sr16_4.png" with Fade(2,1,2,color="#FFF")
        time 162
        "images/sr17_4.png" with Fade(2,1,2,color="#FFF")
        time 173
        "images/sr18_4.png" with Fade(2,1,2,color="#FFF")
        time 184
        "images/sr19.png" with Fade(2,1,2,color="#FFF")
        time 199
        Solid("#FFF") with Dissolve(4)
        time 206
        linear 5.0 alpha 0.0


    image ending05:
        Solid("#FFF")
        alpha 0.0
        linear 7 alpha 1.0
        time 9
        "images/sr01.png" with Dissolve(4)
        time 19
        "images/sr02_5.png" with Fade(2,1,2,color="#FFF")
        time 30
        "images/sr03_5.png" with Fade(2,1,2,color="#FFF")
        time 41
        "images/sr04_5.png" with Fade(2,1,2,color="#FFF")
        time 52
        "images/sr05_5.png" with Fade(2,1,2,color="#FFF")
        time 63
        "images/sr06_5.png" with Fade(2,1,2,color="#FFF")
        time 74
        "images/sr07.png" with Fade(2,1,2,color="#FFF")
        time 85
        "images/sr08.png" with Fade(2,1,2,color="#FFF")
        time 96
        "images/sr11_5.png" with Fade(2,1,2,color="#FFF")
        time 107
        "images/sr12_5.png" with Fade(2,1,2,color="#FFF")
        time 118
        "images/sr13_5.png" with Fade(2,1,2,color="#FFF")
        time 129
        "images/sr14_5.png" with Fade(2,1,2,color="#FFF")
        time 140
        "images/sr15_5.png" with Fade(2,1,2,color="#FFF")
        time 151
        "images/sr16_5.png" with Fade(2,1,2,color="#FFF")
        time 162
        "images/sr17_5.png" with Fade(2,1,2,color="#FFF")
        time 173
        "images/sr18_5.png" with Fade(2,1,2,color="#FFF")
        time 184
        "images/sr19.png" with Fade(2,1,2,color="#FFF")
        time 199
        Solid("#FFF") with Dissolve(4)
        time 206
        linear 5.0 alpha 0.0