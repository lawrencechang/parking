# Data preprocessing pipeline
# Start with unaltered data
# Go through whatever preprocessing steps are defined here
# Produce output

# filenames
#csvfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_Regulation_WSG84.csv";
csvfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_Regulation_WSG84_fwtools.csv";
jsonfilename = "C:\Users\Lawrence\Documents\parking\data\Parking.json";
arrowfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_cleanarrow.json";
timefilename = "C:\Users\Lawrence\Documents\parking\data\Parking_cleanarrow_cleantime.json";
daysfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_cleanarrow_cleantime_cleandays.json";
#periodsfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_cleanarrow_cleantime_cleandays_periods.json";
plaintextfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_plaintext.txt";
plaintext500samplefilename = "C:\Users\Lawrence\Documents\parking\data\Parking_plaintext_sample500.txt";
plaintext500periodsfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_plaintext_sample500_periods.txt";
plaintext100samplefilename = "C:\Users\Lawrence\Documents\parking\data\Parking_plaintext_sample100.txt";
plaintext100periodsfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_plaintext_sample100_periods.txt";

plaintextperiodsfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_plaintext_periods.txt";

startandendtimesjsonfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_startend.json";
noparkingjsonfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_startend_noparking.json";
noparkingindexfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_no_parking_index.pickle";
startendtimeindexfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_start_end_index.pickle";
intersectionindexfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_intersection_index.pickle";
htmlfilename = "C:\Users\Lawrence\Documents\parking\src\www\No_parking.html";

outputfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_clean_all.json";

import jsonHelper;
import time;
skip = True;

def preprocess():
	start = time.time();
	tempfilename = "temp";

	if not skip:
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

		# Write descriptions only to plaintext file, and write periods after each description.
		print 'Writing descriptions to plaintext file.';
		import jsonToPlaintext;
		import addPeriods;
		jsonToPlaintext.jsonToPlaintext(daysfilename,plaintextfilename);
		addPeriods.addPeriods(plaintextfilename,plaintextperiodsfilename);

		print 'Writing descriptions to plaintext file, 500 entries.';
		jsonToPlaintext.jsonToPlaintextLineCount(daysfilename,plaintext500samplefilename,500);
		addPeriods.addPeriods(plaintext500samplefilename,plaintext500periodsfilename);
		print 'Writing descriptions to plaintext file, 100 entries.';
		jsonToPlaintext.jsonToPlaintextLineCount(daysfilename,plaintext100samplefilename,100);
		addPeriods.addPeriods(plaintext100samplefilename,plaintext100periodsfilename);

	# Run descriptions through Stanford Core NLP parser
	# I would like to automate it, but I'd rather not spend too much time trying to get
	# that right. I'll just manually do it
	parsedXMLFilename = "C:\Users\Lawrence\Documents\stanford-corenlp-full-2015-01-30\Parking_plaintext_sample500_periods.txt.xml";

	# Add "start" and "end" time elements to the JSON
	print "Adding start and end time elements to the JSON.";
	import addStartAndEndTimes;
	addStartAndEndTimes.run(parsedXMLFilename,daysfilename,startandendtimesjsonfilename);
	tempJSONObj = jsonHelper.getJSONObjectFromFile(startandendtimesjsonfilename);

	# Add "no_parking" element to JSON, true if "no parking" exists in description, false otherwise.
	print "Adding no parking boolean to JSON.";
	import findNoParkingPhrase;
	findNoParkingPhrase.run(startandendtimesjsonfilename,noparkingjsonfilename);
	tempJSONObj = jsonHelper.getJSONObjectFromFile(noparkingjsonfilename);

	# Create index files to get the entries that meet both our criteria
	print "Creating index files for no_parking and startTime and endTime existence.";
	import indexUtility;
	indexUtility.noParkingIndecesPickle(noparkingjsonfilename,noparkingindexfilename);
	indexUtility.startEndTimesIndecesPickle(noparkingjsonfilename,startendtimeindexfilename);
	indexUtility.intersection(noparkingindexfilename,startendtimeindexfilename,intersectionindexfilename);
	
	# Create HTML file that'll put this info onto a Google Maps view
	print "Createing HTML file to display data.";
	import googleMapsCreate;
	googleMapsCreate.createHTML(intersectionindexfilename,noparkingjsonfilename,htmlfilename);

	# return latest JSON object
	return tempJSONObj;

if __name__ == '__main__':
	data = preprocess();