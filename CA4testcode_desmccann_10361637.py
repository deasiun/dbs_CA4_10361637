# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 16:15:25 2017

@author: Des McCann
DBS ID 10361637
Test code to validate functionality
#will need to change the readlog location to get this to work - when you come to run it.
"""

readlog=open('d:\\dbsc\\database\\changes_python.log.txt').readlines()
import unittest
from CA4withFN import fncount,loopbuild

class logchecks(unittest.TestCase):
    
    def test_Loop_Length(self):
        tesresult = len(readlog)# use LEN command on the readfile above.
        scriptresult =fncount(readlog) # use the script counter in the for loop of main program
        self.assertEqual(tesresult,scriptresult)#compare the results.

    def test_transaction_count(self):
        scriptresult =loopbuild(readlog)# cycle through the program looking for "--- etc" and count
        self.assertEqual(422,scriptresult)
if __name__ == '__main__':
    unittest.main()