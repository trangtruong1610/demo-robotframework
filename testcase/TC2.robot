*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Headless Browser Test
    Open Browser    https://app-release.gigacover.com/sg/     Chrome
    Close Browser
