from pages.page import Page


class ProfilePage(Page):

    def __init__(self, driver):
        super(ProfilePage, self).__init__(driver)

    @property
    def url(self):
        return self._driver.current_url
