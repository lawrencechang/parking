# CSV utility file

def getNumLines(csvFilename):
	import csv;
	csvFile = open(csvFilename,'r');
	csvReader = csv.reader(csvFile);
	return sum(1 for row in csvReader);