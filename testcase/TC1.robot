*** Settings ***
Library  SeleniumLibrary
Resource  ${CURDIR}/../lib/keywords.resource    ## import from custom keywords

*** Variables ***
${env}    local

*** Test Cases ***
LoginTest
	Set Selenium Implicit Wait  20
	${remote_url}   ${env}  WebDriver   ${env}  ## input param ${env}, return 2 value   ${remote_url}   ${env}
    Open Browser    https://app-release.gigacover.com/sg/     Chrome    ${remote_url}=${env}
    Click Element  xpath://*[text()='Get Quote Now']
	Click Element  xpath://*[text()='FLEP']
	Sleep  3
	Click Element  name:group
	Click Element  xpath://*[text()='NEXT']
	${ele}  Get Webelement  xpath://*[text()="What is your date of birth?"]/../..//input
	Execute Javascript  arguments[0].removeAttribute('disabled');   ARGUMENTS    ${ele}
	Input Text  xpath://*[text()="What is your date of birth?"]/../..//input    01 Jan 1980
	Click Element  xpath://*[text()='NEXT']
	Close Browser

