#https://bitbar.com/how-to-get-started-with-robot-framework-with-example/
*** Settings ***
Resource                 ...${/}resources${/}common.robot
Test Teardown            Close Application

*** Variables ***
${NAME}                  John Doe
${INPUT_NAME_FIELD}      id=com.bitbar.testdroid:id/editText1
${SUBMIT_BUTTON}         id=com.bitbar.testdroid:id/button1


*** Keywords ***

Input Name
   [Arguments]      ${name}
   Input Text       ${INPUT_NAME_FIELD} ${name}
   Hide Keyboard

Select Option
   [Arguments]      ${option}
   Click Element    xpath = //*[contains(@text, '${option}')]

Submit Selection
   Click Element    ${SUBMIT_BUTTON}

Validate Correct Answer
   Wait Until Page Contains      Congratulations ${NAME}       5s

Validate Wrong Answer
   Wait Until Page Contains      Wrong Answer                  5s
   
*** Test cases ***

Simple Smoke Test - Correct Answer
   [Tags] cloud
   Set Up And Open Android Application
   Input Name ${NAME}
   Select Option Use Testdroid Cloud
   Submit Selection
   Validate Correct Answer

Simple Smoke Test - Wrong Answer
   [Tags] 101
   Set Up And Open Android Application
   Input Name ${NAME}
   Select Option Buy 101 devices
   Submit Selection
   Validate Wrong Answer

Simple Smoke Test - Wrong Answer 2
   [Tags] mom
   Set Up And Open Android Application
   Input Name ${NAME}
   Select Option Ask mom for help
   Submit Selection
   Validate Wrong Answer