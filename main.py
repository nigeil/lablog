#!/usr/bin/python

import sys
import os
import errno
from subprocess import call, check_output

#defining some things
usageStr = ("usage: lablog [add, view, edit, sync, etc.]" 
           "[message, options, etc.]")
#+++ signifies comment block in logbook
initStr = """+++
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
+++"""

#begin parsing command line input

if len(sys.argv) < 2:
    print(usageStr)
command = sys.argv[1]

if command == 'add':
    #do add stuff
    print("Log entry added successfully")

elif command == 'view':
    #do view stuff
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
            sys.exit(1)
    
    #initialize logbook (shouldn't get here if above fails)
    logBookfd = open(os.path.join(baseDir, "logbook.txt"), 'w')
    logBookfd.write(initStr)
    logBookfd.close()

    #print success string
    print("Successfully initialized a logbook and basic"
          " directory structure. See manual for more" 
          " information")

##### END INIT SECTION #####

else:
    print(usageStr)

#exit successfully
sys.exit(0)
