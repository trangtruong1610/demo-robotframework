*** Settings ***
Documentation     This is a resource file, that can contain variables and keywords.
...               Keywords defined here can be used where this Keywords.resource in loaded.
Library           SeleniumLibrary


*** Variables ***
${docker}   http://localhost:4444/wd/hub
${local}    ${CURDIR}/../chromedriver

*** Keywords ***
WebDriver
    [Arguments]    ${env}   ## input parameters
	IF  '${env}'=='local'
		${env}   Set Variable  ${local}
		${remote_url}   Set Variable  executable_path
	ELSE
		${env}   Set Variable  ${docker}
		${remote_url}   Set Variable  remote_url
	END
	[Return]    ${remote_url}   ${env}  ## return value
