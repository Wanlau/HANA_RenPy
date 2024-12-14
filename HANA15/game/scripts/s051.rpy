label s051:
    $ save_name = "◇至此、一件事了结？？"


    #**六夏の部屋・昼
    scene bg34a
    with fade



    window show



    #♂MP17
    play music "bgm/bgm17.ogg" fadein 1.0


    show rikka trk03p
    with dissolve



    voice "RIKKA_1437"
    rikka "「……嗯……啊啊、我……什么时候……嗯」"
    "像是，一不小心睡着了……"
    "虽然很舒适、倦怠感却包围着我全身。"
    "因为真的很舒服、就想要一直保持这样子。"
    "但是……总觉得、会将什么重要的事……"
    "透过窗户隐隐约约能看见的是、泛着白色光辉的朝日。"


    show rikka trk09p

    voice "RIKKA_1438"
    rikka "「『疼爱你到早上』、明明这么向沙雪同学承诺了的……怎么会一个人不小心睡着了啦、我真是的！」"
    "刚才为止还有些睡迷糊的眼睛、一瞬间睁得大开。"

    hide rikka 
    with dissolve


    "沙雪同学、现在说不定在生气啊……略有些焦虑的环顾了周围。"
    "紧接着、就在身边感觉到了温暖的气息。"


label Replay01_05:
    if _in_replay:
        scene black with fade2
        play music "bgm/bgm17.ogg" fadein 1.0

    #※EV025
    scene EV25
    with dissolve

    window show

    voice "SAYUKI0767"
    sayuki "「呼……咕、嗯……呼、呼……」"
    voice "RIKKA_1439"
    rikka "「沙雪同学……沙雪同学也、睡着了啊……呼」"
    "沙雪同学的姿势是横着睡，靠着我的身体。"
    "紧紧地抱着我睡着了的样子。"
    voice "RIKKA_1440"
    rikka "「太好了……你就在我身边」"
    voice "SAYUKI0768"
    sayuki "「呼、呼………………呼、嗯……」"
    voice "RIKKA_1441"
    rikka "「不想离开……不要离开我，沙雪同学……」"
    "想一直都像这样在一起……想呆在这个人的旁边。"
    "为了可以在一起，我应该……做些什么？"
    voice "RIKKA_1442"
    rikka "「我该怎么做才好？……告诉我啊，沙雪同学」"
    voice "SAYUKI0769"
    sayuki "「呼……呼、嗯……呼……」"
    voice "RIKKA_1443"
    rikka "「……这应该是自己来考虑的事情呢，对吧」"
    "我看着沙雪同学的睡脸，一边紧紧地抱住了她的腰。"
    "我想更加，更加贴近爱着的她。"
    voice "RIKKA_1444"
    rikka "「最喜欢你了……我爱你，沙雪同学……」"
    voice "SAYUKI0770"
    sayuki "「嗯、嗯嗯……唔啊……」"


    #※EV025P1
    scene EV25p1
    with dissolve



    voice "RIKKA_1445"
    rikka "「啊……我吵醒你了吗、沙雪同学……」"
    voice "SAYUKI0771"
    sayuki "「嗯、嗯嗯………………呼，呼……嗯……」"
    voice "RIKKA_1446"
    rikka "「……太好了，还没有醒」"
    voice "SAYUKI0772"
    sayuki "「啊……六，六夏同学……？」"
    "啊……不好，果然弄醒她了的样子"
    "不知不觉就抱住了她……"


    #※EV025P2
    scene EV25p2
    with dissolve



    voice "RIKKA_1447"
    rikka "「吵醒你了、对不起……沙雪同学」"
    voice "SAYUKI0773"
    sayuki "「……没、没事……呼啊啊〜……啊、不好意思」"
    "慌慌张张地捂住打哈气的嘴。"
    "一边害羞着、沙雪同学微微笑了。"
    "又可爱又让人怜爱、天使的笑颜。"
    "就像被吸引住了一般、我……"
    voice "RIKKA_1448"
    rikka "「沙雪同学………………嗯{font=Tuffy-Regular-EN.ttf}♡{/font}」"
    voice "SAYUKI0774"
    sayuki "「嗯啾……{font=Tuffy-Regular-EN.ttf}♡{/font}　嗯啊……六夏同学……{font=Tuffy-Regular-EN.ttf}♡{/font}」"
    "一边沙雪同学小巧的唇上轻吻。"
    "我已经、下定了决心。"
    voice "RIKKA_1449"
    rikka "「啾……嗯……那个、沙雪同学……」"
    voice "SAYUKI0775"
    sayuki "「嗯……六夏同学」"
    "似乎是察觉我想说些什么、沙雪同学默默地注视着这里。"
    "其实是……不想说的、因为还想和她在一起。"
    "但是这对她并不好……我这么想着。"


    #endscene
    #setscene 4
    $ renpy.end_replay()
    $ persistent.Replay01_05 = True

