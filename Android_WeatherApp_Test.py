import unittest, time, os
from appium import webdriver
import time
class Android_WeatherApp_Test(unittest.TestCase):
    
    def setUp(self):
        
        desired_caps = {}
        desired_caps[‘platformName’] = ‘Android’
        desired_caps[‘platformVersion’] = ‘6.0’
        desired_caps[‘deviceName’] = ‘MyPhone’
        
        desired_caps[‘appPackage’] = ‘com.macropinch.swan’
        desired_caps[‘appActivity’] = ‘com.macropinch.swan.WeatherActivity2’
        
        self.driver = webdriver.Remote(‘http://localhost:4723/wd/hub’, desired_caps)
    def tearDown(self):
        '''Tear down the test'''
        self.driver.quit()
    def test_wifi(self):
        self.driver.implicitly_wait(30)
        time.sleep(5)
        print "Testing"
		city = raw_input("Enter the city name to be checked: ")
		city = "India"
        city = city.title()
       getcity = self.driver.find_element_by_xpath("//android.widget.TextView[@index=’0′]")
        
        if city not in getcity.get_attribute(‘text’):
            mcity = self.driver.find_element_by_xpath("//android.widget.TextView[@index=’0′]")
            mcity.click()
            tempcity = self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id=’android:id/text1′]")
            tempcity.click()
            time.sleep(2)
        print "Checking temperature in Hyderabad Area.."
        gettemp = self.driver.find_element_by_xpath("//android.widget.TextView[@index=’1′]")
        print "Temp is :",gettemp.get_attribute(‘text’)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Android_WeatherApp_Test)
    unittest.TextTestRunner(verbosity=2).run(suite)