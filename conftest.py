import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    # driver.get(BaseURL)
    yield driver
    driver.quit()
