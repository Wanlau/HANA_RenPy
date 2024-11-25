init -1 python:

    cg_list = [('CU01',), ('CU02',), ('CU03',), ('EV001',), ('EV001p1',), ('EV001p2',), ('EV002',), ('EV003',), ('EV003p1',), ('EV004',), ('EV004p1',), ('EV004p2',), ('EV005',), ('EV005p1',), ('EV005p2',), ('EV006',), ('EV006p1',), ('EV006p2',), ('EV007',), ('EV007p1',), ('EV007p2',), ('EV007p3',), ('EV008',), ('EV008p1',), ('EV009',), ('EV009p1',), ('EV009p2',), ('EV010',), ('EV010p1',), ('EV011',), ('EV011p1',), ('EV011p2',), ('EV011p3',), ('EV012',), ('EV012p1',), ('EV012p2',), ('EV013',), ('EV013p1',), ('EV014',), ('EV014p1',), ('EV015',), ('EV015p1',), ('EV015p2',), ('EV016',), ('EV016p1',), ('EV017',), ('EV017p1',), ('EV017p2',), ('EV017p3',), ('EV018',), ('EV018p1',), ('EV019',), ('EV020',), ('EV020p1',)]
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
    persistent.replay10 = True
