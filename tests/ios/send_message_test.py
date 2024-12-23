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
resource_location = r'C:\Users\Admin\Desktop\Automation-Projects\Mobile-App-Automation\resources\android\send_message_test_locators.resx'
resx_reader_instance = ResxReader(resource_location)

# Test case to validate sending a message functionality
def test_send_message(login, driver):
    """
    Test case to validate the send message functionality by checking if the message
    is successfully sent and appears in the chat view.
    """

    try:
        # Step 1: Retrieve the locator for the message input field
        message_input_locator = resx_reader_instance.get_locator(key="messageInput")
        
        # Step 2: Wait until the message input field is present and interactable
        message_input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, message_input_locator))
        )

        # Step 3: Send a message
        message = "Hello, this is a test message."
        message_input_element.send_keys(message)

        # Step 4: Retrieve the send button locator and click to send the message
        send_button_locator = resx_reader_instance.get_locator(key="sendButton")
        send_button_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, send_button_locator))
        )
        send_button_element.click()

        # Step 5: Verify if the message appears in the chat
        chat_message_locator = resx_reader_instance.get_locator(key="sentMessage")
        sent_message_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, chat_message_locator))
        )
        
        # Step 6: Assert the message is the same as the one sent
        assert sent_message_element.text == message, f"Expected message: '{message}', but got: '{sent_message_element.text}'"

        # Mark the test as passed in BrowserStack
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Message sent successfully!"}}')

    except TimeoutException:
        # Handle timeout errors
        print("Test failed: Timeout while waiting for an element.")
        assert False, "Test failed due to timeout."
    
    except Exception as e:
        # Handle unexpected errors
        print(f"Test failed: {str(e)}")
        assert False, f"Test failed due to: {str(e)}"
