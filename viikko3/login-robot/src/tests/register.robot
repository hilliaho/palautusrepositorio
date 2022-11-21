*** Settings ***
Resource  resource.robot
Test Setup  Create User and Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  jellona  jalopeura666
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  pelle  ankka5678
    Output Should Contain  User with username pelle already exists 

Register With Too Short Username And Valid Password
    Input Credentials  a  ankka7
    Output Should Contain  Username has to be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  paavi  paavi
    Output Should Contain  Password has to be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  paavi  paavipaavi
    Output Should Contain  Password can not consist of only letters

***Keywords***
Create User And Input New Command
    Create User  pelle  peloton44
    Input New Command