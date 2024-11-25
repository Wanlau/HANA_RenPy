init python:

    cg_list = [('ev01',), ('ev01p1',), ('ev01p2',), ('ev02',), ('ev02p1',), ('ev02p2',), ('ev03',), ('ev03p1',), ('ev03p2',), ('ev04',), ('ev04p1',), ('ev04p2',), ('ev05',), ('ev05p1',), ('ev05p2',), ('ev06',), ('ev06p1',), ('ev06p2',), ('ev07',), ('ev07p1',), ('ev07p2',), ('ev08',), ('ev08p1',), ('ev08p2',), ('ev09',), ('ev09p1',), ('ev09p2',), ('ev10',), ('ev10p1',), ('ev10p2',), ('ev11',), ('ev11p1',), ('ev12',), ('ev12p1',), ('ev12p2',), ('ev13',), ('ev13p1',), ('ev14',), ('ev14p1',), ('ev14p2',), ('ev15',), ('ev15p1',), ('ev16',), ('ev16p1',), ('ev17',), ('ev17p1',), ('ev18',), ('ev18p1',), ('ev19',), ('ev19p1',), ('ev20',)]
    for i in cg_list:
        if i in persistent._seen_images:
            persistent._seen_images[i] = True
        else:
            persistent._seen_images.setdefault(i,True)  


    persistent.Replay01 = True
    persistent.Replay02 = True
    persistent.Replay03 = True
    persistent.Replay04 = True
    persistent.Replay05 = True
    persistent.Replay06 = True
    persistent.Replay07 = True
    persistent.Replay08 = True
    