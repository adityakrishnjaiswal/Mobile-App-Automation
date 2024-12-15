import pytest
import sys
import os
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv


# Add the project root to the Python path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the required functions and classes
from utils.driver_setup import initialize_driver
from utils.resource_reader import ResxReader

# Load locators from the .resx resource file
resource_location = r'C:\Users\Admin\Desktop\Automation-Projects\Mobile-App-Automation\resources\android\login_test_locators.resx'
resx_reader_instance = ResxReader(resource_location)

# Test case using the reusable login function
def test_login(login,driver):
    """Test case to validate login functionality."""
    # Step 16: Verify if the 'Chat' element is present, indicating successful login
    chat_locator = resx_reader_instance.get_locator(key="chat")
    chat_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, chat_locator))
    )

    # Assert login success if 'Chat' element is found
    if chat_element.is_enabled():
        assert True
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Results found!"}}')
    else:
        assert False
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Chat element not enabled."}}')
    

