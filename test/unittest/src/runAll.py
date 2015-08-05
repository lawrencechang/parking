import unittest;

import createTimeSlotHTMLsTest;
import findPhrasesTest;
import jsonHelperTest;
import addTimeSlotsTest;

def runAllTests():
	testSuite = unittest.TestSuite([
		createTimeSlotHTMLsTest.getSuite(),
		findPhrasesTest.getSuite(),
		jsonHelperTest.getSuite(),
		addTimeSlotsTest.getSuite()
	]);
	unittest.TextTestRunner(verbosity=2).run(testSuite);

if __name__ == '__main__':
	runAllTests();