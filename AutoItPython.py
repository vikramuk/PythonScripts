#AutoIt Repeat Runs
#https://www.3pillarglobal.com/insights/automated-browser-performance-testing-using-python-and-autoit
# Python 2.7 32b, Pip + Setup Tools, PyWin32 v218 for Python 2.7 32b, xlwt module by pip install
from subprocess import Popen
from test_base import TestBase
import datetime
import os
import time
import xlwt


class TestStartupShutdownTime(TestBase):

    def launch_native_browser(self):
        Popen("c:\Program Files\Internet Explorer\iexplore.exe")
      
    def wait_for_browser_window_to_appear(self, window_title, timeout):
        initial_timeout = timeout
        while (self.search_window_with_title_containing(window_title) == '0') and (timeout > 0):
            timeout -= 0.1
            time.sleep(0.1)
        if timeout == 0:
            raise Exception('Browser did not launch in the maximum timeout of %ds.' %initial_timeout)
        else:
            startup_time = initial_timeout - timeout
            return round(startup_time, 2)
   
    def close_browser_window(self, window_title, timeout):
        initial_timeout = timeout
        while self.search_window_with_title_containing(window_title) != '0':
            self.autoIt.WinClose(window_title)
            timeout -= 0.1
            time.sleep(0.1)
        if timeout == 0:
            raise Exception('Browser window could not be closed in the maximum timeout of %ds.' %initial_timeout)
        else:
            shutdown_time = initial_timeout - timeout 
            return round(shutdown_time, 2)
   
 

    def run_one_sequence(self, environment):
        if environment == "native":
            self.launch_native_browser()
        elif environment == "custom":
            self.launch_custom_browser()
        startup_time = self.wait_for_browser_window_to_appear("Blank Page", 60)
        shutdown_time = self.close_browser_window("Blank Page", 60)
        return startup_time, shutdown_time

    def run_test(self, nb_of_runs, environment):
        startup_times = []
        shutdown_times = []
        
        for i in xrange(nb_of_runs):
            startup, shutdown = self.run_one_sequence(environment)
            startup_times.append(startup)
            shutdown_times.append(shutdown)
            time.sleep(5)
            
        book = xlwt.Workbook(encoding="utf-8")
        self.write_results_to_excel_sheet(book, startup_times, "Startup time(s) - " + environment.upper())
        self.write_results_to_excel_sheet(book, shutdown_times, "Shutdown times(s) - " + environment.upper())
        time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        
        book.save("results/BrowserStartupShutdownTime-WIN7-%s-%s-%s.xls" %(environment.upper(), self.installed_tool_version(), time_stamp))    
        
    
        
if __name__ == '__main__':
    TestStartupShutdownTime().run_test(1000, "native")
    TestStartupShutdownTime().run_test(1000, "custom")

