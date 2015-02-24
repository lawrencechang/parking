# Data preprocessing pipeline
# Start with unaltered data
# Go through whatever preprocessing steps are defined here
# Produce output

# filenames
csvfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_Regulation_WSG84.csv";
jsonfilename = "C:\Users\Lawrence\Documents\parking\data\Parking.json";
arrowfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_cleanarrow.json";
timefilename = "C:\Users\Lawrence\Documents\parking\data\Parking_cleanarrow_cleantime.json";
daysfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_cleanarrow_cleantime_cleandays.json";

outputfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_clean_all.json";

import jsonHelper;
import time;

def preprocess():
	start = time.time();
	tempfilename = "temp";

	# CSV to JSON
	print 'Converting from CSV to JSON.';
	import convertCSVtoJSONList as convertCtoJ;
	convertCtoJ.convertCSVtoJSON(csvfilename,jsonfilename);
	tempJSONObj = jsonHelper.getJSONObjectFromFile(jsonfilename);
	numEntries = jsonHelper.getNumEntries(tempJSONObj);

	# Clean up arrows
	print 'Cleaning up arrows.';
	import replaceArrows;
	replaceArrows.replaceArrows(jsonfilename,arrowfilename);
	tempJSONObj = jsonHelper.getJSONObjectFromFile(arrowfilename);
	numEntriesArrow = jsonHelper.getNumEntries(tempJSONObj);
	assert numEntries == numEntriesArrow;

	# Clean up times
	print 'Cleaning up times.';
	import removeDashesBetweenTimes;
	removeDashesBetweenTimes.run(arrowfilename,timefilename);
	tempJSONObj = jsonHelper.getJSONObjectFromFile(timefilename);
	numEntriesTime = jsonHelper.getNumEntries(tempJSONObj);
	assert numEntries == numEntriesTime;

	# Test times
	print 'Testing time regex.';
	import testTimeRegex;
	timeScriptFilename = 'removeDashesBetweenTimes.py';
	testTimeRegex.testTimeRegex(timefilename,timeScriptFilename);

	# Normalize days of week
	print 'Normalizing days of week.';
	import cleanDays;
	cleanDays.cleanDays(timefilename,daysfilename);
	tempJSONObj = jsonHelper.getJSONObjectFromFile(daysfilename);
	numEntriesDays = jsonHelper.getNumEntries(tempJSONObj);
	assert numEntries == numEntriesDays;

	end = time.time();
	print "Elapsed time was: " + str(end - start);

	# return latest JSON object
	return tempJSONObj;

	# jsonHelper.getNumEntries(jsonHelper.getJSONObjectFromFile('../data/Parking_cleanarrow_cleantime.json'));
	# jsonHelper.getNumEntries(jsonHelper.getJSONObjectFromFile('../data/Parking.json'));

	# # Rename temp file to output
	# from os import rename;
	# from os import remove;
	
	# # remove file if it already exists
	# try:
	# 	remove(outputfilename);
	# except:
	# 	print "File " + outputfilename + " already exists. Deleted.";
	# rename(tempfilename,outputfilename);
	# print "Wrote " + outputfilename;

if __name__ == '__main__':
	data = preprocess();