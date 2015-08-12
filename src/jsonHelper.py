# JSON helper
# Use this file to get stats ona json object / file
# import sys;
# sys.path.append('../');
# from config import config;
# if config.system == 'windows':
# 	filename = '..\data\Parking_cleanarrow_cleantime_cleandays.json';
# elif config.system == 'mac':
# 	filename = '../data/Parking_startend_noparking.json';
import json;
import geojson;
import csv;

def getJSONObjectFromFile(jsonFilename):
	jsonfile = open(jsonFilename, 'r');
	data = json.load(jsonfile);
	return data;

def getGeoJSONObjectFromFile(geoJSONFilename):
	geojsonfile = open(geoJSONFilename, 'r');
	data = geojson.load(geojsonfile);
	return data;

def writeJSONObjectIntoFile(jsonObject,filename):
	outputFile = open(filename,'w');
	json.dump(jsonObject,outputFile);
	outputFile.close();

def getNumEntries(jsonObject):
	return len(jsonObject);

def convertToGeoJSON(jsonObject):
	# We're going to make a FeatureCollection, which will be composed of many Feature's
	# Feature object has a "geometry" object, which I'm assuming can be a Point object.
	# Get the Lat Long from the input JSON
	# "properties", fill it in with the rest of the fields
	# "id", use the id
	featureList = [];
	currentProperty = {};
	for index,line in enumerate(jsonObject):
		# The first entry is some headers.
		if not (index == 0):
			idNum = line['id'];
			latitude = float(line['x']);
			longitude = float(line['y']);
			point = geojson.Point((latitude,longitude));
			for key in line.keys():
				currentProperty[key] = line[key];
			newFeature = geojson.Feature(geometry=point,properties=currentProperty,id=idNum);
			featureList.append(newFeature);

	return geojson.FeatureCollection(featureList);

def convertToGeoJSONFile(inputJSONFilename,outputGeoJSONFilename):
	jsonObject = getJSONObjectFromFile(inputJSONFilename);
	geoJSONObject = convertToGeoJSON(jsonObject);
	outputFile = open(outputGeoJSONFilename,'w');
	json.dump(geoJSONObject,outputFile);
	outputFile.close();

def jsonToCSV(jsonFilename,csvFilename):
	# files
	jsonObject = getJSONObjectFromFile(jsonFilename);
	csvFile = csv.writer(open(csvFilename,'w'));

	# Get list of keys
	keysList = [];
	for key in jsonObject[0].keys():
		keysList.append(key);

	# Write
	csvFile.writerow(keysList);
	for row in jsonObject:
		valuesList = [];
		for key in keysList:
			valuesList.append(row[key]);
		csvFile.writerow(valuesList);

# Same functionality as jsonToCSV, but chunks files.
# Default chunksize is 100,000
def jsonToCSVChunks(jsonFilename,csvFilename,chunkSize=100000):
	import math;
	jsonObject = getJSONObjectFromFile(jsonFilename);
	keysList = [];
	for key in jsonObject[0].keys():
		keysList.append(key);

	csvFilename = csvFilename.rstrip('.csv');
	length = len(jsonObject);
	print "length = "+str(length);
	numFiles = int(math.ceil(length * 1.0 / chunkSize));
	print "numFiles = "+str(numFiles);
	files = [];
	for i in range(numFiles):
		files.append(csv.writer(open(csvFilename+str(i)+'.csv','w')));
		files[i].writerow(keysList);

	for index,row in enumerate(jsonObject):
		#if index == 0:
		#	print "first row: "+str(row);
		fileNumber = int(math.floor(index / chunkSize));
		currentFile = files[fileNumber];
		valuesList = [];
		for key in keysList:
			valuesList.append(row[key]);
		currentFile.writerow(valuesList);
