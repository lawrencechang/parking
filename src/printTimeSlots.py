# Used to print out time slots and their values, clearly.

def printTimeSlots(jsonLine):
	periods = ['am','pm'];
	hours = [0,1,2,3,4,5,6,7,8,9,10,11];
	minutes = ['00','15','30','45'];
	days = ['sun','mon','tues','wed','thurs','fri','sat'];

	print "__________  S  M  T  W  Th  F  S"
	for period in periods:
		for hour in hours:
			for minute in minutes:
				fieldname = 'time'+hourToString(hour)+str(minute)+period;
				print fieldname,;
				for day in days:
					print ' '+jsonLine[fieldname],;
				print '';


def hourToString(hourAsInt):
	hourAsString = str(hourAsInt);
	if len(hourAsString) == 1:
		return '0'+hourAsString;
	return hourAsString;