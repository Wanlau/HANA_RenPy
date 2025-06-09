init python:

    cg_list = [('CU01',), ('CU02',), ('CU03',), ('CU03p1',), ('EV01',), ('EV01p1',), ('EV02',), ('EV02p1',), ('EV03',), ('EV04',), ('EV04p1',), ('EV05',), ('EV05p1',), ('EV06',), ('EV07',), ('EV07p1',), ('EV08',), ('EV08p1',), ('EV09',), ('EV10',), ('EV11',), ('EV12',), ('EV12p1',), ('EV13',), ('EV13p1',), ('EV14',), ('EV15',), ('EV16',), ('EV16p1',), ('EV17',), ('EV17p1',), ('EV18',), ('EV19',), ('EV20',)] 
    for i in cg_list:
        persistent._seen_images[i] = True
