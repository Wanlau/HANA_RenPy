init python:

    cg_list = [('CU01',), ('CU01p1',), ('CU02',), ('CU02p1',), ('CU03',), ('EV01',), ('EV01p1',), ('EV02',), ('EV02p1',), ('EV03',), ('EV03p1',), ('EV04',), ('EV04p1',), ('EV05',), ('EV05p1',), ('EV06',), ('EV06p1',), ('EV07',), ('EV07p1',), ('EV07p2',), ('EV08',), ('EV08p1',), ('EV09',), ('EV10',), ('EV10p1',), ('EV11',), ('EV11p1',), ('EV11p2',), ('EV12',), ('EV12p1',), ('EV12p2',), ('EV13',), ('EV13p1',), ('EV14',), ('EV14p1',), ('EV14p2',), ('EV15',), ('EV15p1',), ('EV16',), ('EV16p1',), ('EV17',), ('EV17p1',), ('EV18',), ('EV18p1',), ('EV18p2',), ('EV19',), ('EV19p1',), ('EV19p2',), ('EV19p3',), ('EV20',)]
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
    persistent.replay9 = True
    