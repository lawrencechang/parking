# Test to see if the time-regex's encompass everything necessary
# I found that there are many lines that hit multiple regex's, 
# but for legitimate reasons. These signs actually have multiple
# time blocks, like different times for weekdays and weekends, all
# on the same sign.
# Instead of trying to find only unique lines, I'll keep a count
# of all the unique lines seen.

def testTimeRegex(inputfilename,scriptfilename):
	import json;
	import re;

	import removeDashesBetweenTimes;
	times_AM_AM = removeDashesBetweenTimes.times_AM_AM;
	times_AM_PM = removeDashesBetweenTimes.times_AM_PM;
	times_PM_AM = removeDashesBetweenTimes.times_PM_AM;
	times_PM_PM = removeDashesBetweenTimes.times_PM_PM;
	times_AM_none = removeDashesBetweenTimes.times_AM_none;
	times_none_AM = removeDashesBetweenTimes.times_none_AM;
	times_PM_none = removeDashesBetweenTimes.times_PM_none;
	times_none_PM = removeDashesBetweenTimes.times_none_PM;

	# Count 
	jsonfile = open(inputfilename, 'r');
	data = json.load(jsonfile);

	# regex flags
	no_case = re.I;

	times_regexes = ([times_AM_AM,times_AM_PM,times_PM_AM,times_PM_PM,
					times_AM_none,times_none_AM,times_PM_none,times_none_PM]);

	count = 0;
	totalLines = 0;

	# in case multiple lines fit the same regex, keep a dictionary of IDs seen
	seen = {};

	for i in range(len(times_regexes)):
		current_regex = times_regexes[i];
		#print "Current regex is " + current_regex;
		for line in data:
			description = line['description'];
			matchobj = re.search(current_regex,description,no_case);
			if not(matchobj is None):
				if seen.has_key(line['id']):
					None;
					#print 'Line already seen!';
					#print data[line['id']]['description'];
				else:
					seen[line['id']] = True;
					count = count + 1;

	print "Total number of lines is: " + str(len(data));
	print "The count for unique lines fitting our 8 regex's is: " + str(count);

if __name__ == '__main__':
	#inputfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_cleanarrow_sample.json";
	#outputfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_cleanarrow_cleantime_sample.json";
	inputfilename = "C:\Users\Lawrence\Documents\parking\data\Parking_cleanarrow.json";
	scriptfilename = "C:\Users\Lawrence\Documents\parking\src\removeDashesBetweenTimes.json";
	testTimeRegex(inputfilename,scriptfilename);
