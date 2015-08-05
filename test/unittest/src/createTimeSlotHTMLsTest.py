import os;
import sys;
sys.path.append(os.path.expanduser('~')+"/Documents/ucla/parking/src/");

import unittest;
import createTimeSlotHTMLs;
import collections;
import traceback;

class createTimeSlotHTMLsTests(unittest.TestCase):
	# Tries a variety of time slot indeces, and makes sure the returned
	# times are correct
	def testTimesFromSlotIndex(self):
		SlotStartEnd = collections.namedtuple('SlotStartEnd','slot start end');
		testList = [
			SlotStartEnd(0,'00:00','00:14'),
			SlotStartEnd(4,'01:00','01:14'),
			SlotStartEnd(5,'01:15','01:29'),
			SlotStartEnd(9,'02:15','02:29'),
			SlotStartEnd(14,'03:30','03:44'),
			SlotStartEnd(19,'04:45','04:59'),
			SlotStartEnd(20,'05:00','05:14'),
			SlotStartEnd(26,'06:30','06:44'),
			SlotStartEnd(29,'07:15','07:29'),
			SlotStartEnd(32,'08:00','08:14'),
			SlotStartEnd(39,'09:45','09:59'),
			SlotStartEnd(41,'10:15','10:29'),
			SlotStartEnd(44,'11:00','11:14'),
			SlotStartEnd(50,'12:30','12:44'),
			SlotStartEnd(55,'13:45','13:59'),
			SlotStartEnd(58,'14:30','14:44'),
			SlotStartEnd(61,'15:15','15:29'),
			SlotStartEnd(64,'16:00','16:14'),
			SlotStartEnd(71,'17:45','17:59'),
			SlotStartEnd(73,'18:15','18:29'),
			SlotStartEnd(78,'19:30','19:44'),
			SlotStartEnd(82,'20:30','20:44'),
			SlotStartEnd(84,'21:00','21:14'),
			SlotStartEnd(89,'22:15','22:29'),
			SlotStartEnd(95,'23:45','23:59')
		];
		for entry in testList:
			(start,end) = createTimeSlotHTMLs.startAndEndTimeFromTimeSlotIndex(entry.slot);
			try:
				self.assertEqual(start,entry.start);
				self.assertEqual(end,entry.end);
			except AssertionError:
				print "slot: "+entry.slot+", start: "+entry.start+", end: "+entry.end;
				raise;

	def testStartTimeIsAfterInclusive(self):
		TimeTimeResult = collections.namedtuple('TimeTimeResult', 'baseline newTime result');
		testList = [
			TimeTimeResult('','00:00',False),
			TimeTimeResult('00:00','',False),
			TimeTimeResult('00:00','00:00',True),
			TimeTimeResult('00:00','00:01',True),
			TimeTimeResult('00:01','00:00',False),
			TimeTimeResult('00:59','00:58',False),
			TimeTimeResult('01:00','00:59',False),
			TimeTimeResult('00:59','01:00',True),
			TimeTimeResult('00:59','01:01',True),
			TimeTimeResult('01:59','01:59',True),
			TimeTimeResult('02:00','01:58',False),
			TimeTimeResult('23:59','00:00',False),
			TimeTimeResult('23:59','22:59',False),
			TimeTimeResult('23:58','23:59',True),
			TimeTimeResult('22:59','22:59',True)
		];
		for entry in testList:
			baseline = entry.baseline;
			newTime = entry.newTime;
			result = entry.result;
			try:
				self.assertEqual(createTimeSlotHTMLs.startTimeIsAfterInclusive(baseline,newTime),
					result);
			except AssertionError:
				print ("baseline: "+entry.baseline+
					", newTime: "+entry.newTime+
					", result: "+str(entry.result)
					);
				raise;

	def testEndTimeIsBeforeInclusive(self):
		TimeTimeResult = collections.namedtuple('TimeTimeResult', 'baseline newTime result');
		testList = [
			TimeTimeResult('','00:00',False),
			TimeTimeResult('00:00','',False),
			TimeTimeResult('00:00','00:00',True),
			TimeTimeResult('00:00','00:01',False),
			TimeTimeResult('00:01','00:00',True),
			TimeTimeResult('00:59','00:58',True),
			TimeTimeResult('01:00','00:59',True),
			TimeTimeResult('00:59','01:00',False),
			TimeTimeResult('00:59','01:01',False),
			TimeTimeResult('01:59','01:59',True),
			TimeTimeResult('02:00','01:58',True),
			TimeTimeResult('23:59','00:00',True),
			TimeTimeResult('23:59','22:59',True),
			TimeTimeResult('23:58','23:59',False),
			TimeTimeResult('22:59','22:59',True),
			TimeTimeResult('12:59','13:00',False),
			TimeTimeResult('01:00','12:59',False)
		];
		for entry in testList:
			baseline = entry.baseline;
			newTime = entry.newTime;
			result = entry.result;
			try:
				self.assertEqual(createTimeSlotHTMLs.endTimeIsBeforeInclusive(baseline,newTime),
					result);
			except AssertionError:
				print ("baseline: "+entry.baseline+
					", newTime: "+entry.newTime+
					", result: "+str(entry.result)
					);
				raise;

def getSuite():
	return unittest.TestLoader().loadTestsFromTestCase(createTimeSlotHTMLsTests);
	
if __name__ == '__main__':
	unittest.main();