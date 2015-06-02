# Replace sentence beginnings with a duration
# Ex. 1 hour, 1 hr, 2 hour, 2 hr, etc
# The parser seems to have a probme with some of these sentences...

import re;
no_case = re.I;

# Regular expression explanation
# Beginning of line, any number of digits, whitespace, hour or hr
hour_regex = r'^([\d]*)\s(hour|hr)';
hour_number_regex = r'^\d*';

def cleanHours(inputFilename,outputFilename):
	import json;
	inputfile = open(inputFilename, 'r')
	outputfile = open(outputFilename, 'w')
	data = json.load(inputfile);

	outputjsonlist = [];

	for line in data:
		obj = None;
		description = line['description'];
		obj = re.match(hour_regex,description,re.I);
		if not obj is None:
			#print 'matched hour regex!';
			#print 'description: '+description;
			hourNumberAsString = obj.group(1);
			hourNumberAsInt = int(hourNumberAsString);
			hourNumberSpelledOut = translate(hourNumberAsInt);
			description = re.sub(hour_number_regex,hourNumberSpelledOut,description);
			#print 'description after: '+description;
		line['description'] = description;
		outputjsonlist.append(line);
	json.dump(outputjsonlist,outputfile);
	outputfile.close();
	inputfile.close();

def translate(numberAsInt):
	if numberAsInt == 0:
		return 'zero';
	elif numberAsInt == 1:
		return 'one';
	elif numberAsInt == 2:
		return 'two';
	elif numberAsInt == 3:
		return 'three';
	elif numberAsInt == 4:
		return 'four';
	elif numberAsInt == 5:
		return 'five';
	elif numberAsInt == 6:
		return 'six';
	elif numberAsInt == 7:
		return 'seven';
	elif numberAsInt == 8:
		return 'eight';
	elif numberAsInt == 9:
		return 'nine';
	elif numberAsInt == 10:
		return 'ten';
	elif numberAsInt == 11:
		return 'eleven';
	elif numberAsInt == 12:
		return 'twelve';
	elif numberAsInt == 13:
		return 'thirteen';
	elif numberAsInt == 14:
		return 'fourteen';
	elif numberAsInt == 15:
		return 'fifteen';
	elif numberAsInt == 16:
		return 'sixteen';
	elif numberAsInt == 17:
		return 'seventeen';
	elif numberAsInt == 18:
		return 'eightteen';
	elif numberAsInt == 19:
		return 'nineteen';
	elif numberAsInt == 20:
		return 'twenty';
	elif numberAsInt == 21:
		return 'twentyone';
	elif numberAsInt == 22:
		return 'twentytwo';
	elif numberAsInt == 23:
		return 'twentythree';
	elif numberAsInt == 24:
		return 'twentyfour';
	else:
		return 'number-too-large';