# Create geoJSON files for each time slot.
# Algorithm:
# For each filename
#	Go through all indeces, writing respective points to file
#	Off by 1 error?
# 	write a geojson file

def createGeoJSONs(geoJSONFilename,outputDir,indexFilenameListFilename,indexFileDir,verbose=False):
	import cPickle;
	import jsonHelper;
	import geojson;
	filenamesList = cPickle.load(open(indexFileDir+indexFilenameListFilename,'r'));

	import shutil;
	import os;
	if os.path.exists(outputDir):
		shutil.rmtree(outputDir);
	if not os.path.exists(outputDir):
		os.makedirs(outputDir);

	if verbose:
		print "Loading full geoJSON file..."
	geoJSONObject = jsonHelper.getGeoJSONObjectFromFile(geoJSONFilename);
	if verbose:
		print "Done."
	for filenameListIndex,(indexFilename,htmlFilename) in enumerate(filenamesList):
		if verbose:
			print "geoJSON file "+str(filenameListIndex)+": "+indexFilename;
		featureList = [];
		properties = {};
		indeces = cPickle.load(open(indexFileDir+indexFilename,'r'));
		for index in indeces:
			# Indeces were created when there was a header row.
			# Since geojson needs real data for each entry, we had to skip this
			# row when creating the total geojson file.
			# See jsonHelper.convertToGeoJSON for details.
			indexNoHeader = index - 1;
			try:
				featureList.append(geoJSONObject['features'][indexNoHeader]);
			except:
				print "Error."
				print "indexNoHeader: "+str(indexNoHeader);
				print "geoJSONFilename: "+geoJSONFilename;
				print "outputDir: "+outputDir;
				print "indexFilenameListFilename: "+indexFilenameListFilename;
				print "indexFileDir: "+indexFileDir;
				print "Size of filenamesList: "+str(len(filenamesList));
				print "Num of indeces: "+str(len(indeces));
				print "Size of geojson object features: "+str(len(geoJSONObject['features']));
				print "geojson: "+geojson.dumps(geoJSONObject['features'][indexNoHeader]);
				raise;

		currentGeoJSONFilename = outputDir+htmlFilename.rstrip('.html')+'.json';
		geojson.dump(geojson.FeatureCollection(featureList),open(currentGeoJSONFilename,'w'));

def createMinimalGeoJSONs(geoJSONFilename,outputDir,indexFilenameListFilename,indexFileDir,verbose=False):
	import cPickle;
	import jsonHelper;
	import geojson;
	filenamesList = cPickle.load(open(indexFileDir+indexFilenameListFilename,'r'));

	import shutil;
	import os;
	if os.path.exists(outputDir):
		shutil.rmtree(outputDir);
	if not os.path.exists(outputDir):
		os.makedirs(outputDir);

	if verbose:
		print "Loading full geoJSON file..."
	geoJSONObject = jsonHelper.getGeoJSONObjectFromFile(geoJSONFilename);
	if verbose:
		print "Done."
	for filenameListIndex,(indexFilename,htmlFilename) in enumerate(filenamesList):
		if verbose:
			print "geoJSON file "+str(filenameListIndex)+": "+indexFilename;
		featureList = [];
		properties = {};
		indeces = cPickle.load(open(indexFileDir+indexFilename,'r'));
		for index in indeces:
			# See comment in createGeoJSONs function.
			indexNoHeader = index - 1;
			try:
				currentGeoJSONObject = geoJSONObject['features'][indexNoHeader];
				geometry = currentGeoJSONObject['geometry'];
				idNum = currentGeoJSONObject['id']
				featureList.append(geojson.Feature(geometry=geometry,id=idNum));
			except:
				print "Error."
				print "indexNoHeader: "+str(indexNoHeader);
				print "geojson: "+geojson.dumps(geoJSONObject['features'][indexNoHeader]);
				raise;

		currentGeoJSONFilename = outputDir+htmlFilename.rstrip('.html')+'.json';
		geojson.dump(geojson.FeatureCollection(featureList),open(currentGeoJSONFilename,'w'));

