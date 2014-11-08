#!/usr/bin/python

import os
import sys
import parse

#Checks to see what files aren't listed in the logbook
#but are within the directory structure - then adds them to
#the logbook. Also (will) check for files in the logbook 
#that have been removed from the directory structure.

#INV: file paths relative to baseDir

def updateFileList(logbookfd, logbookFilename, baseDir):
    addFileStr = "addFile:" #CARE: check init string for logbook
    removeFileStr = "removeFile:"
    filesInLogbook = []
    removedFilesInLogbook = []
    filesInDirectories = []
    difference = []
    filesToAdd = []
    filesToRemove = []

    #check for files that are logged in the logbook
    logbookfd.seek(0)
    fileContents = logbookfd.read()
    filesInLogbook = list(r.fixed[0] for r in 
            parse.findall(addFileStr+"{}\n", fileContents))
    #subtract off files that we've already noted as removed
    removedFilesInLogbook = list(r.fixed[0] for r in 
             parse.findall(removeFileStr+"{}\n", fileContents))
    #final set of files in logbook
    filesInLogbook = list(set(filesInLogbook) 
                            -set(removedFilesInLogbook))

    #check for files in all directories under baseDir
    for root, dirs, files in os.walk(baseDir):
        for file in files:
            filesInDirectories.append((os.path.relpath(
                os.path.join(root, file),baseDir)))
    
    #calculate symmetric difference of lists to determine
    #which files need to be added
    filesToAdd = list(set(filesInDirectories)
                            -set(filesInLogbook))
    filesToRemove = list(set(filesInLogbook) 
                            -set(filesInDirectories))
    print(filesToAdd)
    print(filesToRemove)
    return(filesToAdd, filesToRemove)
