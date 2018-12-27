import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import re
import sys
class Gmail_Login(unittest.TestCase):
    
    def setUp(self):
        self.username = raw_input("Enter Gmail Username : ")
        self.password = raw_input("Enter Gmail Password : ")
        self.driver = webdriver.Firefox()
    
    def test_gmail_inbox(self):
        driver = self.driver
        driver.get("http://www.gmail.com")
        time.sleep(5)        
        try:
            search = driver.find_element_by_id("Email")
            search.clear()
            search.send_keys(self.username)
            driver.find_element_by_id("next").click()        
            time.sleep(3)
            pswd = driver.find_element_by_xpath("//input[@id=’Passwd’]")
            pswd.clear()        
            pswd.send_keys(self.password)
            driver.find_element_by_xpath("//input[@id=’signIn’]").click()
        except NoSuchElementException:
            print "Error: Failed to Login to Gmail Account"
            sys.exit()
        
        time.sleep(5)
        try:
            inbox = driver.find_element_by_partial_link_text("Inbox")
            inboxdata = inbox.get_attribute("title")
            reobj = re.search(r"Inbox \((.*)\)",inboxdata)
            if reobj:
                print "##################################"
                print "You have %s inbox messages" %str(reobj.group(1))
                print "##################################"
            else:
                print "Failed to get your inbox messages"
        except NoSuchElementException:
            print "Error: Failed to Login to Gmail Account"
            sys.exit()
        try:
            driver.find_element_by_xpath(".//*[@id=’gb’]/div[1]/div[1]/div[2]/div[4]/div[1]/a/span").click()
            time.sleep(2)
            driver.find_element_by_xpath(".//*[@id=’gb’]/div[1]/div[1]/div[2]/div[4]/div[2]/div[3]/div[1]/a").click()
            time.sleep(3)
            print "Successfully Logged out from Gmail"
            print "Done"
        except NoSuchElementException:
            print "Error: Failed to Logout from Gmail Account"
            sys.exit()
    
    def tearDown(self):
        self.driver.quit()
        pass
if __name__ == "__main__":
    unittest.main()