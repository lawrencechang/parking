# Data preprocessing pipeline
# Start with unaltered data
# Go through whatever preprocessing steps are defined here
# Produce output

def preprocess(inputfilename, outpufilename):
	tempfilename = "temp";

	# Clean up arrows
	import replaceArrows;
	replaceArrows.replaceArrows(inputfilename,tempfilename);

	# Rename temp file to output
	from os import rename;
	from os import remove;
	
	# remove file if it already exists
	try:
		remove(outputfilename);
	except:
		print "File " + outputfilename + " already exists. Deleted.";
	rename(tempfilename,outputfilename);
	print "Wrote " + outputfilename;


if __name__ == '__main__':
	jsonfilename = "C:\Users\Lawrence\Documents\masters_project\data_converted\Parking_Regulation_WSG84_sample.json";
	outputfilename = "C:\Users\Lawrence\Documents\masters_project\data_converted\Parking_clean_all.json";
	preprocess(jsonfilename,outputfilename);