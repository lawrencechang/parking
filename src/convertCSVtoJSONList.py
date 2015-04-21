# Convert CSV to JSON

def convertCSVtoJSON(csvfilename, jsonfilename):

	import csv;
	import json;

	csvfile = open(csvfilename, 'r');
	jsonfile = open(jsonfilename, 'w');
	#samplefile = open(samplefilename, 'w');

	fieldnames = ("y","x","borough","order","sequence","mutcd","direction","arrow","xx","yy","description");
	reader = csv.DictReader( csvfile, fieldnames)
	counter = 0;
	dictlist = [];
	dictlistsample = [];
	for row in reader:
		# Adding an extra field called 'id', which is a unique identifier
	    row['id']=counter;
	    # Create a sampling
	    if counter < 100:
	    	dictlistsample.append(row);
	    dictlist.append(row);
	    counter = counter + 1;

	# write files
	json.dump(dictlist,jsonfile);
	jsonfile.close();
	#json.dump(dictlistsample,samplefile);
	#samplefile.close();

if __name__ == '__main__':
	csvfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_Regulation_WSG84.csv";
	jsonfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_Regulation_WSG84.json";
	#samplefilename = "C:\Users\Lawrence\Documents\parking\data\Parking_Regulation_WSG84_sample.json";
	convertCSVtoJSON(csvfilename,jsonfilename);
