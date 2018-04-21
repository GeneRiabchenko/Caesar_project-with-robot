import unittest
import logging
from selenium import webdriver
from resource.url_site import PathUrl
from resource.path_driver import GetDriver
from caesar_items.pages.login_page import LogInPage


class TestBase(unittest.TestCase):
    def setUp(self):
        """ Open Chrome browser."""
        self.driver = webdriver.Chrome(
            executable_path=GetDriver.CHROME_DRIVER)
        self.driver.get(PathUrl.SITE_URL)
        self.driver.maximize_window()
        self.login_page = LogInPage(self.driver)
        logging.basicConfig(filename="test.txt", level=logging.WARNING,
                            format='%(module)s: %(funcName)s :%(message)s')

    def tearDown(self):
        logging.warning("____________Test finished____________")
        self.driver.quit()

