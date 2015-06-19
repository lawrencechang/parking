# Find out which days are "valid" per these hard coded rules

# I think this functionality is sneaky complicated.
# All entries are some combination of sunday - saturday, and
# except xxx-day. 
# Can I assume that if there's an "except xxx-day", then there aren't
# other day indicators?
# Perhaps assume, then check for it, and print it out as a warning.
def getValidDaysList(jsonObject):
	validDaysList = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday'];
	if jsonObject['exceptSunday'] == 'true':
		validDaysList.remove('sunday');
		return validDaysList;
	elif jsonObject['exceptMonday'] == 'true':
		validDaysList.remove('monday');
		return validDaysList;
	elif jsonObject['exceptTuesday'] == 'true':
		validDaysList.remove('tuesday');
		return validDaysList;
	elif jsonObject['exceptWednesday'] == 'true':
		validDaysList.remove('wednesday');
		return validDaysList;
	elif jsonObject['exceptThursday'] == 'true':
		validDaysList.remove('thursday');
		return validDaysList;
	elif jsonObject['exceptFriday'] == 'true':
		validDaysList.remove('friday');
		return validDaysList;
	elif jsonObject['exceptSaturday'] == 'true':
		validDaysList.remove('saturday');
		return validDaysList;

	if jsonObject['sunday'] == 'false':
		validDaysList.remove('sunday');
	if jsonObject['monday'] == 'false':
		validDaysList.remove('monday');
	if jsonObject['tuesday'] == 'false':
		validDaysList.remove('tuesday');
	if jsonObject['wednesday'] == 'false':
		validDaysList.remove('wednesday');
	if jsonObject['thursday'] == 'false':
		validDaysList.remove('thursday');
	if jsonObject['friday'] == 'false':
		validDaysList.remove('friday');
	if jsonObject['saturday'] == 'false':
		validDaysList.remove('saturday');

	return validDaysList;

def run(inputJSONFilename,outputJSONFilename,directory):
	import shutil;
	import os;
	# Save current working directory
	originalDirectory = os.getcwd();
	# Go to directory
	os.chdir(directory);
	# Open files
	import json;
	jsonFile = open(inputJSONFilename,'r');
	jsonData = json.load(jsonFile);
	jsonFile.close();
	outputJSONFile = open(outputJSONFilename, 'w');

	# variables
	days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday'];
	outputList = [];
	validDays = [];
	# For each line in input json
	for line in jsonData:
		# Get list of valid days
		validDays = getValidDaysList(line);
		# Add the 7 entries to the line
		for day in days:
			if day in validDays:
				line['valid'+day.capitalize()] = 'true';
			else:
				line['valid'+day.capitalize()] = 'false';
		# Append to new JSON list
		outputList.append(line);
	# Write JSON list to output file
	json.dump(outputList,outputJSONFile);
	outputJSONFile.close();
	# Go back to original directory
	os.chdir(originalDirectory);

