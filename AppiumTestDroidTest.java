/*
 
curl -s --user << testdroid_UserName >>:<< testdroid_ password >> \
      -F myAppFile=@"<< absolute_File_path >>" "http://appium.testdroid.com/upload" 

*/
package appium; 
import io.appium.java_client.AppiumDriver; 
import io.appium.java_client.MobileBy; 
import io.appium.java_client.android.AndroidDriver; 
import java.net.MalformedURLException; 
import java.net.URL; 
import java.util.concurrent.TimeUnit; 
import org.openqa.selenium.remote.DesiredCapabilities; 
import org.openqa.selenium.support. ui.ExpectedConditions; 
import org.openqa.selenium.support.ui.WebDriverWait; 

public class AppiumTestDroidAndroid { 
public static void main(String[] args) throws MalformedURLException, InterruptedException { 
//Declaring WebDriver variables 
AppiumDriver driver; 
WebDriverWait wait; 
// setting capabilities 
DesiredCapabilities capabilities = new DesiredCapabilities(); 

capabilities.setCapability("deviceName", "AndroidDevice"); 
capabilities.setCapability("testdroid_target", "Android"); 
capabilities.setCapability("testdroid_apiKey", "<< API_Key >>"); 
capabilities.setCapability("testdroid_project", "AppiumBook"); 
capabilities.setCapability("testdroid_testrun", "Android Run 1"); 
capabilities.setCapability("testdroid_device", "LG Google Nexus 5 6.0.1 -US");   
capabilities.setCapability("testdroid_app", "af9de10fcddf-4cae-a494-4c86a53e7552/ApiDemos-debug.apk"); 
// initializing driver object - TestDroid 
driver = new AndroidDriver(new URL(" http://appium. testdroid.com/wd/hub "), capabilities); 
//initializing  waits 
driver.manage().timeouts().implicitlyWait(10, TimeUnit. SECONDS); 
wait = new WebDriverWait(driver, 10); 
// click on 'Accessibility' link 
wait.until(ExpectedConditions.presenceOfElementLocated( MobileBy.AccessibilityId("Accessibility"))); 
driver.findElement(MobileBy.AccessibilityId("Acc essibility")).click(); 
// click on 'Accessibility Node Querying' link 
wait.until(ExpectedConditions.presenceOfElementLoc ated(MobileBy.AccessibilityId("Accessibility Node Querying"))); 
driver.findElement(MobileBy. AccessibilityId("Accessibility Node Querying")). click(); 
driver.navigate().back(); 
driver.navigate().back(); 
//close driver 
driver.quit(); 
} 
