# Used to print out time slots and their values, clearly.

def printTimeSlots(jsonLine):
	periods = ['am','pm'];
	hours = [0,1,2,3,4,5,6,7,8,9,10,11];
	minutes = ['00','15','30','45'];
	days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];

	print "__________  S  M  T  W  Th  F  S"
	for period in periods:
		for hour in hours:
			for minute in minutes:
				fieldname = 'time'+hourToString(hour)+str(minute)+period;
				print fieldname,;
				for day in days:
					if jsonLine['valid'+day] == 'true':
						print ' '+jsonLine[fieldname],;
					else:
						print ' '+'f',;
				print '';


def hourToString(hourAsInt):
	hourAsString = str(hourAsInt);
	if len(hourAsString) == 1:
		return '0'+hourAsString;
	return hourAsString;