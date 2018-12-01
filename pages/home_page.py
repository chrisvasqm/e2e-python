from selenium.webdriver.common.by import By

from lib.pagefactory_support import callable_find_by as find_by
from pages.page import Page
from pages.search_page import SearchPage


class HomePage(Page):
    _url = "https://medium.com"
    _icon_search = find_by(how=By.XPATH, using="//label[@title='Search Medium']")
    _input_search = find_by(how=By.XPATH, using="//input[@placeholder='Search Medium']")

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def open(self):
        self._driver.get(self._url)

    def search_for(self, query: str):
        self._icon_search().click()
        self._icon_search().send_keys(query + "\n")

        return SearchPage(self._driver)
