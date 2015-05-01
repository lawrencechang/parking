# JSON helper
# Use this file to get stats ona json object / file

def getJSONObjectFromFile(jsonFilename):
	import json;
	jsonfile = open(jsonFilename, 'r');
	data = json.load(jsonfile);
	return data;

def getNumEntries(jsonObject):
	return len(jsonObject);

if __name__ == '__main__':
	filename = '..\data\Parking_cleanarrow_cleantime_cleandays.json';
	print 'count is: '+getNumEntries(getJSONObjectFromFile(filename));
	