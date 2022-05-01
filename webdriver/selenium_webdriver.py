import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

filepath = os.path.dirname(__file__)
IMPLICITLY_WAIT = 10

def wd_chrome_local():
    option = webdriver.ChromeOptions()
    # option.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    driver.implicitly_wait(IMPLICITLY_WAIT)
    return driver

def wd_firefox():
    option = webdriver.FirefoxOptions()
    option.headless = True
    driver = webdriver.Firefox(options=option)
    driver.implicitly_wait(IMPLICITLY_WAIT)
    return driver

def wd_chrome():
    option = webdriver.ChromeOptions()
    option.headless = True
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(IMPLICITLY_WAIT)
    return driver

def wd_selenium_grid(platformName="MAC", browserName="chrome"):
    chrome_options = webdriver.FirefoxOptions()
    chrome_options.set_capability("browserName", browserName)
    chrome_options.set_capability("platformName", platformName)
    # chrome_options.add_argument("--headless")

    driver = webdriver.Remote(
        command_executor='http://localhost:4444',
        options=chrome_options
    )
    return driver
