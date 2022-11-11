"""
This module contains Zero Bank Home,
the page object for the Zero Bank Home page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from pages.feedback import FeedbackPage


class HomePage:

    # Locators
    HOME_TAB = (By.XPATH, "//strong[contains(.,'Home')]")
    ONLINE_BANKING_TAB = (By.XPATH, "//strong[contains(.,'Online Banking')]")
    FEEDBACK_TAB = (By.XPATH, "//strong[contains(.,'Feedback')]")
    NAVIGATION_BAR = (By.ID, "nav")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def click_home_tab(self):
        home_tab = self.browser.find_element(*self.HOME_TAB)
        home_tab.click()

    def click_online_banking_tab(self):
        home_tab = self.browser.find_element(*self.ONLINE_BANKING_TAB)
        home_tab.click()

    def click_feedback_tab(self):
        home_tab = self.browser.find_element(*self.FEEDBACK_TAB)
        home_tab.click()
        return FeedbackPage(self.browser)

    def navigation_bar_is_displayed(self):
        navigation_bar = self.browser.find_element(*self.NAVIGATION_BAR)
        return navigation_bar.is_displayed()



