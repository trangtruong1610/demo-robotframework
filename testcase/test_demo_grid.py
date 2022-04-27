import unittest

from webdriver.selenium_webdriver import *


class Test(unittest.TestCase):

    def test(self):
        driver = wd_selenium_grid('firefox')

        driver.get("http://www.google.com")
        print(driver.title + ' from firefox')

        driver.quit()

    def test1(self):
        driver = wd_selenium_grid('chrome')

        driver.get("http://www.google.com")
        print(driver.title + ' from chrome')
        driver.quit()

    def test2(self):
        driver = wd_selenium_grid('firefox')

        driver.get("http://www.google.com")
        print(driver.title + ' from chrome')
        driver.quit()

    def test3(self):
        driver = wd_selenium_grid('chrome')

        driver.get("http://www.google.com")
        print(driver.title + ' from chrome')
        driver.quit()

    def test4(self):
        driver = wd_selenium_grid('firefox')

        driver.get("http://www.google.com")
        print(driver.title + ' from chrome')
        driver.quit()

    def test5(self):
        driver = wd_selenium_grid('firefox')

        driver.get("http://www.google.com")
        print(driver.title + ' from chrome')
        driver.quit()

    def test6(self):
        driver = wd_selenium_grid('firefox')

        driver.get("http://www.google.com")
        print(driver.title + ' from chrome')
        driver.quit()

    def test7(self):
        driver = wd_selenium_grid('firefox')

        driver.get("http://www.google.com")
        print(driver.title + ' from chrome')
        driver.quit()

    def test8(self):
        driver = wd_selenium_grid('firefox')

        driver.get("http://www.google.com")
        print(driver.title + ' from chrome')
        driver.quit()

    def test9(self):
        driver = wd_selenium_grid('firefox')

        driver.get("http://www.google.com")
        print(driver.title + ' from chrome')
        driver.quit()

    def test10(self):
        driver = wd_selenium_grid('firefox')

        driver.get("http://www.google.com")
        print(driver.title + ' from chrome')
        driver.quit()

    def test11(self):
        driver = wd_selenium_grid('firefox')

        driver.get("http://www.google.com")
        print(driver.title + ' from firefox')

        driver.quit()

    def test12(self):
        driver = wd_selenium_grid('chrome')

        driver.get("http://www.google.com")
        print(driver.title + ' from chrome')
        driver.quit()

    def test13(self):
        driver = wd_selenium_grid('firefox')

        driver.get("http://www.google.com")
        print(driver.title + ' from chrome')
        driver.quit()

    def test14(self):
        driver = wd_selenium_grid('WINDOWS','chrome')

        driver.get("http://www.google.com")
        print(driver.get_cookies())
        print(driver.title + ' from chrome')
        driver.quit()

    def test15(self):
        driver = wd_selenium_grid('MAC','firefox')

        driver.get("http://www.google.com")
        print(driver.title + ' from chrome')
        driver.quit()

    def test16(self):
        driver = wd_selenium_grid('firefox')

        driver.get("http://www.google.com")
        print(driver.title + ' from chrome')
        driver.quit()

    def test17(self):
        driver = wd_selenium_grid('firefox')

        driver.get("http://www.google.com")
        print(driver.title + ' from chrome')
        driver.quit()

    def test18(self):
        driver = wd_selenium_grid('firefox')

        driver.get("http://www.google.com")
        print(driver.title + ' from chrome')
        driver.quit()

    def test19(self):
        driver = wd_selenium_grid('firefox')

        driver.get("http://www.google.com")
        print(driver.title + ' from chrome')
        driver.quit()

    def test20(self):
        driver = wd_selenium_grid('firefox')

        driver.get("http://www.google.com")
        print(driver.title + ' from chrome')
        driver.quit()

    def test21(self):
        driver = wd_selenium_grid('firefox')

        driver.get("http://www.google.com")
        print(driver.title + ' from chrome')
        driver.quit()

