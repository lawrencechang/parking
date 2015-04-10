# Adds two new fields to a JSON object
# A start time, and an end time
# Only do this when the XML found exactly 2 times, no more, no less
# If there are more than 2, perhaps 4, then it becomes more complicated.

def run(xmlFilename,inputJSONFilename,outputJSONFilename):
	# My XML parsing utility
	import parseXML;
	parsedXML = parseXML.parse(xmlFilename);

	# open JSON files
	import json;
	inputJSONFile = open(inputJSONFilename, 'r');
	outputJSONFile = open(outputJSONFilename, 'w');
	inputJSON = json.load(inputJSONFile);

	outputJSONList = [];
	# allocate start and end time vars
	startTime = "";
	endTime = "";
	# Loop through the entire input JSON file
	lineCounter = 0;
	for line in inputJSON:
		# if the line exists in the XML file, 
		if (parseXML.hasLine(parsedXML,lineCounter)):
			#print "lineCounter: "+str(lineCounter);
			# and if so, if that line contains two times
			if (parseXML.hasTwoTimes(parsedXML,lineCounter)):
				# Set the start and end time variables
				(startTime,endTime) = parseXML.getTwoTimes(parsedXML,lineCounter);
		else:
			break;
		# Add times to output JSON
		line['startTime'] = startTime;
		line['endTime'] = endTime;
		outputJSONList.append(line);

		# reset times
		startTime = "";
		endTime = "";
		lineCounter = lineCounter + 1;

	json.dump(outputJSONList,outputJSONFile);
	outputJSONFile.close();

	return outputJSONList;

if __name__ == '__main__':
	xmlFilename = "";
	inputJSONFilename = "";
	outputJSONFilename = "";

	run(xmlFilename,inputJSONFilename,outputJSONFilename);
