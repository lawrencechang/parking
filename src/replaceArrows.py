# Remove all the <-----> things
# The number of dashes seems inconsistent
# Replace with some unique keyword, like ARROW_BOTH_DIRECTION

def replaceArrows(jsonfilename, outputfilename):
	import csv;
	import json;

	jsonfile = open(jsonfilename, 'r')
	cleanfile = open(outputfilename, 'w')

	data = json.load(jsonfile);

	import re;
	# regex flags
	no_case = re.I;
	# Regular expression
	arrows_regex = r'<-+>';
	replacement = 'ARROW_BOTH_DIRECTION';

	outputjsonlist = [];

	for line in data:
		matchobj = re.search(arrows_regex,line['description'],no_case);
		description = line['description'];
		replaceobj = re.sub(arrows_regex,replacement,description);
		if not(matchobj is None):
			#print str(line['id']) + " " + matchobj.group() + " " + replaceobj
			line['description'] = replaceobj;
		outputjsonlist.append(line);

	json.dump(outputjsonlist,cleanfile);
	cleanfile.close();

if __name__ == '__main__':
	jsonfilename = "C:\Users\Lawrence\Documents\masters_project\data_converted\Parking_Regulation_WSG84_sample.json";
	outputfilename = "C:\Users\Lawrence\Documents\masters_project\data_converted\Parking_cleanarrow.json";
	replaceArrows(jsonfilename,outputfilename);