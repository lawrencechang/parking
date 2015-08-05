# Add fields to the JSON for every time slot in a day.
# This is to support the fusion table database querying
# Note - this does not support differing time slots on differing dates.
# For example - "No parking 8am - 10am mondays 7pm-9pm thursdays"

# Load main JSON
# Go through the time slots
# 	open appropriate time slot file
#	for a given index
#		put in appropriate field into the json object
# 

import jsonHelper;
import cPickle;

periods = ['am','pm'];
hours = ['00','01','02','03','04','05','06','07','08','09','10','11'];
minutes = [0,15,30,45];
days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday'];

def run(indexFileListFilename,indexFileListDir,inputJSONFilename,outputJSONFilename):
	data = jsonHelper.getJSONObjectFromFile(inputJSONFilename);
	fileList = []
	with open(indexFileListDir+indexFileListFilename,'r') as f:
		fileList = cPickle.load(f);

	# Go through all of JSON, filling in default values
	for period in periods:
		for hour in hours:
			for minute in minutes:
				for index in range(len(data)):
					#data[index][getFieldName(period,hour,minute)] = 'false';
					data[index][getFieldName(period,hour,minute)] = 'f';

	# Fill in actual values
	for period in periods:
		for hour in hours:
			for minute in minutes:
				for day in days:
					startMin = getStartMin(minute);
					endMin = getEndMin(minute); 
					filename = day+'TimeSlot'+hour+startMin+'-'+hour+endMin+'Index.pickle';
					indeces = cPickle.load(open(indexFileListDir+filename,'r'));
					for index in indeces:
						#data[index][getFieldName(period,hour,minute)] = 'true';
						data[index][getFieldName(period,hour,minute)] = 't';

	jsonHelper.writeJSONObjectIntoFile(data,outputJSONFilename);

def getStartMin(minInt):
	if minInt == 0:
		return '00';
	elif minInt == 15:
		return '15';
	elif minInt == 30:
		return '30';
	elif minInt == 45:
		return '45';
	else:
		raise Exception('getStartMin function given a minute that was undefined.');

def getEndMin(minInt):
	if minInt == 0:
		return '14';
	elif minInt == 15:
		return '29';
	elif minInt == 30:
		return '44';
	elif minInt == 45:
		return '59';
	else:
		raise Exception('getEndMin function given a minute that was undefined.');

def getFieldName(period,hour,minute):
	return 'time'+hour+getStartMin(minute)+period;