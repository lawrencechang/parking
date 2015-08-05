# Find instances of the phrases, store results in JSON as new fields
from copy import deepcopy;
import time;
import re;
import json;

noparking_regex = r'(\s|\A)no(\s+|\S)parking(\s|\Z)';
nostopping_regex = r'(\s|\A)no(\s+|\S)stopping(\s|\Z)';
nostanding_regex = r'(\s|\A)no(\s+|\S)standing(\s|\Z)';
anytime_regex = r'(\s|\A)any(\s*)time(\s|\Z)';
sunday_regex = r'(\s|\A)sunday(\s|\Z)';
monday_regex = r'(\s|\A)monday(\s|\Z)';
tuesday_regex = r'(\s|\A)tuesday(\s|\Z)';
wednesday_regex = r'(\s|\A)wednesday(\s|\Z)';
thursday_regex = r'(\s|\A)thursday(\s|\Z)';
friday_regex = r'(\s|\A)friday(\s|\Z)';
saturday_regex = r'(\s|\A)saturday(\s|\Z)';
exceptAnywordRegex =r'(\s|\A)except\s+(\S+)(\s|\Z)'; 
exceptSundayRegex = r'(\s|\A)except\s+sunday(\s|\Z)';
exceptMondayRegex = r'(\s|\A)except\s+monday(\s|\Z)';
exceptTuesdayRegex = r'(\s|\A)except\s+tuesday(\s|\Z)';
exceptWednesdayRegex = r'(\s|\A)except\s+wednesday(\s|\Z)';
exceptThursdayRegex = r'(\s|\A)except\s+thursday(\s|\Z)';
exceptFridayRegex = r'(\s|\A)except\s+friday(\s|\Z)';
exceptSaturdayRegex = r'(\s|\A)except\s+saturday(\s|\Z)';
anyDayRegex = r'((sunday)|(monday)|(tuesday)|(wednesday)|(thursday)|(friday)|(saturday))';
thruRegex = anyDayRegex+'(\s)thru(\s)'+anyDayRegex;

def run(inputJSONFilename,outputJSONFilename):
	inputJSONFile = open(inputJSONFilename, 'r');
	outputJSONFile = open(outputJSONFilename, 'w');
	inputJSON = json.load(inputJSONFile);
	outputJSONList = [];
	startTime = time.time();
	for line in inputJSON:
		line = addPhrasesNoParkingVariety(line);
		line = addPhraseAnytime(line);
		line = addPhrasesDaysOfWeek(line);
		line = addPhrasesExceptDays(line);
		line = addThruBetweenDays(line);
		outputJSONList.append(line);
	endTime = time.time();
	print "Elapsed time was: " + str(endTime - startTime);
	json.dump(outputJSONList,outputJSONFile);
	outputJSONFile.close();

# Input a JSON line, output updated JSON line
def addPhrasesNoParkingVariety(jsonLine):
	line = deepcopy(jsonLine);
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
	return line;

def addPhraseAnytime(jsonLine):
	line = deepcopy(jsonLine);
	description = line['description'];
	matchobj_anytime = re.search(anytime_regex,description,re.I);
	if not(matchobj_anytime is None):
		line['anytime'] = 'true';
	else:
		line['anytime'] = 'false';
	return line;

def addPhrasesDaysOfWeek(jsonLine):
	line = deepcopy(jsonLine);
	description = line['description'];
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
	return line;

def addPhrasesExceptDays(jsonLine):
	line = deepcopy(jsonLine);
	description = line['description'];
	line['exceptSunday'] = 'false';
	line['exceptMonday'] = 'false';
	line['exceptTuesday'] = 'false';
	line['exceptWednesday'] = 'false';
	line['exceptThursday'] = 'false';
	line['exceptFriday'] = 'false';
	line['exceptSaturday'] = 'false';
	matchobj_exceptSunday = re.search(exceptSundayRegex,description,re.I);
	if not (matchobj_exceptSunday is None):
		line['exceptSunday'] = 'true';
		return line;
	matchobj_exceptMonday = re.search(exceptMondayRegex,description,re.I);
	if not (matchobj_exceptMonday is None):
		line['exceptMonday'] = 'true';
		return line;
	matchobj_exceptTuesday = re.search(exceptTuesdayRegex,description,re.I);
	if not (matchobj_exceptTuesday is None):
		line['exceptTuesday'] = 'true';
		return line;
	matchobj_exceptWednesday = re.search(exceptWednesdayRegex,description,re.I);
	if not (matchobj_exceptWednesday is None):
		line['exceptWednesday'] = 'true';
		return line;
	matchobj_exceptThursday = re.search(exceptThursdayRegex,description,re.I);
	if not (matchobj_exceptThursday is None):
		line['exceptThursday'] = 'true';
		return line;
	matchobj_exceptFriday = re.search(exceptFridayRegex,description,re.I);
	if not (matchobj_exceptFriday is None):
		line['exceptFriday'] = 'true';
		return line;
	matchobj_exceptSaturday = re.search(exceptSaturdayRegex,description,re.I);
	if not (matchobj_exceptSaturday is None):
		line['exceptSaturday'] = 'true';
		return line;
	return line;

# Look for instances of "(dayname) thru (dayname)"
# What if there are two or more such sets?
def addThruBetweenDays(jsonLine):
	line = deepcopy(jsonLine);
	description = line['description'];
	matchobj = re.search(thruRegex,description,re.I);
	line['thru'] = 'false';
	if not (matchobj is None):
		line['thru'] = 'true';
	return line;

def searchThru(text):
	searchobj = re.search(thruRegex,text,re.I);
	return searchobj;

def searchAnyDay(text):
	searchobj = re.search(anyDayRegex,text,re.I);
	return searchobj;
