# csvHelper
# Read number of lines in a CSV file for signs, but might actually live in "locations.csv".
# 7 fields
# Also, create a special function to not count certain lines

def getNumLines(csvFilename):
	import csv;

	csvfile = open(csvFilename, 'r');

	fieldnames = ("borough","order","sequence","dstance","arrow","description","code");
	reader = csv.DictReader( csvfile, fieldnames);

	counter = 0;
	for row in reader:
		counter = counter + 1;

	return counter;

def getNumLinesCutList(csvFilename):
	# The cutList is a list of words that if they are in the "sign code" field,
	# don't include them in the count.

	cutList = ["CL","PL","BL"];

	import csv;

	csvfile = open(csvFilename, 'r');

	fieldnames = ("borough","order","sequence","dstance","arrow","description","code");
	reader = csv.DictReader( csvfile, fieldnames);

	counter = 0;
	for row in reader:
		#print row['code'];
		# "strip"ing because whitespace
		if not row['code'].strip() in cutList:
			counter = counter + 1;

	return counter;
