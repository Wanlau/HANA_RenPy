init -2:
    image white = Solid("#fff")

    define risa = Character('璃纱', color="#FF197A")
    define miya = Character('美夜', color="#2809FF")
    define teacher = Character('老师', color="#09B5FF")
    define girl_a = Character('女生A', color="#09B5FF")
    define girl_b = Character('女生B', color="#09B5FF")

    image splash_first:
        Solid("#000")
        "ui/stmichael.png" with dissolve
        pause 3
        
    image stmichael = "ui/stmichael.png"
    image sr_ex00 = "ui/sr_ex00.png"
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
        size 26

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

    image font = ConditionSwitch(
        "(renpy.get_style_preference('shadow') == 'on')","images/font.png",
        "(renpy.get_style_preference('shadow') == 'off')","images/font2.png"
        )
    image tilde = ConditionSwitch(
        "(renpy.get_style_preference('shadow') == 'on')","images/tilde.png",
        "(renpy.get_style_preference('shadow') == 'off')","images/tilde2.png"
        )

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


    define gs_en_ns = ImageDissolve("images/gs_en_ns.png",1,ramplen=256)
    define gs_en_sn = ImageDissolve("images/gs_en_sn.png",1,ramplen=256)
    define gs_udc = ImageDissolve("images/gs_udc.png",1,ramplen=256)
    define gs_cud = ImageDissolve("images/gs_cud.png",1,ramplen=256)
    define gs_clr = ImageDissolve("images/gs_clr.png",1,ramplen=256)
    define gs_hi_ns = ImageDissolve("images/gs_hi_ns.png",1,ramplen=256)
    define gs_r = ImageDissolve("images/gs_r.png",1)
    define gs_rl = ImageDissolve("images/gs_rl.png",1,ramplen=256)
    define gs_lr = ImageDissolve("images/gs_lr.png",1,ramplen=256)
    define gs_du = ImageDissolve("images/gs_du.png",1,ramplen=256)
    define gs_ud = ImageDissolve("images/gs_ud.png",1,ramplen=256)
    define fade2 = Fade(1.0,0,1.0)
    define clouds = ImageDissolve("images/clouds.png",2,ramplen=256)


    define windowin = ComposeTransition(dissolve,None,MoveTransition(0.4,enter=d,leave=u,layers=['screens']))
    define windowout = ComposeTransition(dissolve,MoveTransition(0.4,enter=u,leave=d,layers=['screens']))

    image eyecatch01 = ("images/eyecatch01.png")
    image eyecatch02 = ("images/eyecatch02.png")
    image eyecatch03 = ("images/eyecatch03.png")
    image eyecatch04 = ("images/eyecatch04.png")

    image endcut = "images/cg/endcut.png"
    image ev01 = "images/cg/ev01.png"
    image ev01p1 = "images/cg/ev01p1.png"
    image ev01p2 = "images/cg/ev01p2.png"
    image ev02 = "images/cg/ev02.png"
    image ev02p1 = "images/cg/ev02p1.png"
    image ev02p2 = "images/cg/ev02p2.png"
    image ev03 = "images/cg/ev03.png"
    image ev03p1 = "images/cg/ev03p1.png"
    image ev03p2 = "images/cg/ev03p2.png"
    image ev04 = "images/cg/ev04.png"
    image ev04p1 = "images/cg/ev04p1.png"
    image ev04p2 = "images/cg/ev04p2.png"
    image ev05 = "images/cg/ev05.png"
    image ev05p1 = "images/cg/ev05p1.png"
    image ev05p2 = "images/cg/ev05p2.png"
    image ev06 = "images/cg/ev06.png"
    image ev06p1 = "images/cg/ev06p1.png"
    image ev06p2 = "images/cg/ev06p2.png"
    image ev07 = "images/cg/ev07.png"
    image ev07p1 = "images/cg/ev07p1.png"
    image ev07p2 = "images/cg/ev07p2.png"
    image ev08 = "images/cg/ev08.png"
    image ev08p1 = "images/cg/ev08p1.png"
    image ev08p2 = "images/cg/ev08p2.png"
    image ev09 = "images/cg/ev09.png"
    image ev09p1 = "images/cg/ev09p1.png"
    image ev09p2 = "images/cg/ev09p2.png"
    image ev10 = "images/cg/ev10.png"
    image ev10p1 = "images/cg/ev10p1.png"
    image ev10p2 = "images/cg/ev10p2.png"
    image ev11 = "images/cg/ev11.png"
    image ev11p1 = "images/cg/ev11p1.png"
    image ev12 = "images/cg/ev12.png"
    image ev12p1 = "images/cg/ev12p1.png"
    image ev12p2 = "images/cg/ev12p2.png"
    image ev13 = "images/cg/ev13.png"
    image ev13p1 = "images/cg/ev13p1.png"
    image ev14 = "images/cg/ev14.png"
    image ev14p1 = "images/cg/ev14p1.png"
    image ev14p2 = "images/cg/ev14p2.png"
    image ev15 = "images/cg/ev15.png"
    image ev15p1 = "images/cg/ev15p1.png"
    image ev16 = "images/cg/ev16.png"
    image ev16p1 = "images/cg/ev16p1.png"
    image ev17 = "images/cg/ev17.png"
    image ev17p1 = "images/cg/ev17p1.png"
    image ev18 = "images/cg/ev18.png"
    image ev18p1 = "images/cg/ev18p1.png"
    image ev19 = "images/cg/ev19.png"
    image ev19p1 = "images/cg/ev19p1.png"
    image ev20 = "images/cg/ev20.png"

    image bg01a = "images/bg/bg01a.png"
    image bg01c = "images/bg/bg01c.png"
    image bg02a = "images/bg/bg02a.png"
    image bg02c = "images/bg/bg02c.png"
    image bg03a = "images/bg/bg03a.png"
    image bg04a = "images/bg/bg04a.png"
    image bg04b = "images/bg/bg04b.png"
    image bg05a = "images/bg/bg05a.png"
    image bg05b = "images/bg/bg05b.png"
    image bg08a = "images/bg/bg08a.png"
    image bg08c = "images/bg/bg08c.png"
    image bg08d = "images/bg/bg08d.png"
    image bg16a = "images/bg/bg16a.png"
    image bg16c = "images/bg/bg16c.png"
    image bg17a = "images/bg/bg17a.png"
    image bg17c = "images/bg/bg17c.png"
    image bg18a = "images/bg/bg18a.png"
    image bg18b = "images/bg/bg18b.png"
    image bg19a = "images/bg/bg19a.png"
    image bg19b = "images/bg/bg19b.png"
    image bg21a = "images/bg/bg21a.png"
    image bg21b = "images/bg/bg21b.png"
    image bg29a = "images/bg/bg29a.png"
    image bg29b = "images/bg/bg29b.png"
    image bg29c = "images/bg/bg29c.png"
    image bg40a = "images/bg/bg40a.png"
    image bg40b = "images/bg/bg40b.png"
    image bg40c = "images/bg/bg40c.png"

    image miya tmi01f = "images/chars/tmi01f.png"
    image miya tmi01fc = "images/chars/tmi01fc.png"
    image miya tmi01p = "images/chars/tmi01p.png"
    image miya tmi01s = "images/chars/tmi01s.png"
    image miya tmi01sc = "images/chars/tmi01sc.png"
    image miya tmi01z = "images/chars/tmi01z.png"
    image miya tmi02f = "images/chars/tmi02f.png"
    image miya tmi02fc = "images/chars/tmi02fc.png"
    image miya tmi02p = "images/chars/tmi02p.png"
    image miya tmi02s = "images/chars/tmi02s.png"
    image miya tmi02sc = "images/chars/tmi02sc.png"
    image miya tmi02z = "images/chars/tmi02z.png"
    image miya tmi03f = "images/chars/tmi03f.png"
    image miya tmi03fc = "images/chars/tmi03fc.png"
    image miya tmi03p = "images/chars/tmi03p.png"
    image miya tmi03s = "images/chars/tmi03s.png"
    image miya tmi03sc = "images/chars/tmi03sc.png"
    image miya tmi03z = "images/chars/tmi03z.png"
    image miya tmi04f = "images/chars/tmi04f.png"
    image miya tmi04fc = "images/chars/tmi04fc.png"
    image miya tmi04p = "images/chars/tmi04p.png"
    image miya tmi04s = "images/chars/tmi04s.png"
    image miya tmi04sc = "images/chars/tmi04sc.png"
    image miya tmi04z = "images/chars/tmi04z.png"
    image miya tmi05f = "images/chars/tmi05f.png"
    image miya tmi05fc = "images/chars/tmi05fc.png"
    image miya tmi05p = "images/chars/tmi05p.png"
    image miya tmi05s = "images/chars/tmi05s.png"
    image miya tmi05sc = "images/chars/tmi05sc.png"
    image miya tmi05z = "images/chars/tmi05z.png"
    image miya tmi06f = "images/chars/tmi06f.png"
    image miya tmi06fc = "images/chars/tmi06fc.png"
    image miya tmi06p = "images/chars/tmi06p.png"
    image miya tmi06s = "images/chars/tmi06s.png"
    image miya tmi06sc = "images/chars/tmi06sc.png"
    image miya tmi06z = "images/chars/tmi06z.png"
    image miya tmi07f = "images/chars/tmi07f.png"
    image miya tmi07fc = "images/chars/tmi07fc.png"
    image miya tmi07p = "images/chars/tmi07p.png"
    image miya tmi07s = "images/chars/tmi07s.png"
    image miya tmi07sc = "images/chars/tmi07sc.png"
    image miya tmi07z = "images/chars/tmi07z.png"
    image miya tmi08f = "images/chars/tmi08f.png"
    image miya tmi08fc = "images/chars/tmi08fc.png"
    image miya tmi08p = "images/chars/tmi08p.png"
    image miya tmi08s = "images/chars/tmi08s.png"
    image miya tmi08sc = "images/chars/tmi08sc.png"
    image miya tmi08z = "images/chars/tmi08z.png"
    image miya tmi09f = "images/chars/tmi09f.png"
    image miya tmi09fc = "images/chars/tmi09fc.png"
    image miya tmi09p = "images/chars/tmi09p.png"
    image miya tmi09s = "images/chars/tmi09s.png"
    image miya tmi09sc = "images/chars/tmi09sc.png"
    image miya tmi09z = "images/chars/tmi09z.png"
    image miya tmi10f = "images/chars/tmi10f.png"
    image miya tmi10fc = "images/chars/tmi10fc.png"
    image miya tmi10p = "images/chars/tmi10p.png"
    image miya tmi10s = "images/chars/tmi10s.png"
    image miya tmi10sc = "images/chars/tmi10sc.png"
    image miya tmi10z = "images/chars/tmi10z.png"
    image miya tmi11f = "images/chars/tmi11f.png"
    image miya tmi11fc = "images/chars/tmi11fc.png"
    image miya tmi11p = "images/chars/tmi11p.png"
    image miya tmi11s = "images/chars/tmi11s.png"
    image miya tmi11sc = "images/chars/tmi11sc.png"
    image miya tmi11z = "images/chars/tmi11z.png"
    
    image risa tri01f = "images/chars/tri01f.png"
    image risa tri01fc = "images/chars/tri01fc.png"
    image risa tri01p = "images/chars/tri01p.png"
    image risa tri01s = "images/chars/tri01s.png"
    image risa tri01sc = "images/chars/tri01sc.png"
    image risa tri01z = "images/chars/tri01z.png"
    image risa tri02f = "images/chars/tri02f.png"
    image risa tri02fc = "images/chars/tri02fc.png"
    image risa tri02p = "images/chars/tri02p.png"
    image risa tri02s = "images/chars/tri02s.png"
    image risa tri02sc = "images/chars/tri02sc.png"
    image risa tri02z = "images/chars/tri02z.png"
    image risa tri03f = "images/chars/tri03f.png"
    image risa tri03fc = "images/chars/tri03fc.png"
    image risa tri03p = "images/chars/tri03p.png"
    image risa tri03s = "images/chars/tri03s.png"
    image risa tri03sc = "images/chars/tri03sc.png"
    image risa tri03z = "images/chars/tri03z.png"
    image risa tri04f = "images/chars/tri04f.png"
    image risa tri04fc = "images/chars/tri04fc.png"
    image risa tri04p = "images/chars/tri04p.png"
    image risa tri04s = "images/chars/tri04s.png"
    image risa tri04sc = "images/chars/tri04sc.png"
    image risa tri04z = "images/chars/tri04z.png"
    image risa tri05f = "images/chars/tri05f.png"
    image risa tri05fc = "images/chars/tri05fc.png"
    image risa tri05p = "images/chars/tri05p.png"
    image risa tri05s = "images/chars/tri05s.png"
    image risa tri05sc = "images/chars/tri05sc.png"
    image risa tri05z = "images/chars/tri05z.png"
    image risa tri06f = "images/chars/tri06f.png"
    image risa tri06fc = "images/chars/tri06fc.png"
    image risa tri06p = "images/chars/tri06p.png"
    image risa tri06s = "images/chars/tri06s.png"
    image risa tri06sc = "images/chars/tri06sc.png"
    image risa tri06z = "images/chars/tri06z.png"
    image risa tri07f = "images/chars/tri07f.png"
    image risa tri07fc = "images/chars/tri07fc.png"
    image risa tri07p = "images/chars/tri07p.png"
    image risa tri07s = "images/chars/tri07s.png"
    image risa tri07sc = "images/chars/tri07sc.png"
    image risa tri07z = "images/chars/tri07z.png"
    image risa tri08f = "images/chars/tri08f.png"
    image risa tri08fc = "images/chars/tri08fc.png"
    image risa tri08p = "images/chars/tri08p.png"
    image risa tri08s = "images/chars/tri08s.png"
    image risa tri08sc = "images/chars/tri08sc.png"
    image risa tri08z = "images/chars/tri08z.png"
    image risa tri09f = "images/chars/tri09f.png"
    image risa tri09fc = "images/chars/tri09fc.png"
    image risa tri09p = "images/chars/tri09p.png"
    image risa tri09s = "images/chars/tri09s.png"
    image risa tri09sc = "images/chars/tri09sc.png"
    image risa tri09z = "images/chars/tri09z.png"
    image risa tri10f = "images/chars/tri10f.png"
    image risa tri10fc = "images/chars/tri10fc.png"
    image risa tri10p = "images/chars/tri10p.png"
    image risa tri10s = "images/chars/tri10s.png"
    image risa tri10sc = "images/chars/tri10sc.png"
    image risa tri10z = "images/chars/tri10z.png"
    image risa tri11f = "images/chars/tri11f.png"
    image risa tri11fc = "images/chars/tri11fc.png"
    image risa tri11p = "images/chars/tri11p.png"
    image risa tri11s = "images/chars/tri11s.png"
    image risa tri11sc = "images/chars/tri11sc.png"
    image risa tri11z = "images/chars/tri11z.png"

    image ending:
        Solid("#FFF")
        alpha 0.0
        linear 5 alpha 1.0
        time 10
        "images/sr01.png" with Dissolve(4)
        time 17.5
        "images/sr02.png" with Fade(1,1,2,color="#FFF")
        time 31.5
        "images/sr03.png" with Fade(1,1,2,color="#FFF")
        time 44
        "images/sr04.png" with Fade(1,1,2,color="#FFF")
        time 56.5
        "images/sr05.png" with Fade(1,1,2,color="#FFF")
        time 69
        "images/sr06.png" with Fade(1,1,2,color="#FFF")
        time 81.5
        "images/sr07.png" with Fade(1,1,2,color="#FFF")
        time 94
        "images/sr08.png" with Fade(1,1,2,color="#FFF")
        time 106.5
        "images/sr09.png" with Fade(1,1,2,color="#FFF")
        time 125.5
        Solid("#FFF") with Dissolve(4)
        time 131
        linear 3.0 alpha 0.0