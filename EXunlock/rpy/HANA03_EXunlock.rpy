init -1 python:

    cg_list = [('CU04',), ('CU05',), ('CU06',), ('EV021',), ('EV022',), ('EV022p1',), ('EV023',), ('EV023p1',), ('EV023p2',), ('EV024',), ('EV024p1',), ('EV025',), ('EV025p1',), ('EV026',), ('EV026p1',), ('EV026p2',), ('EV027',), ('EV028',), ('EV028p1',), ('EV028p2',), ('EV029',), ('EV029p1',), ('EV030',), ('EV031',), ('EV031p1',), ('EV032',), ('EV032p1',), ('EV033',), ('EV033p1',), ('EV034',), ('EV034p1',), ('EV034p2',), ('EV035',), ('EV035p1',), ('EV036',), ('EV036p1',), ('EV037',), ('EV037p1',), ('EV038',), ('EV038p1',), ('EV038p2',), ('EV039',), ('EV040',)]
    for i in cg_list:
        if i in persistent._seen_images:
            persistent._seen_images[i] = True
        else:
            persistent._seen_images.setdefault(i,True)  

    persistent.replay1 = True
    persistent.replay2 = True
    persistent.replay3 = True
    persistent.replay4 = True
    persistent.replay5 = True
    persistent.replay6 = True
    persistent.replay7 = True
    persistent.replay8 = True
