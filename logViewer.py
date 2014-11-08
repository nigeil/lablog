#!/usr/bin/python

import os
import sys
import parse

import logEntry

class logViewer:
    def __init__(self,logbookfd):
        self.fileContents = logbookfd.read()
        self.rawLogEntries = list(r.fixed[0] for r in
                parse.findall("+++Begin log entry+++{}"
                    + "+++End log entry+++", self.fileContents))
        print(self.rawLogEntries)
        self.logEntries = []
        for entry in self.rawLogEntries:
            timestamp = parse.search("Time:{i}\n", entry)['i']
            user = parse.search("User:{i}\n", entry)['i']
            note = parse.search("Note:{i}\n", entry)['i']
            tags = list(r.fixed[0] for r in
                    parse.findall("\'+{}\'", entry))
            addedFiles = list(r.fixed[0] for r in 
                    parse.findall("addFile:{}\n", entry))
            removedFiles = list(r.fixed[0] for r in 
                    parse.findall("removeFile:{}\n", entry))
            self.logEntries.append(logEntry.logEntry(timestamp, 
                user, note, tags, addedFiles, removedFiles))

        for entry in self.logEntries:
            entry.fullDisplay()
