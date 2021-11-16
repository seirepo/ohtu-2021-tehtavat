*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Open Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  maija
    Set Password  maija123
    Set Password Confirmation  maija123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  li
    Set Password  salasana1
    Set Password Confirmation  salasana1
    Submit Credentials
    Register Should Fail With Message  Username li too short

Register With Valid Username And Too Short Password
    Set Username  maija
    Set Password  mai12
    Set Password Confirmation  mai12
    Submit Credentials
    Register Should Fail With Message  Password too short (less than 8 characters)

Register With Nonmatching Password And Password Confirmation
    Set Username  maija
    Set Password  maija123
    Set Password Confirmation  maija12
    Submit Credentials
    Register Should Fail With Message  Given passwords do not match


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Open Register Page
    Go To Register Page
    Register Page Should Be Open