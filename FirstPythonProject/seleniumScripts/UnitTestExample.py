'''
Created on Apr 20, 2020

@author: talk2
'''
import unittest
from selenium import webdriver
#import pytest

class sampleTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("https://www.yahoo.com")
        
    def testName(self):
        self.signinLink = self.driver.find_element_by_id('header-signin-link')
        self.signinLink.click()
        winHandle = self.driver.current_window_handle
        print ("Window Handle is "+winHandle)
        
        imageVal = self.driver.find_element_by_class_name('logo').is_displayed()
        if imageVal == True:
            print('Yahoo Image displayed as expected')
            self.assertEqual(imageVal, True, "Logo Image displayed as expected")
            self.driver.save_screenshot("Image.png")
        else:
            print("Yahoo image not displayed in the screen")
            
    def tearDown(self):
        self.driver.quit()
       
if __name__=="__main__":
    unittest.main() 