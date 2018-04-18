*** Settings ***
Test Setup
Library           Selenium2Library
Resource          Resource/admin_resource.robot

*** Variables ***
${User Photo}     xpath=//*[@id="icon"]/div/img
${Logout right button}    css=a.logout:nth-child(3)
${Login Title}    Log in - Caesar
${Top Menu}       css=#top-menu
${Logout top button}    css=a.logout:nth-child(1)

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
