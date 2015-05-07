# Data preprocessing pipeline
# Start with unaltered data
# Go through whatever preprocessing steps are defined here
# Produce output

# filenames
import config;
if config.system == 'windows':
	print 'Using Windows filenames...';
	csvfilename = "..\data\Parking_Regulation_WSG84_fwtools.csv";
	jsonfilename = "..\data\Parking.json";
	arrowfilename = "..\data\Parking_cleanarrow.json";
	timefilename = "..\data\Parking_cleanarrow_cleantime.json";
	daysfilename = "..\data\Parking_cleanarrow_cleantime_cleandays.json";
	plaintextfilename = "..\data\Parking_plaintext.txt";
	plaintext500samplefilename = "..\data\Parking_plaintext_sample500.txt";
	plaintext500periodsfilename = "..\data\Parking_plaintext_sample500_periods.txt";
	plaintext100samplefilename = "..\data\Parking_plaintext_sample100.txt";
	plaintext100periodsfilename = "..\data\Parking_plaintext_sample100_periods.txt";
	plaintextperiodsfilename = "..\data\Parking_plaintext_periods.txt";
	filesDir = "..\data\plaintextChunkFiles\\";
	stanfordNLPclasspath="\"..\stanford-corenlp-full-2015-01-30\*\"";
	startandendtimesjsonfilename = "..\data\Parking_startend.json";
	noparkingjsonfilename = "..\data\Parking_startend_noparking.json";
	noparkingindexfilename = "..\data\Parking_no_parking_index.pickle";
	startendtimeindexfilename = "..\data\Parking_start_end_index.pickle";
	intersectionindexfilename = "..\data\Parking_intersection_index.pickle";
	htmlfileDir="..\src\www\\";
	htmlfilename = "..\src\www\No_parking.html";

	outputfilename = "..\data\Parking_clean_all.json";
elif config.system == 'mac':
	print 'Using Mac filenames...';
	csvfilename = "../data/Parking_Regulation_Shapefile_converted.csv";
	jsonfilename = "../data/Parking.json";
	arrowfilename = "../data/Parking_cleanarrow.json";
	timefilename = "../data/Parking_cleanarrow_cleantime.json";
	daysfilename = "../data/Parking_cleanarrow_cleantime_cleandays.json";
	plaintextfilename = "../data/Parking_plaintext.txt";
	plaintext500samplefilename = "../data/Parking_plaintext_sample500.txt";
	plaintext500periodsfilename = "../data/Parking_plaintext_sample500_periods.txt";
	plaintext100samplefilename = "../data/Parking_plaintext_sample100.txt";
	plaintext100periodsfilename = "../data/Parking_plaintext_sample100_periods.txt";
	plaintextperiodsfilename = "../data/Parking_plaintext_periods.txt";
	filesDir = "../data/plaintextChunkFiles/";
	stanfordNLPclasspath="\"../stanford-corenlp-full-2015-04-20/*\"";
	startandendtimesjsonfilename = "../data/Parking_startend.json";
	noparkingjsonfilename = "../data/Parking_startend_noparking.json";
	noparkingindexfilename = "../data/Parking_no_parking_index.pickle";
	startendtimeindexfilename = "../data/Parking_start_end_index.pickle";
	intersectionindexfilename = "../data/Parking_intersection_index.pickle";
	htmlfileDir="../src/www/";
	htmlfilename = "../src/www/No_parking.html";

	outputfilename = "../data/Parking_clean_all.json";

import jsonHelper;
import time;
skipPreprocess = True;
skipNLP = True;
skipParse = True;
skipIndex = True;

def preprocess():
	start = time.time();
	tempfilename = "temp";

	tempJSONObj = "";

	if not skipPreprocess:
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
	#parsedXMLFilename = "C:\Users\Lawrence\Documents\stanford-corenlp-full-2015-01-30\Parking_plaintext_sample500_periods.txt.xml";
	# Call the parser...
	fileList = "fileList.txt";
	if not skipNLP:
		print "Calling Stanford Core NLP Parser...";
		import callStanfordCoreNLPParser;
		#callStanfordCoreNLPParser.run(plaintext500periodsfilename);
		callStanfordCoreNLPParser.runChunk(plaintextperiodsfilename,outputDir=filesDir,fileListFilename=fileList,chunkSize=500);
		callStanfordCoreNLPParser.runFilelist(classPath=stanfordNLPclasspath,fileListFilename=fileList,outputDir=filesDir);

	if not skipParse:
		# Add "start" and "end" time elements to the JSON
		print "Adding start and end time elements to the JSON.";
		import addStartAndEndTimes;
		#addStartAndEndTimes.run(parsedXMLFilename,daysfilename,startandendtimesjsonfilename);
		addStartAndEndTimes.runXMLFileList(filesDir+fileList,daysfilename,startandendtimesjsonfilename);
		tempJSONObj = jsonHelper.getJSONObjectFromFile(startandendtimesjsonfilename);

	if not skipIndex:
		# Add "no_parking" element to JSON, true if "no parking" exists in description, false otherwise.
		print "Adding no parking, no stopping, no standing boolean to JSON.";
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
	print "Creating HTML file to display data.";
	import googleMapsCreate;
	googleMapsCreate.createHTML(intersectionindexfilename,noparkingjsonfilename,htmlfileDir,htmlfilename);

	# return latest JSON object
	return tempJSONObj;

if __name__ == '__main__':
	data = preprocess();