import json;
import jsonHelper;
from addTimeSlots import periods, hours, minutes, getFieldName;

def trimFieldsValidDaysOnly(inputJSONFilename,outputJSONFilename):
	jsonObject = jsonHelper.getJSONObjectFromFile(inputJSONFilename);
	jsonOutputFile = open(outputJSONFilename, 'w');
	fields = ['x','y','validSunday','validMonday','validTuesday',
		'validWednesday','validThursday','validFriday','validSaturday',
		'description','id','no_parking','no_stopping','no_standing'];
	outputList = [];
	for row in jsonObject:
		currentLine = {};
		for field in fields:
			currentLine[field] = row[field];
		outputList.append(currentLine);

	json.dump(outputList,jsonOutputFile);
	jsonOutputFile.close();

def trimFieldsValidDaysTimeSlots(inputJSONFilename,outputJSONFilename):
	jsonObject = jsonHelper.getJSONObjectFromFile(inputJSONFilename);
	jsonOutputFile = open(outputJSONFilename, 'w');
	fields = ['x','y','validSunday','validMonday','validTuesday',
		'validWednesday','validThursday','validFriday','validSaturday',
		'description','id','no_parking','no_stopping','no_standing'];

	# Add the time fields
	for period in periods:
		for hour in hours:
			for minute in minutes:
				fields.append(getFieldName(period,hour,minute));

	outputList = [];
	for row in jsonObject:
		currentLine = {};
		for field in fields:
			currentLine[field] = row[field];
		outputList.append(currentLine);

	json.dump(outputList,jsonOutputFile);
	jsonOutputFile.close();