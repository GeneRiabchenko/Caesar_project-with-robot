*** Settings ***
Library           Selenium2Library
Resource          Resource/login_page_resource.robot

*** Variables ***
${Group page title}    Caesar
${User Photo}     xpath=//*[@id="icon"]/div/img
${Login Title}    Log in - Caesar

*** Test Cases ***
Login as Admin
    [Documentation]    Login on Caesar as Admin
    [Tags]    login
    [Setup]    OpenBrowserCustom    http://localhost:3000/    chrome
    Input Text    name=login    qwerty
    Input Text    name=password    1234
    Click Element    class=submit
    Wait Until Element Is Visible    ${User Photo}    5    Element user image not found.
    Click Element    ${User Photo}
    ${User Name}    Get Text    class=name
    ${User Role}    Get Text    class=role
    Should Be Equal    ${User Name}    Kirill\nKozak
    Should Be Equal    ${User Role}    ITA Administrator
    [Teardown]    Close Browser

Login as Teacher
    [Documentation]    Login on Caesar as Teacher
    [Tags]    login
    [Setup]    OpenBrowserCustom    http://localhost:3000/    chrome
    Input Text    name=login    sasha
    Input Text    name=password    1234
    Click Element    class=submit
    Wait Until Element Is Visible    xpath=//*[@id="icon"]/div/img    5    Element user image not found.
    Click Element    xpath=//*[@id="icon"]/div/img
    ${User Name}    Get Text    class=name
    ${User Role}    Get Text    class=role
    Should Be Equal    ${User Name}    Olexandr\nReuta
    Should Be Equal    ${User Role}    ITA Teacher
    [Teardown]    Close Browser

Login as Coordinator
    [Documentation]    Login on Caesar as Coordinator
    [Tags]    login
    [Setup]    OpenBrowserCustom    http://localhost:3000/    chrome
    Input Text    name=login    dmytro
    Input Text    name=password    1234
    Click Element    class=submit
    Wait Until Element Is Visible    xpath=//*[@id="icon"]/div/img    5    Element user image not found.
    Click Element    xpath=//*[@id="icon"]/div/img
    ${User Name}    Get Text    class=name
    ${User Role}    Get Text    class=role
    Should Be Equal    ${User Name}    Dmytro\nPetin
    Should Be Equal    ${User Role}    ITA Coordinator
    [Teardown]    Close Browser

Login length 4
    [Documentation]    User have login length equal 4
    [Tags]    login
    [Setup]    OpenBrowserCustom    http://localhost:3000/    chrome
    Input Text    name=login    vasy
    Input Text    name=password    1234
    Click Element    class=submit
    Wait Until Element Is Visible    xpath=//*[@id="icon"]/div/img    5    Element user image not found.
    ${Caesar title}    Get Title
    Should Be Equal    ${Caesar title}    ${Group page title}
    [Teardown]    Close Browser

Login length 10
    [Documentation]    User have login length equal 10
    [Tags]    login
    [Setup]    OpenBrowserCustom    http://localhost:3000/    chrome
    Input Text    name=login    vasyavasya
    Input Text    name=password    1234
    Click Element    class=submit
    Wait Until Element Is Visible    xpath=//*[@id="icon"]/div/img    5    Element user image not found.
    ${Caesar title}    Get Title
    Should Be Equal    ${Caesar title}    ${Group page title}
    [Teardown]    Close Browser

Login length 3
    [Documentation]    User have login length equal 3
    [Tags]    login
    [Setup]    OpenBrowserCustom    http://localhost:3000/    chrome
    Input Text    name=login    vas
    Input Text    name=password    1234
    Click Element    class=submit
    ${Caesar title}    Get Title
    Should Be Equal    ${Caesar title}    ${Login Title}
    [Teardown]    Close Browser

Login length 11
    [Documentation]    User have login length equal 11
    [Tags]    login
    [Setup]    OpenBrowserCustom    http://localhost:3000/    chrome
    Input Text    name=login    vasyavasya1
    Input Text    name=password    1234
    Click Element    class=submit
    ${Caesar title}    Get Title
    Should Be Equal    ${Caesar title}    ${Login Title}
    [Teardown]    Close Browser

Password length 4
    [Documentation]    User have password length equal 4
    [Tags]    login
    [Setup]    OpenBrowserCustom    http://localhost:3000/    chrome
    Input Text    name=login    petya
    Input Text    name=password    1234
    Click Element    class=submit
    Wait Until Element Is Visible    xpath=//*[@id="icon"]/div/img    5    Element user image not found.
    ${Caesar title}    Get Title
    Should Be Equal    ${Caesar title}    ${Group page title}
    [Teardown]    Close Browser

Password length 10
    [Documentation]    User have password length equal 10
    [Tags]    login
    [Setup]    OpenBrowserCustom    http://localhost:3000/    chrome
    Input Text    name=login    vasya
    Input Text    name=password    1234567890
    Click Element    class=submit
    Wait Until Element Is Visible    xpath=//*[@id="icon"]/div/img    5    Element user image not found.
    ${Caesar title}    Get Title
    Should Be Equal    ${Caesar title}    ${Group page title}
    [Teardown]    Close Browser

Password length 3
    [Documentation]    User have password length equal 3
    [Tags]    login
    [Setup]    OpenBrowserCustom    http://localhost:3000/    chrome
    Input Text    name=login    vasya1
    Input Text    name=password    123
    Click Element    class=submit
    ${Caesar title}    Get Title
    Should Be Equal    ${Caesar title}    ${Login Title}
    [Teardown]    Close Browser

Password length 11
    [Documentation]    User have password length equal 11
    [Tags]    login
    [Setup]    OpenBrowserCustom    http://localhost:3000/    chrome
    Input Text    name=login    vasya2
    Input Text    name=password    12345678901
    Click Element    class=submit
    ${Caesar title}    Get Title
    Should Be Equal    ${Caesar title}    ${Login Title}
    [Teardown]    Close Browser

Submit button enable
    [Documentation]    Submit button enable when login and password fields are filled
    [Tags]    login
    [Setup]    OpenBrowserCustom    http://localhost:3000/    chrome
    Input Text    name=login    vasya
    Input Text    name=password    1234
    Wait Until Element Is Enabled    class=submit
    [Teardown]    Close Browser

Submit button disabled when login and password fields are empty
    [Documentation]    Submit button disabled when login and password fields are empty
    [Tags]    login
    [Setup]    OpenBrowserCustom    http://localhost:3000/    chrome
    Element Should Be Disabled    class=submit
    [Teardown]    Close Browser

Submit button disabled when login field is empty
    [Documentation]    Submit button disabled when login field is empty
    [Tags]    login
    [Setup]    OpenBrowserCustom    http://localhost:3000/    chrome
    Input Text    name=password    1234
    Element Should Be Disabled    class=submit
    [Teardown]    Close Browser

Submit button disabled when password field is empty
    [Documentation]    Submit button disabled when password field is empty
    [Tags]    login
    [Setup]    OpenBrowserCustom    http://localhost:3000/    chrome
    Input Text    name=login    vasya
    Element Should Be Disabled    class=submit
    [Teardown]    Close Browser
