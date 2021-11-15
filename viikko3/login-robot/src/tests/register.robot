*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  jaana  jaana123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  maija  maija123
    Output Should Contain  User with username maija already exists

Register With Too Short Username And Valid Password
    Input Credentials  li  asd123
    Output Should Contain  Username li too short

Register With Valid Username And Too Short Password
    Input Credentials  jaana  asd1
    Output Should Contain  Password too short (less than 8 characters)

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  jaana  salasana
    Output Should Contain  Password can't contain only letters


*** Keywords ***
Input New Command And Create User
    Create User  maija  maija123
    Input New Command