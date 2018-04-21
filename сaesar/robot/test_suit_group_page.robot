*** Settings ***
Test Setup
Library           Selenium2Library
Resource          Resource/admin_resource.robot
Resource          Resource/group_page_resource.robot
Resource          Resource/login_page_resource.robot

*** Variables ***

*** Test Cases ***
log_out_from_right_menu
    [Setup]    Login with arguments    qwerty    1234
    Wait Until Element Is Visible    ${User Photo}    5    Element user image not found.
    Click Element    ${User Photo}
    Wait Until Element Is Visible    ${Logout right button}    5    Element user image not found.
    Click Element    ${Logout right button}
    ${Caesar title}    Get Title
    Should Be Equal    ${Caesar title}    ${Login Title}
    [Teardown]    Close Browser

log_out_top_menu
    [Setup]    Login with arguments    qwerty    1234
    Mouse Over    ${Top Menu}
    Wait Until Element Is Visible    ${Logout top button}    5    Element user image not found.
    Click Element    ${Logout top button}
    ${Caesar title}    Get Title
    Should Be Equal    ${Caesar title}    ${Login Title}
    [Teardown]    Close Browser

open_about_page
    [Setup]    Login with arguments    qwerty    1234
    Wait Until Element Is Visible    class=groupLocation
    Mouse Over    id=top-menu
    Click Element    css=div.itemMenu:nth-child(6)
    Page Should Contain Element    css=.javascript
    [Teardown]    Close Browser

open_schedule_page
    [Setup]    Login with arguments    qwerty    1234
    Wait Until Element Is Visible    class=groupLocation
    Mouse Over    id=top-menu
    Click Element    css=div.itemMenu:nth-child(4)
    Page Should Contain Element    css=.javascript
    [Teardown]    Close Browser
