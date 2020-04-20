'''
Created on Apr 19, 2020

@author: talk2
'''
from selenium import webdriver
def takeScreenshot(driver, nameVal):
    driver.get_screenshot_as_file(nameVal +'.png')
    driver.get_screenshot_as_base64()