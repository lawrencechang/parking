# Create the HTML that'll display the "no parking" locations

def createHTML(indexFilename,jsonObject,outputDir,outputFilename,limit=10000):
	# import shutil;
	# import os;
	# if os.path.exists(outputDir):
	# 	shutil.rmtree(outputDir);
	# if not os.path.exists(outputDir):
	# 	os.makedirs(outputDir);
	# currentDirectory = os.getcwd();
	# print "In googleMapsCreate, the current working dir is: "+currentDirectory;

	outputFile = open(outputDir+outputFilename,'w');
	import googleMapsJavascriptStrings as gStrings;
	outputFile.write(gStrings.top);

	# create variables for all the lat longs
  	varFront = "var myLatlng";
  	varMiddle = " = new google.maps.LatLng(";
  	varEnd = ");";

  	import json;
  	#print "In googleMapsCreate, jsonFilename: "+jsonFilename;
  	#inputJSONFile = open(jsonFilename, 'r');
	#inputJSON = json.load(inputJSONFile);
	inputJSON = jsonObject;
	import cPickle;
	#print "In googleMapsCreate, outputDir+indexFilename: "+outputDir+indexFilename;
	indeces = cPickle.load(open(outputDir+indexFilename,'r'));

	counter = 0;
	for counter,index in enumerate(indeces):
		#print "index: "+str(index);
		firstCoord = str(inputJSON[index]['y']);
		secondCoord = str(inputJSON[index]['x']);
		outputFile.write(varFront+str(counter)+varMiddle+firstCoord+","+secondCoord+varEnd+"\n");

		if limit > 0 and counter >= limit:
			print "WARNING - number of data points limited to "+str(limit)+".";
			break;

	firstCounter = counter;
	#
	outputFile.write(gStrings.middle);

	# create marker entries using the variables
	# NOTE - remove last comma
	marFront = "new google.maps.Marker({position: myLatlng";
	marEnd = ", map: map, title: \'Hello World!\'}),\n";
	marEndNoComma = ", map: map, title: \'Hello World!\'})\n";
	for counter,index in enumerate(indeces):
		if firstCounter != counter:
			outputFile.write(marFront+str(counter)+marEnd);
		else:
			outputFile.write(marFront+str(counter)+marEndNoComma);

		if limit > 0 and counter >= limit:
			break;

	#
	outputFile.write(gStrings.bottom);

	outputFile.close();

