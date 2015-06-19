# Test pipeline

# Get paths
print "importing paths.";
import sys;
sys.path.append('../');

# filenames
from config import config;
if config.system == 'windows':
	intersectionindexfilename = "..\data\Parking_intersection_index.pickle";
	noparkingjsonfilename = "..\data\Parking_startend_noparking.json";
elif config.system == 'mac':
	csvFilename = "../data/Parking_Regulation_Shapefile_converted.csv";
	noparkingjsonfilename = "../data/Parking_startend_noparking.json";
	noParkingIndexFilename = "../data/Parking_no_parking_index.pickle";
	startEndIndexFilename = "../data/Parking_start_end_index.pickle";
	intersectionindexfilename = "../data/Parking_intersection_index.pickle";

# Skips
# True
# False
skipStatistics = False;
skipPrecision = False;
skipRandomSample = True;

import precision;
# 1. Get statistics
# How many total data points? Check files starting from CSV and all JSONs
# 	or maybe just the starting csv and the last JSON
if not skipStatistics:
	print "Getting statistics.";
	print "1. Number of data points.";
	import src.csvUtility as csvUtility;
	print "Number of lines in CSV file: "+str(csvUtility.getNumLines(csvFilename));
	import src.jsonHelper as jsonHelper;
	print ("Number of lines in JSON file: " +
		str(jsonHelper.getNumEntries(jsonHelper.getJSONObjectFromFile(noparkingjsonfilename))) );
	# How many points meet the no parking / standing / stopping criteria?
	import cPickle;
	print "2. Number of no parking / standing / stopping data points."
	numIndecesNoParking = len(cPickle.load(open(noParkingIndexFilename,'r')));
	print str(numIndecesNoParking);
	# How many points meet the start and end time criteria?
	print "3. Number of start and end time data points."
	numIndecesStartEnd = len(cPickle.load(open(startEndIndexFilename,'r')));
	print str(numIndecesStartEnd);
	# How many meet both?
	print "4. Number of points that meet both criteria."
	numIndecesIntersection = len(cPickle.load(open(intersectionindexfilename,'r')));
	print str(numIndecesIntersection);

# 2. Precision
if not skipPrecision:
	print "Running precision test.";
	numSamples = 50;
	inputJSON = precision.test(intersectionindexfilename,noparkingjsonfilename,50);

# 3. Inspect top 10
#print "Inspecting top 10.";
#inputJSON = precision.inspect(intersectionindexfilename,noparkingjsonfilename, 10);

# 4. Print descriptions for 50 random guys
# Used for sampling, getting the number of criteria fitting (verified by hand)
if not skipRandomSample:
	numSamplesCoverage = 50;
	print "Sampling "+str(numSamplesCoverage)+" descriptions.";
	inputJSON = precision.printDescriptionsWithInspection(noparkingjsonfilename,numSamplesCoverage);

if not inputJSON is None:
	print "Variable \"inputJSON\" is in your workspace now.";

