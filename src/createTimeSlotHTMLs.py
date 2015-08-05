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

def createIndexFiles(jsonFilename,outputDir,indexFilenameListFilename):
	import shutil;
	import os;
	if os.path.exists(outputDir):
		shutil.rmtree(outputDir);
	if not os.path.exists(outputDir):
		os.makedirs(outputDir);
	originalDirectory = os.getcwd();

	import cPickle;
	import json;
	jsonFile = open(jsonFilename, 'r');
	jsonData = json.load(jsonFile);

	print "Creating tuples list.";
	tuplesList = createTuplesList();

	filenameList = [];
	indexList = None;
	os.chdir(outputDir);
	for tupleIndex,tupleInfo in enumerate(tuplesList):
		print "tupleIndex: "+str(tupleIndex);
		indexList = [];
		for jsonIndex,jsonLine in enumerate(jsonData):
			validDaysList = buildValidDaysList(jsonLine);
			if ((tupleInfo.dayOfWeek in validDaysList) and
				(startTimeIsAfterInclusive(jsonLine['startTime'],tupleInfo.startTime,False)) and
				(endTimeIsBeforeInclusive(jsonLine['endTime'],tupleInfo.endTime,False))
				):
				indexList.append(jsonIndex);
		indexFile = open(tupleInfo.indexFilename,'w');
		cPickle.dump(indexList,indexFile);
		indexFile.close();

		filenameList.append((tupleInfo.indexFilename,tupleInfo.htmlFilename));

	outputFile = open(indexFilenameListFilename,'w');
	cPickle.dump(filenameList,outputFile);
	outputFile.close();

	os.chdir(originalDirectory);

def createIndexFilesList(outputDir,indexFilenameListFilename):
	import shutil;
	import os;
	if not os.path.exists(outputDir):
		os.makedirs(outputDir);
	originalDirectory = os.getcwd();

	import cPickle;
	print "Creating tuples list.";
	tuplesList = createTuplesList();

	filenameList = [];
	indexList = None;
	os.chdir(outputDir);
	for tupleIndex,tupleInfo in enumerate(tuplesList):
		print "tupleIndex: "+str(tupleIndex);
		filenameList.append((tupleInfo.indexFilename,tupleInfo.htmlFilename));

	outputFile = open(indexFilenameListFilename,'w');
	cPickle.dump(filenameList,outputFile);
	outputFile.close();
	print "Created index file list: "+indexFilenameListFilename;
	print "In directory: "+outputDir;	
	os.chdir(originalDirectory);

def createHTMLs(jsonFilename,outputDir,indexFilenameListFilename,indexFileDir):
	import cPickle;
	import jsonHelper;
	import googleMapsCreate;
	filenamesList = cPickle.load(open(indexFileDir+indexFilenameListFilename,'r'));

	import shutil;
	import os;
	if os.path.exists(outputDir):
		shutil.rmtree(outputDir);
	if not os.path.exists(outputDir):
		os.makedirs(outputDir);

	jsonObject = jsonHelper.getJSONObjectFromFile(jsonFilename);
	for index,(indexFilename,htmlFilename) in enumerate(filenamesList):
		print "HTML file: "+str(index)+", "+htmlFilename;
		googleMapsCreate.createHTML(indexFilename,jsonObject,outputDir,htmlFilename,indexFileDir,0);

def createTuplesList():
	tuplesList = [];
	numTimeSlotsPerDay = 4 * 24;
	daysOfWeek = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday'];
	for dayOfWeek in daysOfWeek:
		for timeSlotIndex in range(numTimeSlotsPerDay):
			(startTime,endTime) = startAndEndTimeFromTimeSlotIndex(timeSlotIndex);
			startTimeNoColon = startTime.replace(':','');
			endTimeNoColon = endTime.replace(':','');
			htmlFilename = dayOfWeek+"TimeSlot"+startTimeNoColon+"-"+endTimeNoColon+".html";
			indexFilename = dayOfWeek+"TimeSlot"+startTimeNoColon+"-"+endTimeNoColon+"Index.pickle";
			tuplesList.append(FileInfo(htmlFilename,indexFilename,
				dayOfWeek,startTime,endTime));
	return tuplesList;

def startAndEndTimeFromTimeSlotIndex(timeSlotIndex):
	hour = str(int(floor(timeSlotIndex / 4.0)));
	minute = str(int(timeSlotIndex%4) * 15);
	minutePlus14 = str((int(timeSlotIndex%4) * 15) + 14);
	if len(hour) == 1:
		hour = '0'+hour;
	if len(minute) == 1:
		minute = '0'+minute;
	if len(minutePlus14) == 1:
		print "ERROR - minutePlus14 has only one digit: >"+minutePlus14+"<";
		raise Exception;
	startTime = hour+":"+minute+'';
	endTime = hour+":"+minutePlus14+'';
	return (startTime,endTime);

def startTimeIsAfterInclusive(baselineTime,newTime,debug=False):
	if baselineTime == '' or newTime == '':
		if debug:
			print 'Error: baselineTime: '+str(baselineTime)+', newTime: '+str(newTime);
		return False;
	try:
		parsedBaselineTime = parse(baselineTime);
		parsedNewTime = parse(newTime);
	except:
		if debug:
			print 'Error parsing.'
			print 'Error: baselineTime: '+str(baselineTime)+', newTime: '+str(newTime);
		# Can handle this case
		if baselineTime=='TNI':
			return False;
		else:
			print 'Uncaught exception.'
			print 'Error: baselineTime: '+str(baselineTime)+', newTime: '+str(newTime);
		raise;
	timeDiff = relativedelta(parsedBaselineTime,parsedNewTime);
	if (timeDiff.hours <= 0 and timeDiff.minutes <= 0 and timeDiff.seconds <= 0):
		return True;
	else:
		return False;

def endTimeIsBeforeInclusive(baselineTime,newTime,debug=False):
	if baselineTime == '' or newTime == '':
		if debug:
			print 'Error: baselineTime: '+str(baselineTime)+', newTime: '+str(newTime);
		return False;
	try:
		parsedBaselineTime = parse(baselineTime);
		parsedNewTime = parse(newTime);
	except:
		if debug:
			print 'Error parsing.'
			print 'Error: baselineTime: '+str(baselineTime)+', newTime: '+str(newTime);
		# Can handle this case
		if baselineTime=='TNI':
			return False;
		else:
			print 'Uncaught exception.'
			print 'Error: baselineTime: '+str(baselineTime)+', newTime: '+str(newTime);
		raise;
		#return False;
	timeDiff = relativedelta(parsedBaselineTime,parsedNewTime);
	if (timeDiff.hours >= 0 and timeDiff.minutes >= 0 and timeDiff.seconds >= 0):
		return True;
	else:
		return False;

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
