################################################################################
#   Notifications menu
################################################################################
screen notify(message):
    zorder 100

    window:
        at _notify_transform
        style 'notify_box'

        text message style 'notify_message'

    # Time which must elapse to hide message
    timer 3.25 action Hide('notify')

style notify_message:
    outlines [(0, (0, 0, 0, 90), 1.5, 1), (0, (0, 0, 0, 45), 2, 1), (0, (0, 0, 0, 45), 2, 1.5)]

# English notifications style
translate None style notify_message:
    size 22
    font 'fonts/Tuffy-Regular.ttf'

# Polish notifications style
translate Polish style notify_message:
    size 22
    font 'fonts/Tuffy-Regular.ttf'

# Japanese notifications style
translate Japanese style notify_message:
    size 20
    font 'fonts/Adobe Heiti Std R.ttf'

# Chinese notifications style
translate Chinese style notify_message:
    size 20
    font 'fonts/Tuffy-Regular-CN.ttf'

style notify_box:
    ypos 8
    background Frame(Crop((17, 5, 678, 170), 'images/gui/window.png'), 0, 12, 12, 12)
    padding(18, 10)

transform _notify_transform:
    on show:
        xanchor 1.0
        linear 0.25 xanchor 0.0
    on hide:
        linear 0.5 xanchor 1.0
