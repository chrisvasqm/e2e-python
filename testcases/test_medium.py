import unittest

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

from pages.home_page import HomePage


@allure.feature("Medium Tests")
class MediumTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

        self.home_page = HomePage(self.driver)
        self.home_page.open()

    @allure.testcase("Search for people")
    def test_search_for_people(self):
        search_page = self.home_page.search_for("christian vasquez")
        search_page.filter_by_people()
        profile_page = search_page.select_first_result()

        assert "@christianv07s" in profile_page.url

    def tearDown(self):
        allure.attach(self.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
