# Find instances of the phrase "no parking"

noparking_regex = r'no[\s\S]parking';

def run(inputJSONFilename,outputJSONFilename):
	import re;
	import json;
	inputJSONFile = open(inputJSONFilename, 'r');
	outputJSONFile = open(outputJSONFilename, 'w');
	inputJSON = json.load(inputJSONFile);

	outputJSONList = [];

	for line in inputJSON:
		matchobj = re.search(noparking_regex,line['description'],re.I);
		if not(matchobj is None):
			line['no_parking'] = 'true';
		else:
			line['no_parking'] = 'false';
		outputJSONList.append(line);

	json.dump(outputJSONList,outputJSONFile);
	outputJSONFile.close();

if __name__ == '__main__':
	inputJSONFilename = "";
	outputJSONFilename = "";
	run(inputJSONFilename,outputJSONFilename);
