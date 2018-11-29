import constants
from pages.page import Page
from pages.search_page import SearchPage


class HomePage(Page):

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.driver = driver
        self.icon_search = self.driver.find_element_by_xpath("//label[@title='Search Medium']")
        self.input_search = self.driver.find_element_by_xpath("//input[@placeholder='Search Medium']")

    def open(self):
        self.driver.get(constants.base_url)

    def search_for(self, query: str):
        self.icon_search.click()
        self.input_search.send_keys(query + "\n")
        return SearchPage(self.driver)
