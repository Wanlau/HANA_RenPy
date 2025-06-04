label s044:

    scene bg08a
    with gs_cud

    play music "bgm/M01.ogg" fadein 1.0

    show kaori tka02sa at c
    with dissolve

    window show
    voice "KAORI_1101"
    kaori "「是因为发烧吗，风好舒服啊……」"

    show kaori tka02sa at l
    show amane tam03sa at r
    with dissolve

    voice "AMANE_1070"
    amane "「佳织酱，没事吗？」"

    show kaori tka01sa at l

    voice "KAORI_1102"
    kaori "「嗯……」"

    show amane tam02sa at r

    voice "AMANE_1071"
    amane "「可以早退真是太好了。」"

    voice "AMANE_1072"
    amane "「就算被保健老师要求在保健室休息，也只是陪睡而已呢！」"

    show kaori tka03sa at l

    voice "KAORI_1103"
    kaori "「不对，那得该乖乖回教室吧。」"

    show amane tam03sa at r

    voice "AMANE_1073"
    amane "「可不能丢下感冒的佳织酱啊。」"

    show kaori tka05sa at l

    voice "KAORI_1104"
    kaori "「是，是吗……」"

    voice "AMANE_1074"
    amane "「而且测量了还接近３８度。」"

    show kaori tka03sa at l

    voice "KAORI_1105"
    kaori "「可是，说不定会把感冒传染给你啊。」"

    voice "KAORI_1106"
    kaori "「嘛……就算只是这样挨着走，也有可能传染就是了。」"

    show amane tam01sa at r

    voice "AMANE_1075"
    amane "「又没有咳嗽，没问题。」"

    show kaori tka01sa at l

    voice "KAORI_1107"
    kaori "「是这样吗……」"

    voice "AMANE_1076"
    amane "「啊，差不多能看到家了。」"

    voice "KAORI_1108"
    kaori "「终于回到家了呢……家比平常还遥远的感觉……」"

    voice "AMANE_1077"
    amane "「是慢慢地走嘛。」"

    voice "KAORI_1109"
    kaori "「嗯……」"

    show amane tam03sa at r

    voice "AMANE_1078"
    amane "「说起来有感冒药吗？」"

    voice "KAORI_1110"
    kaori "「应该有……」"

    show amane tam08sa at r

    voice "AMANE_1079"
    amane "「好的。」"

    voice "KAORI_1111"
    kaori "「……」"

    show kaori tka03sa at l

    voice "KAORI_1112"
    kaori "「有什么，好的……？」"

    voice "AMANE_1080"
    amane "「那是，由我来照顾佳织酱哦！」"

    voice "KAORI_1113"
    kaori "「天音吗……」"

    show amane tam03sa at r

    voice "AMANE_1081"
    amane "「啊咧，为什么皱着眉头？」"

    voice "KAORI_1114"
    kaori "「不是……我在想会这么发展的不祥预感还真应验了呢……」"

    show amane tam02sa at r

    voice "AMANE_1082"
    amane "「嘛嘛，不要这么说，都交给我吧。」"

    voice "KAORI_1115"
    kaori "「没问题么……」"

    show amane tam01sa at r

    voice "AMANE_1083"
    amane "「比起身体不适的佳织酱要强呢。」"

    voice "KAORI_1116"
    kaori "「……啊呜。」"

    window hide
    scene bg09a
    with gs_cud

    play music "bgm/M13.ogg" fadein 1.0

    show amane tam01sa at c
    with dissolve

    window show
    voice "AMANE_1084"
    amane "「打扰啦——」"

    show kaori tka01sa at l
    show amane tam01sa at r
    with dissolve

    voice "KAORI_1117"
    kaori "「请……」"

    show amane tam08sa at r

    voice "AMANE_1085"
    amane "「来，看护时间！」"

    show kaori tka03sa at l

    voice "KAORI_1118"
    kaori "「不要用这么兴奋的语气说出来……」"

    voice "AMANE_1086"
    amane "「就是兴奋，是看护佳织酱哦？这种机会可不多嘛。」"

    voice "AMANE_1087"
    amane "「鼓足干劲照顾吧——，首先来换衣服！」"

    voice "KAORI_1119"
    kaori "「换，换衣服？我自己也做得来所以就免了吧。」"

    show amane tam02sa at r

    voice "AMANE_1088"
    amane "「好啦，好啦。」"

    show amane tam01sa at r

    voice "AMANE_1089"
    amane "「更换的衣服在哪里呢。佳织酱，可以打开衣柜吗？」"

label select04:
    menu:
        amane "「更换的衣服在哪里呢。佳织酱，可以打开衣柜吗？」{fast}"
        "不行！？":
            jump select04_1
        "……可以":
            jump select04_2

label select04_1:
    "（当然是不行了！）"

    "（虽然打算这么说……但在发呆的时候就已经被擅自打开了。）"

    "（啊呜呜。）"

    voice "KAORI_1120"
    kaori "「呜，嗯……」"

    $ lily_rank += 1
    jump select04_end

label select04_2:
    jump select04_end

