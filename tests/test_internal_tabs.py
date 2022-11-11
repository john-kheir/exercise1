"""
These tests cover internal tabs tests.
"""

from pages.home import HomePage
import pytest


# to run smoke tests: pipenv run python -m pytest -m smoke
@pytest.mark.smoke
def test_001_check_if_navigation_bar_exists_home_tab(browser):

    # Go to home page
    home_page = HomePage(browser)

    # Click on Home tab, navigation bar should be displayed
    home_page.click_home_tab()
    assert home_page.navigation_bar_is_displayed() == True, "Navigation bar is not displayed"

@pytest.mark.smoke
def test_002_check_if_navigation_bar_exists_online_tab(browser):

    # Go to home page
    home_page = HomePage(browser)

    # Click on Online Banking tab, navigation bar should be displayed
    home_page.click_online_banking_tab()
    assert home_page.navigation_bar_is_displayed() == True, "Navigation bar is not displayed"

@pytest.mark.smoke
def test_003_check_if_navigation_bar_exists_feedback_tab(browser):

    # Go to home page
    home_page = HomePage(browser)

    # Click on Feedback tab, navigation bar should be displayed
    home_page.click_feedback_tab()
    assert home_page.navigation_bar_is_displayed() == True, "Navigation bar is not displayed"

