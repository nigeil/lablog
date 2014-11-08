#!/usr/bin/python

import sys
import os
import parse
import configparser

import add
import logViewer
import logEntry
import init
from globalFile import *

#load info from config file
if not os.path.isfile(configLoc):
    print("Config file not found. Should be located at:\n" +
            configLoc + "\n"
            +"Try running $lablog init <baseDirName> <username>"
            +" if this is your first time using this program.")
else:
    config = configparser.RawConfigParser()
    config.read(configLoc)
    baseDir = config.get("Main", "baseDir")
    user = config.get("Main", "user")
    logbookFilename = config.get("Main", "logbookFilename")

#begin parsing command line arguments
if len(sys.argv) < 2:
    print(usageStr)
command = sys.argv[1]

#check for specific commands at command line
if command == 'add':
    logbookfd = open(os.path.join(baseDir, logbookFilename), 'a+')
    add.add(sys.argv, logbookfd, logbookFilename, baseDir, user)
    logbookfd.close()
    print("Log entry added successfully")

elif command == 'view':
    logbookfd = open(os.path.join(baseDir, logbookFilename), 'r')
    v = logViewer.logViewer(logbookfd)
    v.filterDisplay(list(sys.argv))
    #v.fullDisplay()
    print("\nLog entries viewed successfully")

elif command == 'sync':
    print("Log synchronized successfully")

elif command == 'edit':
    print("Log entry edited successfully")

elif command == "init":
    #initialize directory structure (run once)
    baseDir = sys.argv[2]
    user = sys.argv[3]
    init.initializer(baseDir, user, logbookFilename)

else:
    print(usageStr)

#exit successfully
sys.exit(0)
