import os;
import sys;
sys.path.append(os.path.expanduser('~')+"/Documents/ucla/parking/src/");

import unittest;
import jsonHelper;
import collections;
import json;
import geojson;

class createJSONHelperTests(unittest.TestCase):
	def testAlwaysPass(self):
		self.assertTrue(True);

	'''
	def testConvertToGeoJSON(self):
		JSONGeoJSON = collections.namedtuple(
			'JSONGeoJSON', 
			'jsonObject geoJSONObject');

		jsonDict = {};
		jsonDict['id'] = 100;
		jsonDict['y'] = 40.1234567890012345;
		jsonDict['x'] = 40.1234567890012345;
		point = geojson.Point((jsonDict['y'],jsonDict['x']));
		geoJSONFeature = geojson.Feature(geometry=point,id=jsonDict['id']);
		geoJSONFeatureCollection = geojson.FeatureCollection([geoJSONFeature]);
		testList = [
			JSONGeoJSON(json.dumps(jsonDict),geoJSONFeatureCollection),
		];
		jsonLine = {};
		jsonResult = None;
		for entry in testList:
			jsonObject = entry.jsonObject;
			geoJSONObject = jsonHelper.convertToGeoJSON(jsonLine);
			try:
				self.assertEqual(entry.geoJSONObject,geoJSONObject);
			except AssertionError:
				print "\n"+"jsonObject: "+json.dumps(jsonObject);
				print "expected geojson: "+geojson.dumps(entry.geoJSONObject);
				print "result geojson: "+geojson.dumps(geoJSONObject);
				raise;
	'''
def getSuite():
	return unittest.TestLoader().loadTestsFromTestCase(createJSONHelperTests);

if __name__ == '__main__':
	unittest.main();