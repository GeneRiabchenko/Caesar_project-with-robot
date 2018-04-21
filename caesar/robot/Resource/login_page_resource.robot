*** Settings ***
Library           Selenium2Library

*** Variables ***
${Login Title}    Log in - Caesar
${User Photo}     xpath=//*[@id="icon"]/div/img
${Group page title}    Caesar

*** Keywords ***
OpenBrowserCustom
    [Arguments]    ${url}    ${browser}
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
