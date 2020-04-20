'''
Created on Apr 19, 2020

@author: talk2
'''
from selenium import webdriver


def initializeDriver(browserType):
    if browserType.upper() == "CHROME":
        print('Initializing Chrome Driver value')
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe");
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(20)
    return driver
    