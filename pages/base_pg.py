from seleniumpagefactory import *


class BasePage(PageFactory):
    baseURL = 'https://www.amazon.in/'

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.get_current_url

