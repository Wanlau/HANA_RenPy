label start:
    $ lily_rank = 0
    stop music fadeout 1.0
    scene black 
    with fade2

    jump s001

label s001:
    $ save_name = _("『无所事事的一天日常』")

    scene bg09a
    with gs_cud

    play music "bgm/M01.ogg" fadein 1.0

    play sound "se/SE001.ogg"

    window show
    voice "KAORI_0000"
    kaori "「嗯……嗯嗯……呼啊啊……得起床了……」"

    voice "KAORI_0001"
    kaori "「哈咻！」"

    voice "KAORI_0002"
    kaori "「呜～……总觉得有点冷……？」"

    play sound "se/SE002.ogg"

    voice "KAORI_0003"
    kaori "「哈咻……感冒了吗。」"

    voice "KAORI_0004"
    kaori "「啊咧？我没盖被子。」"

    voice "KAORI_0005"
    kaori "「奇怪，我的睡相应该没有这么糟糕的说……是太累了吗？」"

    play sound "se/SE003.ogg"

    voice "AMANE_0000"
    amane "「Ｚｚｚ～……」"

    scene EV01
    with gs_en_ns

    voice "KAORI_0006"
    kaori "「呜呀啊！」"

    voice "KAORI_0007"
    kaori "「怎，怎么怎么！？」"

    voice "AMANE_0001"
    amane "「Ｚ……ＺＺｚｚ——」"

    voice "KAORI_0008"
    kaori "「天音！？」"

    voice "AMANE_0002"
    amane "「呼呼……呜呼呼呼……」"

    voice "KAORI_0009"
    kaori "「你啊，又擅自潜入别人家里！天音家在隔壁吧！」"

    voice "KAORI_0010"
    kaori "「而且夺走别人被子，还一副幸福的睡脸。」"

    voice "AMANE_0003"
    amane "「呜呼……呜呼呼呼……」"

    voice "KAORI_0011"
    kaori "「呜哇，居然在笑……喂，天音快起来！」"

    voice "AMANE_0004"
    amane "「啊啊嗯——，不要～」"

    voice "KAORI_0012"
    kaori "「这算什么梦话……」"

    voice "AMANE_0005"
    amane "「呜嗯——……把馒头还给我啊……真是的，佳织真嘴馋呢。」"

    voice "KAORI_0013"
    kaori "「谁嘴馋啊！给我起来——！」"

    play sound "se/SE004.ogg"

    scene bg09a
    with gs_cud

    show amane tam04pb at c
    with dissolve

    voice "AMANE_0006"
    amane "「呀啊啊啊！」"

    show kaori tka01pb at l
    show amane tam04pb at r
    with dissolve

    voice "KAORI_0014"
    kaori "「起来啦？天音。」"

    show amane tam03pb at r

    voice "AMANE_0007"
    amane "「呼诶……佳织酱？」"

    voice "KAORI_0015"
    kaori "「没错——清醒了吗？」"

    show amane tam04pb at r

    voice "AMANE_0008"
    amane "「为什么佳织酱会在这里？这里是哪里！我的被子呢？」"

    show kaori tka08pb at l

    voice "KAORI_0016"
    kaori "「这是我的台词啊。这里是我的房间，天音的被子在天音自己的房间。」"

    voice "AMANE_0009"
    amane "「……哦哦！」"

    voice "KAORI_0017"
    kaori "「明白了吗？」"

    show amane tam02pb at r

    voice "AMANE_0010"
    amane "「佳织酱的睡衣……是新的呢～」"

    show kaori tka09pb at l

    voice "KAORI_0018"
    kaori "「不对——！」"

    show amane tam03pb at r

    voice "AMANE_0011"
    amane "「诶——可是，很可爱哦——？」"

    show kaori tka05pb at l

    voice "KAORI_0019"
    kaori "「哎……是吗？」"

    show amane tam02pb at r

    voice "AMANE_0012"
    amane "「嗯，虽然上次的也不错，这次也不错！很合身啊。」"

    voice "KAORI_0020"
    kaori "「是，是吗……如果天音这样说的话……买下来也不坏呢。」"

    voice "AMANE_0013"
    amane "「摸摸{note}」"

    show kaori tka04pb at l

    voice "KAORI_0021"
    kaori "「哇啊啊！？」"

    voice "AMANE_0014"
    amane "「触感真好，果然新品就是不一样呢。」"

    show kaori tka07pb at l

    voice "KAORI_0022"
    kaori "「等，等一下在干什么。快走开……啊嗯。」"

    voice "AMANE_0015"
    amane "「胸部，弹弹的——」"

    voice "KAORI_0023"
    kaori "「天·音·啊！」"

    voice "AMANE_0016"
    amane "「哈——这是不错的枕头呢——」"

    show kaori tka09pb at l

    voice "KAORI_0024"
    kaori "「够，够啦！真是的，快回房间换衣服去。」"

    show amane tam03pb at r

    voice "AMANE_0017"
    amane "「感觉好舒服不想离开啊——」"

    show kaori tka08pb at l

    voice "KAORI_0025"
    kaori "「都说不行，被这样摸的话我会……」"

    voice "AMANE_0018"
    amane "「嗯……？」"

    show kaori tka12pb at l

    voice "KAORI_0026"
    kaori "「我……不是会，心跳不已嘛……」"

    scene EV01p1
    with gs_en_ns

    voice "AMANE_0019"
    amane "「晚安咯——」"

    voice "KAORI_0027"
    kaori "「别睡啦！」"

    voice "AMANE_0020"
    amane "「……咕……咕。」"

    voice "KAORI_0028"
    kaori "「真的别睡了啦！」"

    voice "AMANE_0021"
    amane "「呼喵～～{heart}{heart}」"

    voice "KAORI_0029"
    kaori "「咕，总觉得比刚刚还要幸福的表情，叫也叫不起来。」"

    voice "AMANE_0022"
    amane "「佳织酱……呜喵呜喵……」"

    voice "KAORI_0030"
    kaori "「……唔。」"

    voice "KAORI_0031"
    kaori "「真是的，只有５分钟了哦。」"

    voice "AMANE_0023"
    amane "「呜咻呜咻{note}」"

    voice "KAORI_0032"
    kaori "「哈啊啊……」"

    stop voice
    window hide

    stop music fadeout 2.0
    scene black  with fade2
    pause 1

    jump s002
