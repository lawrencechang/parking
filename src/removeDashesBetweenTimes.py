# Replace dashes between times with spaces
# Otherwise, Stanford CoreNLP only recognizes one of the times

# Algorithm
# Load json file
# Go through each entry
# 	Access the "description" field
#	Look for pattern (regular expression?) TIME-TIME
#	Remove the dashe
#	Write updated line to file

# Regular expression
times_AM_AM = r'([0-9]+:?[0-9]*AM)-([0-9]+:?[0-9]*AM)';
times_AM_PM = r'([0-9]+:?[0-9]*AM)-([0-9]+:?[0-9]*PM)';
times_PM_AM = r'([0-9]+:?[0-9]*PM)-([0-9]+:?[0-9]*AM)';
times_PM_PM = r'([0-9]+:?[0-9]*PM)-([0-9]+:?[0-9]*PM)';
times_AM_none = r'([0-9]+:?[0-9]*AM)-([0-9]+:?[0-9]*)';
times_none_AM = r'([0-9]+:?[0-9]*)-([0-9]+:?[0-9]*AM)';
times_PM_none = r'([0-9]+:?[0-9]*PM)-([0-9]+:?[0-9]*)';
times_none_PM = r'([0-9]+:?[0-9]*)-([0-9]+:?[0-9]*PM)';

import re;
# regex flags
no_case = re.I;

# Given a string, return the regular expression that matches it.
# Return None if none match.
def findMatch(inputString):
	if not(re.match(times_AM_AM,inputString,no_case) is None):
		return times_AM_AM;
	if not(re.match(times_AM_PM,inputString,no_case) is None):
		return times_AM_PM;
	if not(re.match(times_PM_AM,inputString,no_case) is None):
		return times_PM_AM;
	if not(re.match(times_PM_PM,inputString,no_case) is None):
		return times_PM_PM;
	if not(re.match(times_AM_none,inputString,no_case) is None):
		return times_AM_none;
	if not(re.match(times_none_AM,inputString,no_case) is None):
		return times_none_AM;
	if not(re.match(times_PM_none,inputString,no_case) is None):
		return times_PM_none;
	if not(re.match(times_none_PM,inputString,no_case) is None):
		return times_none_PM;

	return None;

# Find "search" hits
def findSearch(inputString):
	if not(re.search(times_AM_AM,inputString,no_case) is None):
		return times_AM_AM;
	if not(re.search(times_AM_PM,inputString,no_case) is None):
		return times_AM_PM;
	if not(re.search(times_PM_AM,inputString,no_case) is None):
		return times_PM_AM;
	if not(re.search(times_PM_PM,inputString,no_case) is None):
		return times_PM_PM;
	if not(re.search(times_AM_none,inputString,no_case) is None):
		return times_AM_none;
	if not(re.search(times_none_AM,inputString,no_case) is None):
		return times_none_AM;
	if not(re.search(times_PM_none,inputString,no_case) is None):
		return times_PM_none;
	if not(re.search(times_none_PM,inputString,no_case) is None):
		return times_none_PM;

	return None;

def run(inputfilename, outputfilename):
	import csv;
	import json;

	jsonfile = open(inputfilename, 'r');
	cleanfile = open(outputfilename, 'w');

	data = json.load(jsonfile);

	times_regexes = ([times_AM_AM,times_AM_PM,times_PM_AM,times_PM_PM]);
	#times_regexes_with_none = ([times_AM_none,times_none_AM,times_PM_none,times_none_PM]);

	outputjsonlist = [];

	for line in data:
		description = line['description'];
		for i in range(len(times_regexes)):
			current_regex = times_regexes[i];
			matchobj = re.search(current_regex,description,no_case);
			if not(matchobj is None):
				description = re.sub(current_regex,'\g<1> \g<2>',description,no_case);
		# Test individually for the four cases that have a "none" AM or PM
		# AM, none
		current_regex = times_AM_none;
		matchobj = re.search(current_regex,description,no_case);
		if not(matchobj is None):
			description = re.sub(current_regex,'\g<1> \g<2>AM',description,no_case);
		# none, AM
		current_regex = times_none_AM;
		matchobj = re.search(current_regex,description,no_case);
		if not(matchobj is None):
			description = re.sub(current_regex,'\g<1>AM \g<2>',description,no_case);
		# PM, none
		current_regex = times_PM_none;
		matchobj = re.search(current_regex,description,no_case);
		if not(matchobj is None):
			description = re.sub(current_regex,'\g<1> \g<2>PM',description,no_case);
		# none, PM
		current_regex = times_none_PM;
		matchobj = re.search(current_regex,description,no_case);
		if not(matchobj is None):
			description = re.sub(current_regex,'\g<1>PM \g<2>',description,no_case);

		line['description'] = description;
		outputjsonlist.append(line);

	json.dump(outputjsonlist,cleanfile);
	cleanfile.close();

if __name__ == '__main__':
	#inputfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_cleanarrow_sample.json";
	#outputfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_cleanarrow_cleantime_sample.json";
	inputfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_cleanarrow.json";
	outputfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_cleanarrow_cleantime.json";
	run(inputfilename,outputfilename);


