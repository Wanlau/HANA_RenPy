label s032:
    $ save_name = "◇想坦白的沙雪同学"


    #**中庭・昼
    scene bg21a
    with fade



    window show



    #♂MP02
    play music "bgm/bgm02.ogg" fadein 1.0


    show rikka trk03s2
    with dissolve



    voice "RIKKA_0670"
    rikka "「哈啊，哈啊……哈啊……」"


    show rikka trk03s2 at l
    show sayuki tsy03s2 at r
    with dissolve



    voice "SAYUKI0283"
    sayuki "「那，那个……六夏同学……很，很难受……这样」"
    voice "RIKKA_0671"
    rikka "「诶………………啊，对不起！！」"

    hide rikka 
    hide sayuki 
    with dissolve


    "我慌慌张张地刹住，停下站着放开沙雪同学的手。"
    "在这之后，我突然被同班同学包围着，被追问了很多问题。"
    "沙雪同学也一样被大家包围着。"
    "好似要逃离同学一样，我带着沙雪同学一直逃到了中庭。"
    "从教室里逃出来的时候，后面传来『好帅气』『是要来场爱的私奔吗』『骑士带着公主逃跑了呢……啊啊，真浪漫{font=Tuffy-Regular-EN.ttf}♡{/font}』之类的很随心所欲的尖叫声。"
    "至于为什么还要把沙雪同学也一起带出来……除了是因为想帮助她以外，还有比这更要重要的事情。"
    "在等沙雪同学调整好呼吸后，我问了她我最想知道的事情。"


    show rikka trk03s2 at l
    show sayuki tsy01s2 at r
    with dissolve



    voice "RIKKA_0672"
    rikka "「那个……沙雪同学，为什么班上同学会开始讨论我们在交往这件事情啊？」"
    "对……我和沙雪同学两情相悦这件事，已经被全班同学知道了。"
    "然后这个起因，居然是沙雪同学自己。"
    "今天早上，看上去很高兴的样子，便被大家问『暑假是不是发生了什么好事呢？』之类的话。"
    "就非常爽快地把和我的关系说了出来。"
    "看着烦恼到头的我，沙雪同学轻轻地歪了一下脑袋。"


    #※CU06
    hide rikka 
    hide sayuki 
    show CU06
    with dissolve



    voice "SAYUKI0284"
    sayuki "「那个……难道这样不行吗？」"
    voice "RIKKA_0673"
    rikka "「与，与其说是不行……会很困扰，之类的……」"
    voice "SAYUKI0285"
    sayuki "「我觉得不会有人在背后说坏话，做的事也问心无愧，所以就……一不小心」"
    voice "RIKKA_0674"
    rikka "「那就，这……呜呜……」"
    "沙雪同学说的话我也懂。"
    "毕竟我们也没有做什么坏事。"
    "我今天早上也想过这样的事情，想要告诉别人，想要让别人倾听。"
    "不过冷静下来一想，会变成现在这样子，也是早该想到的事情了。"
    voice "RIKKA_0675"
    rikka "「那个……该怎么说好呢……」"
    voice "SAYUKI0286"
    sayuki "「难道说，六夏同学……你觉得很困扰吗？」"
    "用仰视的眼神，一动不动地盯着我的脸看。"
    "就好像发出了『丘噜』那样的声音一样的表情，让我的体温突然上升了。"


    #★★★選択肢　ここから


    "太可爱了，实在是太可爱了{font=Tuffy-Regular-EN.ttf}♡{/font}"
    "对这样的沙雪同学，我……"



#++選択肢（１）
#１．『很困扰什么的……说不出来』○
#２．『要好好说出口……我很困扰』×
label select07:
    menu:
        "对这样的沙雪同学，我……{fast}"
        "很困扰什么的……说不出来":
            jump select07_1
        "要好好说出口……我很困扰":
            jump select07_2



