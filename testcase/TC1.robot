*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Test Cases ***
LoginTest
    Open Browser    https://app-release.gigacover.com/sg/     Chrome      executable_path=/Users/trangtruong/Desktop/demo-robot-framework/chromedriver
    Sleep  3
    Click Element  xpath://*[text()='Get Quote Now']
    Sleep  3
	Click Element  xpath://*[text()='FLEP']
	Sleep  3
	Click Element  name:group
	Click Element  xpath://*[text()='NEXT']
	Sleep  5
	${ele}  Get Webelement  xpath://*[text()="What is your date of birth?"]/../..//input
	Execute Javascript  arguments[0].removeAttribute('disabled');   ARGUMENTS    ${ele}
	Input Text  xpath://*[text()="What is your date of birth?"]/../..//input    01 Jan 1980
	Click Element  xpath://*[text()='NEXT']
	Sleep  10
	Close Window