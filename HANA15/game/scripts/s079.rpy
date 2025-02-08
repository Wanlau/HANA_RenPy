label s079:
    $ save_name = "◇在活动委员会上等着你哦{font=Tuffy-Regular-EN.ttf}♡{/font}"
    
    
    #**委員会室・昼
    scene bg30a
    with fade
    
    
    
    window show
    
    
    #♂MP07
    play music "bgm/bgm07.ogg" fadein 1.0
    
    
    "从环境整备委员会引退后的姐姐大人，完全沉浸在了活动委员会里。"
    
    
    show yuuna tyu01s2 at c
    with dissolve
    
    
    
    voice "YUUNA_0439"
    yuuna "「那，这件事就我来办吧」"
    
    
    show yuuna tyu01s2 at l
    show risa tri02s2 at r
    with dissolve
    
    
    
    voice "RISA_1856"
    risa "「好的，拜托了。优菜大人在的话就以一敌百了啊。最近经常到这边来，帮大忙了」"
    
    
    show yuuna tyu02s2 at l
    
    
    
    voice "YUUNA_0440"
    yuuna "「呜呵呵，这么说我很开心哦。从环境整备委员会引退之后，在学校内要做的事情也完全没有了……」"
    voice "RISA_1857"
    risa "「这边倒是很感激啊」"
    
    
    show yuuna tyu01s2 at l
    
    
    
    voice "YUUNA_0441"
    yuuna "「不过，我闲下来的份，七海就必须得去补上了……呐？」"
    "唐突把话题转向了我，吓了一跳。"
    
    
    hide yuuna
    hide risa
    show nanami tna04s2 at c
    with dissolve
    
    
    
    voice "NANAMI0717"
    nanami "「诶？　啊，是啊」"
    
    
    show yuuna tyu03s2 at l
    show nanami tna04s2 at r
    with dissolve
    
    
    
    voice "YUUNA_0442"
    yuuna "「其实，把负担都加到七海身上了……」"
    
    
    show nanami tna01s2 at r
    
    
    
    voice "NANAMI0718"
    nanami "「完全没有啊。活动委员会和环境整备委员会两方的调和，优菜大人不也处理得很好吗」"
    voice "YUUNA_0443"
    yuuna "「虽然是这样〜引退之后，我就不能在环境整备委员会和七海碰面了……」"
    voice "NANAMI0719"
    nanami "「不不，但是在这边的委员会能见面啊」"
    voice "YUUNA_0444"
    yuuna "「但是啊〜〜七海很忙啊，也不常在这边呆着啊？」"
    
    
    show nanami tna03s2 at r
    
    
    
    voice "NANAMI0720"
    nanami "「这、这话倒是真的……」"
    voice "YUUNA_0445"
    yuuna "「七海也是，和我分开，很寂寞吧〜？」"
    
    
    show nanami tna04s2 at r
    
    
    
    voice "NANAMI0721"
    nanami "「在在在、在说什么啊」"
    
    
    show yuuna tyu02s2 at l
    
    
    
    voice "YUUNA_0446"
    yuuna "「不用勉强也可以哦〜来，乖乖{font=Tuffy-Regular-EN.ttf}♡{/font}」"
    "姐姐大人安抚着我的头，就好像顶级饲养员的手法一样。"
    "被当作宠物对待，我有点火大。"
    
    
    show nanami tna08s2 at r
    
    
    
    voice "NANAMI0722"
    nanami "「只是稍微不能与优菜大人见面，我完全、一点都不寂寞啊！」"
    voice "YUUNA_0447"
    yuuna "「真是的，嘴上这么说……对自己的心情要坦率哦〜」"
    "姐姐大人紧紧地抱住了我，在我脸上蹭来蹭去。"
    
    
    show nanami tna09s2 at r
    
    
    
    voice "NANAMI0723"
    nanami "「呀啊，优菜大人！！　众目睽睽之下！！　请住手啊啊〜〜！！」"
    voice "YUUNA_0448"
    yuuna "「我完〜全，不介意哦〜〜{font=Tuffy-Regular-EN.ttf}♪{/font}」"
    voice "NANAMI0724"
    nanami "「我和大家都会介意的〜〜！！」"
    
    
    hide yuuna
    hide nanami
    show risa tri03s2 at c
    with dissolve
    
    
    
    voice "RISA_1858"
    risa "「不不……七海同学，事到如今你还说什么……对吧？」"
    
    
    show sara tsa02s2 at l
    show risa tri03s2 at r
    with dissolve
    
    
    
    voice "SARA_0280"
    sara "「就是啊〜两个人一直都这么火热好羡慕啊。对吧，枫酱？」"
    
    
    show kaede tka03s2 at sl
    show sara tsa02s2 at c
    show risa tri03s2 at sr
    with dissolve
    
    
    
    voice "KAEDE_0140"
    kaede "「诶……诶诶，是啊……」"
    
    
    hide kaede
    hide sara
    hide risa
    show nanami tna03s2 at c
    with dissolve
    
    
    
    voice "NANAMI0725"
    nanami "「唔……唔唔……」"
    "大家是不是宽容过度了啊！？"
    "就算是米卡女校内公认的情侣……"
    
    
    
    #★★★選択肢　ここから
    
    
    
    voice "NANAMI0726"
    nanami "「优、优菜大人，在人前还是……」"
    
    
