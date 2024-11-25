init -1 python:

    cg_list = [('bg', 'story01a'), ('bg', 'story02a'), ('bg', 'story02b'), ('bg', 'story03a'), ('bg', 'story04a'), ('bg', 'story04b'), ('bg', 'story04c'), ('bg', 'story05a'), ('bg', 'story05b'), ('bg', 'story05c'), ('bg', 'story06a'), ('bg', 'story06b'), ('bg', 'story06c'), ('bg', 'story07a'), ('bg', 'story07b'), ('bg', 'story08a'), ('bg', 'story08b'), ('bg', 'story08c'), ('bg', 'story09a'), ('bg', 'story09b'), ('bg', 'story09c'), ('bg', 'story09d'), ('bg', 'story10a'), ('bg', 'story10b'), ('bg', 'story11a'), ('bg', 'story11b'), ('bg', 'story11c'), ('bg', 'story12a'), ('bg', 'story12b'), ('bg', 'story13a'), ('bg', 'story13b'), ('bg', 'story13c'), ('bg', 'story13d'), ('bg', 'story14a'), ('bg', 'story14b'), ('bg', 'story14c'), ('bg', 'story15a'), ('bg', 'story15b'), ('bg', 'story16a'), ('bg', 'story16b'), ('bg', 'story17a'), ('bg', 'story18a'), ('bg', 'story18b'), ('bg', 'story18c'), ('bg', 'story19a'), ('bg', 'story19b'), ('bg', 'story20a'), ('bg', 'story20b')]
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
