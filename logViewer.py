#!/usr/bin/python

import os
import sys
import parse
import dateutil.parser
import datetime

from logEntry import logEntry
from globalFile import *


#logViewer handles parsing the existing logbook, creating new 
#'entry' objects, and calling the appropriate display functions
#on said objects. 

class logViewer:
    def __init__(self,logbookfd):
        self.fileContents = logbookfd.read()
        self.rawLogEntries = list(r.fixed[0] for r in
                parse.findall("+++Begin log entry+++{}"
                    + "+++End log entry+++", self.fileContents))
        self.logEntries = []
        for entry in self.rawLogEntries:
            timestamp = parse.search("Time:{i}\n", entry)['i']
            user = parse.search("User:{i}\n", entry)['i']
            note = parse.search("Note:{i}\n", entry)['i']
            tags = list(r.fixed[0] for r in
                    parse.findall("\'+{}\'", entry))
            addedFiles = list(r.fixed[0] for r in 
                    parse.findall(addFileStr + "{}\n", entry))
            removedFiles = list(r.fixed[0] for r in 
                    parse.findall(removeFileStr + "{}\n", entry))
            self.logEntries.append(logEntry(timestamp, 
                user, note, tags, addedFiles, removedFiles))

    #displays all entries
    def fullDisplay(self):    
        for entry in self.logEntries:
            entry.fullDisplay()

    #filters the display based on a number of different criteria
    #still a work in progress - might need to be split up
    #into seperate functions, but its not so bad.
    def filterDisplay(self, argv):
        #just display all - no other arg(s) provided
        if len(argv) < 3 :
            print("Defaulting to full display")
            self.fullDisplay()
        
        #a "view NUM" directive, the user wants to latest NUM of
        #log entries displayed
        elif isInt(argv[2]):
            numEntries = int(argv[2])
            if (len(self.logEntries)<=numEntries):
                print(color.RED + "Requested number of entries" 
                " greater than actual number present." 
                + color.END)
                self.fullDisplay()
            else:    
                print("Showing latest: " + str(numEntries))
                i = 0
                for entry in self.logEntries:
                    if i>(len(self.logEntries)-(1+numEntries)):
                        entry.fullDisplay()
                    i = i + 1
        #a "view DATE1 DATE2" directive, the user wants all 
        #entries between the two dates (inclusive)
        elif (isDate(argv[2]) and isDate(argv[3])):
            for entry in self.logEntries:
                if (argv[2] <= entry.date <= argv[3]
                    or argv[2] >= entry.date >= argv[3]):
                    entry.fullDisplay()
