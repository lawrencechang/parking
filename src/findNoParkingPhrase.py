# Find instances of the phrase "no parking"

noparking_regex = r'no[\s\S]parking';
nostopping_regex = r'no[\s\S]stopping';
nostanding_regex = r'no[\s\S]standing';

def run(inputJSONFilename,outputJSONFilename):
	import re;
	import json;
	inputJSONFile = open(inputJSONFilename, 'r');
	outputJSONFile = open(outputJSONFilename, 'w');
	inputJSON = json.load(inputJSONFile);

	outputJSONList = [];

	for line in inputJSON:
		matchobj_parking = re.search(noparking_regex,line['description'],re.I);
		if not(matchobj_parking is None):
			line['no_parking'] = 'true';
		else:
			line['no_parking'] = 'false';
		matchobj_stopping = re.search(nostopping_regex,line['description'],re.I);
		if not(matchobj_stopping is None):
			line['no_stopping'] = 'true';
		else:
			line['no_stopping'] = 'false';
		matchobj_standing = re.search(nostanding_regex,line['description'],re.I);
		if not(matchobj_standing is None):
			line['no_standing'] = 'true';
		else:
			line['no_standing'] = 'false';
		outputJSONList.append(line);

	json.dump(outputJSONList,outputJSONFile);
	outputJSONFile.close();

if __name__ == '__main__':
	inputJSONFilename = "";
	outputJSONFilename = "";
	run(inputJSONFilename,outputJSONFilename);
