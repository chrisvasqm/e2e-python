from selenium.webdriver.common.by import By

from lib.pagefactory_support import callable_find_by as find_by
from pages.page import Page
from pages.profile_page import ProfilePage


class SearchPage(Page):
    _filter_people = find_by(how=By.XPATH, using="//a[text()='People']")
    _first_people_result = find_by(how=By.XPATH, using="//div[2]/h3/a")

    def __init__(self, driver):
        super(SearchPage, self).__init__(driver)

    def filter_by_people(self):
        self._filter_people().click()

    def select_first_result(self):
        self._first_people_result().click()

        return ProfilePage(self._driver)
