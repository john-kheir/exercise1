"""
These tests cover feedback form tests.
"""

from pages.home import HomePage
import pytest


def _add_info_to_the_form(browser, name, email):
    # Go to home page
    home_page = HomePage(browser)

    # go to feedback tab
    feedback_page = home_page.click_feedback_tab()

    # add name, email, subject, and comment
    feedback_page.add_name(name)
    feedback_page.add_email(email)
    feedback_page.add_subject("subject")
    feedback_page.add_comment("comment")

    return feedback_page

#@pytest.mark.skip(reason="for now")
@pytest.mark.smoke
def test_004_send_different_values_to_form(browser):
    name = "name1"
    feedback_page = _add_info_to_the_form(browser, name, "email@test.com",)

    # Click on send message button
    feedback_page.click_send_message_button()

    # Assert on result
    assert f"Thank you for your comments, {name}." in feedback_page.get_feedback_text()

@pytest.mark.parametrize("name,email", [("1234", "email@test.com"),
                                        ("name2", "email")])
def test_005_send_different_values_to_form(browser, name, email):
    feedback_page = _add_info_to_the_form(browser, name, email)

    # Click on send message button
    feedback_page.click_send_message_button()

    # Assert on that send message button is still displayed
    assert feedback_page.send_message_button_is_displayed() == True

def test_006_clear_the_form(browser):
    feedback_page = _add_info_to_the_form(browser, "name", "email")

    # Click on clear button
    feedback_page.click_clear_button()

    # assert that all boxes are empty
    assert feedback_page.get_value_from_name_box() == ""
    assert feedback_page.get_value_from_email_box() == ""
    assert feedback_page.get_value_from_subject_box() == ""
    assert feedback_page.get_value_from_comment_box() == ""