label select04_end:

    voice "AMANE_1090"
    amane "「那个——睡衣在哪呢……就这件。」"

    voice "AMANE_1091"
    amane "「那么帮你脱校服吧。」"

    voice "KAORI_1121"
    kaori "「明明自己也做得到……」"

    show amane tam02sa at r

    voice "AMANE_1092"
    amane "「因为佳织酱是病人，所以依靠我也是可以的哦！」"

    show kaori tka05sa at l

    voice "KAORI_1122"
    kaori "「该说是依靠呢……还是难为情呢……」"

    window hide
    scene EV16
    with gs_en_ns

    window show
    voice "AMANE_1093"
    amane "「解开领巾。」"

    voice "KAORI_1123"
    kaori "「哇哇，一下子，就到这里。」"

    voice "AMANE_1094"
    amane "「一般，首先脱的是领巾吧？」"

    voice "KAORI_1124"
    kaori "「呜呜，话虽如此……」"

    voice "AMANE_1095"
    amane "「叠好领巾，接着是……」"

    voice "KAORI_1125"
    kaori "「不行，果然还是害羞啊，这个。」"

    voice "AMANE_1096"
    amane "「可不能穿着校服就睡啊？」"

    voice "KAORI_1126"
    kaori "「所以啊，我自己也可以脱了啦……」"

    voice "AMANE_1097"
    amane "「那样就算不上看护了！」"

    voice "KAORI_1127"
    kaori "「都说没这回事……」"

    voice "AMANE_1098"
    amane "「把手伸进裙子里了哦。」"

    play sound "se/SE039.ogg"

    voice "KAORI_1128"
    kaori "「咿呀嗯。」"

    window hide
    scene EV16p1
    with gs_en_ns

    window show
    voice "AMANE_1099"
    amane "「佳织酱真敏感啊{note}」"

    voice "KAORI_1129"
    kaori "「天——音——！」"

    voice "KAORI_1130"
    kaori "「咕啊啊……眼又冒金花了……」"

    voice "AMANE_1100"
    amane "「还在发烧所以别大叫啦。」"

    voice "KAORI_1131"
    kaori "「我知道，不过，不过……」"

    voice "AMANE_1101"
    amane "「佳织酱什么也不用干。全部交给我吧{note}」"

    voice "KAORI_1132"
    kaori "「呜呜呜……」"

    window hide
    scene bg09a
    with gs_cud

    show amane tam01sa at c
    with dissolve

    window show
    voice "AMANE_1102"
    amane "「脱下校服。内衣就——」"

    voice "KAORI_1133"
    kaori "「用不着脱到那里。」"

    voice "AMANE_1103"
    amane "「但是汗之类的——」"

    voice "KAORI_1134"
    kaori "「没有出汗了啦。」"

    show amane tam03sa at c

    voice "AMANE_1104"
    amane "「是么？明明连我都出汗了。」"

    voice "KAORI_1135"
    kaori "「比起那个还是快点给我换睡衣。」"

    show amane tam01sa at c

    voice "AMANE_1105"
    amane "「是——」"

    voice "AMANE_1106"
    amane "「嗯咻，嗯咻……」"

    voice "KAORI_1136"
    kaori "「……快点～～」"

    show amane tam04sa at c

    voice "AMANE_1107"
    amane "「啊……」"

    voice "KAORI_1137"
    kaori "「……什么。」"

    show amane tam02sa at c

    voice "AMANE_1108"
    amane "「睡衣的纽扣是心形的好可爱。」"

    voice "KAORI_1138"
    kaori "「那种事怎样都好～～」"

    voice "AMANE_1109"
    amane "「呵呵。」"

    show amane tam01sa at c

    voice "AMANE_1110"
    amane "「——好，换好了哦，急性子。」"

    show kaori tka07pa at l
    show amane tam01sa at r
    with dissolve

    voice "KAORI_1139"
    kaori "「没有急性子。」"

    show amane tam03sa at r

    voice "AMANE_1111"
    amane "「好啦好啦，这么生气的话体温又会上升哦？」"

    show kaori tka08pa at l

    voice "KAORI_1140"
    kaori "「呜呜……」"

    voice "AMANE_1112"
    amane "「佳织酱，发烧更严重了吗？连耳朵都红了哦？」"

    voice "KAORI_1141"
    kaori "「全都是你的错啦。」"

    voice "AMANE_1113"
    amane "「呵诶……哪方面？」"

    voice "KAORI_1142"
    kaori "「全方面。」"

    show amane tam01sa at r

    voice "AMANE_1114"
    amane "「总之，换装结束——」"

    show kaori tka03pa at l

    voice "KAORI_1143"
    kaori "「……哈啊啊，总觉得更累了。」"

    voice "AMANE_1115"
    amane "「因为还在发烧呢。佳织酱就躺下休息吧。」"

    show kaori tka01pa at l

    voice "KAORI_1144"
    kaori "「我知道了……」"

    voice "AMANE_1116"
    amane "「以这个势头，全力照顾佳织酱咯。」"

    show amane tam08sa at r

    voice "AMANE_1117"
    amane "「我的看护，才刚刚开始！」"

    show kaori tka03pa at l

    voice "KAORI_1145"
    kaori "「感到非常不安啊……」"

    stop voice
    window hide

    stop music fadeout 2.0
    scene black  with fade2
    pause 1

    jump s045