label s051_2:
    #**六夏同学の部屋・昼
    scene bg34a
    with dissolve



    show rikka trk08z
    with dissolve



    voice "RIKKA_1450"
    rikka "「果然你还是回家去比较好……沙雪同学」"


    show rikka trk08z at l
    show sayuki tsy03z at r
    with dissolve



    voice "SAYUKI0776"
    sayuki "「六夏同学……果然我呆在这里是个麻烦吗……」"
    voice "RIKKA_1451"
    rikka "「怎么会、没有那种事！！如果可以的话倒是一直……就这样一\n直、想让沙雪同学呆在我身边」"
    voice "SAYUKI0777"
    sayuki "「那么为什么……」"


    show rikka trk03z at l

    voice "RIKKA_1452"
    rikka "「那是……现在的我的话、没有那么奢望的资格……」"
    voice "SAYUKI0778"
    sayuki "「资格……难道你是指家族或者社会地位那种……」"
    voice "RIKKA_1453"
    rikka "「那些、也算吧……」"
    voice "SAYUKI0779"
    sayuki "「怎么会……我对六夏同学没有期望着那种东西啊。只要六夏同学说真心爱着我的话、仅那一句话就……」"


    show rikka trk08z at l

    voice "RIKKA_1454"
    rikka "「不、那样不行。我希望沙雪同学一定能够幸福、也想给予你幸福……但是那样的话、肯定需要得到沙雪同学家人的认可」"


    show sayuki tsy06z at r

    voice "SAYUKI0780"
    sayuki "「六夏同学……呜、呜呜……」"
    "稳重的沙雪同学此时却渗出了眼泪。"
    "用手帕将她的眼泪拭去的同时、我又一次向她开口到。"
    voice "RIKKA_1455"
    rikka "「沙雪同学……现在的我的话、如何都无法配上沙雪同学你。但是……」"


    show sayuki tsy03z at r

    voice "SAYUKI0781"
    sayuki "「但是……？」"
    voice "RIKKA_1456"
    rikka "「我会加油、会努力、成为优秀的人。变得独当一面之后、我就回来接沙雪同学、所以……呜呜」"
    "过于激动的我、就那样紧紧的抱住了沙雪同学。"


    show rikka trk09z at l

    voice "RIKKA_1457"
    rikka "「所以说到那为止、请等着我……我绝对、会去接你的！！」"


    show sayuki tsy08z at r

    voice "SAYUKI0782"
    sayuki "「六夏同学……」"
    "用力、一味用力的、将沙雪同学紧紧抱住。"
    "她什么也没有说、只是默默地、将身体交付于我的怀抱。"


    show rikka trk03z at l

    voice "RIKKA_1458"
    rikka "（啊啊……怎么办、说了很不得了的话……沙雪同学说不定吓到了……）"
    "不安一下涌了上来、好像又要回到平常没用的自己。"
    "在那样的我的臂腕中、沙雪同学静静的开口。"
    voice "SAYUKI0783"
    sayuki "「我明白了……六夏同学。我相信六夏同学所说的话。」"


    show rikka trk01z at l

    voice "RIKKA_1459"
    rikka "「沙雪同学……那……」"
    "有没有变得可以回家了呢…"
    voice "SAYUKI0784"
    sayuki "「我会等着六夏同学……所以说、这次的婚约我没有办法不拒绝」"


    show rikka trk04z at l

    voice "RIKKA_1460"
    rikka "「诶！？」"
    "那、也就是说……"
    voice "SAYUKI0785"
    sayuki "「虽然很对不起六夏同学、但是我还不能回家。」"


    show rikka trk03z at l

    voice "RIKKA_1461"
    rikka "「沙雪同学……」"
    voice "SAYUKI0786"
    sayuki "「如果我呆在这里会给六夏同学你添麻烦的话……我马上离开……」"
    voice "RIKKA_1462"
    rikka "「不。不是、那、那个……虽然完全没又给我添麻烦、那个……」"
    "希望她呆在这里、如果能一直在一起的话将会是多么令人开心的事。"
    "但是让沙雪同学再这样一直离家出走是不对的……"
    voice "RIKKA_1463"
    rikka "（怎么办、啊啊怎么办、我要怎么做才……）"
    "越思考、却越焦急而不知所措。"
    "这么下去、我的大脑都快要过热了……"

    #//SE：電話のコール音
    #♀SE026
    play sound "se/se026.ogg"


    show rikka trk04z at l

    voice "RIKKA_1464"
    rikka "「吓！？电电、电话……！？」"
    "那里传来的熟悉的声音、是我家里的电话铃。"
    "在这种时候、到底是什么事情啦、我明明没有接电话什么的空闲啊！！"


    show sayuki tsy03z at r

    voice "SAYUKI0787"
    sayuki "「六夏同学……有电话哦。还是接一下比较好……」"


    show rikka trk03z at l

    voice "RIKKA_1465"
    rikka "「也、也对哦、我知道了、去接去接。」"
    "放开沙雪同学的身体、匆忙的拿起听筒。"
    voice "RIKKA_1466"
    rikka "「喂、这里是篠崎家……」"
    voice "mobSAYUGM0000"
    unknown "『您那边是、篠崎六夏家没错吧？』"
    voice "RIKKA_1467"
    rikka "「是、是的……我就是六夏……」"
    voice "mobSAYUGM0001"
    unknown "『我家的沙雪、应该现在在贵府吧。能把电话给她听吗』"


    show rikka trk04z at l

    voice "RIKKA_1468"
    rikka "「我家的沙雪………………诶诶！？」"
    "就是说、这个电话对面的人是……沙雪同学的家人？"
    voice "RIKKA_1469"
    rikka "「怎、怎么办……呜、要怎么说才好呢……啊！？」"


    show sayuki tsy08z at r

    voice "SAYUKI0788"
    sayuki "「电话换人听了……我是沙雪。是祖母大人吗」"
    voice "mobSAYUGM0002"
    sayuki_grandma "『啊啊、是的。果然你在那里吗、沙雪』"


    show sayuki tsy03z at r

    voice "SAYUKI0789"
    sayuki "「祖母大人……是怎么、调查到这里的？」"
    voice "mobSAYUGM0003"
    sayuki_grandma "『比起那种小事、沙雪……快点回来吧』"


    show sayuki tsy07z at r

    voice "SAYUKI0790"
    sayuki "「不。 我不想和未曾谋面又素不相识的人结婚！！」"
    voice "RIKKA_1470"
    rikka "「沙雪同学……」"
    "那个一直十分大方乖巧而老实的沙雪同学、这时却用了很大声量。"
    "为了守护、和我的承诺……真的和她的家人……"


    show rikka trk08z at l

    voice "RIKKA_1471"
    rikka "（我也、想要表达出来……把自己的决意……）"
    "但是现在突然插入沙雪同学和她家人的对话里也不是很好……"
    voice "mobSAYUGM0004"
    sayuki_grandma "『够了、沙雪你给我回来！』"
    voice "SAYUKI0791"
    sayuki "「绝对不……除非这次的婚约解除…我是不会回到家里的！！」"
    voice "mobSAYUGM0005"
    sayuki_grandma "『那个婚约的话、已经解除了。所以…拜托了、快回来吧沙雪』"


    show sayuki tsy03z at r

    voice "SAYUKI0792"
    sayuki "「都说了、我是不会回………………诶！？祖母大人、您刚刚说……？」"
    voice "mobSAYUGM0006"
    sayuki_grandma "『所以说，这次的婚约解除了。我没想到对方是那样的人。』"
    voice "SAYUKI0793"
    sayuki "「到底是因为什么事情才──」"


    show rikka trk03z at l

    voice "RIKKA_1472"
    rikka "「沙雪同学……难道说……」"
    "虽然因为听筒对面的声音听不清楚、不能完全了解现在的状况。"
    "但看来发生了预想之外的事应该是没有错。"


    show rikka trk01z at l

    voice "RIKKA_1473"
    rikka "「这样的话说不定能行！……加油、沙雪同学！」"

    #//SE：携帯着信音
    #♀SE007
    play sound "se/se007.ogg"


    show rikka trk04z at l

    voice "RIKKA_1474"
    rikka "「吓、这、这次是手机……」"
    "总之先掏出手机、看了下屏幕。"
    "那里显示着一个我完全没有印象的号码。"


    show rikka trk03z at l

    voice "RIKKA_1475"
    rikka "「还是不接比较好……不、接吧」"
    "一瞬的踌躇之后、我按下了接听键。"
    voice "RIKKA_1476"
    rikka "「喂……请问是哪位？」"
    voice "mobSAYUHH0000"
    sayuki_mother "『六夏对吧、初次见面。我是白河沙雪的母亲。』"


    show rikka trk04z at l

    voice "RIKKA_1477"
    rikka "「咦、诶诶、诶诶诶诶诶诶诶诶！？沙雪同学的、母亲！？」"


    show sayuki tsy04z at r

    voice "SAYUKI0794"
    sayuki "「！！」"
    "在听到我那句话的瞬间、沙雪同学刷的将手伸了过来。"
    "从颤抖着的我的手中抢过了手机。"
    "右手拿着家里电话的分机、左手里又是手机……变成电话二刀流的沙雪同学先向手机那端说到……"
    voice "SAYUKI0795"
    sayuki "「母亲大人？真的是母亲大人吗！？」"
    voice "mobSAYUHH0001"
    sayuki_mother "『嗯、是的』"


    show sayuki tsy03z at r

    voice "SAYUKI0796"
    sayuki "「怎么会……究竟是怎么样、查到六夏同学的手机号码──」"
    voice "mobSAYUHH0002"
    sayuki_mother "『那种事怎样都好。能再把电话给六夏一下吗』"


    show sayuki tsy08z at r

    voice "SAYUKI0797"
    sayuki "「不要、如果你们和六夏同学讲什么奇怪的事……就算是我也是会生气的。」"
    voice "mobSAYUHH0003"
    sayuki_mother "『我不会做那么失礼的事。只是想表达一下帮我照看我重要的女儿一晚上的谢意罢了。』"
    voice "SAYUKI0798"
    sayuki "「母亲大人……那从我这里转达就可以了。总之六夏同学和我的离家出走没有任何关系」"
    voice "mobSAYUHH0004"
    sayuki_mother "『啊啊、我知道……我全都知道的。沙雪、你和六夏的事也、呐』"


    show sayuki tsy04z at r

    voice "SAYUKI0799"
    sayuki "「为、为什么那种事情、母亲大人会知道！？」"
    voice "mobSAYUHH0005"
    sayuki_mother "『沙雪、妈妈被小看的话可是会很困扰的。明明每天都从你那里听到那么多关于六夏的事情、呐？』"


    show sayuki tsy03z at r

    voice "SAYUKI0800"
    sayuki "「呜呜、怎么会……和六夏同学的事、都已经被母亲大人知道了什么的」"


    show rikka trk05z at l

    voice "RIKKA_1478"
    rikka "「沙雪同学……啊啊」"
    "就连在一边听着的我也变得害羞起来了。"
    "向班级里的大家、最佳情侣的前辈们都报告了和我恋爱进行时的沙雪同学。"
    "看来在家里也有向母亲提起过的样子……"
    voice "SAYUKI0801"
    sayuki "「母亲大人总是什么都一眼看穿呢……」"
    voice "mobSAYUHH0006"
    sayuki_mother "『嗯、说的没错』"
    voice "mobSAYUGM0007"
    sayuki_grandma "『沙雪……那种事的话明明也可以说给我听的』"
    "虽然不清楚对面是什么情况、这次是家里电话那边、沙雪同学的祖母大人向她说到。"
    voice "mobSAYUGM0008"
    sayuki_grandma "『如果沙雪有了能够寄予感情的对象的话、我马上就去见见那个人……用这双眼睛严格的品评一下才行』"


    show rikka trk04z at l

    voice "RIKKA_1479"
    rikka "「吓、吓！！」"
    "略有匕首般效果的低沉的声线、让我不禁颤抖起来。"


    show rikka trk03z at l

    voice "RIKKA_1480"
    rikka "（对、哦……和沙雪同学这样有力财阀的大小姐交往的话、与沙雪同学的祖母大人、母亲大人什么的也得好好相处才行……呜呜……）"
    "太可怕了、真心太可怕了。"
    "这么平民的我要怎么和那种大人物们交锋啦？"
    "说实话、我连一点自信都没有。"
    voice "mobSAYUGM0009"
    sayuki_grandma "『总之、沙雪。不能再给人家添麻烦了』"
    voice "mobSAYUHH0007"
    sayuki_mother "『就是啊、沙雪。这次的婚约已经取消了、你先回家再慢慢说吧……包括你今后的事情也是』"
    "被左右两边的电话同时劝说了。"
    "沙雪同学轻轻的点了点头。"
    voice "SAYUKI0802"
    sayuki "「我知道了……现在就回来…」"
    "朝两边都这么说了之后、沙雪同学把家里的电话挂断、将手机递还给了我。"
    voice "mobSAYUHH0008"
    sayuki_mother "『突然间抢了电话、抱歉哦、六夏』"
    voice "RIKKA_1481"
    rikka "「不、不……没关系……」"
    voice "mobSAYUHH0009"
    sayuki_mother "『以后我会让沙雪也带着手机的……那么再见了』"


    show rikka trk04z at l

    voice "RIKKA_1482"
    rikka "「好、好的、失礼了！！」"
    "背后渗出了汗、心也砰砰直跳的状态下、我总算是结束了和沙雪同学母亲的对话。"


    show rikka trk03z at l

    voice "RIKKA_1483"
    rikka "「哈，啊，哈……我太，太紧张了……哈唔……」"
    voice "SAYUKI0803"
    sayuki "「我……我也是，但是……六夏同学……哈啊〜」"
    "就要这样崩塌过去一样，两个人倒在了床上。"
    "在电话打来之前，都没有想过有这样的急展开。"
    "我和沙雪同学两个人都没有开始思考，就笑了出来。"


    show rikka trk02z at l
    show sayuki tsy02z at r

    voice "RIKKA_1484"
    rikka "「呼呼，但是累了呢……要不要喝点茶，沙雪同学？」"
    voice "SAYUKI0804"
    sayuki "「啊，好。我要喝。不过……喝了之后，我……要回家去」"
    voice "RIKKA_1485"
    rikka "「也，是呢……这样也的确，比较好……嗯」"


    stop music fadeout 1.0


    play music "bgm/bgm20.ogg" fadein 1.0


    "沙雪同学要，回家了啊……虽然从昨天，我就期望着她这么做。"
    "但，这个时候真的到来，没想到会，会这么的寂寞。"


    show rikka trk03z at l

    voice "RIKKA_1486"
    rikka "（就，只有两天……两天之间的，新婚夫妇一样的时间……已经结束了）"
    "到了现在，才觉得可惜。"
    "现在开始，几天也……不，多少天都好，好希望她能呆在这里。"


    show rikka trk02z at l

    voice "RIKKA_1487"
    rikka "「沙雪……同学，那个……这两天很高兴」"
    voice "SAYUKI0805"
    sayuki "「我也是，六夏同学……真的」"
    voice "RIKKA_1488"
    rikka "「不单单是快乐，怎么说，非常的幸福……十分十分的幸福，没有比这更幸福的了！」"
    voice "SAYUKI0806"
    sayuki "「六夏同学……唔……请不要说下去了。我会走不了的……」"


    show rikka trk10z at l

    voice "RIKKA_1489"
    rikka "「沙雪同学……我，不想让沙雪同学回去……唔，唔啊啊」"
    "不好，眼泪要渗出来了。"


    show sayuki tsy10z at r

    "接下来，沙雪同学也一样。"
    "不知道是谁先，我们两个抱在了一起。"
    voice "RIKKA_1490"
    rikka "「啊，沙雪同学……沙雪同学……唔，嗯咕……」"
    voice "SAYUKI0807"
    sayuki "「六夏同学……谢谢，谢谢你。真的，麻烦你照顾了。」"
    "不想离开你，想就这样下去……沙雪同学，也是这么想的。"
    "但是也明白这是不可能的事。"
    "所以她忍住悲伤，说出的……道别的话语。"
    "对于这样下了决意的沙雪同学，我已经不能再挽留了。"
    "所以我，轻轻放开了深爱的沙雪同学的身体。"


    show rikka trk01z at l

    voice "RIKKA_1491"
    rikka "「沙雪同学……那，再见……」"


    stop music fadeout 1.0


    #**暗転
    window hide


    scene black
    with fade


    play music "bgm/bgm22.ogg" fadein 1.0


    #**アトリエ・昼
    scene bg29a
    with fade



    window show



    #//SE：携帯コール音
    #♀SE007
    play sound "se/se007.ogg"


    show miya tmi01s2
    with dissolve



    voice "MIYA_0559"
    miya "「喂……」"
    voice "mobSAYUGM0010"
    sayuki_grandma "『绫濑家的大小姐……真的谢谢了。差点就让我重要的孙女惹出不得了的事情了……麻烦你了』"
    voice "MIYA_0560"
    miya "「因为沙雪也是我的朋友……能帮上忙真是太好了」"
    voice "mobSAYUGM0011"
    sayuki_grandma "『我也真是上年纪了……『智能机』啊『社交APP』什么的、搞不懂的东西越来越多了』"
    voice "MIYA_0561"
    miya "「不、您还算现役呢。最近的确是出现了与以前截然不同的商业模式……或许配置一个对那些方面都比较精通的年轻的助理会比较好」"
    voice "MIYA_0562"
    miya "「但是最终的判断、还是由聪明的白河会长来下达的比较好」"
    voice "mobSAYUGM0012"
    sayuki_grandma "『十分正确的意见……怎样啊、绫濑家的大小姐。我有些想将你『Headhunting（猎头）』来呢』"


    show miya tmi03s2

    voice "MIYA_0563"
    miya "「虽然我很高兴…但是…」"
    voice "mobSAYUGM0013"
    sayuki_grandma "『啊啊、我知道。只是老年人的玩笑罢了』"


    show miya tmi02s2

    voice "MIYA_0564"
    miya "「呼呼……说起来、之前拜托您的东西、刚刚送到了。谢谢您」"
    voice "mobSAYUGM0014"
    sayuki_grandma "『这次的回礼、像这样的东西便可以了吗？』"
    voice "MIYA_0565"
    miya "「已经足够了……十分感谢您」"
    voice "mobSAYUGM0015"
    sayuki_grandma "『以后有机会的话还想悠闲地和你聊天呢……什、沙雪回来了！？抱歉了绫濑家的大小姐、今天就说到这儿吧』"


    show miya tmi01s2

    voice "MIYA_0566"
    miya "「好的、那么贵安……啊啦、时间刚好呢」"

    #//SE：ドアの開く音
    #♀SE027
    play sound "se/se027.ogg"


    show miya tmi01s2 at l
    show risa tri01s2 at r
    with dissolve



    voice "RISA_0920"
    risa "「久等了、美夜。你在和谁通电话吗？」"
    voice "MIYA_0567"
    miya "「啊啊、有个小商谈……说起来璃纱、我入手了可口的西洋松露巧克力。一起吃吧」"


    show risa tri02s2 at r

    voice "RISA_0921"
    risa "「我最喜欢西洋松露巧克力了……咦这个不是以前在电视上播过的法国的超高档的那个吗{font=Tuffy-Regular-EN.ttf}♪{/font}呜哇{font=Tuffy-Regular-EN.ttf}♡{/font}真的可以吗、美夜？」"


    show miya tmi02s2 at l

    voice "MIYA_0568"
    miya "「当然。想吃多少尽管吃吧、璃纱……呼呼{font=Tuffy-Regular-EN.ttf}♡{/font}」"


    #**暗転
    stop voice
    window hide

    stop music fadeout 2.0
    scene black with fade2
    pause 1
    
    $ _rollback = False
    $ old_game_menu_screen = _game_menu_screen
    $ _game_menu_screen = None
    show eyecatch01 at eyecatch_in 
    $ renpy.pause(delay=2,hard=True)
    show eyecatch01 at eyecatch_out 
    $ renpy.pause(delay=5,hard=True)
    $ _game_menu_screen = old_game_menu_screen
    $ _rollback = True
    pause 1
    
    jump s052
