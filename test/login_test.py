import time
from pages.home_pg import HomePage

def test_The_home_page_has_the_correct_title(driver):
    hp = HomePage(driver)
    hp.goto_homepage()
    page_title = hp.get_page_title()
    # print(page_title)
    expected_title = 'Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'
    assert page_title == expected_title
    # time.sleep(3)
def test_to_authenticate_login_with_correct_credentials(driver):
    hp = HomePage(driver)
    hp.goto_homepage()

    # time.sleep(3)

