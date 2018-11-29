import constants
from pages.page import Page


class HomePage(Page):

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get(constants.base_url)
