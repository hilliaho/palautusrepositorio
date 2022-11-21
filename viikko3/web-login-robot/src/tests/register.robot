*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

***Test Cases***
Register With Valid Username And Password
    Set Username  polle
    Set Password  heppafani98
    Set Password Confirmation  heppafani98
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  th
    Set Password  tainahilliaho
    Set Password Confirmation  tainahilliaho
    Submit Register Credentials
    Register Should Fail With Message  Username has to be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  helmi
    Set Password  helm1
    Set Password Confirmation  helmi
    Submit Register Credentials
    Register Should Fail With Message  Password has to be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  paavi
    Set Password  bestpaavi666
    Set Password Confirmation  paavi247
    Submit Register Credentials
    Register Should Fail With Message  Password and password confirmation don't match

Login After Successful Registration
    Set Username  polle
    Set Password  heppafani98
    Set Password Confirmation  heppafani98
    Submit Register Credentials
    Register Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Set Username  polle
    Set Password  heppafani98
    Submit Login Credentials
    Login Should Succeed
    
Login After Failed Registration
    Set Username  palle
    Set Password  palle
    Set Password Confirmation  palle
    Submit Register Credentials
    Register Should Fail With Message  Password has to be at least 8 characters long
    Go To Login Page
    Login Page Should Be Open
    Set Username  palle
    Set Password  palle
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password


***Keywords***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Register Credentials
    Click Button  Register

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open