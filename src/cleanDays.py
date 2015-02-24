# Clean up days of the week
# Ex. tues -> tuesday, etc

import re;
# regex flags
no_case = re.I;
# Regular expression
# sunday_regex = r'[ \t\n\r\f\v]sun[ \t\n\r\f\v]';
# monday_regex = r'[ \t\n\r\f\v]mon[ \t\n\r\f\v]';
# tuesday_regex = r'[ \t\n\r\f\v]tues[ \t\n\r\f\v]';
# wednesday_regex = r'[ \t\n\r\f\v]wed[ \t\n\r\f\v]';
# thursday_regex = r'[ \t\n\r\f\v]thurs[ \t\n\r\f\v]';
# friday_regex = r'[ \t\n\r\f\v]fri[ \t\n\r\f\v]';
# saturday_regex = r'[ \t\n\r\f\v]sat[ \t\n\r\f\v]';
sunday_regex = r'[\s]sun[\s]';
monday_regex = r'[\s]mon[\s]';
tuesday_regex = r'[\s]tues[\s]';
wednesday_regex = r'[\s]wed[\s]';
thursday_regex = r'[\s]thurs[\s]';
friday_regex = r'[\s]fri[\s]';
saturday_regex = r'[\s]sat[\s]';

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