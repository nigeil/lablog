#!/usr/bin/python

import sys
import os
import errno
from subprocess import call, check_output

#defining some things
usage = "usage: lablog [add, view, edit, sync, etc.] [message, options, etc.]"

#begin parsing command line input

##print('Number of arguments:', len(sys.argv), 'arguments.')
##print('Argument List:', str(sys.argv))

if len(sys.argv) < 2:
    print(usage)
command = sys.argv[1]

if command == 'add':
    #do add stuff
    print("Log entry added successfully")

elif command == 'view':
    #do view stuff
    print("Log entry viewed successfully")

elif command == 'sync':
    #do sync stuff
    print("Log entry synched(?) successfully")

elif command == 'edit':
    #do edit stuff
    print("Log entry edited successfully")

elif command == "init":
    
    #initialize directory structure
    baseDir = sys.argv[2]
    
    #check for window systems, change path accordingly
    if os.name == 'nt':
        initPath = str(baseDir + "\mainProject\data")
    else:
        initPath = str(baseDir + "/mainProject/data")
    
    #try and make directories; print error if it fails
    try:
        os.makedirs(initPath)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
        else:
            print("Failed to initialize - are you sure you have" 
                    " permissions to create directories here? " 
                    "Does a directory exist with the name you " 
                    "provided?")
            sys.exit(1)

    print("Successfully initialized a log and basic directory " 
            "structure")
    print("See manual for more information")

else:
    print(usage)

#exit successfully
sys.exit(0)
