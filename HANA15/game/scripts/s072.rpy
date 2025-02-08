label s072:
    $ save_name = "◇优菜的『没问题{font=Tuffy-Regular-EN.ttf}♡{/font}』"


    #**新校舎教室・昼
    scene bg04a
    with fade



    window show


    #♂MP02
    play music "bgm/bgm02.ogg" fadein 1.0


    "不想输给沙雪同学……这样的念头在我心里生根发芽。"
    "我开始更加努力地学习。"
    "虽然平时，一直都是优菜姐姐大人在指导我，"
    "但是今天放学后，我只身一人在教室里学习。"
    "今天，我自己去图书馆和资料室搜集了各种资料，正在自学。"


    show nanami tna08s2 at c
    with dissolve



    voice "NANAMI0421"
    nanami "「唔嗯……啊、这个要这样……嗯」"
    "各种资料对于我来说都稍微有些难懂。"
    "但是我边参考书本边思考，用自己的方法拼命地学习。"


    show nanami tna03s2 at c



    voice "NANAMI0422"
    nanami "「嗯〜……这个很难呐。但是就这么留着疑问也不行……总是依赖姐姐大人，也不好」"
    "握着笔的手，一下子攥紧，感觉汗液黏在手心。"


    hide nanami
    show yuuna tyu03p at c
    with dissolve



    voice "YUUNA_0227"
    yuuna "「啊、七海〜。注意身体呀，不要太用功了哦……」"


    hide yuuna
    with dissolve


    "透过教室门，优菜姐姐大人用爱护得不得了的视线注视着我。"
    "原来，我竟然没有注意到她的存在，一直学习到了天黑……"


    #**暗転
    window hide
    scene black
    with fade



    #**新校舎廊下
    scene bg05a
    with fade



    window show


    show nanami tna01s2 at c
    with dissolve



    voice "NANAMI0423"
    nanami "「……啊、六夏同学」"


    show nanami tna01s2 at l
    show rikka trk03s2 at r
    with dissolve



    voice "RIKKA_1601"
    rikka "「七、七海大人……那个……您好……」"
    "我和六夏同学在走廊上碰个正着。"
    "六夏同学很明显有些不安。"
    voice "NANAMI0424"
    nanami "（一定是之前的事，让她不好意思吧……）"
    "六夏同学一定很不安很在意吧。"
    "那种心情，我很能理解。"
    voice "NANAMI0425"
    nanami "「那个……之前在中庭的事情，我们都忘掉吧」"
    voice "RIKKA_1602"
    rikka "「诶……」"
    voice "NANAMI0426"
    nanami "「虽然确实让人不安……但是我们也各自努力加油吧」"


    show rikka trk01s2 at r



    voice "RIKKA_1603"
    rikka "「七海……大人……」"


    #★★★選択肢　ここから

    "我对六夏同学说了鼓励的话。"


#++選択肢（１）
#１．『相信我们的恋人吧』○
#２．『更加努力吧』×
label select13:
    menu:
        "我对六夏同学说了鼓励的话。{fast}"
        "相信我们的恋人吧":
            jump select13_1
        "更加努力吧":
            jump select13_2


#１．『相信我们的恋人吧』○
label select13_1:


    voice "NANAMI0427"
    nanami "「优菜大人的恋人是我，沙雪同学的恋人是六夏同学……对吧？」"
    voice "RIKKA_1604"
    rikka "「那、那个……是！」"


    show nanami tna02s2 at l



    voice "NANAMI0428"
    nanami "「相信我们的恋人吧、呐？」"
    "我对着六夏同学微微一笑。"
    "我能感觉到，刚才又紧张又有些僵硬的六夏同学，肩膀稍稍放松了力气。"


    show rikka trk02s2 at r



    voice "RIKKA_1605"
    rikka "「是呢，七海大人。不相信所爱的人，是不配在一起的呀」"
    "六夏同学笑着，用力地点头。"
    voice "NANAMI0429"
    nanami "「是呢……是呀」"
    "我也一起点头了……把它说给自己听。"


    show rikka trk01s2 at r



    voice "RIKKA_1606"
    rikka "「我要尽努力做好现在能做的事！」"
    voice "NANAMI0430"
    nanami "「嗯，我也是」"
    voice "RIKKA_1607"
    rikka "「那，我先走了……」"
    voice "NANAMI0431"
    nanami "「嗯……再见」"


    hide rikka
    with dissolve


    "于是六夏同学轻快地，向着我前边走远了。"
    "做自己能做的事……相信恋人……"


    #set f1 f1+1
    $ lily_rank += 1
    jump select13_end


