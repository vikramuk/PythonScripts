#https://www.3pillarglobal.com/insights/automated-browser-performance-testing-using-python-and-autoit
from test_base import TestBase
import datetime
import os
import platform
import time
import webbrowser
import win32com.client
import xlwt
                                                                                                                      
auto = win32com.client.Dispatch("AutoItX3.Control")                                                                   
url="http://172.16.228.48/wordpress"
bookmark="Loading"
                                                                                                                      
class TestAddBookmarksLoadTime(TestBase):                                                                             
    total_wait = 0                                                     
    
    def wait_seconds(self, seconds):
        time.sleep(seconds)
        self.total_wait += seconds
    
    def access_bookmark(self,bookmark):                                                                               
        self.wait_seconds(3)        
        auto.Send("!{A}")
        self.wait_seconds(1)
        auto.Send("{UP}")
        auto.Send("{ENTER}")
        self.wait_for_browser_window_to_appear(bookmark, 20)
                                                                                                                      
    def remove_bookmarks(self):                                                                                       
        folder_native = ""
        folder_guest = ""
        if "Windows-XP" in platform.platform():
            folder_native = os.environ['USERPROFILE'] + "\Favorites"
            folder_guest = os.environ['USERPROFILE'] + "..."
        elif "Windows-7" in platform.platform():
            folder_native = os.environ["USERPROFILE"] + "\Favorites" 
            folder_guest = os.environ["USERPROFILE"] + "..."
        os.system("cd %s & rd /s /q ." %folder_native)
        if os.path.exists(folder_guest):
            os.system("cd %s & rd /s /q ." %folder_guest)
                                                                                                                      
    def go_to_homepage(self):  
        self.wait_for_browser_window_to_appear(bookmark, 20)
        print "wait"
        self.wait_seconds(3)
        print "title=" + self.search_window_with_title_containing("Blank Page")
        while self.search_window_with_title_containing("Blank Page") == '0':
            print "press alt+home"
            auto.Send("{ALT}")
            auto.Send("!{HOME}")                                                                                          
            auto.Send("{ALTUP}")
            print "pressed"
            self.wait_seconds(1)
                                                                                                                      
    def add_bookmark(self, bookmark):                                                                                 
        auto.Send("^d")   
        self.wait_for_browser_window_to_appear("Add", 20)
        self.wait_seconds(1)
        auto.Send(bookmark)                                                                                           
        auto.Send("{ENTER}")                                                                                          
                                                                                                                      
    def run_test_once(self):                                                                           
        self.total_wait = 0
        starttime=time.time()
        browser=webbrowser.get()                                                                                      
        browser.open(url)  
        self.wait_for_browser_window_to_appear(bookmark, 40)
        self.add_bookmark(bookmark)                                                                               
        self.go_to_homepage()  
        self.access_bookmark(bookmark)
        stoptime=time.time()
        self.close_browser_window(bookmark, 10)
        self.remove_bookmarks() 
        self.clear_cache()
        return stoptime-starttime-self.total_wait                                                                                        
                                       
    def run_test_multiple_times(self,times):
        start_list=[]
        for k in xrange(times):
            try:
                print "--- RUN %d ---" %k
                start_list.append(self.run_test_once())
                time.sleep(7)
            except:
                time.sleep(5)
                os.system("taskkill /IM iexplore.exe /T") # if page is not fully loaded in the given timeout, kill the crashed IE process
                self.remove_bookmarks() 
                self.clear_cache()
                time.sleep(1)
                continue
        
        book = xlwt.Workbook(encoding="utf-8")
        self.write_results_to_excel_sheet(book, start_list, "Duration(s)")
        time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        
        if self.installed_tool_version() == "":
            environment = "NATIVE"
        else:
            environment = "CUSTOM"
        book.save("results/AddBookmarkHomepageAccessBookmark-WIN7-%s-%s-%s.xls" %(environment, self.installed_tool_version(), time_stamp))    
             
                                                                                          
if __name__ == '__main__':                                                                                            
    TestAddBookmarksLoadTime().run_test_multiple_times(1000)
