import os;
import sys;
sys.path.append(os.path.expanduser('~')+"/Documents/ucla/parking/src/");

import unittest;
import findPhrases;
import collections;
import traceback;

class createFindPhrasesTests(unittest.TestCase):
	def testNoParkingVariety(self):
		DescParkStopStand = collections.namedtuple(
			'DescParkStopStand', 
			'description parkResult standResult stopResult');
		testList = [
			DescParkStopStand('hello','false','false','false'),
			DescParkStopStand('no parking','true','false','false'),
			DescParkStopStand('no standing','false','true','false'),
			DescParkStopStand('no stopping','false','false','true'),
			DescParkStopStand('No parking','true','false','false'),
			DescParkStopStand('no Standing','false','true','false'),
			DescParkStopStand('nO stopping','false','false','true'),
			DescParkStopStand(' no parking','true','false','false'),
			DescParkStopStand(' no standing','false','true','false'),
			DescParkStopStand(' no stopping','false','false','true'),
			DescParkStopStand('no parking ','true','false','false'),
			DescParkStopStand('no standing ','false','true','false'),
			DescParkStopStand('no stopping ','false','false','true'),
			DescParkStopStand(' no parking ','true','false','false'),
			DescParkStopStand(' no standing ','false','true','false'),
			DescParkStopStand(' no stopping ','false','false','true'),
			DescParkStopStand('no   parking','true','false','false'),
			DescParkStopStand('no   standing','false','true','false'),
			DescParkStopStand('no   stopping','false','false','true'),
			DescParkStopStand('no-parking','true','false','false'),
			DescParkStopStand('no_standing','false','true','false'),
			DescParkStopStand('noxstopping','false','false','true'),

			DescParkStopStand('xno parking','false','false','false'),
			DescParkStopStand('noparking','false','false','false'),
			DescParkStopStand('no parkingx','false','false','false'),
			DescParkStopStand('x 3 x 10:00 no parking','true','false','false'),
			DescParkStopStand('23 29xj9 no parking x92 10:00','true','false','false'),

			DescParkStopStand('xno standing','false','false','false'),
			DescParkStopStand('nostanding','false','false','false'),
			DescParkStopStand('no standingx','false','false','false'),
			DescParkStopStand('x 3 x 10:00 no standing','false','true','false'),
			DescParkStopStand('23 29xj9 no standing x92 10:00','false','true','false'),

			DescParkStopStand('xno stopping','false','false','false'),
			DescParkStopStand('nostopping','false','false','false'),
			DescParkStopStand('no stoppingx','false','false','false'),
			DescParkStopStand('x 3 x 10:00 no stopping','false','false','true'),
			DescParkStopStand('23 29xj9 no stopping x92 10:00','false','false','true'),

		];

		jsonLine = {};
		jsonResult = None;
		for entry in testList:
			jsonLine['description'] = entry.description;
			jsonResult = findPhrases.addPhrasesNoParkingVariety(jsonLine);
			try:
				self.assertEqual(entry.parkResult,jsonResult['no_parking']);
				self.assertEqual(entry.standResult,jsonResult['no_standing']);
				self.assertEqual(entry.stopResult,jsonResult['no_stopping']);
			except AssertionError:
				print ("\nDescription: \""+entry.description+"\""+
					"\nparkResult: "+entry.parkResult+
					", standResult: "+entry.standResult+
					", stopResult: "+entry.stopResult+
					"\nno_parking: "+jsonResult['no_parking']+
					", no_standing: "+jsonResult['no_standing']+
					", no_stopping: "+jsonResult['no_stopping']
					);
				raise;

	def testAnytime(self):
		DescResult = collections.namedtuple(
			'DescResult', 
			'description result');
		testList = [
			DescResult('anytime','true'),
			DescResult(' anytime','true'),
			DescResult('anytime ','true'),
			DescResult(' AnytiMe','true'),
			DescResult('Anytime','true'),
			DescResult('anyTime','true'),
			DescResult('no parking anytime','true'),
			DescResult('anytimee','false'),
			DescResult('any time','true'),
			DescResult('anytime is a good time','true'),
			DescResult('anytimeanytime','false'),
			DescResult('anytime anytime','true'),

		];
		jsonLine = {};
		jsonResult = None;
		for entry in testList:
			jsonLine['description'] = entry.description;
			jsonResult = findPhrases.addPhraseAnytime(jsonLine);
			try:
				self.assertEqual(entry.result,jsonResult['anytime']);
			except AssertionError:
				print ("\nDescription: \""+entry.description+"\""+
					"\nresult: "+entry.result+
					"\nanytime field: "+jsonResult['anytime']
					);
				raise;

	def testDaysOfWeek(self):
		DescDays = collections.namedtuple(
			'DescResult', 
			'description sun mon tues wed thurs fri sat');
		testList = [
			DescDays('sunday','true','false','false','false','false','false','false'),
			DescDays('monday','false','true','false','false','false','false','false'),
			DescDays('tuesday','false','false','true','false','false','false','false'),
			DescDays('wednesday','false','false','false','true','false','false','false'),
			DescDays('thursday','false','false','false','false','true','false','false'),
			DescDays('friday','false','false','false','false','false','true','false'),
			DescDays('saturday','false','false','false','false','false','false','true'),
			DescDays(' sunday','true','false','false','false','false','false','false'),
			DescDays(' monday','false','true','false','false','false','false','false'),
			DescDays(' tuesday','false','false','true','false','false','false','false'),
			DescDays(' wednesday','false','false','false','true','false','false','false'),
			DescDays(' thursday','false','false','false','false','true','false','false'),
			DescDays(' friday','false','false','false','false','false','true','false'),
			DescDays(' saturday','false','false','false','false','false','false','true'),
			DescDays('sunday ','true','false','false','false','false','false','false'),
			DescDays('monday ','false','true','false','false','false','false','false'),
			DescDays('tuesday ','false','false','true','false','false','false','false'),
			DescDays('wednesday ','false','false','false','true','false','false','false'),
			DescDays('thursday ','false','false','false','false','true','false','false'),
			DescDays('friday ','false','false','false','false','false','true','false'),
			DescDays('saturday ','false','false','false','false','false','false','true'),

			DescDays('xsunday','false','false','false','false','false','false','false'),
			DescDays('xmonday','false','false','false','false','false','false','false'),
			DescDays('xtuesday','false','false','false','false','false','false','false'),
			DescDays('xwednesday','false','false','false','false','false','false','false'),
			DescDays('xthursday','false','false','false','false','false','false','false'),
			DescDays('xfriday','false','false','false','false','false','false','false'),
			DescDays('xsaturday','false','false','false','false','false','false','false'),
			DescDays(' xsunday','false','false','false','false','false','false','false'),
			DescDays(' xmonday','false','false','false','false','false','false','false'),
			DescDays(' xtuesday','false','false','false','false','false','false','false'),
			DescDays(' xwednesday','false','false','false','false','false','false','false'),
			DescDays(' xthursday','false','false','false','false','false','false','false'),
			DescDays(' xfriday','false','false','false','false','false','false','false'),
			DescDays(' xsaturday','false','false','false','false','false','false','false'),
			DescDays('sundayx','false','false','false','false','false','false','false'),
			DescDays('mondayx','false','false','false','false','false','false','false'),
			DescDays('tuesdayx','false','false','false','false','false','false','false'),
			DescDays('wednesdayx','false','false','false','false','false','false','false'),
			DescDays('thursdayx','false','false','false','false','false','false','false'),
			DescDays('fridayx','false','false','false','false','false','false','false'),
			DescDays('saturdayx','false','false','false','false','false','false','false'),
			DescDays(' sundayx','false','false','false','false','false','false','false'),
			DescDays(' mondayx','false','false','false','false','false','false','false'),
			DescDays(' tuesdayx','false','false','false','false','false','false','false'),
			DescDays(' wednesdayx','false','false','false','false','false','false','false'),
			DescDays(' thursdayx','false','false','false','false','false','false','false'),
			DescDays(' fridayx','false','false','false','false','false','false','false'),
			DescDays(' saturdayx','false','false','false','false','false','false','false'),

			DescDays('a sunday','true','false','false','false','false','false','false'),
			DescDays('# monday','false','true','false','false','false','false','false'),
			DescDays('4 tuesday','false','false','true','false','false','false','false'),
			DescDays('wednesday a','false','false','false','true','false','false','false'),
			DescDays('thursday @','false','false','false','false','true','false','false'),
			DescDays('friday 9','false','false','false','false','false','true','false'),
			DescDays(' a saturday 3','false','false','false','false','false','false','true'),
		];
		jsonLine = {};
		jsonResult = None;
		for entry in testList:
			jsonLine['description'] = entry.description;
			jsonResult = findPhrases.addPhrasesDaysOfWeek(jsonLine);
			try:
				self.assertEqual(entry.sun,jsonResult['sunday']);
				self.assertEqual(entry.mon,jsonResult['monday']);
				self.assertEqual(entry.tues,jsonResult['tuesday']);
				self.assertEqual(entry.wed,jsonResult['wednesday']);
				self.assertEqual(entry.thurs,jsonResult['thursday']);
				self.assertEqual(entry.fri,jsonResult['friday']);
				self.assertEqual(entry.sat,jsonResult['saturday']);
			except AssertionError:
				print "\n"+"Description: \""+entry.description+"\"";
				print "sun expected: "+entry.sun+", result: "+jsonResult['sunday'];
				print "mon expected: "+entry.mon+", result: "+jsonResult['monday'];
				print "tues expected: "+entry.tues+", result: "+jsonResult['tuesday'];
				print "wed expected: "+entry.wed+", result: "+jsonResult['wednesday'];
				print "thurs expected: "+entry.thurs+", result: "+jsonResult['thursday'];
				print "fri expected: "+entry.fri+", result: "+jsonResult['friday'];
				print "sat expected: "+entry.sat+", result: "+jsonResult['saturday'];
				raise;

	def testExceptDays(self):
		self.assertTrue(True);
		DescDays = collections.namedtuple(
			'DescResult', 
			'description sun mon tues wed thurs fri sat');
		testList = [
			DescDays('except sunday','true','false','false','false','false','false','false'),
			DescDays('except monday','false','true','false','false','false','false','false'),
			DescDays('except tuesday','false','false','true','false','false','false','false'),
			DescDays('except wednesday','false','false','false','true','false','false','false'),
			DescDays('except thursday','false','false','false','false','true','false','false'),
			DescDays('except friday','false','false','false','false','false','true','false'),
			DescDays('except saturday','false','false','false','false','false','false','true'),
			DescDays(' except sunday','true','false','false','false','false','false','false'),
			DescDays(' except monday','false','true','false','false','false','false','false'),
			DescDays(' except tuesday','false','false','true','false','false','false','false'),
			DescDays(' except wednesday','false','false','false','true','false','false','false'),
			DescDays(' except thursday','false','false','false','false','true','false','false'),
			DescDays(' except friday','false','false','false','false','false','true','false'),
			DescDays(' except saturday','false','false','false','false','false','false','true'),
			DescDays('x except sunday','true','false','false','false','false','false','false'),
			DescDays('x except monday','false','true','false','false','false','false','false'),
			DescDays('x except tuesday','false','false','true','false','false','false','false'),
			DescDays('x except wednesday','false','false','false','true','false','false','false'),
			DescDays('x except thursday','false','false','false','false','true','false','false'),
			DescDays('x except friday','false','false','false','false','false','true','false'),
			DescDays('x except saturday','false','false','false','false','false','false','true'),
			DescDays('xexcept sunday','false','false','false','false','false','false','false'),
			DescDays('xexcept monday','false','false','false','false','false','false','false'),
			DescDays('xexcept tuesday','false','false','false','false','false','false','false'),
			DescDays('xexcept wednesday','false','false','false','false','false','false','false'),
			DescDays('xexcept thursday','false','false','false','false','false','false','false'),
			DescDays('xexcept friday','false','false','false','false','false','false','false'),
			DescDays('xexcept saturday','false','false','false','false','false','false','false'),
			DescDays(' xexcept sunday','false','false','false','false','false','false','false'),
			DescDays(' xexcept monday','false','false','false','false','false','false','false'),
			DescDays(' xexcept tuesday','false','false','false','false','false','false','false'),
			DescDays(' xexcept wednesday','false','false','false','false','false','false','false'),
			DescDays(' xexcept thursday','false','false','false','false','false','false','false'),
			DescDays(' xexcept friday','false','false','false','false','false','false','false'),
			DescDays(' xexcept saturday','false','false','false','false','false','false','false'),
			DescDays('except sunday ','true','false','false','false','false','false','false'),
			DescDays('except monday ','false','true','false','false','false','false','false'),
			DescDays('except tuesday ','false','false','true','false','false','false','false'),
			DescDays('except wednesday ','false','false','false','true','false','false','false'),
			DescDays('except thursday ','false','false','false','false','true','false','false'),
			DescDays('except friday ','false','false','false','false','false','true','false'),
			DescDays('except saturday ','false','false','false','false','false','false','true'),
			DescDays('except sunday x','true','false','false','false','false','false','false'),
			DescDays('except monday x','false','true','false','false','false','false','false'),
			DescDays('except tuesday x','false','false','true','false','false','false','false'),
			DescDays('except wednesday x','false','false','false','true','false','false','false'),
			DescDays('except thursday x','false','false','false','false','true','false','false'),
			DescDays('except friday x','false','false','false','false','false','true','false'),
			DescDays('except saturday x','false','false','false','false','false','false','true'),
			# One of's
			DescDays('except saturdayx','false','false','false','false','false','false','false'),
			DescDays(' except saturdayx','false','false','false','false','false','false','false'),
			DescDays('except saturdayx ','false','false','false','false','false','false','false'),
			DescDays(' except saturdayx ','false','false','false','false','false','false','false'),
			DescDays('except   saturday','false','false','false','false','false','false','true'),
			DescDays('Except Sunday','true','false','false','false','false','false','false'),
			DescDays('EXCEPT MONDAY','false','true','false','false','false','false','false'),
			DescDays('NO STANDING EXCEPT TRUCKS LOADING & UNLOADING 8AM 7PM EXCEPT SUNDAY','true','false','false','false','false','false','false'),

		];
		jsonLine = {};
		jsonResult = None;
		for entry in testList:
			jsonLine['description'] = entry.description;
			jsonResult = findPhrases.addPhrasesExceptDays(jsonLine);
			try:
				self.assertEqual(entry.sun,jsonResult['exceptSunday']);
				self.assertEqual(entry.mon,jsonResult['exceptMonday']);
				self.assertEqual(entry.tues,jsonResult['exceptTuesday']);
				self.assertEqual(entry.wed,jsonResult['exceptWednesday']);
				self.assertEqual(entry.thurs,jsonResult['exceptThursday']);
				self.assertEqual(entry.fri,jsonResult['exceptFriday']);
				self.assertEqual(entry.sat,jsonResult['exceptSaturday']);
			except AssertionError:
				print "\n"+"Description: \""+entry.description+"\"";
				print "sun expected: "+entry.sun+", result: "+jsonResult['exceptSunday'];
				print "mon expected: "+entry.mon+", result: "+jsonResult['exceptMonday'];
				print "tues expected: "+entry.tues+", result: "+jsonResult['exceptTuesday'];
				print "wed expected: "+entry.wed+", result: "+jsonResult['exceptWednesday'];
				print "thurs expected: "+entry.thurs+", result: "+jsonResult['exceptThursday'];
				print "fri expected: "+entry.fri+", result: "+jsonResult['exceptFriday'];
				print "sat expected: "+entry.sat+", result: "+jsonResult['exceptSaturday'];
				raise;


def getSuite():
	return unittest.TestLoader().loadTestsFromTestCase(createFindPhrasesTests);

if __name__ == '__main__':
	unittest.main();