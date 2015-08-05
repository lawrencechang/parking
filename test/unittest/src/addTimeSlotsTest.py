# addTimeSlots unit test

import os;
import sys;
sys.path.append(os.path.expanduser('~')+"/Documents/ucla/parking/src/");
import unittest;
import addTimeSlots;
import collections;

class createAddTimeSlotsTests(unittest.TestCase):
	def testAlwaysPass(self):
		self.assertTrue(True);

	def testGetStartMin(self):
		MinuteString = collections.namedtuple(
			'MinuteString', 
			'minuteInput stringResult');
		testList = [
			MinuteString(0,'00'),
			MinuteString(15,'15'),
			MinuteString(30,'30'),
			MinuteString(45,'45'),
		];

		for entry in testList:
			result = addTimeSlots.getStartMin(entry.minuteInput)
			try:
				self.assertEqual(entry.stringResult,result);
			except AssertionError:
				print "AssertionError in addTimeSlotsTest.";
				print "input: "+str(entry.minuteInput);
				print "output: "+str(result);
				print "expected output: "+entry.stringResult;
				raise;

def getSuite():
	return unittest.TestLoader().loadTestsFromTestCase(createAddTimeSlotsTests);

if __name__ == '__main__':
	unittest.main();