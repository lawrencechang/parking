# Getting statistics regarding the term "except"
# At a cursory glance, every instance of "except" applies to "sunday",
# which implies that the sign is valid for every day of the week
# except sunday.
# Get the count of all "except"s.
# For each "except", keep track of the word (hopefully the day of week) after it.
# Print statistics.

def exceptStats(jsonFilename):
	import json;
	import re;
	from collections import Counter;

	inputfile = open(jsonFilename, 'r');
	data = json.load(inputfile);
	except_regex = r'([\s]except[\s])([^\s]+)(\s|\Z)';
	wordList = [];

	for line in data:
		description = line['description'];
		match = re.search(except_regex,description,re.I);
		if not (match is None):
			wordList.append(match.group(2));

	counts = Counter(wordList);
	print(counts);

	#return data;