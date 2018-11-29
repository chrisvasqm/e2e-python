import unittest

from selenium import webdriver

import constants


class MediumTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(constants.base_url)

    def test_search_for_user(self):
        pass

    def tearDown(self):
        self.driver.quit()
