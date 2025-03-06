################################################################################
#   Save and Load menu
################################################################################

### Save/Load slots ############################################################
screen file_picker(title):
    if renpy.loadable('images/gui/menu_sub_bg.png'):
        add 'images/gui/menu_sub_bg.png'
    else:
        add 'images/gui/menu_bg.png'
    add 'images/gui/saveload_[title]_title.png' align(0.0, 0.0)

    use back_button(670, 555)

    grid 2 7:
        pos(20, 70)
        xspacing 20
        yspacing 10
        transpose True

        for i in range(1, 15):
            button:
                xysize(370, 60)

                insensitive_background 'images/gui/saveload_slot_insensitive.png'
                idle_background 'images/gui/saveload_slot_idle.png'
                hover_background 'images/gui/saveload_slot_hover.png'
                selected_idle_background 'images/gui/saveload_slot_selected_idle.png'
                selected_hover_background 'images/gui/saveload_slot_selected_hover.png'

                action FileAction(i)
                add FileScreenshot(i) pos(8, 8)

                text _('No. ') + FileSlotName(i, 14) style 'save_number'
                text FileTime(i, format=_('%d/%m/%Y  %H:%M'), empty=('')) style 'save_date'
                text FileSaveName(i) style 'save_title'

                # Long press on touch screens to delete save
                if renpy.variant('touch'):
                    alternate FileDelete(i)

                key 'save_delete' action FileDelete(i)

    hbox:
        pos(608, 28)
        spacing 2

        for i in range(1, 6):
            imagebutton auto 'images/gui/btn_' + str(i) + '_%s.png' action FilePage(i)
            key 'page' + str(i) action FilePage(i)

    key 'cancel_action' action Return()
    key 'scroll_up' action FilePagePrevious(max=1, wrap=False, auto=False, quick=False)
    key 'scroll_down' action FilePageNext(max=5, wrap=False, auto=False, quick=False)

style file_picker_text:
    idle_color '#7e7e7e'
    idle_outlines[(0, '#000', 1, 1)]
    hover_color '#FFF'
    hover_outlines[(0, '#6045bc', 1, 1)]
    insensitive_color(92, 148, 251, 150)
    insensitive_outlines[(0, '#2d497c', 1, 1)]
    font 'fonts/Arial.ttf'

style save_number:
    take file_picker_text
    size 22
    pos(88, 3)

style save_date:
    take file_picker_text
    size 14
    xanchor 1.0
    pos(357, 9)

# General chapter name font size
style save_title:
    take file_picker_text
    size 16

# English chapter name position
translate None style save_title:
    font "fonts/Arial.ttf"
    pos(83, 32)

# Polish chapter name position
translate Polish style save_title:
    font "fonts/Arial.ttf"
    pos(83, 32)

# Japanese chapter name position
translate Japanese style save_title:
    font 'fonts/Adobe Heiti Std R.ttf'
    pos(75, 30)

# Chinese chapter name position
translate Chinese style save_title:
    font 'fonts/Tuffy-Regular-CN.ttf'
    pos(75, 30)


### Save screen ################################################################
screen save():
    tag menu
    use file_picker('save')


### Load screen ################################################################
screen load():
    tag menu
    use file_picker('load')
