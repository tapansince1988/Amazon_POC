import time
from pages.home_pg import HomePage

def test_to_authenticate_login_with_correct_credentials(driver):
    hp = HomePage(driver)
    hp.goto_homepage()
    time.sleep(3)
