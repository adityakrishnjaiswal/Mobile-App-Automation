import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Import required modules
from utils.resource_reader import ResxReader

# Load locators from the .resx resource file
resource_location = r'C:\Users\Admin\Desktop\Automation-Projects\Mobile-App-Automation\resources\android\call_in_teams_locators.resx'
resx_reader_instance = ResxReader(resource_location)


def test_call(login, driver):
    """
    Test case to validate calling functionality in Teams by verifying the
    successful initiation and presence of an ongoing call indicator.
    """

    # Step 1: Retrieve locators from .resx
    teams_tab_locator = resx_reader_instance.get_locator(key="teams_tab")
    call_button_locator = resx_reader_instance.get_locator(key="call_button")
    ongoing_call_indicator_locator = resx_reader_instance.get_locator(key="ongoing_call_indicator")

    # Step 2: Navigate to Teams tab
    teams_tab_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, teams_tab_locator))
    )
    teams_tab_element.click()

    # Step 3: Initiate a Teams call
    call_button_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, call_button_locator))
    )
    call_button_element.click()

    # Step 4: Verify the ongoing call indicator
    ongoing_call_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ongoing_call_indicator_locator))
    )

    # Step 5: Validate the test case outcome
    if ongoing_call_element.is_displayed():
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Teams call initiated successfully!"}}'
        )
        assert True  # Test Passed
    else:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Teams call initiation failed!"}}'
        )
        assert False  # Test Failed
