label s050:

    scene bg19a
    with gs_cud

    play music "bgm/M12.ogg" fadein 1.0

    show kaori tka02sa at c
    with dissolve

    window show
    voice "KAORI_1291"
    kaori "「贵安。」"

    show kaori tka02sa at l
    show koharu tko01sa at r
    with dissolve

    voice "KOHARU_0524"
    koharu "「啊，是佳织。」"

    show kaori tka02sa at sl
    show makoto tma01sa at sr
    show koharu tko01sa at c
    with dissolve

    voice "MAKOTO_0448"
    makoto "「感冒已经好了吗……？」"

    voice "KAORI_1292"
    kaori "「已经完全精神了，托大家的福呢。」"

    show koharu tko02sa at c

    voice "KOHARU_0525"
    koharu "「没有这回事。可是太好了。」"

    voice "KAORI_1293"
    kaori "「嗯，今天开始又能跟你们在一起了呢。」"

    hide kaori
    hide makoto
    hide koharu
    show amane tam03sa at c
    with dissolve

    voice "AMANE_1263"
    amane "「……咳。」"

    show amane tam03sa at l
    show koharu tko03sa at r
    with dissolve

    voice "KOHARU_0526"
    koharu "「天音……？」"

    show amane tam02sa at l

    voice "AMANE_1264"
    amane "「那个——，漂亮地被传染了啊——」"

    show koharu tko04sa at r

    voice "KOHARU_0527"
    koharu "「诶诶诶？」"

    hide koharu
    show kaori tka08sa at l
    show amane tam02sa at r
    with dissolve

    voice "KAORI_1294"
    kaori "「没有咳嗽感冒就不会传染，这么说的是谁呢。」"

    show amane tam03sa at r

    voice "AMANE_1265"
    amane "「根据我的知识，应该是这样子的啊，怪了。」"

    show kaori tka03sa at l

    voice "KAORI_1295"
    kaori "「睡在我旁边才会变成这样吧？」"

    hide kaori
    show amane tam03sa at l
    show koharu tko03sa at r
    with dissolve

    voice "KOHARU_0528"
    koharu "「还来上学没关系吗？」"

    show amane tam01sa at l

    voice "AMANE_1266"
    amane "「嗯，没有发烧，也吃了止咳药。」"

    voice "AMANE_1267"
    amane "「再过一段时间，应该就能完全止住了吧。」"

    hide koharu
    show kaori tka03sa at l
    show amane tam01sa at r
    with dissolve

    voice "KAORI_1296"
    kaori "「虽然我说过要休息呢。」"

    voice "AMANE_1268"
    amane "「因为，想来学校嘛。」"

    voice "KAORI_1297"
    kaori "「因为扁桃腺发炎而发烧的话我可不管哦？」"

    show amane tam02sa at r

    voice "AMANE_1269"
    amane "「那个时候，佳织酱会来看护的所以没关系。」"

    voice "KAORI_1298"
    kaori "「什么没关系啊……」"

    show amane tam03sa at r

    voice "AMANE_1270"
    amane "「话说回来，为什么会被传染了呢？」"

    show kaori tka01sa at l

    voice "KAORI_1299"
    kaori "「是空气传染之类的吧。」"

    voice "AMANE_1271"
    amane "「明明没有咳嗽？」"

    hide amane
    show makoto tma01sa at r
    with dissolve

    voice "MAKOTO_0449"
    makoto "「一起洗澡之类的……」"

    voice "KAORI_1300"
    kaori "「不是，我只是用淋浴洗了一下而已。」"

    hide makoto
    show amane tam02sa at r
    with dissolve

    voice "AMANE_1272"
    amane "「啊，或许明白了。」"

    voice "KAORI_1301"
    kaori "「什么？」"

    window hide
    scene EV20
    with gs_en_ns

    window show
    voice "AMANE_1273"
    amane "「一定是因为和佳织酱ＫＩＳＳ的原因啦——」"

    voice "KAORI_1302"
    kaori "「什！？」"

    voice "KOHARU_0529"
    koharu "「！！」"

    voice "MAKOTO_0450"
    makoto "「ＫＩ……ＫＩＳＳ……」"

    voice "KAORI_1303"
    kaori "「笨，笨蛋！在说什么啊！」"

    voice "AMANE_1274"
    amane "「一定是这样，除此之外想不到其他了嘛。」"

    voice "KAORI_1304"
    kaori "「所，所以，这种事不要在别人面前说出来啊。」"

    voice "KOHARU_0530"
    koharu "「哈哇哇，果然两人是……」"

    voice "MAKOTO_0451"
    makoto "「特别的关系……」"

    voice "MAKOTO_0452"
    makoto "「哈呜……咻呜呜呜呜。」"

    voice "KOHARU_0531"
    koharu "「啊啊，真琴又晕倒啦！」"

    voice "AMANE_1275"
    amane "「嗯嗯。」"

    voice "KAORI_1305"
    kaori "「求你了，不要再说下去了啦～～～！」"

    voice "AMANE_1276"
    amane "「是吗，所以才被传染了啊。」"

    voice "AMANE_1277"
    amane "「那就没办法呢。我和佳织酱ＬＯＶＥＬＯＶＥ嘛。」"

    voice "AMANE_1278"
    amane "「佳织酱，最喜欢你了哦{note}」"

    voice "KAORI_1306"
    kaori "「天……天……」"

    voice "AMANE_1279"
    amane "「嗯？咋了？佳织酱。」"

    voice "KAORI_1307"
    kaori "「呜……咕咕……天音个笨蛋～～～！」"

    stop voice
    window hide
    pause 3

    stop music fadeout 4.0
    scene black with Dissolve(4)
    pause 1

label Ending:
    scene black with None
    play music "bgm/ED.ogg" noloop
    show ending

    python:
        if not _in_replay:
            _game_menu_screen = None
            _dismiss_pause = False
            _rollback = False
            renpy.pause(delay=173,hard=True)
            renpy.full_restart()
        else:
            _game_menu_screen = None
            renpy.pause(delay=173)
            _game_menu_screen = "save"
            renpy.end_replay()
