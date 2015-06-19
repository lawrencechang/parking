# Creating the HTML files for each time slot
# Ideas
# - Use the existing HTML creator functionality
# 	- might need to refactor for this to work
# 	- ACTUALLY, it might work out of the box
# 		- the creator works via index files
# - Easy, brute force approach
# 	- for each HTML file that we're creating, run through the entire JSON,
# 	pulling out the relevant points
# 	- Potential performance issues, since we're running through the JSON
# 	96 times. EDIT - 672 times
# - Faster, but more complicated approach
# 	- open a file pointer for all 96 files
# 	- We run through the JSON once
# 		- For each line, write it into the relevant file
# 	- Would be on the order of 100x faster, but harder to write
# - Start easy first, I think. Perhaps it won't be slow enough to be a problem?

# Algorithm
# - Create a list of tuples
# 	- the contents of the tuple are:
# 		- filename
# 		- day of week
# 		- start time
# 		- end time
# 	- My earlier calculations were wrong.
# 		- 7 days x 24 hours x 4 15 minute slots = 672
# 		- Gonna be hard to create that by hand
# - For each line in the list
# 	- Create empty list
# 	- Go through the JSON
# 		- If it fits our time slot, add index to list
# 	- Save list to index file, named appropriately
# 	- Generate HTML with this, giving appropriate name.
	


# - Need a validDays function, which returns a list of the valid days of the week
# 	- input
# 		- The JSON line.
# 	- output
# 		- List of day names. Could be empty

# Using "named tuples", which seem better
from collections import namedtuple;
FileInfo = namedtuple('FileInfo',
	'htmlFilename indexFilename dayOfWeek startTime endTime');
# Another date/time resolution NLP package
from dateutil.parser import *;
from dateutil.relativedelta import *;
from datetime import *;
# Math for floor
from math import floor;

def run(jsonFilename,outputDir,limit=0):
	import shutil;
	import os;
	if os.path.exists(outputDir):
		shutil.rmtree(outputDir);
	if not os.path.exists(outputDir):
		os.makedirs(outputDir);
	currentDirectory = os.getcwd();
	#print "In createTimeSlotHTMLs, the current working dir is: "+currentDirectory;
	import cPickle;
	import googleMapsCreate;
	import json;
	jsonFile = open(jsonFilename, 'r');
	jsonData = json.load(jsonFile);

	print "Creating tuples list.";
	tuplesList = createTuplesList();

	indexList = None;
	for tupleIndex,tupleInfo in enumerate(tuplesList):
		print "tupleIndex: "+str(tupleIndex);
		indexList = [];
		for jsonIndex,jsonLine in enumerate(jsonData):
			validDaysList = buildValidDaysList(jsonLine);
			if ((tupleInfo.dayOfWeek in validDaysList) and
				(startTimeIsAfterInclusive(jsonLine['startTime'],tupleInfo.startTime)) and
				(endTimeIsBeforeInclusive(jsonLine['endTime'],tupleInfo.endTime))
				):
				indexList.append(jsonIndex);
		# write indexList to file
		#print "Writing index file: "+outputDir+tupleInfo.indexFilename;
		indexFile = open(outputDir+tupleInfo.indexFilename,'w');
		cPickle.dump(indexList,indexFile);
		indexFile.close();
		#print "Done writing index file: "+outputDir+tupleInfo.indexFilename;

		# Create HTML file
		googleMapsCreate.createHTML(tupleInfo.indexFilename,
			jsonData,outputDir,tupleInfo.htmlFilename,limit=limit);


def createTuplesList():
	tuplesList = [];

	numTimeSlotsPerDay = 4 * 24;
	daysOfWeek = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday'];
	for dayOfWeek in daysOfWeek:
		for timeSlotIndex in range(numTimeSlotsPerDay):
			htmlFilename = dayOfWeek+"TimeSlot"+str(timeSlotIndex)+".html";
			indexFilename = dayOfWeek+"TimeSlot"+str(timeSlotIndex)+"Index.pickle";
			(startTime,endTime) = startAndEndTimeFromTimeSlotIndex(timeSlotIndex);
			tuplesList.append(FileInfo(htmlFilename,indexFilename,
				dayOfWeek,startTime,endTime));

	return tuplesList;

def startAndEndTimeFromTimeSlotIndex(timeSlotIndex):
	hour = int(floor(timeSlotIndex / 4.0));
	minute = int(timeSlotIndex%4) * 15;
	startTime = str(hour)+":"+str(minute)+"";
	endTime = str(hour)+":"+str(minute+14)+"";
	return (startTime,endTime);

def startTimeIsAfterInclusive(baselineTime,newTime):
	#print "baselineTime: "+baselineTime;
	#print "newtime: "+newTime;
	try:
		parsedBaselineTime = parse(baselineTime);
		parsedNewTime = parse(newTime);
	except:
		#print "Exception: baselineTime: "+baselineTime+", newTime: "+newTime;
		parsedBaselineTime = parse("00:00");
		parsedNewTime = parse("00:00");
	timeDiff = relativedelta(parsedBaselineTime,parsedNewTime);
	hours = None;
	minutes = None;
	seconds = None;
	hours = 1 if timeDiff.hours == 0 else timeDiff.hours;
	minutes = 1 if timeDiff.minutes == 0 else timeDiff.minutes;
	seconds = 1 if timeDiff.seconds == 0 else timeDiff.seconds;

	return (True if hours*minutes*seconds >= 0 else False);

def endTimeIsBeforeInclusive(baselineTime,newTime):
	#print "baselineTime: "+baselineTime;
	#print "newtime: "+newTime;
	try:
		parsedBaselineTime = parse(baselineTime);
		parsedNewTime = parse(newTime);
	except:
		print "Exception: baselineTime: "+baselineTime+", newTime: "+newTime;
		parsedBaselineTime = parse("00:00");
		parsedNewTime = parse("00:00");
	timeDiff = relativedelta(parsedBaselineTime,parsedNewTime);
	hours = None;
	minutes = None;
	seconds = None;
	hours = 1 if timeDiff.hours == 0 else timeDiff.hours;
	minutes = 1 if timeDiff.minutes == 0 else timeDiff.minutes;
	seconds = 1 if timeDiff.seconds == 0 else timeDiff.seconds;

	return (True if hours*minutes*seconds < 0 else False);

def buildValidDaysList(jsonLine):
	result = [];
	if jsonLine['validSunday'] == 'true':
		result.append('sunday');
	if jsonLine['validMonday'] == 'true':
		result.append('monday');
	if jsonLine['validTuesday'] == 'true':
		result.append('tuesday');
	if jsonLine['validWednesday'] == 'true':
		result.append('wednesday');
	if jsonLine['validThursday'] == 'true':
		result.append('thursday');
	if jsonLine['validFriday'] == 'true':
		result.append('friday');
	if jsonLine['validSaturday'] == 'true':
		result.append('saturday');
	return result;
