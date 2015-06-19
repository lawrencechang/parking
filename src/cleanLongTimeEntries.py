# Clean the weird time texts that look like "XXXX-11-30T08:00";
# Another possiblity is "XXXX-WXX-7T08:00"
# This works, in that it'll replace any phrase of the preceding format with
# just the type. However, it will not clean out an entire string. For example,
# if there's a bunch of other cruft, the other cruft remains. Like extra
# words before and after. This should never be the case, from my
# experience.

import re;
regex = r'(XXXX-[\d\w]+-\d+)(T\d+:\d+)';

def run(inputJSONFilename,outputJSONFilename):
	import json;

	inputFile = open(inputJSONFilename,'r');
	outputFile = open(outputJSONFilename,'w');

	data = json.load(inputFile);

	outputJSONList = [];

	for line in data:
		startTime = line['startTime'];
		startTime = re.sub(regex,"\g<2>",startTime,re.I);
		endTime = line['endTime'];
		endTime = re.sub(regex,"\g<2>",endTime,re.I);
		line['startTime'] = startTime;
		line['endTime'] = endTime;
		outputJSONList.append(line);
	json.dump(outputJSONList,outputFile);
	inputFile.close();
	outputFile.close();

