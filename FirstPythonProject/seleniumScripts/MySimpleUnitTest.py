'''
Created on Apr 20, 2020

@author: talk2
'''
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        print("Hello")


    def tearDown(self):
        print("How are you")


    def testName(self):
        print("Test Passed")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()