import unittest

from webdriver.selenium_webdriver import *

class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver_local()

    def tearDown(self): self.driver.quit()

    def test_add_employee(self):
        self.driver.get('https://www.google.com/')
        print('aaa')
