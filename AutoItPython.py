#AutoIt Repeat Runs
#https://www.3pillarglobal.com/insights/automated-browser-performance-testing-using-python-and-autoit
# Python 2.7 32b, Pip + Setup Tools, PyWin32 v218 for Python 2.7 32b, xlwt module by pip install
from subprocess import Popen, PIPE
from test_base import TestBase
import datetime
import os
import time
import win32com.client
import xlwt


class TestLocalWebpageLoadTime(TestBase):


    def __init__(self):
        self.autoIt = win32com.client.Dispatch("AutoItX3.Control")
        self.autoIt.AutoItSetOption("WinTitleMatchMode", 4)
        

    def open_webpage_in_browser(self, address):
        Popen("c:\Program Files\Internet Explorer\iexplore.exe %s" %address)
        
    def extract_load_time_from_title(self, full_title):
        elements = full_title.split(" ")
        return float(elements[2])/1000
   
    def get_value_from_wmic_output(self, proc):
        return float(str(proc.communicate()).split()[1].split('\\n')[-1])
    
    def get_cpu_load_percentage(self):
        proc = Popen('wmic cpu get LoadPercentage',stdout=PIPE, stderr=PIPE)
        return self.get_value_from_wmic_output(proc)
    
    def get_mem_load_percentage(self):
        proc_free = Popen('wmic os get FreePhysicalMemory',stdout=PIPE, stderr=PIPE)
        proc_total = Popen('wmic ComputerSystem get TotalPhysicalMemory',stdout=PIPE, stderr=PIPE)
        free = self.get_value_from_wmic_output(proc_free)
        total = self.get_value_from_wmic_output(proc_total)/1024
        used = total-free
        load_percent = used/total*100 
        return round(load_percent, 1)
   
	def search_window_with_title_containing(self, string_in_title):
        mainWindowHandle = self.autoIt.WinGetHandle(string_in_title)
        testHandle = "[HANDLE:%s]" %mainWindowHandle
        full_title = self.autoIt.WinGetTitle(testHandle)
        return full_title

    def wait_for_browser_window_to_appear(self, string_in_title, timeout):
        initial_timeout = timeout
        full_title = self.search_window_with_title_containing(string_in_title)
        while (full_title == '0') and (timeout > 0):
            timeout -= 0.5
            time.sleep(0.5)
            full_title = self.search_window_with_title_containing(string_in_title)
        if timeout == 0:
            raise Exception('Window with title containing "%s" did not appear in %ds.' %(string_in_title, initial_timeout))
        else:
            return full_title

	def write_results_to_excel_sheet(self, book, results, sheet_name):
        sheet = book.add_sheet(sheet_name)
        sheet.write(0, 1, sheet_name)
        i=1
        for res in results:
            sheet.write(i, 0, "Run %d" %i)
            sheet.write(i, 1, res)
            i += 1

	def close_browser_window(self, substring_in_title, timeout):
        initial_timeout = timeout
        full_title = self.search_window_with_title_containing(substring_in_title)
        while full_title != '0':
            self.autoIt.WinClose(full_title)
            timeout -= 1
            time.sleep(1)
            full_title = self.search_window_with_title_containing(substring_in_title)
        if timeout == 0:
            raise Exception('Window with title containing "%s" could not be closed in a %ds interval.' %initial_timeout)
       
    def clear_cache(self):
        folder_native = ""
        folder_guest = ""
        if "Windows-XP" in platform.platform():
            folder_native = os.environ['USERPROFILE'] + "\Local Settings\Temporary Internet Files"
            folder_guest = os.environ['USERPROFILE'] + "..."
        elif "Windows-7" in platform.platform():
            folder_native = os.environ['USERPROFILE'] + "\AppData\Local\Microsoft\Windows\Temporary Internet Files"
            folder_guest = os.environ['APPDATA'] + "..."
        os.system("cd %s & rd /s /q ." %folder_native)
        if os.path.exists(folder_guest):
            os.system("cd %s & rd /s /q ." %folder_guest)

 
	def run_one_sequence(self):
        self.clear_cache()
        self.open_webpage_in_browser("http://xxx/wordpress/")
        full_title = self.wait_for_browser_window_to_appear("Loading time:", 60)
        load_time = self.extract_load_time_from_title(full_title)
        cpu_load = self.get_cpu_load_percentage()
        mem_load = self.get_mem_load_percentage()
        self.close_browser_window(full_title, 20)
        return load_time, int(cpu_load), mem_load
    
	   
    def run_test(self, nb_of_runs):
        all_times = []
        all_cpu_loads = []
        all_mem_loads = []
        
        for i in xrange(nb_of_runs):
            try:
                t, cpu_load, mem_load = self.run_one_sequence()
                all_times.append(t)
                all_cpu_loads.append(cpu_load)
                all_mem_loads.append(mem_load)
                time.sleep(5) # pause between runs
            except:
                time.sleep(5)
                os.system("taskkill /IM iexplore.exe /T") # if page is not fully loaded in the given timeout, kill the crashed IE process
                time.sleep(1)
                continue
        self.clear_cache()
         
        book = xlwt.Workbook(encoding="utf-8")
        self.write_results_to_excel_sheet(book, all_times, "All Load Times(s)")
        self.write_results_to_excel_sheet(book, all_cpu_loads, "CPU Loads (%)")
        self.write_results_to_excel_sheet(book, all_mem_loads, "MEM Loads (%)")
        time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        book.save("results/LocalWebpageLoadTime-WIN7-CUSTOM-%s-%s.xls" %(self.installed_tool_version(), time_stamp))
