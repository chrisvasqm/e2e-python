import unittest

from selenium import webdriver

from pages.home_page import HomePage


class MediumTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.home_page = HomePage(self.driver)

    def test_search_for_user(self):
        self.home_page.open()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
