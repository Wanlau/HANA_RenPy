init -1 python:

    cg_list = [('bg', 'story01a',), ('bg', 'story01b',), ('bg', 'story02a',), ('bg', 'story02b',), ('bg', 'story03a',), ('bg', 'story03b',), ('bg', 'story03c',), ('bg', 'story04a',), ('bg', 'story05a',), ('bg', 'story05b',), ('bg', 'story06a',), ('bg', 'story06b',), ('bg', 'story07a',), ('bg', 'story07b',), ('bg', 'story08a',), ('bg', 'story08b',), ('bg', 'story09a',), ('bg', 'story09b',), ('bg', 'story10a',), ('bg', 'story11a',), ('bg', 'story11b',), ('bg', 'story12a',), ('bg', 'story13a',), ('bg', 'story13b',), ('bg', 'story13c',), ('bg', 'story14a',), ('bg', 'story14b',), ('bg', 'story15a',), ('bg', 'story15b',), ('bg', 'story16a',), ('bg', 'story16b',), ('bg', 'story17a',), ('bg', 'story18a',), ('bg', 'story18b',), ('bg', 'story19a',), ('bg', 'story20a',), ('bg', 'story20b',)]
    for i in cg_list:
        if i in persistent._seen_images:
            persistent._seen_images[i] = True
        else:
            persistent._seen_images.setdefault(i,True)  

    ## 本作中下列数据与回想解锁无关
    persistent.replay1 = True
    persistent.replay2 = True
    persistent.replay3 = True
    persistent.replay4 = True
    persistent.replay5 = True
    persistent.replay6 = True
    persistent.replay7 = True
    persistent.replay8 = True
    persistent.replay9 = True
    
    ## 当回想页面的函数Replay()的入参locked值为None时，需要以_seen_ever解锁。
    scene_list = ['replay1', 'replay2', 'replay3', 'replay4', 'replay5', 'replay6', 'replay7', 'replay8', 'replay9', ]
    for i in scene_list:
        if i in persistent._seen_ever:
            persistent._seen_ever[i] = True
        else:
            persistent._seen_ever.setdefault(i,True) 