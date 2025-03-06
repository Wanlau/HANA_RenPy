################################################################################
#   Say screen
################################################################################

### Textbox ####################################################################
screen say(who, what):
    window:
        id 'window'

        if who is not None:

            window:
                id 'namebox'
                text who id 'who'

        text what id 'what'

    use quick_menu

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style say_window:
    align(0.5, 1.0)
    xysize(800, 180)
    right_padding 130
    left_padding 38
    top_padding 10
    background 'images/gui/window.png'

style say_label:
    outlines [(1, (0, 0, 0, 30), 2.5, 1.5), (1.5, (0, 0, 0, 45), 2.5, 1.5), (2, (0, 0, 0, 60), 2.5, 1.5), (2, (255, 255, 255, 75)), (1.5, (255, 255, 255, 200)), (1, (255, 255, 255))]

style say_dialogue:
    outlines [(0, (0, 0, 0, 90), 1.5, 1), (0, (0, 0, 0, 45), 2, 1), (0, (0, 0, 0, 45), 2, 1.5)]

# English names and dialogues style
translate None style say_label:
    font 'fonts/Tuffy-Bold.ttf'
    size 27
    xpos 27
    ypos 3

translate None style say_dialogue:
    font 'fonts/Tuffy-Regular.ttf'
    size 23
    ypos 43

# Polish names and dialogues style
translate Polish style say_label:
    font 'fonts/Tuffy-Bold.ttf'
    size 27
    xpos 27
    ypos 3

translate Polish style say_dialogue:
    font 'fonts/Tuffy-Regular.ttf'
    size 23
    ypos 43

# Japanese names and dialogues style
translate Japanese style say_label:
    font 'fonts/Adobe Heiti Std R.ttf'
    size 25
    xpos 27
    ypos 3

translate Japanese style say_dialogue:
    font 'fonts/Adobe Heiti Std R.ttf'
    line_spacing 3
    size 23
    ypos 43

# Chinese names and dialogues style
translate Chinese style say_label:
    font 'fonts/Homizio-bold.ttf'
    size 25
    xpos 27
    ypos 3

translate Chinese style say_dialogue:
    font 'fonts/Tuffy-Regular-CN.ttf'
    line_spacing 3
    size 23
    ypos 43
