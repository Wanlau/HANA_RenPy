init -1 python:

    cg_list = [('CU01',), ('CU02',), ('CU03',), ('EV001',), ('EV002',), ('EV002p1',), ('EV003',), ('EV003p1',), ('EV003p2',), ('EV004',), ('EV005',), ('EV005p1',), ('EV005p2',), ('EV006',), ('EV007',), ('EV008',), ('EV009',), ('EV009p1',), ('EV010',), ('EV010p1',), ('EV011',), ('EV011p1',), ('EV011p2',), ('EV012',), ('EV012p1',), ('EV013',), ('EV014',), ('EV014p1',), ('EV015',), ('EV016',), ('EV016p1',), ('EV017',), ('EV017p1',), ('EV018',), ('EV019',), ('EV019p1',), ('EV020',)]
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
