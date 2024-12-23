import pytest
import sys
import os
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Add the project root to the Python path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the required functions and classes
from utils.driver_setup import initialize_driver
from utils.resource_reader import ResxReader

# Load locators from the .resx resource file
resource_location = r'C:\Users\Admin\Desktop\Automation-Projects\Mobile-App-Automation\resources\ios\create_channel_test_locators.resx'
resx_reader_instance = ResxReader(resource_location)

# Test case to validate creating a channel functionality
def test_create_channel(login, driver):
    """
    Test case to validate the create channel functionality in Teams mobile app.
    The test ensures that a new channel is created and appears in the channel list.
    """

    try:
        # Step 1: Retrieve the locator for the Teams tab
        teams_tab_locator = resx_reader_instance.get_locator(key="teams_tab")
        
        # Step 2: Wait until the Teams tab is present and click to open it
        teams_tab_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, teams_tab_locator))
        )
        teams_tab_element.click()

        # Step 3: Retrieve the locator for the "Create Channel" button
        create_channel_button_locator = resx_reader_instance.get_locator(key="create_channel_button")
        create_channel_button_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, create_channel_button_locator))
        )
        create_channel_button_element.click()

        # Step 4: Retrieve the locator for the channel name input field and enter the channel name
        channel_name_input_locator = resx_reader_instance.get_locator(key="channel_name_input")
        channel_name_input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, channel_name_input_locator))
        )
        channel_name = "Test Channel"
        channel_name_input_element.send_keys(channel_name)

        # Step 5: Retrieve the locator for the "Create" button and click to create the channel
        create_button_locator = resx_reader_instance.get_locator(key="create_button")
        create_button_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, create_button_locator))
        )
        create_button_element.click()

        # Step 6: Verify if the new channel appears in the channel list
        new_channel_locator = resx_reader_instance.get_locator(key="new_channel")
        new_channel_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, new_channel_locator))
        )
        
        # Step 7: Assert that the created channel is the same as the entered name
        assert new_channel_element.text == channel_name, f"Expected channel name: '{channel_name}', but got: '{new_channel_element.text}'"

        # Mark the test as passed in BrowserStack
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Channel created successfully!"}}')

    except TimeoutException:
        # Handle timeout errors
        print("Test failed: Timeout while waiting for an element.")
        assert False, "Test failed due to timeout."
    
    except Exception as e:
        # Handle unexpected errors
        print(f"Test failed: {str(e)}")
        assert False, f"Test failed due to: {str(e)}"
