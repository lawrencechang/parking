# JSON helper
# Use this file to get stats ona json object / file

def getJSONObjectFromFile(jsonFilename):
	import json;
	jsonfile = open(jsonFilename, 'r');
	data = json.load(jsonfile);
	return data;

def getNumEntries(jsonObject):
	return len(jsonObject);

	