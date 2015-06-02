# JSON helper
# Use this file to get stats ona json object / file
# import sys;
# sys.path.append('../');
# from config import config;
# if config.system == 'windows':
# 	filename = '..\data\Parking_cleanarrow_cleantime_cleandays.json';
# elif config.system == 'mac':
# 	filename = '../data/Parking_startend_noparking.json';

def getJSONObjectFromFile(jsonFilename):
	import json;
	jsonfile = open(jsonFilename, 'r');
	data = json.load(jsonfile);
	return data;

def getNumEntries(jsonObject):
	return len(jsonObject);

# if __name__ == '__main__':
# 	print 'filename is: '+filename
# 	data = getJSONObjectFromFile(filename);
# 	print 'count is: '+str(getNumEntries(data));
	