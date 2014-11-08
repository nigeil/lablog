#!/usr/bin/python

import parse
import datetime

def add(argv, logbookfd, user):
    #timestamp in ISO format
    timeStamp = datetime.datetime.now().isoformat()
    
    #parsing text and tags
    for item in argv:
        print(item)
    note = argv[2]
    if len(argv) > 3:
        meta = argv[3::]
    
    #string to be written to file
    writeMe = ("Time:" + str(timeStamp) + "\nUser:" 
            + str(user) +"\n" + str(note) + "\n"
            + str(meta) +"\n\n") 
    
    #writing to file
    logbookfd.write(writeMe)

