import pages.base_pg as BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super.__init__(self, driver)

    locators = {
        'SignInLink': ('ID', 'nav-link-accountList'),
        'SearchBar': ('ID', 'twotabsearchtextbox')
    }