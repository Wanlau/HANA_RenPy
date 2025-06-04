init -2:
    image white = Solid("#fff")

    define amane = Character('天音', color="#1e83ff")
    define kaori = Character('佳织', color="#ff4aa4")
    define makoto = Character('真琴', color="#8809ff")
    define koharu = Character('小春', color="#fe8c00")

    define teacher = Character('教师', color="#09B5FF")
    define kaori_makoto = Character('佳织&真琴', color="#09B5FF")

    style window:
        ypos 584
        top_margin 0
        bottom_margin 0
        xpadding 32
        top_padding 27
        bottom_padding -28
        xsize 800
        ysize 156

    style say_dialogue is say_thought:
        yanchor 52

    style say_thought:
        font "fonts/Tuffy-Regular.ttf"
        size 25

    style say_label:
        xanchor -40
        yanchor 34
        ypos -10
        outlines [(2,"#00000060",3,3),(2,"#FFFFFF",0,0)]
        font "fonts/Homizio-bold.ttf"
        size 28

    style save_slot:
        font "fonts/Homizio-bold.ttf"
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


    define gs_clr = ImageDissolve("images/GS_CLR.png",2,ramplen=256)
    define gs_cud = ImageDissolve("images/GS_CUD.png",2,ramplen=256)
    define gs_du = ImageDissolve("images/GS_DU.png",2,ramplen=256)
    define gs_en_ns = ImageDissolve("images/GS_EN_NS.png",2,ramplen=256)
    define gs_en_sn = ImageDissolve("images/GS_EN_SN.png",2,ramplen=256)
    define gs_hi_ns = ImageDissolve("images/GS_HI_NS.png",2,ramplen=256)
    define gs_lr = ImageDissolve("images/GS_LR.png",2,ramplen=256)
    define gs_r = ImageDissolve("images/GS_R.png",2)
    define gs_rl = ImageDissolve("images/GS_RL.png",2,ramplen=256)
    define gs_ud = ImageDissolve("images/GS_UD.png",2,ramplen=256)
    define gs_udc = ImageDissolve("images/GS_UDC.png",2,ramplen=256)
    define fade2 = Fade(1.0,0,1.0)

    define windowin = ComposeTransition(dissolve,None,MoveTransition(0.4,enter=d,leave=u,layers=['screens']))
    define windowout = ComposeTransition(dissolve,MoveTransition(0.4,enter=u,leave=d,layers=['screens']))

    image eyecatch01 = ("images/eyecatch01.png")
    image eyecatch02 = ("images/eyecatch02.png")
    image eyecatch03 = ("images/eyecatch03.png")
    image eyecatch04 = ("images/eyecatch04.png")

    image fuguriya = "images/ui/fuguriya.png"

    image CU01 = "images/cg/CU01.png"
    image CU02 = "images/cg/CU02.png"
    image CU03 = "images/cg/CU03.png"
    image CU03p1 = "images/cg/CU03p1.png"
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
    image EV07 = "images/cg/EV07.png"
    image EV07p1 = "images/cg/EV07p1.png"
    image EV08 = "images/cg/EV08.png"
    image EV08p1 = "images/cg/EV08p1.png"
    image EV09 = "images/cg/EV09.png"
    image EV10 = "images/cg/EV10.png"
    image EV11 = "images/cg/EV11.png"
    image EV12 = "images/cg/EV12.png"
    image EV12p1 = "images/cg/EV12p1.png"
    image EV13 = "images/cg/EV13.png"
    image EV13p1 = "images/cg/EV13p1.png"
    image EV14 = "images/cg/EV14.png"
    image EV15 = "images/cg/EV15.png"
    image EV16 = "images/cg/EV16.png"
    image EV16p1 = "images/cg/EV16p1.png"
    image EV17 = "images/cg/EV17.png"
    image EV17p1 = "images/cg/EV17p1.png"
    image EV18 = "images/cg/EV18.png"
    image EV19 = "images/cg/EV19.png"
    image EV20 = "images/cg/EV20.png"

    image bg02a = "images/bg/bg02a.png"
    image bg05a = "images/bg/bg05a.png"
    image bg06a = "images/bg/bg06a.png"
    image bg07a = "images/bg/bg07a.png"
    image bg08a = "images/bg/bg08a.png"
    image bg08c = "images/bg/bg08c.png"
    image bg09a = "images/bg/bg09a.png"
    image bg09c = "images/bg/bg09c.png"
    image bg09d = "images/bg/bg09d.png"
    image bg10a = "images/bg/bg10a.png"
    image bg10c = "images/bg/bg10c.png"
    image bg11c = "images/bg/bg11c.png"
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
    image BLACK = "images/bg/BLACK.png"
    image WHITE = "images/bg/WHITE.png"

    image amane tam01pa = "images/chars/tam01pa.png"
    image amane tam01pb = "images/chars/tam01pb.png"
    image amane tam01sa = "images/chars/tam01sa.png"
    image amane tam01sb = "images/chars/tam01sb.png"
    image amane tam01ta = "images/chars/tam01ta.png"
    image amane tam01tb = "images/chars/tam01tb.png"
    image amane tam02pa = "images/chars/tam02pa.png"
    image amane tam02pb = "images/chars/tam02pb.png"
    image amane tam02sa = "images/chars/tam02sa.png"
    image amane tam02sb = "images/chars/tam02sb.png"
    image amane tam02ta = "images/chars/tam02ta.png"
    image amane tam02tb = "images/chars/tam02tb.png"
    image amane tam03pa = "images/chars/tam03pa.png"
    image amane tam03pb = "images/chars/tam03pb.png"
    image amane tam03sa = "images/chars/tam03sa.png"
    image amane tam03sb = "images/chars/tam03sb.png"
    image amane tam03ta = "images/chars/tam03ta.png"
    image amane tam03tb = "images/chars/tam03tb.png"
    image amane tam04pa = "images/chars/tam04pa.png"
    image amane tam04pb = "images/chars/tam04pb.png"
    image amane tam04sa = "images/chars/tam04sa.png"
    image amane tam04sb = "images/chars/tam04sb.png"
    image amane tam04ta = "images/chars/tam04ta.png"
    image amane tam04tb = "images/chars/tam04tb.png"
    image amane tam05pa = "images/chars/tam05pa.png"
    image amane tam05pb = "images/chars/tam05pb.png"
    image amane tam05sa = "images/chars/tam05sa.png"
    image amane tam05sb = "images/chars/tam05sb.png"
    image amane tam05ta = "images/chars/tam05ta.png"
    image amane tam05tb = "images/chars/tam05tb.png"
    image amane tam06pa = "images/chars/tam06pa.png"
    image amane tam06pb = "images/chars/tam06pb.png"
    image amane tam06sa = "images/chars/tam06sa.png"
    image amane tam06sb = "images/chars/tam06sb.png"
    image amane tam06ta = "images/chars/tam06ta.png"
    image amane tam06tb = "images/chars/tam06tb.png"
    image amane tam08pa = "images/chars/tam08pa.png"
    image amane tam08pb = "images/chars/tam08pb.png"
    image amane tam08sa = "images/chars/tam08sa.png"
    image amane tam08sb = "images/chars/tam08sb.png"
    image amane tam08ta = "images/chars/tam08ta.png"
    image amane tam08tb = "images/chars/tam08tb.png"
    image amane tam09pa = "images/chars/tam09pa.png"
    image amane tam09pb = "images/chars/tam09pb.png"
    image amane tam09sa = "images/chars/tam09sa.png"
    image amane tam09sb = "images/chars/tam09sb.png"
    image amane tam09ta = "images/chars/tam09ta.png"
    image amane tam09tb = "images/chars/tam09tb.png"
    image amane tam10pa = "images/chars/tam10pa.png"
    image amane tam10pb = "images/chars/tam10pb.png"
    image amane tam10sa = "images/chars/tam10sa.png"
    image amane tam10sb = "images/chars/tam10sb.png"
    image amane tam10ta = "images/chars/tam10ta.png"
    image amane tam10tb = "images/chars/tam10tb.png"
    image kaori tka01pa = "images/chars/tka01pa.png"
    image kaori tka01pb = "images/chars/tka01pb.png"
    image kaori tka01sa = "images/chars/tka01sa.png"
    image kaori tka01sb = "images/chars/tka01sb.png"
    image kaori tka01ta = "images/chars/tka01ta.png"
    image kaori tka01tb = "images/chars/tka01tb.png"
    image kaori tka02pa = "images/chars/tka02pa.png"
    image kaori tka02pb = "images/chars/tka02pb.png"
    image kaori tka02sa = "images/chars/tka02sa.png"
    image kaori tka02sb = "images/chars/tka02sb.png"
    image kaori tka02ta = "images/chars/tka02ta.png"
    image kaori tka02tb = "images/chars/tka02tb.png"
    image kaori tka03pa = "images/chars/tka03pa.png"
    image kaori tka03pb = "images/chars/tka03pb.png"
    image kaori tka03sa = "images/chars/tka03sa.png"
    image kaori tka03sb = "images/chars/tka03sb.png"
    image kaori tka03ta = "images/chars/tka03ta.png"
    image kaori tka03tb = "images/chars/tka03tb.png"
    image kaori tka04pa = "images/chars/tka04pa.png"
    image kaori tka04pb = "images/chars/tka04pb.png"
    image kaori tka04sa = "images/chars/tka04sa.png"
    image kaori tka04sb = "images/chars/tka04sb.png"
    image kaori tka04ta = "images/chars/tka04ta.png"
    image kaori tka04tb = "images/chars/tka04tb.png"
    image kaori tka05pa = "images/chars/tka05pa.png"
    image kaori tka05pb = "images/chars/tka05pb.png"
    image kaori tka05sa = "images/chars/tka05sa.png"
    image kaori tka05sb = "images/chars/tka05sb.png"
    image kaori tka05ta = "images/chars/tka05ta.png"
    image kaori tka05tb = "images/chars/tka05tb.png"
    image kaori tka06pa = "images/chars/tka06pa.png"
    image kaori tka06pb = "images/chars/tka06pb.png"
    image kaori tka06sa = "images/chars/tka06sa.png"
    image kaori tka06sb = "images/chars/tka06sb.png"
    image kaori tka06ta = "images/chars/tka06ta.png"
    image kaori tka06tb = "images/chars/tka06tb.png"
    image kaori tka07pa = "images/chars/tka07pa.png"
    image kaori tka07pb = "images/chars/tka07pb.png"
    image kaori tka07sa = "images/chars/tka07sa.png"
    image kaori tka07sb = "images/chars/tka07sb.png"
    image kaori tka07ta = "images/chars/tka07ta.png"
    image kaori tka07tb = "images/chars/tka07tb.png"
    image kaori tka08pa = "images/chars/tka08pa.png"
    image kaori tka08pb = "images/chars/tka08pb.png"
    image kaori tka08sa = "images/chars/tka08sa.png"
    image kaori tka08sb = "images/chars/tka08sb.png"
    image kaori tka08ta = "images/chars/tka08ta.png"
    image kaori tka08tb = "images/chars/tka08tb.png"
    image kaori tka09pa = "images/chars/tka09pa.png"
    image kaori tka09pb = "images/chars/tka09pb.png"
    image kaori tka09sa = "images/chars/tka09sa.png"
    image kaori tka09sb = "images/chars/tka09sb.png"
    image kaori tka09ta = "images/chars/tka09ta.png"
    image kaori tka09tb = "images/chars/tka09tb.png"
    image kaori tka10pa = "images/chars/tka10pa.png"
    image kaori tka10pb = "images/chars/tka10pb.png"
    image kaori tka10sa = "images/chars/tka10sa.png"
    image kaori tka10sb = "images/chars/tka10sb.png"
    image kaori tka10ta = "images/chars/tka10ta.png"
    image kaori tka10tb = "images/chars/tka10tb.png"
    image kaori tka12pa = "images/chars/tka12pa.png"
    image kaori tka12pb = "images/chars/tka12pb.png"
    image kaori tka12sa = "images/chars/tka12sa.png"
    image kaori tka12sb = "images/chars/tka12sb.png"
    image kaori tka12ta = "images/chars/tka12ta.png"
    image kaori tka12tb = "images/chars/tka12tb.png"
    image koharu tko01pa = "images/chars/tko01pa.png"
    image koharu tko01pb = "images/chars/tko01pb.png"
    image koharu tko01sa = "images/chars/tko01sa.png"
    image koharu tko01sb = "images/chars/tko01sb.png"
    image koharu tko01ta = "images/chars/tko01ta.png"
    image koharu tko01tb = "images/chars/tko01tb.png"
    image koharu tko02pa = "images/chars/tko02pa.png"
    image koharu tko02pb = "images/chars/tko02pb.png"
    image koharu tko02sa = "images/chars/tko02sa.png"
    image koharu tko02sb = "images/chars/tko02sb.png"
    image koharu tko02ta = "images/chars/tko02ta.png"
    image koharu tko02tb = "images/chars/tko02tb.png"
    image koharu tko03pa = "images/chars/tko03pa.png"
    image koharu tko03pb = "images/chars/tko03pb.png"
    image koharu tko03sa = "images/chars/tko03sa.png"
    image koharu tko03sb = "images/chars/tko03sb.png"
    image koharu tko03ta = "images/chars/tko03ta.png"
    image koharu tko03tb = "images/chars/tko03tb.png"
    image koharu tko04pa = "images/chars/tko04pa.png"
    image koharu tko04pb = "images/chars/tko04pb.png"
    image koharu tko04sa = "images/chars/tko04sa.png"
    image koharu tko04sb = "images/chars/tko04sb.png"
    image koharu tko04ta = "images/chars/tko04ta.png"
    image koharu tko04tb = "images/chars/tko04tb.png"
    image koharu tko05pa = "images/chars/tko05pa.png"
    image koharu tko05pb = "images/chars/tko05pb.png"
    image koharu tko05sa = "images/chars/tko05sa.png"
    image koharu tko05sb = "images/chars/tko05sb.png"
    image koharu tko05ta = "images/chars/tko05ta.png"
    image koharu tko05tb = "images/chars/tko05tb.png"
    image koharu tko06pa = "images/chars/tko06pa.png"
    image koharu tko06pb = "images/chars/tko06pb.png"
    image koharu tko06sa = "images/chars/tko06sa.png"
    image koharu tko06sb = "images/chars/tko06sb.png"
    image koharu tko06ta = "images/chars/tko06ta.png"
    image koharu tko06tb = "images/chars/tko06tb.png"
    image koharu tko07pa = "images/chars/tko07pa.png"
    image koharu tko07pb = "images/chars/tko07pb.png"
    image koharu tko07sa = "images/chars/tko07sa.png"
    image koharu tko07sb = "images/chars/tko07sb.png"
    image koharu tko07ta = "images/chars/tko07ta.png"
    image koharu tko07tb = "images/chars/tko07tb.png"
    image koharu tko08pa = "images/chars/tko08pa.png"
    image koharu tko08pb = "images/chars/tko08pb.png"
    image koharu tko08sa = "images/chars/tko08sa.png"
    image koharu tko08sb = "images/chars/tko08sb.png"
    image koharu tko08ta = "images/chars/tko08ta.png"
    image koharu tko08tb = "images/chars/tko08tb.png"
    image koharu tko09pa = "images/chars/tko09pa.png"
    image koharu tko09pb = "images/chars/tko09pb.png"
    image koharu tko09sa = "images/chars/tko09sa.png"
    image koharu tko09sb = "images/chars/tko09sb.png"
    image koharu tko09ta = "images/chars/tko09ta.png"
    image koharu tko09tb = "images/chars/tko09tb.png"
    image koharu tko10pa = "images/chars/tko10pa.png"
    image koharu tko10pb = "images/chars/tko10pb.png"
    image koharu tko10sa = "images/chars/tko10sa.png"
    image koharu tko10sb = "images/chars/tko10sb.png"
    image koharu tko10ta = "images/chars/tko10ta.png"
    image koharu tko10tb = "images/chars/tko10tb.png"
    image makoto tma01pa = "images/chars/tma01pa.png"
    image makoto tma01pb = "images/chars/tma01pb.png"
    image makoto tma01sa = "images/chars/tma01sa.png"
    image makoto tma01sb = "images/chars/tma01sb.png"
    image makoto tma01ta = "images/chars/tma01ta.png"
    image makoto tma01tb = "images/chars/tma01tb.png"
    image makoto tma02pa = "images/chars/tma02pa.png"
    image makoto tma02pb = "images/chars/tma02pb.png"
    image makoto tma02sa = "images/chars/tma02sa.png"
    image makoto tma02sb = "images/chars/tma02sb.png"
    image makoto tma02ta = "images/chars/tma02ta.png"
    image makoto tma02tb = "images/chars/tma02tb.png"
    image makoto tma03pa = "images/chars/tma03pa.png"
    image makoto tma03pb = "images/chars/tma03pb.png"
    image makoto tma03sa = "images/chars/tma03sa.png"
    image makoto tma03sb = "images/chars/tma03sb.png"
    image makoto tma03ta = "images/chars/tma03ta.png"
    image makoto tma03tb = "images/chars/tma03tb.png"
    image makoto tma04pa = "images/chars/tma04pa.png"
    image makoto tma04pb = "images/chars/tma04pb.png"
    image makoto tma04sa = "images/chars/tma04sa.png"
    image makoto tma04sb = "images/chars/tma04sb.png"
    image makoto tma04ta = "images/chars/tma04ta.png"
    image makoto tma04tb = "images/chars/tma04tb.png"
    image makoto tma05pa = "images/chars/tma05pa.png"
    image makoto tma05pb = "images/chars/tma05pb.png"
    image makoto tma05sa = "images/chars/tma05sa.png"
    image makoto tma05sb = "images/chars/tma05sb.png"
    image makoto tma05ta = "images/chars/tma05ta.png"
    image makoto tma05tb = "images/chars/tma05tb.png"
    image makoto tma06pa = "images/chars/tma06pa.png"
    image makoto tma06pb = "images/chars/tma06pb.png"
    image makoto tma06sa = "images/chars/tma06sa.png"
    image makoto tma06sb = "images/chars/tma06sb.png"
    image makoto tma06ta = "images/chars/tma06ta.png"
    image makoto tma06tb = "images/chars/tma06tb.png"
    image makoto tma07pa = "images/chars/tma07pa.png"
    image makoto tma07pb = "images/chars/tma07pb.png"
    image makoto tma07sa = "images/chars/tma07sa.png"
    image makoto tma07sb = "images/chars/tma07sb.png"
    image makoto tma07ta = "images/chars/tma07ta.png"
    image makoto tma07tb = "images/chars/tma07tb.png"
    image makoto tma08pa = "images/chars/tma08pa.png"
    image makoto tma08pb = "images/chars/tma08pb.png"
    image makoto tma08sa = "images/chars/tma08sa.png"
    image makoto tma08sb = "images/chars/tma08sb.png"
    image makoto tma08ta = "images/chars/tma08ta.png"
    image makoto tma08tb = "images/chars/tma08tb.png"
    image makoto tma09pa = "images/chars/tma09pa.png"
    image makoto tma09pb = "images/chars/tma09pb.png"
    image makoto tma09sa = "images/chars/tma09sa.png"
    image makoto tma09sb = "images/chars/tma09sb.png"
    image makoto tma09ta = "images/chars/tma09ta.png"
    image makoto tma09tb = "images/chars/tma09tb.png"
    image makoto tma10pa = "images/chars/tma10pa.png"
    image makoto tma10pb = "images/chars/tma10pb.png"
    image makoto tma10sa = "images/chars/tma10sa.png"
    image makoto tma10sb = "images/chars/tma10sb.png"
    image makoto tma10ta = "images/chars/tma10ta.png"
    image makoto tma10tb = "images/chars/tma10tb.png"

    image ending:
        Solid("#FFF")
        alpha 0.0
        linear 5 alpha 1.0
        time 7
        "images/sr01.png" with Dissolve(4)
        time 19
        "images/sr02.png" with Fade(2,1,2,color="#FFF")
        time 36
        "images/sr03.png" with Fade(2,1,2,color="#FFF")
        time 53
        "images/sr04.png" with Fade(2,1,2,color="#FFF")
        time 70
        "images/sr05.png" with Fade(2,1,2,color="#FFF")
        time 87
        "images/sr06.png" with Fade(2,1,2,color="#FFF")
        time 104
        "images/sr07.png" with Fade(2,1,2,color="#FFF")
        time 121
        "images/sr08.png" with Fade(2,1,2,color="#FFF")
        time 138
        "images/sr09.png" with Fade(2,1,2,color="#FFF")
        time 160
        Solid("#FFF") with Dissolve(4)
        time 167
        linear 5.0 alpha 0.0

##replace characters with tags
##fork from HANA10
init python:
    # Replaces '♪' symbol with {note} tag.
    def note_tag(tag, argument):
        return [
                (renpy.TEXT_TAG, 'font=fonts/Tuffy-Regular-EN.ttf'),
                (renpy.TEXT_TEXT, '♪'),
                (renpy.TEXT_TAG, '/font')
                ]
    config.self_closing_custom_text_tags['note'] = note_tag

    # Replaces '♡' symbol with {heart} tag.
    def heart_tag(tag, argument):
        return [
                (renpy.TEXT_TAG, 'font=fonts/Tuffy-Regular-EN.ttf'),
                (renpy.TEXT_TEXT, '♡'),
                (renpy.TEXT_TAG, '/font')
                ]
    config.self_closing_custom_text_tags['heart'] = heart_tag