#１．『很困扰什么的……说不出来』○
label select07_1:


    voice "RIKKA_0676"
    rikka "「没，没有……困扰什么的，才没有……」"
    "说着古怪的话，只是不想让沙雪同学心情不好罢了。"
    "所以并没有对她说出真心话。"


    #set f1 f1+1
    $ lily_rank += 1
    jump select07_end


#２．『要好好说出口……我很困扰』×
label select07_2:


    voice "RIKKA_0677"
    rikka "「其，其实我……那个，很困扰……」"
    voice "SAYUKI0287"
    sayuki "「你觉得……很困扰，吗……？」"
    "啊啊， 沙雪同学看上去就像马上就会哭出来一样……"
    "果然还是不行，说不出口。"
    voice "RIKKA_0678"
    rikka "「果然，还是……没事」"
    voice "SAYUKI0288"
    sayuki "「是，吗……呼」"


#++選択肢終了
#★★★選択肢　ここまで
label select07_end:


    voice "SAYUKI0289"
    sayuki "「那就太好了。大家都非常热心地祝福我们俩的事情」"
    voice "RIKKA_0679"
    rikka "「是，是这样吗……啊哈，啊哈哈哈」"
    "看着她这么开心地说着，我根本说不出『因为觉得很害羞所以不想让大家知道』这样的话。"
    "可是，这么说来……"
    voice "RIKKA_0680"
    rikka "「和我的妄想中的沙雪同学，还真是很大的差别呢」"
    "虽然那只是我任意捏造的沙雪同学。"
    "我还一心认为沙雪同学是很害羞，希望把这件事当做秘密的人呢。"
    "原来是和我的预想差别十分大的角色啊……还真是意料之外。"
    "还在想着这样的事情的时候，突然沙雪同学向我搭话了。"
    voice "SAYUKI0290"
    sayuki "「六夏同学……这里的树阴，很凉爽呢」"
    voice "RIKKA_0681"
    rikka "「嗯，对啊。虽然暑假已经结束了，但秋老虎还是很猖狂呢……对了，去食堂买果汁来这里喝怎么样」"
    voice "RIKKA_0682"
    rikka "「沙雪同学，之前不也说过想去食堂看看吗？」"
    voice "SAYUKI0291"
    sayuki "「你还记得这件事呢，六夏同学。我很高兴……我们走吧」"
    "这种小小的事情也能让她开心。"
    "虽然让大家知道我们的事情是有一些困扰……但并不代表我们之前的关系就变味了。"
    "果然，两情相悦就是……开心啊。"
    voice "RIKKA_0683"
    rikka "「那么我们走吧，沙雪同学」"
    "从现在开始，让我们更加深入地了解对方吧。"
    "有不同的意见的时候，互相分享自己的想法就好了吧。"
    "至少，我是这么想的……但是。"


    #**暗転
    window hide


    scene black
    with fade



    #**新校舎教室・昼
    scene bg04a
    with fade



    window show



    show rikka trk03s2
    with dissolve



    voice "RIKKA_0684"
    rikka "「……嗯？」"
    "第二天，进教室的时候，又开始喧闹起来。"
    "大家都呀——呀——地叫着。"
    voice "RIKKA_0685"
    rikka "「怎么了啊……啊，大家都在沙雪同学周围……」"
    "沙雪同学周围都是班上同学，十分的吵闹。"
    voice "RIKKA_0686"
    rikka "「……好讨厌的感觉，无视好了」"

    hide rikka 
    with dissolve


    "而且，到底是什么事情让她们讨论得那么火爆啊……好似想知道，又好似不想知道那样。"
    "实在是忍不住想要快点确认，我便慢慢地靠近沙雪同学。"
    "然后，听到的内容是……"
    voice "mobJyosiA0060"
    girl_a "「居然，一起去了南方小岛，度过了旅行休假时光了吗！」"


    show sayuki tsy01s2
    with dissolve



    voice "SAYUKI0292"
    sayuki "「对……和六夏同学两个人，手牵着手一起爬上了岩地」"
    voice "mobJyosiB0036"
    girl_b "「手，牵着手……啊，那是怎样的感觉呢？」"


    show sayuki tsy02s2

    voice "SAYUKI0293"
    sayuki "「手十分的温暖……情不自禁地，用力回握了」"

    hide sayuki 
    show rikka trk05s2
    with dissolve



    voice "RIKKA_0687"
    rikka "「沙……沙雪同学……」"


    hide rikka 
    with dissolve


    "总觉得，光是听着我这边都开始害羞起来了。"
    "沙雪同学仍旧在同班同学的面前继续说着休假旅行的话题。"
    voice "mobJyosiC0015"
    girl_c "「那，那么说……那个，接……已经，接过吻了吗？」"


    show sayuki tsy05s2
    with dissolve



    voice "SAYUKI0294"
    sayuki "「接吻……吗。那个嘛……」"

    hide sayuki 
    show rikka trk09s2
    with dissolve



    voice "RIKKA_0688"
    rikka "「你，你们都在问些什么啊！！」"

    hide rikka 
    with dissolve


    "不行，说得越来越超过了……必须去阻止她们！！"
    "我慌慌张张地用手扒开了沙雪同学周边的同班同学。"
    "正在这个时候，圈子突然沸腾起来了。"
    voice "mobJyosiA0061"
    girl_a "「六夏同学闯进来了。是来保护公主的吧」"


    show rikka trk05s2
    with dissolve



    voice "RIKKA_0689"
    rikka "「虽然，根本不是什么保护之类的事……呜呜呜」"
    "我好像听到了沙雪同学很小声地说着『已经……接过吻了』之类的话。"


    show rikka trk03s2

    voice "RIKKA_0690"
    rikka "「沙雪同学，也不用把什么事情都说出来吧……」"

    hide rikka 
    with dissolve


    "就算我突然闯入了，好奇心满载的少女们的十万个为什么还是不会停止。"
    voice "mobJyosiB0037"
    girl_b "「沙雪同学，接吻之后的事怎么样了呢？」"


    show sayuki tsy03s2
    with dissolve



    voice "SAYUKI0295"
    sayuki "「………………诶？」"

    hide sayuki 
    show rikka trk04s2
    with dissolve



    voice "RIKKA_0691"
    rikka "「什，什什什什什什……」"

    hide rikka 
    with dissolve


    "到底在问沙雪同学怎样的问题啊！！"
    "终于来到了沙雪同学身边的我，像要挡住大家的视线一样站在了她的前面。"


    show rikka trk03s2
    with dissolve



    voice "RIKKA_0692"
    rikka "「哈啊，哈啊……沙雪同学……」"


    show rikka trk03s2 at l
    show sayuki tsy05s2 at r
    with dissolve



    voice "SAYUKI0296"
    sayuki "「六……六夏……同学……」"
    "沙雪同学的脸，很明显红成一片。"
    "都怪大家问这种问题才会让她为难的啊。"
    "虽然自己这么说很奇怪，但是看来即使是平时很废材的我。"
    "也必须在这里好好地说说她们了。"


    show rikka trk01s2 at l

    voice "RIKKA_0693"
    rikka "「大，大家，能不能请大家不要再继续问更多问题了？」"
    "在我说这句话的同时，沙雪同学也回答了之前的问题。"
    voice "SAYUKI0297"
    sayuki "「接吻之后的事情，还没有……还只是没有身体接触的关系阶段」"


    show rikka trk05s2 at l

    voice "RIKKA_0694"
    rikka "「呃！！」"
    "为什么连这些都要回答啊，沙雪同学……呜呜，哭哭哦……"
    "大家对着只能害羞到满脸通红的我，投来了羡慕的眼神。"
    voice "mobJyosiA0062"
    girl_a "「那还真是，原来是这样啊」"
    voice "mobJyosiB0038"
    girl_b "「不愧是，保护白雪的骑士啊」"
    voice "mobJyosiC0016"
    girl_c "「真的是……十分的禁欲主义呢」"


    show sayuki tsy02s2 at r

    voice "SAYUKI0298"
    sayuki "「是的，六夏同学是个非常棒的人」"
    voice "RIKKA_0695"
    rikka "「……啊啊……沙雪，同学……」"
    "在眼前就听到被这么说了的我，感觉马上就要倒地不起了。"
    voice "mobJyosiA0063"
    girl_a "「不过沙雪同学。还没有……就是说……」"
    voice "mobJyosiB0039"
    girl_b "「那就是说，难道说……现在开始……」"


    show rikka trk04s2 at l

    voice "RIKKA_0696"
    rikka "「等，等一下，给我停下来！！」"
    "沙雪同学稍微凝视了一会儿情不自禁加大声音的我。"
    voice "SAYUKI0299"
    sayuki "「哎呀，六夏同学……请问你怎么了？」"
    "笑嘻嘻的样子很可爱的沙雪同学，虽然还是那个可爱的沙雪同学。"
    "但是现在她的行为，她的言行，都让我始料未及。"
    "为什么要回答听到的所有问题，告诉别人我们的一切呢！？"


    show rikka trk03s2 at l

    voice "RIKKA_0697"
    rikka "「哈啊啊啊……可能，已经有点累了……」"
    "我没有隐藏困惑的样子，直接消沉了下去。"


    #**暗転
    window hide


    scene black
    with fade



    #**新校舎廊下・昼
    scene bg05a
    with fade



    window show



    show rikka trk03s2
    with dissolve



    voice "RIKKA_0698"
    rikka "「………………哈啊〜」"


    show risa tri03s2 at l
    show rikka trk03s2 at r
    with dissolve



    voice "RISA_0807"
    risa "「六夏，没什么精神呢……是得了苦夏了吗？」"
    "因为今天有活动执行委员的会议，我便向往常集合的教室走去。"
    "在半路，遇到了璃纱姐，就这样并肩一起走了。"
    voice "RIKKA_0699"
    rikka "「璃纱姐……你能，听我说一下吗？」"


    show risa tri01s2 at l

    voice "RISA_0808"
    risa "「可以啊。怎么了？」"
    "表现出『有兴趣』 的样子，璃纱姐开始关心了起来。"
    voice "RIKKA_0700"
    rikka "「那个，是……是关于沙雪同学的事情……」"
    voice "RISA_0809"
    risa "「果然是沙雪同学的事情啊。那到底是什么事情，是不是想秀恩爱？」"
    voice "RIKKA_0701"
    rikka "「不是这个啦……我和沙雪同学在交往这件事，好像全班同学都已经知道了……」"


    show risa tri04s2 at l

    voice "RISA_0810"
    risa "「好……好快呢。是谁说出来的呢……」"
    voice "RIKKA_0702"
    rikka "「那正是……沙雪同学本人说出来的样子」"
    "听了这话的璃纱姐一瞬间露出了一点点惊讶的表情，动摇了一下。"
    "毕竟，沙雪同学看上去就不像会对人坦白的角色呢。"
    voice "RIKKA_0703"
    rikka "「然后每天每天，都要被大家戏弄一番……那样子实在太辛苦了」"


    show risa tri01s2 at l

    voice "RISA_0811"
    risa "「那倒也是呢……呼——」"
    voice "RIKKA_0704"
    rikka "「呼什么的……总觉得，太……」"
    "明明我说得很严肃认真，璃纱姐却好似不愿意认真对待一样。"


    show rikka trk07s2 at r

    voice "RIKKA_0705"
    rikka "「太过分了，璃纱姐！我明明以为只有璃纱姐你能懂我的辛苦的说……」"
    voice "RISA_0812"
    risa "「因为嘛……那个嘛，六夏。就算沙雪同学不说，你们俩的关系发生进展这件事周围的人也早就知道了哦？」"


    show rikka trk03s2 at r

    voice "RIKKA_0706"
    rikka "「欸？为什么？？」"
    voice "RISA_0813"
    risa "「因为嘛……你们俩在一起的时候的气氛就感觉到了嘛。六夏你和我一样，什么事情都写在脸上了嘛」"
    voice "RIKKA_0707"
    rikka "「这，这种事情〜」"
    voice "RISA_0814"
    risa "「而且我觉得，沙雪同学不止是对同班同学们坦白了这件事」"
    voice "RIKKA_0708"
    rikka "「那么说，到底是怎样……」"
    voice "RISA_0815"
    risa "「看，就是这样」"
    "璃纱姐停下来指向了教室。"
    "指向了我们的目的地，活动执行委员的教室。"
    "是不是委员都到了，就算在教室外也能听到里面回响着欢乐的笑声。"
    voice "RISA_0816"
    risa "「那我就……打开了哦」"
    "璃纱姐看着我的脸，刷的一声把门给打开了。"


    #♀SE003
    play sound "se/se003.ogg"


    #**暗転
    window hide


    scene black
    with fade



    #**委員会室・昼
    scene bg30a
    with fade



    window show



    show sara tsa01s2
    with dissolve



    voice "SARA_0153"
    sara "「嘿诶〜，这么说沙雪是第一次去学校食堂啊」"


    show sara tsa01s2 at l
    show sayuki tsy02s2 at r
    with dissolve



    voice "SAYUKI0300"
    sayuki "「是的。然后在那里，两个人买了一样的果汁。我还是第一次喝在纸盒里面的果汁呢{font=Tuffy-Regular-EN.ttf}♪{/font}」"


    show sara tsa02s2 at l

    voice "SARA_0154"
    sara "「这样啊……总觉得，你们关系很好的样子呢{font=Tuffy-Regular-EN.ttf}♪{/font}」"


    show sara tsa02s2 at sl
    show sayuki tsy02s2 at c
    show nanami tna01s2 at sr
    with dissolve



    voice "NANAMI0260"
    nanami "「那，你们会一起回家吗？」"


    show sayuki tsy01s2 at c

    voice "SAYUKI0301"
    sayuki "「在车子不来接我的时候，偶尔会……」"
    voice "NANAMI0261"
    nanami "「那么说那么说，会手牵手之类的吗？？」"


    show sayuki tsy02s2 at c

    voice "SAYUKI0302"
    sayuki "「偶尔也会那样子。前几天一起逃出教室的时候也紧紧地握住了手{font=Tuffy-Regular-EN.ttf}♡{/font}」"

    hide sara 
    show yuuna tyu01s2 at sl
    with dissolve



    voice "YUUNA_0149"
    yuuna "「感觉天真烂漫的真好……分别的时候，会不会接吻呢？」"

    show sayuki tsy01s2 at c

    voice "SAYUKI0303"
    sayuki "「那个的话……还，不会」"


    hide yuuna 
    hide sayuki 
    hide nanami 
    show rikka trk04s2
    with dissolve



    voice "RIKKA_0709"
    rikka "「沙……沙雪同学！！」"
    "大家都把目光放到了大声叫她的名字的我的身上。"

    hide rikka 
    show sayuki tsy01s2
    with dissolve



    voice "SAYUKI0304"
    sayuki "「哎呀，六夏同学你也来了啊」"

    hide sayuki 
    show mai tma01s2
    with dissolve



    voice "MAI_0237"
    mai "「璃纱也来了的话……那就全部到齐了呢」"

    hide mai 
    with dissolve


    "然后这个话题总算是完了。"
    "大家都坐到了各自的座位上，我根本跟不上这个情况的脚步，只能站在那里一动不动的。"


    show sayuki tsy03s2
    with dissolve



    voice "SAYUKI0305"
    sayuki "「六夏同学……你怎么了？」"


    show rikka trk03s2 at l
    show sayuki tsy03s2 at r
    with dissolve



    voice "RIKKA_0710"
    rikka "「沙雪同学你才是……刚才，对大家都在说些什么啊？」"


    show sayuki tsy01s2 at r

    voice "SAYUKI0306"
    sayuki "「关于我们的事情。被问到了在旅行后发生了什么事情，就说明了一下」"
    voice "RIKKA_0711"
    rikka "「在这里……也要说啊，哈啊〜」"
    "不止是在班上，在这里沙雪同学也是有问必答的样子。"


    show sara tsa02s2 at sl
    show rikka trk03s2 at c
    show sayuki tsy01s2 at sr
    with dissolve



    voice "SARA_0155"
    sara "「年轻真好啊，新婚妇妇的感觉真般配呢，你们俩」"
    voice "RIKKA_0712"
    rikka "「纱良大人……」"

    hide sara 
    show yuuna tyu02s2 at sl
    show rikka trk03s2 at c
    show sayuki tsy01s2 at sr
    with dissolve



    voice "YUUNA_0150"
    yuuna "「对对，真的很可爱呢{font=Tuffy-Regular-EN.ttf}♡{/font}」"


    show rikka trk05s2 at c

    voice "RIKKA_0713"
    rikka "「呜呜呜……」"
    "被大家这样笑话，我便有些招架不住了。"

    hide yuuna 
    hide rikka 
    hide sayuki 
    show miya tmi01s2
    with dissolve



    voice "MIYA_0413"
    miya "「……六夏同学」"


    show miya tmi01s2 at l
    show rikka trk03s2 at r
    with dissolve



    voice "RIKKA_0714"
    rikka "「美，美夜大人，怎么了？」"
    "我曾经给美夜大人添了不少麻烦。"
    "如果被她问了我和沙雪同学的恋爱发展情况的话，感觉又会给添麻烦了……"
    "情不自禁的思考就会转向消极的方向去了。"
    voice "RIKKA_0715"
    rikka "「那个……我……」"
    voice "MIYA_0414"
    miya "「你们俩，看上去还是没有身体接触的样子呢」"
    voice "RIKKA_0716"
    rikka "「……啊？」"
    "沙雪同学，连这种事情也说出来了呢。"
    "气氛变得沉重之后，美夜大人对低着头的我的耳边说了悄悄话。"


    show miya tmi02s2 at l

    voice "MIYA_0415"
    miya "「六夏同学，不更加努力去攻略可不行哦……嗯哼哼{font=Tuffy-Regular-EN.ttf}♡{/font}」"


    show rikka trk04s2 at r

    voice "RIKKA_0717"
    rikka "「诶诶诶诶！？」"
    "美夜大人看上去很高兴的样子说出了不得了的话。"


    show rikka trk05s2 at r

    voice "RIKKA_0718"
    rikka "「啊呜……感觉，怎么说好呢……」"
    "因为实在是太害羞了，我都不知道该怎么回答好了。"
    "我可能已经，受不了这种话题了。"
    "快改变话题吧，这种话题就让它快快结束吧。"

    hide miya 
    show rikka trk03s2 at c
    with dissolve



    voice "RIKKA_0719"
    rikka "「那个，优菜大人，今天要从什么工作开始做呢？」"
    "总之，先开始做执行委员的工作吧。"


    show yuuna tyu01s2 at l
    show rikka trk03s2 at r
    with dissolve



    voice "YUUNA_0151"
    yuuna "「是呢……今天才刚刚开学不久，只是要见个面而已。没什么着急的工作呢」"


    show rikka trk04s2 at r

    voice "RIKKA_0720"
    rikka "「诶诶诶？」"
    voice "YUUNA_0152"
    yuuna "「六夏你还真是热血呢〜」"


    show rikka trk03s2 at r

    voice "RIKKA_0721"
    rikka "「不，也不是这样……」"


    show yuuna tyu02s2 at l

    voice "YUUNA_0153"
    yuuna "「不过没关系的。马上就会变得忙起来了……今天就悠闲地度过\n吧，六夏{font=Tuffy-Regular-EN.ttf}♪{/font}」"
    "也就是说……"

    hide yuuna 
    hide rikka 
    show reo tre01s2
    with dissolve



    voice "REO_0185"
    reo "「也就是说今天可以随便喝茶吃零食了吗？」"


    show mai tma01s2 at l
    show reo tre01s2 at r
    with dissolve



    voice "MAI_0238"
    mai "「嗯？会是这样吗。好吧，我去倒茶大家悠闲地喝茶聊天吧」"

    hide mai 
    hide reo 
    show yuuna tyu01s2
    with dissolve



    voice "YUUNA_0154"
    yuuna "「对对，我觉得这种感觉很好」"

    hide yuuna 
    show kaede tka01s2
    with dissolve



    voice "KAEDE_0124"
    kaede "「那么我也去帮忙倒茶了」"

    hide kaede 
    show sara tsa02s2
    with dissolve



    voice "SARA_0156"
    sara "「开茶会了呢，好开心{font=Tuffy-Regular-EN.ttf}♪{/font}　啊，零食怎么办呢」"


    show sara tsa02s2 at l
    show nanami tna01s2 at r
    with dissolve



    voice "NANAMI0262"
    nanami "「那么现在就去买来吧」"

    hide sara 
    hide nanami 
    show rikka trk03s2
    with dissolve



    voice "RIKKA_0722"
    rikka "「开，开茶会也太……」"
    "如果再这么悠闲下去的话，说不定什么时候又要开始回到我和沙雪同学的话题上来了。"
    voice "RIKKA_0723"
    rikka "「这，这种事情……还是饶了我吧……」"


    show rikka trk03s2 at l
    show sayuki tsy03s2 at r
    with dissolve



    voice "SAYUKI0307"
    sayuki "「六夏……同学？」"


    show rikka trk01s2 at l

    voice "RIKKA_0724"
    rikka "「走，走吧，沙雪同学！反正今天也没什么工作的样子」"
    voice "SAYUKI0308"
    sayuki "「六夏同学，这么说了的话……我没有关系的」"
    "在大家因为茶会而骚动的时候，我强硬地握住沙雪同学的手，离开了这个地方。"
    "但是，这个打算马上就被纱良大人发现了。"

    hide rikka 
    hide sayuki 
    show sara tsa02s2
    with dissolve



    voice "SARA_0157"
    sara "「呀啊，六夏抓着沙雪的手，想要从这里离开哦〜」"

    hide sara 
    show mai tma02s2
    with dissolve



    voice "MAI_0239"
    mai "「呵呵呵，肯定是想要两人独处吧。我懂你的〜」"

    hide mai 
    show yuuna tyu02s2
    with dissolve



    voice "YUUNA_0155"
    yuuna "「哎呀，所以六夏才会问有没有工作呢。想要快点结束，然后两人一起回去呢」"

    hide yuuna 
    show rikka trk05s2
    with dissolve



    voice "RIKKA_0725"
    rikka "「不，不是……呜」"
    "如果在这里反驳的话，这样下去会更加跳进黄河也洗不清了。"
    "既然都已经这样了，就只能将计就计了。"


    show rikka trk02s2

    voice "RIKKA_0726"
    rikka "「啊，啊哈……哈哈哈，被这么说了的话，我会为难的啊」"


    show rikka trk02s2 at l
    show sayuki tsy05s2 at r
    with dissolve



    "我带着苦笑的脸看向沙雪同学那边，她很好懂一般脸变得一片通红。"


    show rikka trk03s2 at l

    voice "RIKKA_0727"
    rikka "「沙雪……同学？」"
    voice "SAYUKI0309"
    sayuki "「在大家的面前把我带出去什么的……我，倒也不讨厌这样强硬又热情的六夏同学{font=Tuffy-Regular-EN.ttf}♡{/font}」"


    show rikka trk04s2 at l

    voice "RIKKA_0728"
    rikka "「诶诶诶诶！？」"
    "总觉得这样下去，又要被误会了。"


    show rikka trk03s2 at l

    "为什么事情总是会变成这样啊……呜呜呜。"


    #**暗転
    stop voice
    window hide


    stop music fadeout 2.0
    scene black  with fade2
    pause 1

    jump s033
