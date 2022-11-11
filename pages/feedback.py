"""
This module contains Feedback page,
the page object for the Zero Bank Feedback page.
"""

from selenium.webdriver.common.by import By

class FeedbackPage:

    # Locators
    NAME_BOX = (By.ID, 'name')
    EMAIL_BOX = (By.ID, 'email')
    SUBJECT_BOX = (By.ID, 'subject')
    COMMENT_BOX = (By.ID, 'comment')
    SEND_MESSAGE_BUTTON = (By.CSS_SELECTOR, 'input.btn-signin')
    CLEAR_BUTTON = (By.NAME, 'clear')
    FEEDBACK_MESSAGE = (By.XPATH, '//div[contains(@class,"offset3")]')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def __send_text(self, text, locator):
        """
        Common function ro send text to boxes
        """
        box = self.browser.find_element(*locator)
        box.send_keys(text)

    def __get_value_from_box(self, locator):
        """
        Common function to get values in the boxes
        """
        box = self.browser.find_element(*locator)
        return box.get_attribute('value')


    def add_name(self, name):
        self.__send_text(name, self.NAME_BOX)

    def add_email(self, email):
        self.__send_text(email, self.EMAIL_BOX)

    def add_subject(self, subject):
        self.__send_text(subject, self.SUBJECT_BOX)

    def add_comment(self, comment):
        self.__send_text(comment, self.COMMENT_BOX)

    def click_send_message_button(self):
        send_message_button = self.browser.find_element(*self.SEND_MESSAGE_BUTTON)
        send_message_button.click()

    def click_clear_button(self):
        clear_button = self.browser.find_element(*self.CLEAR_BUTTON)
        clear_button.click()

    def get_value_from_name_box(self):
        return self.__get_value_from_box(self.NAME_BOX)

    def get_value_from_email_box(self):
        return self.__get_value_from_box(self.EMAIL_BOX)

    def get_value_from_subject_box(self):
        return self.__get_value_from_box(self.SUBJECT_BOX)

    def get_value_from_comment_box(self):
        return self.__get_value_from_box(self.COMMENT_BOX)

    def get_feedback_text(self):
        feedback_msg = self.browser.find_element(*self.FEEDBACK_MESSAGE)
        return feedback_msg.text

    def send_message_button_is_displayed(self):
        send_message_button = self.browser.find_element(*self.SEND_MESSAGE_BUTTON)
        return send_message_button.is_displayed()



