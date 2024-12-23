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
resource_location = r'C:\Users\Admin\Desktop\Automation-Projects\Mobile-App-Automation\resources\ios\login_test_locators.resx'
resx_reader_instance = ResxReader(resource_location)

# Test case to validate login functionality
def test_login(login, driver):
    """
    Test case to validate login functionality by verifying the presence of 
    a 'Chat' element, which indicates successful login.
    """

    # Step 1: Retrieve the locator for the 'Chat' element
    chat_locator = resx_reader_instance.get_locator(key="chat")
    
    # Step 2: Wait until the 'Chat' element is clickable (indicating the app has loaded)
    chat_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, chat_locator))
    )

    # Step 3: Assert that the 'Chat' element is enabled to confirm login success
    if chat_element.is_enabled():
        # Mark the test as passed in BrowserStack
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Logged in Successfully!"}}')
        assert True  # Pass the test if the element is enabled
    else:
        # Mark the test as failed in BrowserStack
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Chat element not enabled."}}')
        assert False  # Fail the test if the element is not enabled
