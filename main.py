#!/usr/bin/python

import sys
import os
import errno
import parse
import configparser
from subprocess import call, check_output

import add
import logViewer
import logEntry

#defining some things
usageStr = ("usage: lablog [add, view, edit, sync, etc.]" 
           "[message, options, etc.]")
initStr = """+++++
Logbook generated automatically by lablog, 
an open-source electronic lab notebook tool.
Copyright (C) 2014 Nigel S. Michki
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
Log begins below.
+++++

"""

configLoc = os.path.join(os.environ['HOME'], ".lablog.conf")
badExit = 1

#begin parsing command line input

if len(sys.argv) < 2:
    print(usageStr)
command = sys.argv[1]

#load info from config file
if not os.path.isfile(configLoc):
    print("Config file not found. Should be located at:\n" +
            configLoc + "\n"
            +"Try running $lablog init <baseDirName> if this"
            +" is your first time using this program.")
else:
    config = configparser.RawConfigParser()
    config.read(configLoc)
    baseDir = config.get("Main", "baseDir")
    user = config.get("Main", "user")
    logbookFilename = config.get("Main", "logbookFilename")

#check for specific commands at command line
if command == 'add':
    #do add stuff
    logbookfd = open(os.path.join(baseDir, logbookFilename), 'a+')
    add.add(sys.argv, logbookfd, logbookFilename, baseDir, user)
    logbookfd.close()
    print("Log entry added successfully")

elif command == 'view':
    #do view stuff
    logbookfd = open(os.path.join(baseDir, logbookFilename), 'r')
    v = logViewer.logViewer(logbookfd)
    print("Log entry viewed successfully")

elif command == 'sync':
    #do sync stuff
    print("Log entry synchronized successfully")

elif command == 'edit':
    #do edit stuff
    print("Log entry edited successfully")

elif command == "init":

##### BEGIN INIT SECTION #####

    #initialize directory structure
    baseDir = sys.argv[2]
    user = sys.argv[3]
    
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
            print("Failed to initialize - are you sure you" 
            " have permissions to create directories" 
            " here? Does a directory exist with the name" 
            " you provided?")
            sys.exit(badExit)
    
    #initialize logbook (shouldn't get here if above fails)
    logBookfd = open(os.path.join(baseDir, logbookFilename), 'w')
    logBookfd.write(initStr+ "addFile:" +logbookFilename)
    logBookfd.close()

    #print some data to a config file
    config = configparser.RawConfigParser()
    config.add_section("Main")
    config.set("Main", "baseDir", 
            os.path.join(os.getcwd(), baseDir))
    config.set("Main", "logbookFilename", "logbook.txt")
    config.set("Main", "user", user)
    with open(configLoc, 'w') as configfile:
            config.write(configfile)

    #print on success 
    print("Successfully initialized a logbook and basic"
          " directory structure. See manual for more" 
          " information")

##### END INIT SECTION #####

else:
    print(usageStr)

#exit successfully
sys.exit(0)
