import os
from selenium import webdriver

filepath = os.path.dirname(__file__)
IMPLICITLY_WAIT = 10

def wd_chrome():
    option = webdriver.ChromeOptions()
    option.headless = True
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(IMPLICITLY_WAIT)
    return driver

def wd_firefox():
    option = webdriver.FirefoxOptions()
    option.headless = True
    driver = webdriver.Firefox(options=option)
    driver.implicitly_wait(IMPLICITLY_WAIT)
    return driver
