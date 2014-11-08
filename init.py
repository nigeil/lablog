#!/usr/bin/python

import sys
import os
import configparser
import errno

from globalFile import *

#an instance of initializer is called
#in order to initialize a lab log system,
#similar to running a 'git init' for a git
#repository. Only run ONCE

class initializer:
	def __init__(self, baseDir, user, logbookFilename):
		#check for different system, change path accordingly
		if os.name == 'nt':
		    initPath = str(baseDir + "\project1\data")
		else:
		    initPath = str(baseDir + "/project1/data")
		
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
		logBookfd.write(initStr)
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

	

