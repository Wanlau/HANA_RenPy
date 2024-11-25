init python:

    cg_list = [('cu01',),('cu01p1',),('cu02',),('cu02p1',),('cu03',),('endcut',),('ev01',),('ev01p1',),('ev02',),('ev03',),('ev03p1',),('ev04',),('ev04p1',),('ev05',),('ev05p1',),('ev05p2',),('ev06',),('ev06p1',),('ev06p2',),('ev07',),('ev08',),('ev08p1',),('ev09',),('ev10',),('ev11',),('ev12',),('ev12p1',),('ev13',),('ev13p1',),('ev14',),('ev14p1',),('ev14p2',),('ev14p3',),('ev15',),('ev15p1',),('ev16',),('ev16p1',),('ev16p2',),('ev16p3',),('ev17',),('ev17p1',),('ev17p2',),('ev18',),('ev18p1',),('ev18p2',),('ev19',),('ev19p1',),('ev19p2',),('ev19p3',),('ev20',),('ev20p1',)]
    for i in cg_list:
        if i in persistent._seen_images:
            persistent._seen_images[i] = True
        else:
            persistent._seen_images.setdefault(i,True)  


    persistent.Ending = True
    persistent.Replay1 = True
    persistent.Replay2 = True
    persistent.Replay3 = True
    persistent.Replay4 = True
    persistent.Replay5 = True
    persistent.Replay6 = True
    persistent.Replay7 = True
    persistent.Replay8 = True
    persistent.Replay9 = True
    persistent.Replay10 = True
    persistent.Replay11 = True
    