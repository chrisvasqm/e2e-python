import unittest

from selenium import webdriver

from pages.home_page import HomePage


class MediumTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.home_page = HomePage(self.driver)

    def test_search_for_user(self):
        self.home_page.open()
        search_page = self.home_page.search_for("christian vasquez")
        search_page.filter_by_people()
        profile_page = search_page.select_first_result()

        assert "@christianv07" in profile_page.url

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
