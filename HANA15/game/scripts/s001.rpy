label start:
    $ lily_rank_pre = 0
    $ lily_rank = 0
    $ lily_route = 0
    $ save_name = ''
    stop music fadeout 1.0
    scene black 
    with fade2

    if persistent.Ending01 == True:
        window show
        menu:
            "从头开始":
                window hide
                pause 1
                jump s001
            "从海滩夏夜开始":
                window hide
                $ lily_rank_pre = 5
                pause 1
                jump s030

    jump s001

label s001:
    $ save_name = "◇成为了二年级生"

    #♂MP01
    play music "bgm/bgm01.ogg" fadein 1.0


    #**青空
    scene bg42a
    with fade



    window show



    "升入二年级后，我依然当选了班长。"
    "妈妈那令人棘手的再婚事件姑且算是解决了。"
    "不知不觉间季节交替，从春天进入了初夏。"
    "换上了更加轻薄的衣物，6月的轻风中已经感觉不到凉爽。"
    "我安昙璃纱与心爱的恋人绫濑美夜，过着一如既往的每一天。"


    #**新校舎廊下・昼
    scene bg05a
    with dissolve



    show risa tri08s2
    with dissolve



    voice "RISA_0000"
    risa "「美夜真是的……又跑到哪里去了？」"
    "这句话我到底重复过多少遍啊。"
    "哎，人生总计貌似已经说过有1000次了吧……"
    "这样想着，今天我也在一边发着牢骚一边四处寻找美夜。"
    voice "RISA_0001"
    risa "「虽说春天的时候因为讨厌花粉和粉尘，她大多数时间都会在画室……所以找起来很轻松」"
    "但最近美夜的翘课地点也跟随季节在变化。"
    "比起你追我赶，这更像是在捉迷藏吧。"

    show risa tri02s2

    voice "RISA_0002"
    risa "「都这年纪了还和恋人玩捉迷藏……噗噗」"
    "不觉间笑了出来。"
    "还真是悠闲的语调呢。"


    show risa tri04s2

    voice "RISA_0003"
    risa "「……呀！？」"


    show risa tri03s2

    "突然间觉察到周围的视线，我巡视着四周。"
    "不小心就傻笑了起来……应该没被人看见吧？"


    show risa tri01s2

    voice "RISA_0004"
    risa "「……咳咳，啊，嗯，接下来……去中庭找找吧？」"
    "真是……恋人什么的不自觉地就脱口而出了。"
    "虽然很喜欢美夜……但在他人面前还是很羞涩。"


    show risa tri03s2

    voice "RISA_0005"
    risa "「告诉美夜的话肯定会被说事到如今还说这种话……」"
    "不过，在和美夜正式确立关系前，就已经被同学们想当然的选作了最佳情侣。"
    "大概在大家眼中完全就是一副情侣的样子吧。"


    show risa tri05s2

    voice "RISA_0006"
    risa "「虽然那时曾拼命否认过情侣关系……可现在已经完全是」"
    "完全是相思相爱的情侣了。"
    "昨天美夜也到我家里来玩……"
    "一想到那会儿发生的事情，脸颊便开始发烫。"

    voice "RISA_0007"
    risa "「啊，真热……嗯，今天温度好像挺高的，美夜果然会在室外吧」"
    "我轻拍脸颊，仰起头向中庭走去。"



    #**中庭・昼
    scene bg21a
    with fade



    show risa tri03s2
    with dissolve



    voice "RISA_0008"
    risa "「长椅上没见着……也就是说不在这里啊」"
    "那么，接下来美夜还有可能去的地方是……"


    show risa tri01s2

    voice "RISA_0009"
    risa "「会在树荫一带么，那边又凉快又舒服啊」"
    "偶尔会跟低年级的学生擦肩而过。"
    "身着全新夏季制服的她们，在看见我后急忙低头行礼。"
    "遇到此类情况，就不禁生出我们已是高年级学生的自觉。"
    "在刚当选最佳情侣，参与活动实行委员会工作的时候，我们还曾是最低年级的成员。"
    "现在轮到我们被后辈们信赖了。"
    voice "RISA_0010"
    risa "「虽然跟完美主义的雫大人，或是米卡女的偶像优菜大人相比还遥不可及」"
    "能够变成那样就好了呢……嗯，要继续努力。"
    "身边就有如此完美的榜样，我还得拼命加油才行。"


    show risa tri03s2

    voice "RISA_0011"
    risa "「麻衣大人也非常认真可靠……玲绪大人的话……还是一如既往的可爱吧？」"
    "虽然这句微妙的变成了疑问语气。"
    "『最佳情侣』们的每个人都依然精神十足。"
    "虽然最近没什么活动所以比之前聚会次数要少了……"


    show risa tri01s2

    voice "RISA_0012"
    risa "「不过偶尔会举办茶会，爱丽丝大人和雫大人也会过来玩」"
    "二人毕业后，最初其实觉得有点寂寞。"
    "现在她们只要有空就会过来露面，所以非常开心。"
    voice "RISA_0013"
    risa "「……虽然年级变了，可大家都还是老样子啊」"
    "当然也包括我和美夜。"
    "我一如既往的在继续找寻翘课狂魔美夜。"


    show risa tri03s2

    voice "RISA_0014"
    risa "「唔……也没在这里」"
    "预料的地点并没有出现美夜的身影。"


    show risa tri04s2

    voice "RISA_0015"
    risa "「哈……难道说推测到了我会去的地点，一直在移动吗！？」"
    "有可能，很可能就是这样。"
    "以前美夜也曾干过隐藏自己气息，一直悄悄跟着我这种事。"


    show risa tri03s2


    voice "RISA_0016"
    risa "「呜呜，那不是根本找不到了嘛」"
    voice "mobJyosiA0000"
    girl_a "「……然后啊，关于最佳情侣……」"
    voice "RISA_0017"
    risa "「……诶？」"
    "在树荫下，突然听到不知何处飘来的谈话声。"
    "说到『最佳情侣』这个词，第一反应就觉得是在讲关于我们的事情。"


    show risa tri01s2


    voice "RISA_0018"
    risa "「在说话的好像是……一年级学生啊」"
    "我的身体正好被树木所遮挡，所以她们似乎看不见我。"
    "声音并没有停止，对话还在继续。"
    "内容全都听得一清二楚。"
    "这可不是在偷听，是声音自己传过来的嘛。"
    "我一边这么告诉自己一边竖起了耳朵。"
    voice "mobJyosiA0001"
    girl_a "「去年举办了最佳情侣的活动，你有听说过吗？」"
    voice "mobJyosiB0000"
    girl_b "「嗯，当然了，在一年级学生里早已人尽皆知了吧」"
    voice "mobJyosiA0002"
    girl_a "「圣诞节、情人节……举行了超棒的庆典，都变成传说了~」"



    show risa tri03s2

    voice "RISA_0019"
    risa "「传，传说什么的……」"
    "明明只是几个月前的事而已。"
    "看来在她们之间已经被传得很夸张了。"
    voice "mobJyosiB0001"
    girl_b "「最佳情侣投票的时候气氛貌似相当热烈」"
    voice "mobJyosiC0000"
    girl_c "「啊啊，那时我们要是也在场就好了」"
    voice "mobJyosiA0003"
    girl_a "「大家都这么觉得……于是我想啊，我们也来推选就行了」"
    voice "mobJyosiB0002"
    girl_b "「推选……是指什么？」"
    voice "mobJyosiA0004"
    girl_a "「一年级生的『最佳情侣』哦」"
    voice "RISA_0020"
    risa "「诶………………推选？」"
    "我听得越发入迷了。"
    "也就是说一年级学生们也要选出自己的『最佳情侣』吧。"
    voice "mobJyosiB0003"
    girl_b "「太棒了，我们自己推选最佳情侣的话……果然应该是那两位吧」"
    voice "mobJyosiA0005"
    girl_a "「是啊，一定是那两位哟」"
    voice "mobJyosiC0001"
    girl_c "「在我们班也相当受欢迎」"
    "虽然我并不知道『那两位』是谁。"
    "显然应该是她们的本命吧。"
    voice "RISA_0021"
    risa "「去年的我也一定是像这样当选上的……」"
    "虽然年级不同，但大家的想法貌似都一样。"
    "要说起这个共通点，大概算是米卡女的特色吧。"



    #//ＳＥ　チャイムの音
    #♀SE001
    play sound "se/se001.ogg"


    voice "mobJyosiA0006"
    girl_a "「啊啦，休息时间这就结束了」"
    voice "mobJyosiB0004"
    girl_b "「下节课是在移动教室呢……赶紧走吧」"
    "嘴上催促着，她们却依然淡定地缓步向教学楼方向走去。"
    "虽然没能找到美夜，可我也必须回教室了。"


    show risa tri01s2

    voice "RISA_0022"
    risa "「新的一年级最佳情侣啊……会是什么样的人当选呢」"
    "稍微……不，相当在意啊。"


    #**暗転
    stop voice
    window hide


    stop music fadeout 2.0
    scene black  with fade2
    pause 1

    jump s002
