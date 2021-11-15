*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  jaana  jaana123
    Output Should Contain  New user registered

*** Keywords ***
Input New Command And Create User
    Input New Command