# rollhed1：六夏&沙雪线
# roll_2：璃纱&美夜线
# roll_3：七海&优菜线
# roll_4：纱良&枫线
# roll_5：玲绪&麻衣线

#skipoff
#wipecancel disabled
#waitcancel disabled
# 以上代码通过向Ren'py引擎作者反馈，已经实现了功能的开启与关闭，此功能包含在最新的每夜版引擎中。
# Statements above was realized by feedback to the author of Ren'py and contained in the latest nightly.

label staffroll:
$ _skipping = False
$ _dismiss_pause = False
# 以上两行变量即对应skipoff与waitcancel，dismiss_pause同时包含wipecancel。
scene black
with dis3


#if f2==1 roll_1
#if f2==2 roll_2
#if f2==3 roll_3
#if f2==4 roll_4
#if f2==5 roll_5
if rikka_route:
 jump rollhed1
if risa_route:
 jump rollhed2
if nanami_route:
 jump rollhed3
if sara_route:
 jump rollhed4
if reo_route:
 jump rollhed5

label rollhed1:
menu:
 "观看制作人员列表":
  jump rollhed1start
 "跳过制作人员列表":
  jump rollend


label rollhed1start:

play music "sound/bgm25.ogg"


scene white
with dis7

scene image "image/sr01.png"
with dis5
pause 7

scene white
with dis3

scene image "image/sr02_1.png"
with dis3
pause 5

scene white
with dis3


scene image "image/sr03_1.png"
with dis3
pause 5

scene white
with dis3


scene image "image/sr04_1.png"
with dis3
pause 5

scene white
with dis3


scene image "image/sr05_1.png"
with dis3
pause 5

scene white
with dis3


scene image "image/sr06_1.png"
with dis3
pause 5

scene white
with dis3


scene image "image/sr07.png"
with dis3
pause 5

scene white
with dis3


scene image "image/sr08.png"
with dis3
pause 5

scene white
with dis3


scene image "image/sr11_1.png"
with dis3
pause 5

scene white
with dis3


scene image "image/sr12_1.png"
with dis3
pause 5

scene white
with dis3


scene image "image/sr13_1.png"
with dis3
pause 5

scene white
with dis3


scene image "image/sr14_1.png"
with dis3
pause 5

scene white
with dis3


scene image "image/sr15_1.png"
with dis3
pause 5

scene white
with dis3


scene image "image/sr16_1.png"
with dis3
pause 5

scene white
with dis3


scene image "image/sr17_1.png"
with dis3
pause 5

scene white
with dis3


scene image "image/sr18_1.png"
with dis3
pause 5

scene white
with dis3


scene image "image/sr19.png"
with dis3
pause 12


stop music fadeout 5.0

scene black
with dis5

jump rollend

 
label rollhed2:
menu:
 "观看制作人员列表":
  jump rollhed2start
 "跳过制作人员列表":
  jump rollend

label rollhed2start:

play music "sound/bgm25.ogg"


scene white
with dis7

scene image sr01
with dis5
pause 5

scene white
with dis3


scene image sr02_2
with dis3
pause 5

scene white
with dis3


scene image sr03_2
with dis3
pause 5

scene white
with dis3


scene image sr04_2
with dis3
pause 5

scene white
with dis3


scene image sr05_2
with dis3
pause 5

scene white
with dis3


scene image sr06_2
with dis3
pause 5

scene white
with dis3


scene image sr07
with dis3
pause 5

scene white
with dis3


scene image sr08
with dis3
pause 5

scene white
with dis3


scene image sr11_2
with dis3
pause 5

scene white
with dis3


scene image sr12_2
with dis3
pause 5

scene white
with dis3


scene image sr13_2
with dis3
pause 5

scene white
with dis3


scene image sr14_2
with dis3
pause 5

scene white
with dis3


scene image sr15_2
with dis3
pause 5

scene white
with dis3


scene image sr16_2
with dis3
pause 5

scene white
with dis3


scene image sr17_2
with dis3
pause 5

scene white
with dis3


scene image sr18_2
with dis3
pause 5

scene white
with dis3


scene image sr19
with dis3
pause 12


stop music fadeout 5.0

scene black
with dis5

#set s2 1

jump rollend


label rollhed3:
menu:
 "观看制作人员列表":
  jump rollhed3start
 "跳过制作人员列表":
  jump rollend


