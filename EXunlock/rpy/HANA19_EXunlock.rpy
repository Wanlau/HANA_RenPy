init python:

    cg_list = [('cu01',), ('cu02',), ('cu03',), ('cu04',), ('cu04p1',), ('cu05',), ('cu06',), ('cu07',), ('cu08',), ('cu08p1',), ('cu09',), ('cu10',), ('cu10p1',), ('cu11',), ('cu12',), ('cu12p1',), ('cu13',), ('cu14',), ('cu15',), ('ev01',), ('ev01p1',), ('ev02',), ('ev02p1',), ('ev03',), ('ev03p1',), ('ev03p2',), ('ev04',), ('ev04p1',), ('ev05',), ('ev05p1',), ('ev06',), ('ev06p1',), ('ev07',), ('ev07p1',), ('ev07p2',), ('ev07p3',), ('ev08',), ('ev08p1',), ('ev09',), ('ev09p1',), ('ev10',), ('ev10p1',), ('ev10p2',), ('ev11',), ('ev11p1',), ('ev12',), ('ev12p1',), ('ev13',), ('ev13p1',), ('ev13p2',), ('ev14',), ('ev14p1',), ('ev14p2',), ('ev15',), ('ev15p1',), ('ev16',), ('ev16p1',), ('ev17',), ('ev17p1',), ('ev18',), ('ev18p1',), ('ev19',), ('ev19p1',), ('ev20',), ('ev20p1',), ('ev21',), ('ev21p1',), ('ev22',), ('ev22p1',), ('ev23',), ('ev23p1',), ('ev24',), ('ev24p1',), ('ev25',), ('ev25p1',), ('ev25p2',), ('ev26',), ('ev26p1',), ('ev27',), ('ev27p1',), ('ev28',), ('ev28p1',), ('ev29',), ('ev29p1',), ('ev29p2',), ('ev30',), ('ev30p1',), ('ev31',), ('ev31p1',), ('ev31p2',), ('ev32',), ('ev32p1',), ('ev32p2',), ('ev33',), ('ev33p1',), ('ev34',), ('ev34p1',), ('ev35',), ('ev35p1',), ('ev36',), ('ev36p1',), ('ev36p2',), ('ev37',), ('ev37p1',), ('ev38',), ('ev38p1',), ('ev39',), ('ev39p1',), ('ev40',), ('ev40p1',), ('ev40p2',), ('ev41',), ('ev41p1',), ('ev42',), ('ev42p1',), ('ev43',), ('ev43p1',), ('ev43p2',), ('ev43p3',), ('ev44',), ('ev44p1',), ('ev44p2',), ('ev45',), ('ev45p1',), ('ev45p2',), ('ev46',), ('ev46p1',), ('ev46p2',), ('ev47',), ('ev47p1',), ('ev47p2',), ('ev47p3',), ('ev47p4',), ('ev48',), ('ev48p1',), ('ev48p2',), ('ev48p3',), ('ev49',), ('ev49p1',), ('ev50',), ('ev50p1',), ('ev51',), ('ev51p1',), ('ev52',), ('ev52p1',), ('ev53',), ('ev54',), ('ev54p1',), ('ev55',), ('ev55p1',), ('ev55p2',), ('ev56',), ('ev56p1',), ('ev56p2',), ('ev57',), ('ev57p1',), ('ev57p2',), ('ev58',), ('ev58p1',), ('ev58p2',), ('ev59',), ('ev59p1',), ('ev60',), ('ev60p1',)]
    for i in cg_list:
        if i in persistent._seen_images:
            persistent._seen_images[i] = True
        else:
            persistent._seen_images.setdefault(i,True)  


    persistent.replays = [
        'H1', 'H2', 'H3', 'H4', 'H5', 'H6',
        'A1', 'A2', 'A3', 'A4', 'A5',
        'N1', 'N2', 'N3', 'N4', 'N5', 'N6',
    ]
    