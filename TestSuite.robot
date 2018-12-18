*** Keywords ***
[Documentation]  Open the Calculator App
 Open Application ${DEV.APPIUM_SERVER} platformName=${DEV.PLATFORM_NAME} $platformVersion=${DEV.PLATFORM_VERSION} deviceName=${DEV.DEVICE_NAME}  appPackage=${DEV.PACKAGE_NAME}
 
Enter Digits and Operator
[Documentation]  Takes 2 digits and Adds te values
[Arguments]  ${digit_1} ${digit_2} ${operator}
Click Element xpath=//*[contains(@text),'$digit_1']
Click Element xpath=//*[contains(@text),'$operator']
Click Element xpath=//*[contains(@text),'$digit_2']

View Result
[Documentation]  View the Result of Addition


Verify Result
[Documentation] Verify the Expected Result
[Arguments]  ${expected_result}
${displayed_result}  = Get Element Attribute ${DISPLAYED_RESULT} text
Should be Equal ${displayed_result} ${expected_result}

*** Test Cases ***
Test Case 1 : Addition
 [Documentation]  Test for Add
 [Tags]  Android Addition

 Log "Step 1: Enter 2 Digits to Add"
 Enter Digits And Operator ${td_digit_1}  ${td_digit_2}
 Log "Step 2 View Result"
 View Result
 Log "Step 3 : Verify Result"
 Verify Result ${td_digit_add}
 
 
 Test Case 2 : Subtraction
 [Documentation]  Test for Sub
 [Tags]  Android Subtraction

 Log "Step 1: Enter 2 Digits to Add"
 Enter Digits And Operator ${td_digit_1}  ${td_digit_2}
 Log "Step 2 View Result"
 View Result
 Log "Step 3 : Verify Result"
 Verify Result ${td_digit_add}