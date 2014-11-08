#!/usr/bin/python

import dateutil.parser
from color import color

class logEntry:
    def __init__ (self, timestamp, user, note, tags, 
            addedFiles, removedFiles):
        self.timestamp = timestamp
        self.user = user
        self.note = note
        self.tags = tags
        self.addedFiles = addedFiles
        self.removedFiles = removedFiles
    
    def getValues(self):
        self.values = [self.timestamp, self.user, self.note,
                self.tags, self.addedFiles, self.removedFiles]
        return(self.values)
    
    def fullDisplay(self):
        print("\nUser: " + self.user
            +"\nDate: " 
            + str(dateutil.parser.parse(self.timestamp)))
        print("\n\t" + color.BOLD +self.note + color.END + "\n") 
        if len(self.addedFiles) > 0:
            print("Added Files: ",end="")
            print(*self.addedFiles, sep=(", "))  
        if len(self.removedFiles) > 0:
            print("Removed Files: ",end="")
            print(*self.removedFiles, sep=(", "))
        if len(self.tags) > 0 :
            print("Tags: ",end="") 
            print(*self.tags, sep=(", "))

