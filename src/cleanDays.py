# Clean up days of the week
# Ex. tues -> tuesday, etc

import re;
# Regular expression
sunday_regex = r'([\s]sun(\s|\Z))|([\s]su(\s|\Z))';
monday_regex = r'[\s]mon(\s|\Z)';
tuesday_regex = r'[\s]tues(\s|\Z)';
wednesday_regex = r'[\s]wed(\s|\Z)';
thursday_regex = r'([\s]thurs(\s|\Z))|([\s]thur(\s|\Z))|([\s]thu(\s|\Z))';
friday_regex = r'([\s]fri(\s|\Z))|([\s]fr(\s|\Z))';
saturday_regex = r'[\s]sat(\s|\Z)';

sunday_replacement = ' SUNDAY ';
monday_replacement = ' MONDAY ';
tuesday_replacement = ' TUESDAY ';
wednesday_replacement = ' WEDNESDAY ';
thursday_replacement = ' THURSDAY ';
friday_replacement = ' FRIDAY ';
saturday_replacement = ' SATURDAY ';

def cleanDays(inputfilename, outputfilename):
	import json;

	inputfile = open(inputfilename, 'r')
	outputfile = open(outputfilename, 'w')

	data = json.load(inputfile);

	outputjsonlist = [];

	for line in data:
		description = line['description'];
		description = re.sub(sunday_regex,sunday_replacement,description,0,re.I);
		description = re.sub(monday_regex,monday_replacement,description,0,re.I);
		description = re.sub(tuesday_regex,tuesday_replacement,description,0,re.I);
		description = re.sub(wednesday_regex,wednesday_replacement,description,0,re.I);
		description = re.sub(thursday_regex,thursday_replacement,description,0,re.I);
		description = re.sub(friday_regex,friday_replacement,description,0,re.I);
		description = re.sub(saturday_regex,saturday_replacement,description,0,re.I);
		line['description'] = description;
		outputjsonlist.append(line);

	json.dump(outputjsonlist,outputfile);
	outputfile.close();


if __name__ == '__main__':
	jsonfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_cleanarrow_cleantime.json";
	outputfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_cleanarrow_cleantime_cleanday.json";

	cleanDays(jsonfilename,outputfilename);