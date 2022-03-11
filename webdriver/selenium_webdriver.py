import os
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

filepath = os.path.dirname(__file__)
IMPLICITLY_WAIT = 10


def options():
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs',  {
        "download.default_directory": f'{filepath}/venta/pdf_file',
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
        })
    chrome_options.add_argument("--headless")
    return chrome_options


def webdriver_local():
    chrome_options = Options()
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.maximize_window()
    return driver

def webdriver_docker():
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME,
        options=options()
    )
    driver.implicitly_wait(IMPLICITLY_WAIT)
    driver.maximize_window()
    return driver
