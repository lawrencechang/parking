# Convert CSV to JSON

def convertCSVtoJSON(csvfilename, jsonfilename):

	import csv;
	import json;

	csvfile = open(csvfilename, 'r');
	jsonfile = open(jsonfilename, 'w');
	#samplefile = open(samplefilename, 'w');

	fieldnames = ("y","x","objectid","borough","order",
		"sequence","mutcd","distance","direction",
		"arrow","xx","yy","description");
	reader = csv.DictReader( csvfile, fieldnames)
	#counter = 0;
	dictlist = [];
	for counter,row in enumerate(reader):
		# Adding an extra field called 'id', which is a unique identifier
	    row['id']=counter;
	    dictlist.append(row);
	    #counter = counter + 1;

	# write files
	json.dump(dictlist,jsonfile);
	jsonfile.close();


def trim(inputCSVFilename,outputCSVFilename,trimSize):
	import csv;
	inputCSVFile = open(inputCSVFilename, 'r');
	outputCSVFile = open(outputCSVFilename, 'w');
	fieldnames = ("y","x","objectid","borough","order",
		"sequence","mutcd","distance","direction",
		"arrow","xx","yy","description");	
	reader = csv.DictReader(inputCSVFile, fieldnames);
	writer = csv.DictWriter(outputCSVFile, fieldnames);
	#counter = 0;
	dictlist = [];
	for counter,row in enumerate(reader):
		if counter <= trimSize:
			writer.writerow(row);
		else:
			break;

	inputCSVFile.close();
	outputCSVFile.close();


if __name__ == '__main__':
	csvfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_Regulation_WSG84.csv";
	jsonfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_Regulation_WSG84.json";
	#samplefilename = "C:\Users\Lawrence\Documents\parking\data\Parking_Regulation_WSG84_sample.json";
	convertCSVtoJSON(csvfilename,jsonfilename);
	
