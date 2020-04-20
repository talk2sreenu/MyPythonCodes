'''
Created on Apr 20, 2020

@author: talk2
'''
import unittest

import seleniumScripts.UnitTestExample

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(seleniumScripts.UnitTestExample))
#suite.addTests(loader.loadTestsFromModule(seleniumScripts.MySimpleUnitTest))
runner = unittest.TextTestRunner(verbosity=3)

result = runner.run(suite)