#++選択肢（３）
#１．『请不要粘过来！！』×
#２．『稍微控制一下吧』○
label select15:
    menu:
        nanami "「优、优菜大人，在人前还是……」{fast}"
        "请不要粘过来！！":
            jump select15_1
        "稍微控制一下吧":
            jump select15_2
    
    
#１．『请不要粘过来！！』×
label select15_1:
    
    
    show nanami tna07s2 at c
    
    
    
    voice "NANAMI0727"
    nanami "「在人前请不要粘过来。别人的目光很刺眼的」"
    
    
    show yuuna tyu03s2 at l
    show nanami tna07s2 at r
    with dissolve
    
    
    
    voice "YUUNA_0449"
    yuuna "「怎、怎么这样……好过分，太过分了。连靠近恋人的七海都不被允许，我……呜呜」"
    
    
    show nanami tna03s2 at r
    
    
    
    voice "NANAMI0728"
    nanami "「谁、谁也没有说那样的话啦……真是麻烦啦」"
    "优菜姐姐大人，真是让人无可奈何……"
    
    
    jump select15_end
    
    
#２．『稍微控制一下吧』○
label select15_2:
    
    
    voice "NANAMI0729"
    nanami "「稍微控制一下吧……拜托了」"
    
    
    show yuuna tyu03s2 at l
    show nanami tna03s2 at r
    
    
    
    voice "YUUNA_0450"
    yuuna "「既然七海说到这个份上……那我就稍微轻轻地摸一摸好了」"
    voice "NANAMI0730"
    nanami "「是吗，只是这个程度的话………………嗯？」"
    "但要是不谨慎一点的话，可能会比被抱住还麻烦。"
    "有感觉的时候，发出了奇怪的声音的话……啊哇哇。"
    
    
    #set f1 f1+1
    $ lily_rank += 1
    
    
