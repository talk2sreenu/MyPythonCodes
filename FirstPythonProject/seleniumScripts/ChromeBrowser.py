'''
Created on Apr 19, 2020

@author: talk2
'''
from selenium.webdriver.common.by import By

from seleniumScripts.captureScreenShot import takeScreenshot
from seleniumScripts.createDriver import initializeDriver

baseUrl = 'https://www.yahoo.com'

driver = initializeDriver("Chrome")

driver.get(baseUrl)

driver.get_log('driver')

driver.find_element_by_id('header-signin-link').click()
winHandle = driver.current_window_handle
print ("Window Handle is "+winHandle)

imageVal = driver.find_element_by_class_name('logo').is_displayed()
if imageVal == True:
    print('Yahoo Image displayed as expected')
    takeScreenshot(driver, 'logo')
    driver.save_screenshot("Image.png")
else:
    print("Yahoo image not displayed in the screen")
    
driver.find_element_by_name('username').send_keys('hello world')
buttnDisplay = driver.find_element_by_name('signin').is_displayed()
print("button displayed : "+ str(buttnDisplay))
driver.find_element(By.ID, 'mbr-forgot-link').click()
takeScreenshot(driver, 'forgot')
'''time.sleep(2)'''
'''driver.switch_to_window(winHandle)'''
driver.quit()