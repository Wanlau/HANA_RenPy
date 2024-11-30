init python:

    cg_list = [('CU01',), ('CU02',), ('CU03',), ('CU04',), ('CU05',), ('CU06',), ('CU07',), ('CU08',), ('CU08p1',), ('CU09',), ('CU10',), ('CU11',), ('CU12',), ('CU13',), ('CU14',), ('CU15',), ('CU16',), ('CU17',), ('CU18',), ('CU19',), ('CU19p1',), ('CU20',), ('EV01',), ('EV01p1',), ('EV02',), ('EV02p1',), ('EV03',), ('EV04',), ('EV04p1',), ('EV05',), ('EV05p1',), ('EV06',), ('EV06p1',), ('EV07',), ('EV07p1',), ('EV08',), ('EV08p1',), ('EV09',), ('EV09p1',), ('EV10',), ('EV10p1',), ('EV11',), ('EV11p1',), ('EV12',), ('EV12p1',), ('EV12p2',), ('EV13',), ('EV13p1',), ('EV14',), ('EV14p1',), ('EV15',), ('EV15p1',), ('EV16',), ('EV16p1',), ('EV16p2',), ('EV17',), ('EV17p1',), ('EV17p2',), ('EV18',), ('EV18p1',), ('EV18p2',), ('EV19',), ('EV19p1',), ('EV20',), ('EV20p1',), ('EV20p2',), ('EV21',), ('EV21p1',), ('EV22',), ('EV22p1',), ('EV22p2',), ('EV22p3',), ('EV23',), ('EV23p1',), ('EV23p2',), ('EV24',), ('EV24p1',), ('EV25',), ('EV25p1',), ('EV25p2',), ('EV26',), ('EV27',), ('EV27p1',), ('EV28',), ('EV28p1',), ('EV29',), ('EV29p1',), ('EV30',), ('EV30p1',), ('EV30p2',), ('EV31',), ('EV31p1',), ('EV31p2',), ('EV32',), ('EV32p1',), ('EV32p2',), ('EV33',), ('EV33p1',), ('EV34',), ('EV34p1',), ('EV34p2',), ('EV35',), ('EV35p1',), ('EV36',), ('EV36p1',), ('EV37',), ('EV37p1',), ('EV37p2',), ('EV38',), ('EV38p1',), ('EV39',), ('EV39p1',), ('EV39p2',), ('EV40',), ('EV40p1',), ('EV41',), ('EV41p1',), ('EV42',), ('EV43',), ('EV44',), ('EV44p1',), ('EV45',), ('EV45p1',), ('EV45p2',), ('EV46',), ('EV46p1',), ('EV47',), ('EV47p1',), ('EV48',), ('EV48p1',), ('EV49',), ('EV49p1',), ('EV50',), ('EV50p1',), ('EV50p2',), ('EV51',), ('EV51p1',), ('EV51p2',), ('EV52',), ('EV52p1',), ('EV53',), ('EV53p1',), ('EV54',), ('EV54p1',), ('EV54p2',), ('EV55',), ('EV55p1',), ('EV56',), ('EV56p1',), ('EV56p2',), ('EV57',), ('EV57p1',), ('EV57p2',), ('EV58',), ('EV58p1',), ('EV58p2',), ('EV59',), ('EV59p1',), ('EV60',), ('EV60p1',), ('EV61',), ('EV61p1',), ('EV61p2',), ('EV62',), ('EV62p1',), ('EV63',), ('EV63p1',), ('EV64',), ('EV64p1',), ('EV64p2',), ('EV64p3',), ('EV65',), ('EV65p1',), ('EV65p2',), ('EV66',), ('EV66p1',), ('EV67',), ('EV67p1',), ('EV68',), ('EV68p1',), ('EV69',), ('EV69p1',), ('EV69p2',), ('EV70',), ('EV70p1',), ('EV71',), ('EV71p1',), ('EV71p2',), ('EV72',), ('EV72p1',), ('EV72p2',), ('EV73',), ('EV73p1',), ('EV74',), ('EV74p1',), ('EV75',), ('EV75p1',), ('EV76',), ('EV76p1',), ('EV77',), ('EV77p1',), ('EV78',), ('EV78p1',), ('EV79',), ('EV79p1',), ('EV80',), ('EV80p1',)]
    for i in cg_list:
        if i in persistent._seen_images:
            persistent._seen_images[i] = True
        else:
            persistent._seen_images.setdefault(i,True)  


    persistent.Ending01 = True
    persistent.Ending02 = True
    persistent.Ending03 = True
    persistent.Ending04 = True
    persistent.Ending05 = True

    persistent.Replay01_01 = True
    persistent.Replay01_02 = True
    persistent.Replay01_03 = True
    persistent.Replay01_04 = True
    persistent.Replay01_05 = True
    persistent.Replay02_01 = True
    persistent.Replay02_02 = True
    persistent.Replay02_03 = True
    persistent.Replay02_04 = True
    persistent.Replay03_01 = True
    persistent.Replay03_02 = True
    persistent.Replay03_03 = True
    persistent.Replay03_04 = True    
    persistent.Replay04_01 = True
    persistent.Replay04_02 = True
    persistent.Replay04_03 = True
    persistent.Replay05_01 = True
    persistent.Replay05_02 = True
    persistent.Replay05_03 = True