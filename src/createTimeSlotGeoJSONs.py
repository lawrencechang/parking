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
			try:
				featureList.append(geoJSONObject['features'][index]);
			except:
				print "Error."
				print "index: "+str(index);
				print "geojson: "+geojson.dumps(geoJSONObject['features'][index]);
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
			try:
				currentGeoJSONObject = geoJSONObject['features'][index];
				geometry = currentGeoJSONObject['geometry'];
				idNum = currentGeoJSONObject['id']
				featureList.append(geojson.Feature(geometry=geometry,id=idNum));
			except:
				print "Error."
				print "index: "+str(index);
				print "geojson: "+geojson.dumps(geoJSONObject['features'][index]);
				raise;

		currentGeoJSONFilename = outputDir+htmlFilename.rstrip('.html')+'.json';
		geojson.dump(geojson.FeatureCollection(featureList),open(currentGeoJSONFilename,'w'));

