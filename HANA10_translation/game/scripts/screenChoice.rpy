################################################################################
#   Choice menu
################################################################################
screen choice(items):
    window:
        style 'menu_window'

        vbox:
            style 'menu'
            spacing 20

            for n, i in enumerate(items, 1):
                button:
                    action i.action
                    style 'menu_choice_button'
                    text i.caption style 'menu_choice_text'
                    at menu_choice_animation(n)

                if n < 10:
                    key str(n) action i.action


style menu_window:
    spacing 20
    xalign 0.5
    ypos 190

style menu_choice_text:
    anchor(0.5, 0.5)
    color '#808080'
    hover_color '#635EFF'
    selected_color '#FF5EE6'
    outlines [(1, (0, 0, 0, 30), 2.5, 1.5), (1.5, (0, 0, 0, 45), 2.5, 1.5), (2, (0, 0, 0, 60), 2.5, 1.5), (2, (255, 255, 255, 75)), (1.5, (255, 255, 255, 200)), (1, (255, 255, 255))]

# English choices menu
translate None style menu_choice_text:
    font 'fonts/Tuffy-Bold.ttf'
    size 21
    pos(250, 20)

# Polish choices menu
translate Polish style menu_choice_text:
    font 'fonts/Tuffy-Bold.ttf'
    size 21
    pos(250, 20)

# Japanese choices menu
translate Japanese style menu_choice_text:
    font 'fonts/Adobe Heiti Std R.ttf'
    size 20
    pos(250, 21)

# Chinese choices menu
translate Chinese style menu_choice_text:
    font 'fonts/Homizio-bold.ttf'
    size 20
    pos(250, 21)

style menu_choice_button:
    idle_background 'images/gui/choice_idle.png'
    hover_background 'images/gui/choice_hover.png'
    selected_background 'images/gui/choice_hover.png'
    xysize(500, 40)

# Menu choice animation
transform menu_choice_animation(delay):
    alpha 0.0
    ypos -50
    pause delay*0.12
    linear 0.25 alpha 1.0 ypos 0
