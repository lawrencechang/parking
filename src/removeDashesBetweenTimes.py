# Replace dashes between times with spaces
# Otherwise, Stanford CoreNLP only recognizes one of the times

# Algorithm
# Load json file
# Go through each entry
# 	Access the "description" field
#	Look for pattern (regular expression?) TIME-TIME
#	Remove the dashe
#	Write updated line to file

#jsonfilename = "C:\Users\Lawrence\Documents\masters_project\data_converted\Parking_Regulation_WSG84.json";
jsonfilename = "C:\Users\Lawrence\Documents\masters_project\data_converted\Parking_Regulation_WSG84_sample.json";
outputfilename = "C:\Users\Lawrence\Documents\masters_project\data_converted\Parking_cleantime.json";

import csv;
import json;

jsonfile = open(jsonfilename, 'r')
cleanfile = open(outputfilename, 'w')

data = json.load(jsonfile);

import re;
# regex flags
no_case = re.I;
# Regular expression
times_AM_AM = r'([0-9]+:?[0-9]*AM)-([0-9]+:?[0-9]*AM)';
times_AM_PM = r'([0-9]+:?[0-9]*AM)-([0-9]+:?[0-9]*PM)';
times_PM_AM = r'([0-9]+:?[0-9]*PM)-([0-9]+:?[0-9]*AM)';
times_PM_PM = r'([0-9]+:?[0-9]*PM)-([0-9]+:?[0-9]*PM)';
times_AM_none = r'([0-9]+:?[0-9]*AM)-([0-9]+:?[0-9]*)';
times_none_AM = r'([0-9]+:?[0-9]*)-([0-9]+:?[0-9]*AM)';
times_PM_none = r'([0-9]+:?[0-9]*PM)-([0-9]+:?[0-9]*)';
times_none_PM = r'([0-9]+:?[0-9]*)-([0-9]+:?[0-9]*PM)';

times_regexes = ([times_AM_AM,times_AM_PM,times_PM_AM,times_PM_PM,
				times_AM_none,times_none_AM,times_PM_none,times_none_PM]);

for i in range(len(times_regexes)):
	current_regex = times_regexes[i];
	print "Current regex is " + current_regex;
	for line in data:
		description = line['description'];
		matchobj = re.search(current_regex,description,no_case);
		if not(matchobj is None):
			re.sub(current_regex,'\1 \2',description,no_case);
			print description;

# for line in data:
# 	#print str(line['id']) + " " + line['description'];
	
# 	# test - print out the segment that is matched
# 	#matchobj = re.search(time_regex,line['description'],no_case);
# 	matchobj = re.search(times_capture,line['description'],no_case);
# 	description = line['description'];
	
# 	if not(matchobj is None):
# 		print matchobj.group(0) + " " + matchobj.group(1) + " " + matchobj.group(2);
# 		# replaceobj = (re.sub(times_capture,
# 		# 	matchobj.group(1) + " " + matchobj.group(2),
# 		# 	description,
# 		# 	no_case));

# 		replaceobj = (re.sub(times_capture,
# 			"",
# 			description,
# 			no_case));

# 		#print str(line['id']) + " " + matchobj.group() + " " + description;
# 		#print str(line['id']) + " " + matchobj.group() + " " + replaceobj;
# 		print str(line['id']) + ". " + replaceobj;

# 		print "\n";
# print 'capture test'
# for line in data:
# 	matchobj = re.search(times_capture,line['description'],no_case);
# 	if not(matchobj is None):
# 		print str(line['id']) + " " + matchobj.group(0) + " " + matchobj.group(1) + " " + matchobj.group(2) + " " + description;




