#!/usr/bin/python

import parse
import datetime
import updateFileList

#Adds a note and metadata to the logfile

def add(argv, logbookfd, logbookFilename, baseDir, user):
    #timestamp in ISO format
    timeStamp = datetime.datetime.now().isoformat()
    
    #parsing text and tags
    note = argv[2]
    if len(argv) > 3:
        meta = argv[3::]
    
    filesToAdd,filesToRemove = updateFileList.updateFileList(
                logbookfd, logbookFilename, baseDir)

    #string to be written to file
    writeMe = ("Time:" + str(timeStamp) + "\nUser:" 
            + str(user) +"\n" + str(note) + "\n"
            + str(meta) +"\n") 
    
    for file in filesToAdd:
        writeMe = writeMe + "addFile:" + file +"\n"
    for file in filesToRemove:
        writeMe = writeMe + "removeFile:" + file + "\n\n"
    
    #writing to file
    logbookfd.write(writeMe)

