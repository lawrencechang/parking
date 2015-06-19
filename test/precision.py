# Testing
# Precision results
# 
# Of the signs that fit our criteria, get a random sampling, and verify that they are correct
# We are verifying that they are indeed "no parking" signs, as opposed to something like an "except" sign
# We are also verifying that the starting and ending times are correct, and only correct. That is
# if there are other times that add more time ranges, this is considered incorrect.

# Get the file that intersects "no parking" descriptions with "two time" descriptions
# Sample 100 of them?

# read "intersections" index file
# 	get total number
# read JSON file
# pick 50 random, print
# self verify

def test(indexFilename,jsonFilename,numSamples = 10):
	import json;
  	inputJSONFile = open(jsonFilename, 'r');
	inputJSON = json.load(inputJSONFile);
	import cPickle;
	indeces = cPickle.load(open(indexFilename,'r'));

	numIndeces = len(indeces);
	print "number of indeces is: "+str(numIndeces);
	print "number of samples is; "+str(numSamples);

	# generate list of random indeces
	import random;
	randomIndeces = random.sample(indeces,numSamples);
	for i in randomIndeces:
		print str(i)+". "+inputJSON[i]['description'];
		print "Start: ->"+inputJSON[i]['startTime']+"<-";
		print "End: ->"+inputJSON[i]['endTime']+"<-";
		print "No Parking: "+inputJSON[i]['no_parking'];
		print "No Standing: "+inputJSON[i]['no_standing'];
		print "No Stopping: "+inputJSON[i]['no_stopping'];
		print "Anytime: "+inputJSON[i]['anytime'];
		print "Monday: "+inputJSON[i]['monday'];
		print "Tuesday: "+inputJSON[i]['tuesday'];
		print "Wednesday: "+inputJSON[i]['wednesday'];
		print "Thursday: "+inputJSON[i]['thursday'];
		print "Friday: "+inputJSON[i]['friday'];
		print "Saturday: "+inputJSON[i]['saturday'];
		print "Sunday: "+inputJSON[i]['sunday'];

	return inputJSON;

def inspect(indexFilename,jsonFilename,numSamples):
	import json;
  	inputJSONFile = open(jsonFilename, 'r');
	inputJSON = json.load(inputJSONFile);
	import cPickle;
	indeces = cPickle.load(open(indexFilename,'r'));

	numIndeces = len(indeces);
	print "number of indeces is: "+str(numIndeces);
	print "number of samples is; "+str(numSamples);

	sortedIndeces = sorted(indeces);
	counter = 0;
	for i in sortedIndeces:
		if counter > numSamples:
			break;
		counter = counter + 1;
		print str(i)+". (counter: "+str(counter)+") "+inputJSON[i]['description'];
		print "Start: ->"+inputJSON[i]['startTime']+"<-";
		print "End: ->"+inputJSON[i]['endTime']+"<-";
		print "No Parking: "+inputJSON[i]['no_parking'];
		print "No Standing: "+inputJSON[i]['no_standing'];
		print "No Stopping: "+inputJSON[i]['no_stopping'];

	return inputJSON;

def printDescriptions(jsonFilename,numSamples):
	import json;
  	inputJSONFile = open(jsonFilename, 'r');
  	print "(loading JSON...)";
	inputJSON = json.load(inputJSONFile);
	print "(finished loading JSON.)";

	numIndeces = len(inputJSON);
	import random;
	randomIndeces = random.sample(range(numIndeces),numSamples);
	for i in randomIndeces:
		print str(i)+". "+inputJSON[i]['description'];

	return inputJSON;

def printDescriptionsWithInspection(jsonFilename,numSamples):
	import json;
  	inputJSONFile = open(jsonFilename, 'r');
  	print "(loading JSON...)";
	inputJSON = json.load(inputJSONFile);
	print "(finished loading JSON.)";

	numIndeces = len(inputJSON);
	import random;
	randomIndeces = random.sample(range(numIndeces),numSamples);
	for i in randomIndeces:
		print str(i)+". "+inputJSON[i]['description'];
		print "Start: "+inputJSON[i]['startTime'];
		print "End: "+inputJSON[i]['endTime'];
		print "No Parking: "+inputJSON[i]['no_parking'];
		print "No Standing: "+inputJSON[i]['no_standing'];
		print "No Stopping: "+inputJSON[i]['no_stopping'];
		print "\n";

	return inputJSON;
