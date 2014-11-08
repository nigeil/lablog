#!/usr/bin/python

import os
import dateutil.parser
import datetime

#defining some things
usageStr = ("usage: lablog [add, view, edit, sync, etc.]" 
        "[message, options, etc.]")

#printed at the top of every new logfile
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

#location of config file - best place for now?
configLoc = os.path.join(os.environ['HOME'], ".lablog.conf")

#exit code on failure
badExit = 1

#markers that make parsing the logbook easier
addFileStr = "addFile:"
removeFileStr = "removeFile:"

#color class, for formatting output
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

#true IFF input string can logically be an integer in python
def isInt(inStr):
    try:
        int(inStr)
        return True
    except ValueError:
        return False

#true IFF input string is date (yyyy-mm-dd)
def isDate(inStr):
            try:
                datetime.datetime.strptime(inStr, 
                        '%Y-%m-%d')
                return True
            except ValueError:
                return False
