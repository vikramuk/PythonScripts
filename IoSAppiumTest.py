#https://qxf2.com/blog/get-set-test-an-ios-app-using-appium-and-python/
import unittest
import os
from appium import webdriver
from time import sleep
 
class TableSearchTest(unittest.TestCase):
 
    def setUp(self):
        # Set up appium
        app = os.path.join(os.path.dirname(__file__),
                           'TableSearchwithUISearchController/Swift',
                           'Search.swift.app')
        app = os.path.abspath(app)
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '9.2',
                'deviceName': 'iPhone 5s',
                'bundleId':'com.example.apple-samplecode.Search-swift'
            })
 
 
    def test_search_field(self):
        # Search for an Apple device and click on it to view the details and navigate back
        # Find the search element and perform send keys action
        search_element = self.driver.find_element_by_xpath("//UIASearchBar[@name='Search']")
        search_element.send_keys("iPad")
        sleep(2)
        # Get the xpath of first element
        first_element = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]")
        # Assert that the text matches
        self.assertEqual('iPad', first_element.get_attribute('name'))
        # Perform click action
        first_element.click()
        sleep(2)
        # Click on search element
        self.driver.find_element_by_name("Search").click()
 
 
    def tearDown(self):
        self.driver.quit()
 
 
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TableSearchTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