#++選択肢終了
#★★★選択肢　ここまで
label select15_end:
    
    
    voice "NANAMI0731"
    nanami "「抱、抱歉……我差不多该走了」"
    "看了一眼时钟，已经是环境整备委员会要开始的时间了。"
    "身为委员长的我，委员会的时候迟到什么的，完全不行。"
    
    
    show yuuna tyu01s2 at l
    
    
    
    voice "YUUNA_0451"
    yuuna "「啊啦，是这样吗……今天也要加倍努力哦」"
    "被姐姐大人抱着就不能离开委员会了，我轻微地推开了紧抱着我的身体，姐姐大人很快就从我身上离开了。"
    "感觉她的那个态度，让我有些气馁。"
    
    
    hide yuuna
    show nanami tna03s2 at c
    with dissolve
    
    
    
    voice "NANAMI0732"
    nanami "「啊，好的……抱歉。帮忙只帮了一半……」"
    
    
    show risa tri01s2 at l
    show nanami tna03s2 at r
    with dissolve
    
    
    
    voice "RISA_1859"
    risa "「不要紧，不如说这么忙还能出面，谢谢了」"
    voice "NANAMI0733"
    nanami "「完全不要紧，我没怎么出力……」"
    voice "RISA_1860"
    risa "「不不，没有那回事，之后就交给我们吧」"
    
    
    show miya tmi01s2 at sl
    show risa tri01s2 at c
    show nanami tna03s2 at sr
    with dissolve
    
    
    
    voice "MIYA_1045"
    miya "「我一个人顶得上十个人，没关系的」"
    
    
    show risa tri03s2 at c
    
    
    
    voice "RISA_1861"
    risa "「美夜又来了……」"
    
    
    show nanami tna01s2 at sr
    
    
    
    voice "NANAMI0734"
    nanami "「１０人……那还真是厉害啊」"
    "这里就交给美夜同学了，我得抓紧时间。"
    
    
    hide miya
    hide risa
    hide nanami
    show yuuna tyu01s2 at c
    with dissolve
    
    
    
    voice "YUUNA_0452"
    yuuna "「七海……和我分开，会很寂寞吧？」"
    
    
    show yuuna tyu01s2 at l
    show nanami tna03s2 at r
    with dissolve
    
    
    
    voice "NANAMI0735"
    nanami "「哈？」"
    
    
    show yuuna tyu02s2 at l
    
    
    
    voice "YUUNA_0453"
    yuuna "「要是想见我的话，就尽快完成环境整备委员会的工作，来这边哦{font=Tuffy-Regular-EN.ttf}♡{/font}」"
    voice "NANAMI0736"
    nanami "「什……什么……」"
    voice "YUUNA_0454"
    yuuna "「要是回来得早，我就给你一个大大的拥抱{font=Tuffy-Regular-EN.ttf}♡{/font}」"
    
    
    show nanami tna09s2 at r
    
    
    
    voice "NANAMI0737"
    nanami "「不、不用了！！」"
    voice "YUUNA_0455"
    yuuna "「不用客气啦〜」"
    voice "NANAMI0738"
    nanami "「才不是客气〜！！」"
    "姐姐大人在呵呵地笑着。"
    "恶作剧，这绝对，是在说着恶作剧。"
    "确实，和姐姐大人分开，很寂寞……"
    "但是又绝对不可能在委员会挖个洞。"
    
    
    show nanami tna01s2 at r
    
    
    
    voice "NANAMI0739"
    nanami "「但是，也想在这边帮忙……我会尽早回来的〜」"
    voice "YUUNA_0456"
    yuuna "「嗯嗯，慢走{font=Tuffy-Regular-EN.ttf}♡{/font}　早点回来哦〜」"
    "我充满留恋，离开了活动委员会的教室。"
    
    
    #**暗転
    window hide
    scene black
    with fade
    
    
    
    #**新校舎教室・昼
    scene bg04a
    with fade
    
    
    
    window show
    
    
    show nanami tna03s2 at c
    with dissolve
    
    
    
    voice "NANAMI0740"
    nanami "「……哈啊〜真是的……」"
    "我最近，经常思考。"
    "姐姐大人，形象转变是不是有点过度了啊！？"
    "这么想的，绝对不只是我一个。"
    
    
    #**青空
    scene bg42a
    with dissolve
    
    
    
    "于是，我向活动委员会的各位最佳情侣，打听最近的优菜姐姐大人的形象转变。"
    
    
    #**委員会室・昼
    scene bg30a
    with dissolve
    
    
    
    "取名为……『七海的突击采访！！』"
    
    
    show nanami tna01s2 at c
    with dissolve
    
    
    
    voice "NANAMI0741"
    nanami "「就是这样，关于最近的姐姐大人，大家怎么看？」"
    
    
    show nanami tna01s2 at l
    show risa tri01s2 at r
    with dissolve
    
    
    
    voice "RISA_1862"
    risa "「嗯……比以前是不是更加亲近了啊。更好说上话了呢」"
    
    
    hide risa
    show sara tsa02s2 at l
    show nanami tna01s2 at r
    with dissolve
    
    
    
    voice "SARA_0281"
    sara "「是啊是啊，坦诚的优菜大人，很好啊{font=Tuffy-Regular-EN.ttf}♡{/font}」"
    
    
    hide sara
    show kaede tka02s2 at l
    with dissolve
    
    
    
    voice "KAEDE_0141"
    kaede "「这样的优菜同学也很出色吧」"
    
    
    hide kaede
    show nanami tna01s2 at l
    show miya tmi01s2 at r
    with dissolve
    
    
    
    voice "MIYA_1046"
    miya "「忠实于欲望的人，我并不讨厌」"
    
    
    hide miya
    show reo tre01s2 at l
    show nanami tna01s2 at r
    with dissolve
    
    
    
    voice "REO_0210"
    reo "「松原优菜经常带点心来……没有恶意的人啊」"
    
    
    hide reo
    show mai tma01s2 at l
    with dissolve
    
    
    
    voice "MAI_0278"
    mai "「……真是有玲绪风格的见解啊。是呢，我也喜欢现在的优菜同学哦」"
    
    
    hide mai
    show nanami tna01s2 at l
    show rikka trk01s2 at r
    with dissolve
    
    
    
    voice "RIKKA_1615"
    rikka "「对后辈的我也是很明朗爽快……是很温柔的前辈」"
    
    
    hide rikka
    show sayuki tsy01s2 at r
    with dissolve
    
    
    
    voice "SAYUKI0894"
    sayuki "「是的，一直都很亲切地照顾关心着我，很是感激」"
    
    
    hide sayuki
    show nanami tna03s2 at c
    with dissolve
    
    
    
    voice "NANAMI0742"
    nanami "「唔唔〜……」"
    "关于姐姐大人的变化，大概都是好评……不如说，反而被大家广为接受了。"
    "当然，姐姐大人又漂亮，又聪明，人又好……作为一名女性该有的真善美全部都有。"
    "再加上亲近可人这点，也难怪印象会越来越好……"
    "虽然，我也很——清楚！！"
    voice "NANAMI0743"
    nanami "「算了，这样也好……」"
    "一直在别人面前接吻啊，袭胸啊，推倒啊，让我很不安……"
    
    
    #**暗転
    window hide
    scene black
    with fade
    
    
    
    #//七海の妄想
    
    #**新校舎教室・昼
    scene bg04a
    with fade    
    
    
    show moyan
    show yuuna tyu01s2 at c
    with dissolve
    
    window show
    
    voice "YUUNA_0457"
    yuuna "「那么大家……今天就让各位来看看我与七海实战的H〜」"
    
    
    show yuuna tyu01s2 at l
    show nanami tna04s2 at r
    with dissolve
    
    
    
    voice "NANAMI0744"
    nanami "「诶诶诶诶诶！？　不，不要啊，饶了我吧〜」"
    
    
    show yuuna tyu02s2 at l
    
    
    
    voice "YUUNA_0458"
    yuuna "「各位请仔细看清楚，沉浸在七海的可爱中吧。来，脱吧脱吧{font=Tuffy-Regular-EN.ttf}♪{/font}」"
    voice "NANAMI0745"
    nanami "「不行不行，会被大家看见的，不能脱啊啊啊」"
    
    
    show yuuna tyu01s2 at l
    with None
    show nanami tna04z at r
    with dissolve
    
    
    
    voice "YUUNA_0459"
    yuuna "「来，这就是被剥光的七海。然后再像这样，把双腿张开……」"
    voice "NANAMI0746"
    nanami "「不要啊啊啊！！」"
    
    
    show yuuna tyu02s2 at l
    
    
    
    voice "YUUNA_0460"
    yuuna "「然后然后，在可爱的私处的秘缝……像这样打开……嘿嘿{font=Tuffy-Regular-EN.ttf}♡{/font}」"
    
    
    show nanami tna05z at r
    
    
    
    voice "NANAMI0747"
    nanami "「大家拜托了，不要看啊，不要看啊啊啊，难为情{font=Tuffy-Regular-EN.ttf}♡{/font}」"
    
    
    #**暗転
    window hide
    scene black
    with fade
    
    
    
    #**新校舎教室・昼
    scene bg04a
    with fade
    
    
    
    window show
    
    
    show nanami tna03s2 at c
    with dissolve
    
    
    
    voice "NANAMI0748"
    nanami "「……这种事，绝对不要啊，唔唔唔」"
    "最近的姐姐大人，在别人面前，完全毫不犹豫，秀恩爱。"
    "照着这个势头发展下去，不知何时，说不定连刚才的妄想PLAY都会成真。"
    voice "NANAMI0749"
    nanami "「在别人面前H……在大家面前接吻什么的，度假的时候已经做过了呢」"
    "对恋人传说进行了实践，那个是……呃，大家都做了。"
    "现在在大家面前，虽然也是恩恩爱爱的感觉。"
    "有一种某天会进一步发展的预感。"
    voice "NANAMI0750"
    nanami "「啊啊……超不安的〜……」"
    "姐姐大人要是不向奇怪的方向暴走就好了……"
    "和以前完全不同意义上的担心，朝我不断袭来。"
    
    
    #**暗転
    stop voice
    window hide


    stop music fadeout 2.0
    scene black  with fade2
    pause 1

    jump s080
