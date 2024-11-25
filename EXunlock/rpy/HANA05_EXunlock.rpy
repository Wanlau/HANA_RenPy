init -1 python:

    cg_list = [('CU01',), ('CU02',), ('CU03',), ('EV001',), ('EV001p1',), ('EV001p2',), ('EV002',), ('EV002p1',), ('EV003',), ('EV004',), ('EV005',), ('EV005p1',), ('EV005p2',), ('EV006',), ('EV006p1',), ('EV007',), ('EV007p1',), ('EV008',), ('EV009',), ('EV009p1',), ('EV009p2',), ('EV010',), ('EV010p1',), ('EV011',), ('EV011p1',), ('EV012',), ('EV012p1',), ('EV013',), ('EV013p1',), ('EV013p2',), ('EV014',), ('EV015',), ('EV015p1',), ('EV016',), ('EV016p1',), ('EV017',), ('EV018',), ('EV018p1',), ('EV019',), ('EV019p1',), ('EV019p2',), ('EV020',), ('EV020p1',)]
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
