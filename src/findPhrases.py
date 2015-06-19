# Find instances of the phrases, store results in JSON as new fields

import time;

noparking_regex = r'no[\s\S]parking';
nostopping_regex = r'no[\s\S]stopping';
nostanding_regex = r'no[\s\S]standing';
anytime_regex = r'\sanytime(\s|\Z)';
sunday_regex = r'\ssunday(\s|\Z)';
monday_regex = r'\smonday(\s|\Z)';
tuesday_regex = r'\stuesday(\s|\Z)';
wednesday_regex = r'\swednesday(\s|\Z)';
thursday_regex = r'\sthursday(\s|\Z)';
friday_regex = r'\sfriday(\s|\Z)';
saturday_regex = r'\ssaturday(\s|\Z)';
exceptAnywordRegex =r'\sexcept\s([^\s]+)(\s|\Z)'; 
# exceptSundayRegex = r'\sexcept\s(sunday)(\s|\Z)';
# exceptMondayRegex = r'\sexcept\s(monday)(\s|\Z)';
# exceptTuesdayRegex = r'\sexcept\s(tuesday)(\s|\Z)';
# exceptWednesdayRegex = r'\sexcept\s(wednesday)(\s|\Z)';
# exceptThursdayRegex = r'\sexcept\s(thursday)(\s|\Z)';
# exceptFridayRegex = r'\sexcept\s(friday)(\s|\Z)';
# exceptSaturdayRegex = r'\sexcept\s(saturday)(\s|\Z)';

def run(inputJSONFilename,outputJSONFilename):
	import re;
	import json;
	inputJSONFile = open(inputJSONFilename, 'r');
	outputJSONFile = open(outputJSONFilename, 'w');
	inputJSON = json.load(inputJSONFile);

	outputJSONList = [];

	matchobj_parking = None;
	matchobj_stopping = None;
	matchobj_standing = None;
	matchobj_anytime = None;
	matchobj_day = None;
	description = "";

	startTime = time.time();
	for line in inputJSON:
		description = line['description'];

		matchobj_parking = re.search(noparking_regex,description,re.I);
		if not(matchobj_parking is None):
			line['no_parking'] = 'true';
		else:
			line['no_parking'] = 'false';
		matchobj_stopping = re.search(nostopping_regex,description,re.I);
		if not(matchobj_stopping is None):
			line['no_stopping'] = 'true';
		else:
			line['no_stopping'] = 'false';
		matchobj_standing = re.search(nostanding_regex,description,re.I);
		if not(matchobj_standing is None):
			line['no_standing'] = 'true';
		else:
			line['no_standing'] = 'false';

		# "anytime" token
		matchobj_anytime = re.search(anytime_regex,description,re.I);
		if not(matchobj_anytime is None):
			line['anytime'] = 'true';
		else:
			line['anytime'] = 'false';

		# Days of the week
		matchobj_day = re.search(sunday_regex,description,re.I);
		if not(matchobj_day is None):
			line['sunday'] = 'true';
		else:
			line['sunday'] = 'false';
		matchobj_day = re.search(monday_regex,description,re.I);
		if not(matchobj_day is None):
			line['monday'] = 'true';
		else:
			line['monday'] = 'false';
		matchobj_day = re.search(tuesday_regex,description,re.I);
		if not(matchobj_day is None):
			line['tuesday'] = 'true';
		else:
			line['tuesday'] = 'false';
		matchobj_day = re.search(wednesday_regex,description,re.I);
		if not(matchobj_day is None):
			line['wednesday'] = 'true';
		else:
			line['wednesday'] = 'false';
		matchobj_day = re.search(thursday_regex,description,re.I);
		if not(matchobj_day is None):
			line['thursday'] = 'true';
		else:
			line['thursday'] = 'false';
		matchobj_day = re.search(friday_regex,description,re.I);
		if not(matchobj_day is None):
			line['friday'] = 'true';
		else:
			line['friday'] = 'false';
		matchobj_day = re.search(saturday_regex,description,re.I);
		if not(matchobj_day is None):
			line['saturday'] = 'true';
		else:
			line['saturday'] = 'false';

		# except days
		matchobj_except = re.search(exceptAnywordRegex,description,re.I);
		line['exceptSunday'] = 'false';
		line['exceptMonday'] = 'false';
		line['exceptTuesday'] = 'false';
		line['exceptWednesday'] = 'false';
		line['exceptThursday'] = 'false';
		line['exceptFriday'] = 'false';
		line['exceptSaturday'] = 'false';
		if not (matchobj_except is None) and not (matchobj_except.group(1) is None):
			# lower() makes a string lowercase
			day = matchobj_except.group(1).lower();
			if day == 'sunday':
				line['exceptSunday'] = 'true'
			elif day == 'monday':
				line['exceptMonday'] = 'true';
			elif day == 'tuesday':
				line['exceptTuesday'] = 'true';
			elif day == 'wednesday':
				line['exceptWednesday'] = 'true';
			elif day == 'thursday':
				line['exceptThursday'] = 'true';
			elif day == 'friday':
				line['exceptFriday'] = 'true';
			elif day == 'saturday':
				line['exceptSaturday'] = 'true';

		outputJSONList.append(line);
	endTime = time.time();
	print "Elapsed time was: " + str(endTime - startTime);

	json.dump(outputJSONList,outputJSONFile);
	outputJSONFile.close();

if __name__ == '__main__':
	inputJSONFilename = "";
	outputJSONFilename = "";
	run(inputJSONFilename,outputJSONFilename);
