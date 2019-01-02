"""
https://qxf2.com/blog/identify-ui-elements-mobile-apps/
The test will show you how you can find UI elements by various methods like xpath, id, accessibility_id and android UIautomator
on a android calculator app
 
"""
import os
import unittest, time
from appium import webdriver
from time import sleep
 
class Android_Calculator(unittest.TestCase):
    "Class to run tests for android calculator"
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'DeviceID'        
        desired_caps['appPackage'] = 'com.android.calculator2'
        desired_caps['appActivity'] = 'com.android.calculator2.Calculator'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
 
    def tearDown(self):
        "Tear down the test"
        self.driver.quit()
 
    def test_calculator(self):
        "Testing android calculator"
        self.driver.implicitly_wait(10)
        # Find the UI element using xpath  
        self.driver.find_element_by_xpath("//android.widget.Button[@text='7']").click()
        self.driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.android.calculator2:id/mul']").click()
 
        # Find UI element using id
        self.driver.find_element_by_id("com.android.calculator2:id/digit7").click()
 
        # Find UI element using accessibility_id
        self.driver.find_element_by_accessibility_id('delete').click()
 
        # Find UI element using android UIautomator
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("3")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.android.calculator2:id/equal")').click()
 
        # Find UI element using class name
        result=self.driver.find_element_by_class_name("android.widget.EditText")
        print result.get_attribute('text')
 
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Android_Calculator)
    unittest.TextTestRunner(verbosity=2).run(suite)
