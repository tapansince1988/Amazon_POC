from pages.base_pg import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        'SignInLink': ('ID', 'nav-link-accountList'),
        'SearchBar': ('ID', 'twotabsearchtextbox')
    }

    def goto_homepage(self):
        self.driver.get(BasePage.baseURL)
