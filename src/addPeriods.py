# Add periods to the end of each line
# This is so that the Stanford NLP parser can properly understand that each line is a new sentence.
# Important to note, this assumes each sentence is on its own single line.

def addPeriods(inputfilename, outputfilename):
	inputfile = open(inputfilename, 'r');
	outputfile = open(outputfilename, 'w');

	for line in inputfile:
		outputfile.write(addPeriodIfThereIsntOne(line));

	inputfile.close();
	outputfile.close();

def addPeriodIfThereIsntOne(inputString):
	if inputString.endswith('.\n'):
		return inputString;
	return inputString[:-1]+'.\n';

if __name__ == '__main__':
	inputfilename = "";
	outputfilename = "";

	addPeriods(inputfilename, outputfilename);

