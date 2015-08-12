# Data preprocessing pipeline
# Start with unaltered data
# Go through whatever preprocessing steps are defined here
# Produce output

# filenames
import sys;
# windows
if sys.platform == 'win32':
	print 'Using Windows filenames...';
	csvfilename = "..\data\Parking_Regulation_WSG84_fwtools.csv";
	csvTrimFilename = "..\data\Parking_Regulation_Shapefile_trim.csv";
	csvTrimSaveFilename = "..\data\Parking_Regulation_Shapefile_trim_save.csv";
	jsonfilename = "..\data\Parking.json";
	cleanHoursFilename = "..\data\Parking_cleanhours.json";
	arrowfilename = "..\data\Parking_cleanarrow.json";
	timefilename = "..\data\Parking_cleanarrow_cleantime.json";
	daysfilename = "..\data\Parking_cleanarrow_cleantime_cleandays.json";
	plaintextfilename = "..\data\Parking_plaintext.txt";
	plaintext500samplefilename = "..\data\Parking_plaintext_sample500.txt";
	plaintext500periodsfilename = "..\data\Parking_plaintext_sample500_periods.txt";
	plaintext600samplefilename = "..\data\Parking_plaintext_sample600.txt";
	plaintext600periodsfilename = "..\data\Parking_plaintext_sample600_periods.txt";
	plaintextperiodsfilename = "..\data\Parking_plaintext_periods.txt";
	filesDir = "..\data\plaintextChunkFiles\\";
	stanfordNLPclasspath="\"..\stanford-corenlp-full-2015-01-30\*\"";
	startandendtimesjsonfilename = "..\data\Parking_startend.json";
	noparkingjsonfilename = "..\data\Parking_startend_noparking.json";
	noparkingindexfilename = "..\data\Parking_no_parking_index.pickle";
	startendtimeindexfilename = "..\data\Parking_start_end_index.pickle";
	intersectionindexfilename = "..\data\Parking_intersection_index.pickle";
	htmlfileDir="..\data\www\\";
	htmlfilename = "..\data\www\No_parking.html";

	outputfilename = "..\data\Parking_clean_all.json";
# Mac
elif sys.platform == 'darwin':
	print 'Using Mac filenames...';
	dataDirectory = "../dataTrim/";
	csvfilename = dataDirectory+"Parking_Regulation_Shapefile_converted.csv";
	csvTrimFilename = dataDirectory+"Parking_Regulation_Shapefile_trim.csv";
	csvTrimSaveFilename = dataDirectory+"Parking_Regulation_Shapefile_trim_save.csv";
	jsonfilename = dataDirectory+"Parking.json";
	cleanHoursFilename = dataDirectory+"Parking_cleanhours.json";
	arrowfilename = dataDirectory+"Parking_cleanarrow.json";
	timefilename = dataDirectory+"Parking_cleanarrow_cleantime.json";
	daysfilename = dataDirectory+"Parking_cleanarrow_cleantime_cleandays.json";
	plaintextfilename = dataDirectory+"Parking_plaintext.txt";
	plaintext500samplefilename = dataDirectory+"Parking_plaintext_sample500.txt";
	plaintext500periodsfilename = dataDirectory+"Parking_plaintext_sample500_periods.txt";
	plaintext600samplefilename = dataDirectory+"Parking_plaintext_sample600.txt";
	plaintext600periodsfilename = dataDirectory+"Parking_plaintext_sample600_periods.txt";
	plaintextperiodsfilename = dataDirectory+"Parking_plaintext_periods.txt";
	filesDir = dataDirectory+"plaintextChunkFiles/";
	stanfordNLPclasspath="\"../stanford-corenlp-full-2015-04-20/*\"";
	startandendtimesjsonfilename = dataDirectory+"Parking_startend.json";
	noparkingjsonfilename = dataDirectory+"Parking_startend_noparking.json";
	cleanLongTimesJSONFilename = dataDirectory+"Parking_startend_noparking_cleanlongtimes.json";
	validDaysJSONFilename = dataDirectory+"Parking_startend_noparking_cleanlongtimes_validdays.json";
	timeSlotJSONFilename = dataDirectory+"Parking_timeslots.json";
	trimValidDaysJSONFilename = dataDirectory+"Parking_validdays_trim.json";
	trimValidDaysTimeFieldsJSONFilename = dataDirectory+"Parking_validdays_timeslots_trim.json"
	validDaysCSVFilename = dataDirectory+"Parking_startend_noparking_cleanlongtimes_validdays.csv";
	validDaysTimeFieldsCSVFilename = dataDirectory+"Parking_validdays_timeslots.csv"
	geoJSONFilename = dataDirectory+"Parking_geojson.json";
	geoJSONOutputDir = dataDirectory+"geojson/";
	geoJSONMinimalOutputDir = dataDirectory+"geojsonMinimal/";
	noparkingindexfilename = dataDirectory+"Parking_no_parking_index.pickle";
	startendtimeindexfilename = dataDirectory+"Parking_start_end_index.pickle";
	intersectionindexfilename = dataDirectory+"Parking_intersection_index.pickle";
	htmlfileDir=dataDirectory+"www/";
	htmlfilename = "No_parking.html";
	timeSlotIndexFilename = "timeSlotIndexFilenames.pickle";
	timeSlotIndexDir = dataDirectory+"timeSlotIndexFiles/";

	outputfilename = dataDirectory+"Parking_clean_all.json";

