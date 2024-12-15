import pytest
import sys
import os
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random

from conftest import driver, login
# Add the project root to the Python path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the required functions and classes
from utils.driver_setup import initialize_driver
from utils.resource_reader import ResxReader

# Load locators from the .resx resource file
resource_location = r'C:\Users\Admin\Desktop\Automation-Projects\Mobile-App-Automation\resources\android\send_message_test.resx'
resx_reader_instance = ResxReader(resource_location)

# Define a list of test messages to send
test_messages = ["Hi", "Hello", "How are You ?", "Test Message", "This is a Testing Message"]

# Randomly select a message to send for the test
messageToSend = random.choice(test_messages)

# Test case to validate the functionality of sending a message
def test_send_message(login, driver):
    """Test case to validate the sending of a message in the chat application."""
    
    # Step 1: Verify if the 'Chat' element is present, indicating successful login
    chat_locator = resx_reader_instance.get_locator(key="chat")
    chat_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, chat_locator))
    )

    # Step 2: Assert that the login was successful if the 'Chat' element is enabled
    if chat_element.is_enabled():
        pass  # Proceed if the element is enabled
    else:
        # Mark the session as failed in BrowserStack and stop the test
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Login Failed"}}')
        assert False
    
    # Step 3: Locate and click the 'Chat Tab'
    chatTab_locator = resx_reader_instance.get_locator(key="chatTab")
    chatTab_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, chatTab_locator))
    )
    chatTab_element.click()

    # Step 4: Locate and click on a one-to-one chat
    oneToOne_locator = resx_reader_instance.get_locator(key="oneToOne")
    oneToOne_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, oneToOne_locator))
    )
    oneToOne_element.click()

    # Step 5: Locate the message box and input the test message
    messageBox_locator = resx_reader_instance.get_locator(key="messageBox")
    messagebox_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, messageBox_locator))
    )
    messagebox_element.send_keys(messageToSend)

    # Step 6: Locate and click the 'Send' button to send the message
    sendButton_locator = resx_reader_instance.get_locator(key="sendButton")
    sendButton_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, sendButton_locator))
    )
    sendButton_element.click()

    # Step 7: Dynamically create the locator for the sent message to validate its presence
    message_locator = f"//android.widget.LinearLayout[contains(@content-desc,'{messageToSend}')]"

    # Step 8: Verify that the sent message is displayed in the chat
    message_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, message_locator))
    )

    # Step 9: Mark the test as passed or failed based on the presence of the sent message
    if message_element.is_enabled():
        # Mark the session as passed in BrowserStack
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Message sent successfully"}}')
        assert True
    else:
        # Mark the session as failed in BrowserStack
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Chat element not enabled."}}')
        assert False

# driver=initialize_driver()
# login(driver)
# test_send_message(login, driver)
