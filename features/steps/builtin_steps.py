from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

@step('I open the url "{url}"')
def step_open_url(context, url):
    context.behave_driver.get(url)

@when('I input "{text}" into the search field with id "{field_id}"')
def step_input_text(context, text, field_id):
    search_field = context.behave_driver.find_element(By.ID, field_id)
    search_field.clear()
    search_field.send_keys(text)

@then('I expect that the element with id "{element_id}" contains the text "{text}"')
def step_verify_text_by_id(context, element_id, text):
    element = context.behave_driver.find_element(By.ID, '{element_id}')
    element_text = element.text.strip()
    assert text in element_text, f"Expected '{text}' to be in '{element_text}'"

@when('I select "{option_text}" from the dropdown with id "{dropdown_id}"')
def step_select_dropdown_option(context, option_text, dropdown_id):
    dropdown = Select(context.behave_driver.find_element(By.ID, dropdown_id))
    dropdown.select_by_visible_text(option_text)

@when('I click button with id of "{button_id}"')
def step_click_button(context, button_id):
    button = context.behave_driver.find_element(By.ID, button_id)
    button.click()

@then('I expect that the element with id "{element_id}" contains the decoded message')
def step_verify_decoded_message(context, element_id):
    expected_text = 'Drsc sc k docd wocckqo. Rs Topp!'
    try:
        element = WebDriverWait(context.behave_driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, element_id), expected_text)
        )
        actual_text = context.behave_driver.find_element(By.ID, element_id).text.strip()
        assert actual_text == expected_text, f"Expected '{expected_text}' but got '{actual_text}'"
    except Exception as e:
        raise AssertionError("text didn't match")
    
@then('I expect that the element with id "{element_id}" contains the encoded message')
def step_verify_decoded_message(context, element_id):
    expected_text = 'This is a test message. Hi Jeff!'
    try:
        element = WebDriverWait(context.behave_driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, element_id), expected_text)
        )
        actual_text = context.behave_driver.find_element(By.ID, element_id).text.strip()
        assert actual_text == expected_text, f"Expected '{expected_text}' but got '{actual_text}'"
    except Exception as e:
        raise AssertionError("text didn't match")