label rollhed3start:

play music "sound/bgm25.ogg"


scene white
with dis7

scene image sr01
with dis5
pause 5

scene white
with dis3


scene image sr02_3
with dis3
pause 5

scene white
with dis3


scene image sr03_3
with dis3
pause 5

scene white
with dis3


scene image sr04_3
with dis3
pause 5

scene white
with dis3


scene image sr05_3
with dis3
pause 5

scene white
with dis3


scene image sr06_3
with dis3
pause 5

scene white
with dis3


scene image sr07
with dis3
pause 5

scene white
with dis3


scene image sr08
with dis3
pause 5

scene white
with dis3


scene image sr11_3
with dis3
pause 5

scene white
with dis3


scene image sr12_3
with dis3
pause 5

scene white
with dis3


scene image sr13_3
with dis3
pause 5

scene white
with dis3


scene image sr14_3
with dis3
pause 5

scene white
with dis3


scene image sr15_3
with dis3
pause 5

scene white
with dis3


scene image sr16_3
with dis3
pause 5

scene white
with dis3


scene image sr17_3
with dis3
pause 5

scene white
with dis3


scene image sr18_3
with dis3
pause 5

scene white
with dis3


scene image sr19
with dis3
pause 12


stop music fadeout 5.0

scene black
with dis5


jump rollend


label rollhed4:
menu:
 "观看制作人员列表":
  jump rollhed4start
 "跳过制作人员列表":
  jump rollend


label rollhed4start:

play music "sound/bgm25.ogg"


scene white
with dis7

scene image sr01
with dis5
pause 5

scene white
with dis3


scene image sr02_4
with dis3
pause 5

scene white
with dis3


scene image sr03_4
with dis3
pause 5

scene white
with dis3


scene image sr04_4
with dis3
pause 5

scene white
with dis3


scene image sr05_4
with dis3
pause 5

scene white
with dis3


scene image sr06_4
with dis3
pause 5

scene white
with dis3


scene image sr07
with dis3
pause 5

scene white
with dis3


scene image sr08
with dis3
pause 5

scene white
with dis3


scene image sr11_4
with dis3
pause 5

scene white
with dis3


scene image sr12_4
with dis3
pause 5

scene white
with dis3


scene image sr13_4
with dis3
pause 5

scene white
with dis3


scene image sr14_4
with dis3
pause 5

scene white
with dis3


scene image sr15_4
with dis3
pause 5

scene white
with dis3


scene image sr16_4
with dis3
pause 5

scene white
with dis3


scene image sr17_4
with dis3
pause 5

scene white
with dis3


scene image sr18_4
with dis3
pause 5

scene white
with dis3


scene image sr19
with dis3
pause 12


stop music fadeout 5.0

scene black
with dis5


jump rollend

label rollhed5:
menu:
 "观看制作人员列表":
  jump rollhed5
 "跳过制作人员列表":
  jump rollend


label rollhed5start:

play music "sound/bgm25.ogg"


scene white
with dis7

scene image sr01
with dis5
pause 5

scene white
with dis3


scene image sr02_5
with dis3
pause 5

scene white
with dis3


scene image sr03_5
with dis3
pause 5

scene white
with dis3


scene image sr04_5
with dis3
pause 5

scene white
with dis3


scene image sr05_5
with dis3
pause 5

scene white
with dis3


scene image sr06_5
with dis3
pause 5

scene white
with dis3


scene image sr07
with dis3
pause 5

scene white
with dis3


scene image sr08
with dis3
pause 5

scene white
with dis3


scene image sr11_5
with dis3
pause 5

scene white
with dis3


scene image sr12_5
with dis3
pause 5

scene white
with dis3


scene image sr13_5
with dis3
pause 5

scene white
with dis3


scene image sr14_5
with dis3
pause 5

scene white
with dis3


scene image sr15_5
with dis3
pause 5

scene white
with dis3


scene image sr16_5
with dis3
pause 5

scene white
with dis3


scene image sr17_5
with dis3
pause 5

scene white
with dis3


scene image sr18_5
with dis3
pause 5

scene white
with dis3


scene image sr19
with dis3
pause 12


stop music fadeout 5.0

scene black
with dis5

jump rollend


label rollend:
$ _skipping = True
$ _dismiss_pause = True
return
