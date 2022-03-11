from selenium import webdriver

options = webdriver.FirefoxOptions()
options.headless = True
webdriver.Firefox(options=options)