import jsonHelper;
import time;
# To run the entire thing, set skipTrim to True, all else to False.
skipTrim = True;
skipPreprocess = True;
skipNLP = True;
skipParse = True;
skipIndex = True;
skipCleanLongTimes = True;
skipAddValidDays = True;
skipGeoJSONConvert = True;
skipTimeSlotIndex = False;
skipTimeSlotHTML = False;
skipTimeSlotGeoJSON = False;
skipTimeSlotGeoJSONMinimal = False;
skipAddTimeFields = False;
skipTrimInfo = False;
skipJSONToCSV = False;

def preprocess():
	start = time.time();
	tempfilename = "temp";

	if not skipTrim:
		print 'Trimming original CSV to a smaller size.';
		trimSize = 1000;
		import convertCSVtoJSONList as convertCtoJ;
		convertCtoJ.trimFromIndex(csvfilename,csvTrimFilename,trimSize,214000);
		import shutil;
		shutil.copyfile(csvTrimFilename,csvTrimSaveFilename);
	else:
		import shutil;
		shutil.copyfile(csvfilename,csvTrimFilename);
	if not skipPreprocess:
		# CSV to JSON
		print 'Converting from CSV to JSON.';
		import convertCSVtoJSONList as convertCtoJ;
		convertCtoJ.convertCSVtoJSON(csvTrimFilename,jsonfilename);
		tempJSONObj = jsonHelper.getJSONObjectFromFile(jsonfilename);
		numEntries = jsonHelper.getNumEntries(tempJSONObj);

		# This didn't seem to be solve the parser bug
		"""
		print 'Spelling out hour numbers at sentence beginnings.';
		import replaceHourBeginnings;
		replaceHourBeginnings.cleanHours(jsonfilename,cleanHoursFilename);
		tempJSONObj = jsonHelper.getJSONObjectFromFile(cleanHoursFilename);
		numEntriesHours = jsonHelper.getNumEntries(tempJSONObj);
		assert numEntries == numEntriesHours;
		"""

		# Clean up arrows
		print 'Cleaning up arrows.';
		import replaceArrows;
		replaceArrows.replaceArrows(jsonfilename,arrowfilename);
		tempJSONObj = jsonHelper.getJSONObjectFromFile(arrowfilename);
		numEntriesArrow = jsonHelper.getNumEntries(tempJSONObj);
		try:
			assert numEntries == numEntriesArrow;
		except AssertionError as e:
			#print "AssertionError: "+e;
			print "numEntries: "+str(numEntries);
			print "numEntriesArrow: "+str(numEntriesArrow);

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
		jsonToPlaintext.jsonToPlaintextLineCount(daysfilename,plaintext600samplefilename,600);
		addPeriods.addPeriods(plaintext600samplefilename,plaintext600periodsfilename);

	# Run descriptions through Stanford Core NLP parser
	# Call the parser...
	fileList = "fileList.txt";
	if not skipNLP:
		print "Calling Stanford Core NLP Parser...";
		import callStanfordCoreNLPParser;
		callStanfordCoreNLPParser.runChunk(plaintextperiodsfilename,outputDir=filesDir,fileListFilename=fileList,chunkSize=500);
		callStanfordCoreNLPParser.runFilelist(classPath=stanfordNLPclasspath,fileListFilename=fileList,outputDir=filesDir);

	if not skipParse:
		# Add "start" and "end" time elements to the JSON
		print "Adding start and end time elements to the JSON.";
		import addStartAndEndTimes;
		addStartAndEndTimes.runXMLFileList(filesDir+fileList,daysfilename,startandendtimesjsonfilename);

		# Add "no_parking" element to JSON, true if "no parking" exists in description, false otherwise.
		print "Adding phrases to JSON.";
		import findPhrases;
		findPhrases.run(startandendtimesjsonfilename,noparkingjsonfilename);

	if not skipIndex:
		# Create index files to get the entries that meet both our criteria
		print "Creating index files for no_parking and startTime and endTime existence.";
		import indexUtility;
		indexUtility.noParkingIndecesPickle(noparkingjsonfilename,noparkingindexfilename);
		indexUtility.startEndTimesIndecesPickle(noparkingjsonfilename,startendtimeindexfilename);
		indexUtility.intersection(noparkingindexfilename,startendtimeindexfilename,intersectionindexfilename);
	
	if not skipCleanLongTimes:
		print "Clean weird time formats."
		import cleanLongTimeEntries;
		cleanLongTimeEntries.run(noparkingjsonfilename,cleanLongTimesJSONFilename);

	if not skipAddValidDays:
		print "Adding fields that describe which days of the week are valid.";
		startValidDays = time.time();
		import validDays;
		validDays.run(cleanLongTimesJSONFilename,validDaysJSONFilename,dataDirectory);
		endValidDays = time.time();
		print "["+str(endValidDays-startValidDays)+" seconds]";

	if not skipGeoJSONConvert:
		print "Converting JSON to geoJSON.";
		startGeoJSON = time.time();
		jsonHelper.convertToGeoJSONFile(validDaysJSONFilename,geoJSONFilename);
		endGeoJSON = time.time();
		print "["+str(endGeoJSON-startGeoJSON)+" seconds]";

	import createTimeSlotHTMLs;
	if not skipTimeSlotIndex:
		print "Creating index files for all time slots.";
		startTimeSlots = time.time();
		createTimeSlotHTMLs.createIndexFiles(validDaysJSONFilename,timeSlotIndexDir,timeSlotIndexFilename,True);
		endTimeSlots = time.time();
		print "["+str(endTimeSlots-startTimeSlots)+" seconds]";
	else:
		print "Creating the index file list ONLY.";
		startTimeSlots = time.time();
		createTimeSlotHTMLs.createIndexFilesList(timeSlotIndexDir,timeSlotIndexFilename);
		endTimeSlots = time.time();
		print "["+str(endTimeSlots-startTimeSlots)+" seconds]";
	
	if not skipTimeSlotHTML:
		print "Creating HTMLs for all time slots.";
		startTimeSlots = time.time();
		createTimeSlotHTMLs.createHTMLs(validDaysJSONFilename,htmlfileDir,timeSlotIndexFilename,timeSlotIndexDir);
		endTimeSlots = time.time();
		print "["+str(endTimeSlots-startTimeSlots)+" seconds]";

	if not skipTimeSlotGeoJSON:
		print "Creating geoJSON files for each time slot.";
		import createTimeSlotGeoJSONs;
		start = time.time();
		createTimeSlotGeoJSONs.createGeoJSONs(geoJSONFilename,geoJSONOutputDir,timeSlotIndexFilename,timeSlotIndexDir,verbose=False);
		end = time.time();
		print "["+str(end-start)+" seconds]";

	if not skipTimeSlotGeoJSONMinimal:
		print "Creating minimal geoJSON files for each time slot.";
		import createTimeSlotGeoJSONs;
		start = time.time();
		createTimeSlotGeoJSONs.createMinimalGeoJSONs(geoJSONFilename,geoJSONMinimalOutputDir,timeSlotIndexFilename,timeSlotIndexDir,verbose=False);
		end = time.time();
		print "["+str(end-start)+" seconds]";

	if not skipAddTimeFields:
		print "Adding the time fields to the JSON. Will make things much bigger...";
		import addTimeSlots;
		start = time.time();
		addTimeSlots.run(timeSlotIndexFilename,timeSlotIndexDir,validDaysJSONFilename,timeSlotJSONFilename);
		end = time.time();
		print "["+str(end-start)+" seconds]";

	if not skipTrimInfo:
		print "Removing most fields except valid days.";
		import jsonTrim;
		startTrim = time.time();
		jsonTrim.trimFieldsValidDaysOnly(timeSlotJSONFilename,trimValidDaysJSONFilename);
		jsonTrim.trimFieldsValidDaysTimeSlots(timeSlotJSONFilename,trimValidDaysTimeFieldsJSONFilename);
		endTrim = time.time();
		print "["+str(endTrim-startTrim)+" seconds]";

	if not skipJSONToCSV:
		print "Creating CSV from last JSON.";
		start = time.time();
		jsonHelper.jsonToCSV(trimValidDaysTimeFieldsJSONFilename,validDaysTimeFieldsCSVFilename);
		jsonHelper.jsonToCSVChunks(trimValidDaysTimeFieldsJSONFilename,validDaysTimeFieldsCSVFilename,10000);
		end = time.time();
		print "["+str(end-start)+" seconds]";

	# return latest JSON object
	tempJSONObj = jsonHelper.getJSONObjectFromFile(timeSlotJSONFilename);
	return tempJSONObj;

if __name__ == '__main__':
	data = preprocess();