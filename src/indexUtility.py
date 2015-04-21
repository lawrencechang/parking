# Create index files, listing the indeces of relevant entries
# 1. entries that have "no_parking" set to true
# 2. entries that have a valid "startTime" and "endTime"
#
# These files will be a list of numbers. For efficiency of reading them,
# perhaps a file format as such:
# First line - number of indecesf
# Second line - all the indeces, separate by white space
# Or maybe, just pickle

def noParkingIndecesPickle(inputJSONFilename,outputIndecesFilename):
	import json;
	inputJSONFile = open(inputJSONFilename, 'r');
	inputJSON = json.load(inputJSONFile);

	outputfile = open(outputIndecesFilename,'w');

	indexCounter = 0;
	indexList = [];

	for line in inputJSON:
		if line['no_parking'] == 'true':
			indexCounter = indexCounter + 1;
			indexList.append(line['id']);

	import cPickle;
	cPickle.dump(indexList,outputfile);

def startEndTimesIndecesPickle(inputJSONFilename,outputIndecesFilename):
	import json;
	inputJSONFile = open(inputJSONFilename, 'r');
	inputJSON = json.load(inputJSONFile);

	outputfile = open(outputIndecesFilename,'w');

	indexCounter = 0;
	indexList = [];

	for line in inputJSON:
		if line['startTime'] != '' and line['endTime'] != '':
			indexCounter = indexCounter + 1;
			indexList.append(line['id']);

	import cPickle;
	cPickle.dump(indexList,outputfile);

def intersection(firstIndexFilename,secondIndexFilename,outputIndexFilename):
	import cPickle;
	firstIndeces = cPickle.load(open(firstIndexFilename,'r'));
	secondIndeces = cPickle.load(open(secondIndexFilename,'r'));

	intersection = set(firstIndeces).intersection(secondIndeces);
	cPickle.dump(intersection,open(outputIndexFilename,'w'));


def noParkingIndecesUniversal(inputJSONFilename,outputIndecesFilename):
	import json;
	inputJSONFile = open(inputJSONFilename, 'r');
	inputJSON = json.load(inputJSONFile);

	outputfile = open(outputIndecesFilename,'w');

	indexCounter = 0;
	indexList = [];

	for line in inputJSON:
		if line['no_parking'] == 'true':
			indexCounter = indexCounter + 1;
			indexList.append(line['id']);

	outputfile.write(str(indexCounter)+'\n');
	#

	inputJSONFile.close();
	outputfile.close();