#２．『更加努力吧』×
label select13_2:


    voice "NANAMI0432"
    nanami "「因为恋人很优秀……所以，总会有些不安呢」"


    show rikka trk03s2 at r

    voice "RIKKA_1608"
    rikka "「嗯……是啊」"
    voice "NANAMI0433"
    nanami "「也正因为如此，我们自身就要更加努力，努力到让自己有自信为止……对吧？」"


    show rikka trk01s2 at r



    voice "RIKKA_1609"
    rikka "「七海大人……您说的没错，没自信真的不行呢」"
    "六夏同学很赞同地点着头。"


    show nanami tna02s2 at l



    voice "NANAMI0434"
    nanami "「是呢……更加努力吧！！」"
    "我也使劲点了一下头……把这句话说给自己听。"
    voice "RIKKA_1610"
    rikka "「我要尽努力做好现在能做的事！」"
    voice "NANAMI0435"
    nanami "「嗯，我也是」"
    voice "RIKKA_1611"
    rikka "「那，我先走了……」"
    voice "NANAMI0436"
    nanami "「嗯……再见」"


    hide rikka
    with dissolve


    "六夏同学向我前边走远了。"
    "努力到，自己所能做到的最大限……"


#++選択肢終了
#★★★選択肢　ここまで
label select13_end:


    "向六夏同学所说的话，其实全部都是说给自己听的话……嗯。"


    show nanami tna08s2 at c
    with dissolve



    voice "NANAMI0437"
    nanami "「……嗯，没问题的。要加油了」"
    "我握紧了拳头。"


    #**暗転
    window hide
    scene black
    with fade



    #**新校舎教室・夕
    scene bg04b
    with fade



    window show


    "我努力向别人展示着我比沙雪同学更适合作为优菜姐姐大人的继任者的优点。"
    "我每天在委员会积极地发言、积极地做事。"


    show nanami tna01s2 at c
    with dissolve



    voice "NANAMI0438"
    nanami "「文化祭要用的资料，我已经做好了。每人一份」"
    voice "mobJYOSIA0095"
    girl_a "「哇，资料这么多，都是您一个人整理的么？」"
    voice "NANAMI0439"
    nanami "「是呢。为了让资料更加易懂，还试着加入了一些插图」"
    voice "mobJYOSIB0056"
    girl_b "「整理得非常方便查阅呢。做得真好」"


    show nanami tna02s2 at c



    voice "NANAMI0440"
    nanami "「谢谢夸奖。要是能帮上大家的忙那就太好了」"
    voice "mobJYOSIC0028"
    girl_c "「七海大人，委员会的用品不够了……」"


    show nanami tna01s2 at c



    voice "NANAMI0441"
    nanami "「啊那个我已经提前准备好了」"
    voice "mobJYOSIC0029"
    girl_c "「哇，帮大忙了。真是非常感谢」"
    voice "NANAMI0442"
    nanami "「不用谢，都是小事」"


    show yuuna tyu01s2 at l
    show nanami tna01s2 at r
    with dissolve



    voice "YUUNA_0228"
    yuuna "「大家，辛苦了……已经这么晚了，今天先解散吧」"


    show nanami tna03s2 at r



    voice "NANAMI0443"
    nanami "「啊……已经这么晚……」"
    "现在才发觉，太阳已经落山了。"
    "对工作太过于集中注意力，完全没有发现。"
    "如果走夜路的话就太危险了，于是我赶紧收拾收拾，准备回家。"


    show nanami tna01s2 at r



    voice "NANAMI0444"
    nanami "「辛苦您了。优菜大人，明天见……」"
    voice "YUUNA_0229"
    yuuna "「……啊，七海同学」"
    voice "NANAMI0445"
    nanami "「诶、优菜大人？」"
    "姐姐大人抓住了我的包，让我停了下来。"
    "一不留神，用了平时的声音回复她。"
    voice "YUUNA_0230"
    yuuna "「我说，今天我们一起回家吧」"
    voice "NANAMI0446"
    nanami "「诶、啊……是」"


    show yuuna tyu02s2 at l



    voice "YUUNA_0231"
    yuuna "「因为最近好久都没有一起回家了{font=Tuffy-Regular-EN.ttf}♪{/font}」"
    voice "NANAMI0447"
    nanami "「哈啊……是……」"
    "于是我和姐姐大人，时隔多日地再一次一起回家了。"


    #**暗転
    window hide
    scene black
    with fade



    #**並木道・夕
    scene bg18b
    with fade



    window show


    show yuuna tyu01s2 at l
    show nanami tna01s2 at r
    with dissolve



    voice "YUUNA_0232"
    yuuna "「像这样并排着走，好久都没有过了呢〜」"
    voice "NANAMI0448"
    nanami "「是呢，最近完全没有呢」"


    show yuuna tyu06s2 at l



    voice "YUUNA_0233"
    yuuna "「是呢〜，连H也是，有些怀念了呢……（哭）」"


    show nanami tna04s2 at r



    voice "NANAMI0449"
    nanami "「姐、姐姐大人……要是被谁听到了可怎么办呀」"
    "姐姐大人突然说出了这样的话，我有些仓皇失措。"



    show nanami tna03s2 at r



    "左左右右地看看有没有人。"
    "呼……太好了，除了我俩没有其他人。"


    show yuuna tyu01s2 at l



    voice "YUUNA_0234"
    yuuna "「我可是每天，都想和七海做好~多、好~多H的事情呐」"


    show nanami tna04s2 at r



    voice "NANAMI0450"
    nanami "「什什什、什么啦。我、我虽然也是这么想的……」"
    voice "YUUNA_0235"
    yuuna "「想把七海可爱的那里弄得湿湿的，想要吸吸那个像小猫一样可爱的小舌头」"


    show nanami tna03s2 at r



    voice "NANAMI0451"
    nanami "「真、真是的~，姐姐大人依然还是个色女……」"
    "虽然表现得一脸讶异，但是心底却完全不讨厌。"
    "因为被喜欢的人求爱，是件太幸福的事情。"
    voice "YUUNA_0236"
    yuuna "「我说，七海……可以亲你么？」"
    voice "NANAMI0452"
    nanami "「姐、姐大人，一定要在这种地方……」"


    show yuuna tyu08s2 at l



    voice "YUUNA_0237"
    yuuna "「欲求不满快要爆发了。忍耐不了了……可以亲么？」"
    voice "NANAMI0453"
    nanami "「姐、姐姐大人……」"
    "姐姐大人真挚的脸庞渐渐靠近，"
    "姐姐大人，真是过分呢……明明知道我反抗不了的……"
    "姐姐大人漂亮的脸在眼里放大，唇与唇相接……那一瞬间。"
    voice "NANAMI0454"
    nanami "「……诶？」"
    "脑海一瞬间变得空白。"


    show yuuna tyu04s2 at l



    voice "YUUNA_0238"
    yuuna "「七、七海！？」"


    #※EV041
    scene EV41
    with dissolve



    "姐姐大人抱紧了我将要倒下的身体。"
    voice "NANAMI0455"
    nanami "「啊……姐姐大人，谢谢……」"
    voice "YUUNA_0239"
    yuuna "「哎呀……很担心啊，没事么，七海？」"
    voice "NANAMI0456"
    nanami "「没事。那个……不好意思」"
    voice "YUUNA_0240"
    yuuna "「是么，那就好……但是七海，你最近脸色不好呢」"
    "姐姐大人用她柔软又光滑的手，摸着我的额头。"
    voice "NANAMI0457"
    nanami "「诶、是么？　我自己倒是完全没感觉」"
    voice "YUUNA_0241"
    yuuna "「努力得都顾不上自己的身体了吧？」"
    voice "NANAMI0458"
    nanami "「那、那是因为……我自己没有好好管理健康状况……我真的，非常不好意思……」"
    "感觉有些消沉了。"


    #※EV041P1
    scene EV41p1
    with dissolve



    voice "YUUNA_0242"
    yuuna "「呼呼……我说，七海，其实不用那么努力也没事的哦」"
    "姐姐大人一边抚摸着我的脸颊，一边点了下头、用十分温柔的表情对我说。"
    voice "YUUNA_0243"
    yuuna "「七海，你已经非常努力了……不用这么拼命，也没问题的」"
    "然后朝着我微笑的姐姐大人，简直就像圣母一样。"
    "就像是有圣光一样让人眩晕。"
    voice "NANAMI0459"
    nanami "「啊……姐姐大人」"
    voice "YUUNA_0244"
    yuuna "「但〜是〜啊〜」"


    #**並木道・夕
    scene bg18b
    with dissolve



    show yuuna tyu08s2 at l
    show nanami tna10s2 at r
    with dissolve



    voice "NANAMI0460"
    nanami "「呀啊啊啊、姐姐大人，痛、好痛」"
    "刚刚还在抚摸脸颊的手，揪了一下脸蛋。"
    voice "YUUNA_0245"
    yuuna "「不可以把自己和沙雪酱，那样子比较哦」"


    show nanami tna04s2 at r



    voice "NANAMI0461"
    nanami "「姐、姐姐大人……你都知道了！？」"
    "听到姐姐大人那句话的瞬间，自己更加没有力气了。"


    show yuuna tyu02s2 at l



    voice "YUUNA_0246"
    yuuna "「只要是七海的事情，我什么都可以看透哦{font=Tuffy-Regular-EN.ttf}♪{/font}」"


    show nanami tna01s2 at r



    voice "NANAMI0462"
    nanami "「姐姐大人……」"


    show yuuna tyu01s2 at l



    voice "YUUNA_0247"
    yuuna "「七海现在在烦恼什么，我也完全明白……呐」"


    show nanami tna03s2 at r



    voice "NANAMI0463"
    nanami "「我、我……」"
    voice "YUUNA_0248"
    yuuna "「七海所能感受到的，不用说我全都能知道，以及连七海今天穿的内裤颜色我都知道……」"


    show nanami tna04s2 at r



    voice "NANAMI0464"
    nanami "「诶、诶诶诶！？　连这都知道吗！？」"


    show yuuna tyu02s2 at l



    voice "YUUNA_0249"
    yuuna "「知道哟〜{font=Tuffy-Regular-EN.ttf}♪{/font}　今天七海的内裤颜色是……」"


    show nanami tna09s2 at r



    voice "NANAMI0465"
    nanami "「讨、讨厌，不要说了！！　还有，在马路中间请不要摸我的大腿！！」"
    "本应该是抚摸着脸颊的姐姐大人的手，不知不觉地在色情地摸我的大腿。"


    show yuuna tyu09s2 at l



    voice "YUUNA_0250"
    yuuna "「七海真是的，真薄情……」"


    show nanami tna07s2 at r



    voice "NANAMI0466"
    nanami "「时间地点场合很重要好吧！！　请好好区分啊」"


    show yuuna tyu01s2 at l



    voice "YUUNA_0251"
    yuuna "「知道了〜。被可爱的小七海这么骂了也没办法呢〜」"
    "姐姐大人这才勉勉强强地挪开了手。"


    show nanami tna03s2 at r



    voice "NANAMI0467"
    nanami "（真是的，一点也不放过机会……果然是色色的姐姐大人）"
    voice "YUUNA_0252"
    yuuna "「那我们快回去吧。今天适当地学习一下就好好休息吧？」"


    show nanami tna01s2 at r



    voice "NANAMI0468"
    nanami "「好的……姐姐大人」"
    "果然完全比不过姐姐大人呀。"
    "已经完全被姐姐大人看透了。"
    voice "NANAMI0469"
    nanami "（得让姐姐大人少担心才对呢……嗯）"
    "于是，我们慢慢地从林间小道走回了家。"


    #**暗転
    stop voice
    window hide


    stop music fadeout 2.0
    scene black  with fade2
    pause 1

    jump s073
