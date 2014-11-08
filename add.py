#!/usr/bin/python

import parse
import datetime
import updateFileList

#Adds a note and metadata to the logfile

def add(argv, logbookfd, logbookFilename, baseDir, user):
    #timestamp in ISO format
    timeStamp = datetime.datetime.now().isoformat()
    
    #parsing text and tags
    meta = []
    note = ''
    i=0
    for word in argv:
        #skip lablob and command
        if i < 2:
            i = i+1
            continue
        else:
            newTag = parse.parse("+{tag}", word)
            if newTag is not None: 
                #if it's a tag, add it to the tag list
                meta.append(newTag['tag'])
            else:
                #otherwise add it to the note
                note = note + " " + word

    filesToAdd,filesToRemove = updateFileList.updateFileList(
                logbookfd, logbookFilename, baseDir)

    #string to be written to file
    writeMe = ("+++Begin log entry+++\n"
            + "Time:" + str(timeStamp) + "\nUser:" 
            + str(user) +"\n" + "Note:" + str(note) + "\n"
            + str(meta) +"\n") 
    
    for file in filesToAdd:
        writeMe = writeMe + "addFile:" + file +"\n"
    for file in filesToRemove:
        writeMe = writeMe + "removeFile:" + file + "\n"
    
    writeMe = writeMe + "+++End log entry+++\n\n"
    
    #writing to file
    logbookfd.write(writeMe)

