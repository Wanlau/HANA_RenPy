################################################################################
#   Language picker menu
################################################################################
screen language_menu():
    tag menu
    if renpy.loadable('images/gui/menu_sub_bg.png'):
        add 'images/gui/menu_sub_bg.png'
    else:
        add 'images/gui/menu_bg.png'

    window:
        style 'language_window'

        vbox:
            style 'menu'
            spacing 20

            button:
                action If(persistent.language_set, true = Language('Japanese'), false = [Language('Japanese'), Hide('language_menu', transition=dissolve), Return()])
                text '{font=fonts/Adobe Heiti Std R.ttf}日本語{/font}' size 20 pos (250, 21) style 'lang_text'
                style 'lang_button'

                if persistent.language_set:
                    selected_background 'images/gui/choice_hover.png'

            button:
                action If(persistent.language_set, true = Language(None), false = [Language(None), Hide('language_menu', transition=dissolve), Return()])
                text '{font=fonts/Tuffy-Regular.ttf}English{/font}' size 22 pos (250, 21) style 'lang_text'
                style 'lang_button'

                if persistent.language_set:
                    selected_background 'images/gui/choice_hover.png'
            button:
                action If(persistent.language_set, true = Language('Polish'), false = [Language('Polish'), Hide('language_menu', transition=dissolve), Return()])
                text '{font=fonts/Tuffy-Regular.ttf}Polski{/font}' size 22 pos (250, 21) style 'lang_text'
                style 'lang_button'

                if persistent.language_set:
                    selected_background 'images/gui/choice_hover.png'

            button:
                action If(persistent.language_set, true = Language('Chinese'), false = [Language('Chinese'), Hide('language_menu', transition=dissolve), Return()])
                text '{font=fonts/Tuffy-Regular-CN.ttf}中文{/font}' size 22 pos (250, 21) style 'lang_text'
                style 'lang_button'

                if persistent.language_set:
                    selected_background 'images/gui/choice_hover.png'

    if persistent.language_set:
        use back_button(660, 500, buttonAction=[Show('options', transition=Dissolve(0.3)), Hide('language_menu')])

        key 'cancel_action' action Return()

style language_window:
    align(0.5, 0.5)

style lang_text:
    anchor(0.5, 0.5)
    color '#FFF'
    outlines [(0, (0, 0, 0, 90), 1.5, 1), (0, (0, 0, 0, 45), 2, 1), (0, (0, 0, 0, 45), 2, 1.5)]

style lang_button:
    idle_background 'images/gui/choice_idle.png'
    hover_background 'images/gui/choice_hover.png'
    xysize(500, 40)