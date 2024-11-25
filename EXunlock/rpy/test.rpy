init python:
    with open("D:\\test_log.txt", 'w', encoding='utf-8') as file:  
        file.write(str(persistent.__dict__))
        #file.write('persistent._seen_ever:')
        #file.write(str(persistent._seen_ever)+'\n')
        #file.write('persistent._seen_images:')
        #file.write(str(persistent._seen_images)+'\n')
        #file.write('persistent._chosen:')
        #file.write(str(persistent._chosen)+'\n')
        #file.write('persistent._seen_audio:')
        #file.write(str(persistent._seen_audio)+'\n')

