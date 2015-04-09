# Parse XML
# At the moment, I think I just want to look for "time" elements.

# The XML that's generated has this structure:
# root, document, sentences, sentence, tokens, token
# In the token objects, perhaps look for the "NER" to be "TIME"
# or, look for the existence of the "Timex" object

##
# Making some utility functions here
# We're looking at the "sentence" objects here. Each "sentence" is a line.
import xml.etree.ElementTree as ET;

# Parse, then return the object
def parse(xmlFilename):
	tree = ET.parse(xmlFilename);
	root = tree.getroot();
	return root;

# Returns whether the line exists
def hasLine(parsedXML,lineNumber):
	root = parsedXML;

	# This code searches manually, but we can use shortcuts
	# "document" is the 0th element of root, sentences is the 0th element of 
	sentenceCounter = 0;
	for document in root.findall('document'):
		for sentences in document.findall('sentences'):
			# Iterative search
			# for sentence in sentences.findall('sentences'):
			# 	if sentenceCounter == lineNumber:
			# 		return true;
			# 	sentenceCounter = sentenceCounter + 1;

			# Direct index search
			try:
				sentence = sentences[lineNumber];
				return True;
			except IndexError:
				return False;

	return False;

# Returns whether a line has two times
def hasTwoTimes(parsedXML,lineNumber):
	root = parsedXML;
	timeCounter = 0;
	for document in root.findall('document'):
		for sentences in document.findall('sentences'):
			try:
				sentence = sentences[lineNumber];
				for tokens in sentence.findall('tokens'):
					for token in tokens.findall('token'):
						for timex in token.findall('Timex'):
							if timex.get('type') == 'TIME':
								timeCounter = timeCounter + 1;
			except IndexError:
				return false;
	if timeCounter == 2:
		return True;
	return False;

def hasTwoTimesDirect(parsedXML,lineNumber):
	root = parsedXML;
	timeCounter = 0;
	documentIndex = 0;
	sentencesIndex = 0;
	tokensIndex = 0;
	try:
		tokens = root[documentIndex][sentencesIndex][lineNumber][tokensIndex];
		for token in tokens.findall('token'):
			for timex in token.findall('Timex'):
				if timex.get('type') == 'TIME':
					timeCounter = timeCounter + 1;
		if timeCounter == 2:
			return True;
		return False;
	except IndexError:
		return False;

	return False;

def getFirstTime(parsedXML,lineNumber):
	(first,second) = getTwoTimes(parsedXML,lineNumber);
	return first;

def getSecondTime(parsedXML,lineNumber):
	(first,second) = getTwoTimes(parsedXML,lineNumber);
	return second;

# return a tuple containing the start and end times
def getTwoTimes(parsedXML,lineNumber):
	root = parsedXML;
	timeCounter = 0;
	firstTime = None;
	secondTime = None;

	for document in root.findall('document'):
		for sentences in document.findall('sentences'):
			try:
				sentence = sentences[lineNumber];
				for tokens in sentence.findall('tokens'):
					for token in tokens.findall('token'):
						for timex in token.findall('Timex'):
							if timex.get('type') == 'TIME':
								if timeCounter == 0:
									firstTime = timex.text;
									timeCounter = timeCounter + 1;
								elif timeCounter == 1:
									secondTime = timex.text;
									timeCounter = timeCounter + 1;

			except IndexError:
				continue;
	
	return (firstTime,secondTime);


if __name__ == '__main__':
	
	#xmlfilename = "C:\Users\Lawrence\Documents\stanford-corenlp-full-2015-01-30\Parking_plaintext_sample100.txt.xml";
	#xmlfilename = "C:\Users\Lawrence\Documents\stanford-corenlp-full-2015-01-30\Parking_plaintext_sample100.txt.xml";

	# 3 lines
	#xmlfilename = "C:\Users\Lawrence\Documents\stanford-corenlp-full-2015-01-30\sample_plaintext.txt.xml";
	# 100 real descriptions
	xmlfilename = "C:\Users\Lawrence\Documents\stanford-corenlp-full-2015-01-30\Parking_plaintext_sample100_periods.txt.xml";

	tree = ET.parse(xmlfilename);
	root = tree.getroot();

	for document in root:
		print "in document"; 
		sentencesCounter = 0;
		for sentences in document.findall('sentences'):
			print "in sentences ";# + str(sentencesCounter);
			sentenceCounter = 1;
			for sentence in sentences:
				if sentenceCounter < 4:
					print "in sentence " + str(sentenceCounter);
					for tokens in sentence.findall('tokens'):
						#print "in tokens";
						tokenCounter = 0;
						timeCounter = 0;
						timexCounter = 0;
						for token in tokens:
							tokenCounter = tokenCounter + 1;
							for timex in token.findall('Timex'):
								timexCounter = timexCounter + 1;
								#print "in element "+timex.get('type')+".";
								if timex.get('type') == 'TIME':
									timeCounter = timeCounter + 1;
									print ("Timex: " + 
									str(timex.tag) + " " + 
									str(timex.attrib) + " " +
									timex.text);
							
						print "There were "+str(tokenCounter)+" tokens in this \"tokens\"";
						tokenCounter = 0;
						if timexCounter != 0:
							print "There were "+str(timexCounter)+" timex elements.";
						timexCounter = 0;
						if timeCounter != 0:
							print 'There were '+str(timeCounter)+' TIME elements here.';
						timeCounter = 0;

				sentenceCounter = sentenceCounter + 1;
			sentencesCounter = sentencesCounter + 1;



