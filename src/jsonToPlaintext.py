# Output the parking sign descriptions' text into a plaintext file.
# One line per description.
# This is to be used for Stanford NLP Parser processing.

def jsonToPlaintext(inputfilename, outputfilename):
	debug = True;
	if debug:
		print "inputfilename: "+inputfilename;
		print "outputfilename: "+outputfilename;

	import json;
	jsonfile = open(inputfilename, 'r');
	data = json.load(jsonfile);

	outputfile = open(outputfilename, 'w');

	for entry in data:
		print "Description: "+entry['description'];
		outputfile.write(entry['description']+'\n');

	outputfile.close();

def jsonToPlaintextLineCount(inputfilename, outputfilename, numLines):
	import json;
	jsonfile = open(inputfilename, 'r');
	data = json.load(jsonfile);

	outputfile = open(outputfilename, 'w');

	count = 0;
	for entry in data:
		count = count + 1;
		outputfile.write(entry['description']+'\n');
		if (count >= numLines):
			outputfile.close();
			return;

	outputfile.close();


if __name__ == '__main__':
	inputfilename = "";
	outputfilename = "";
	jsonToPlaintext(inputfilename, outputfilename);