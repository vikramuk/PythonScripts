#http://lovelysystems.github.io/robotframework-androidlibrary/AndroidLibrary.html
#https://github.com/lovelysystems/robotframework-androidlibrary#readme

#http://randomsync.github.io/robotframework-mqttlibrary/
#https://github.com/lovelysystems/robotframework-androidlibrary#readme
*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource.txt

*** Test Cases ***
Valid Login
    Open Browser To Login Page
    Input Username    demo
    Input Password    mode
    Submit Credentials
    Welcome Page Should Be Open
    [Teardown]    Close Browser
