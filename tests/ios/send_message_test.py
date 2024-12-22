import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.resource_reader import ResxReader

# Load locators from the iOS .resx resource file
resource_location_ios = r'C:\Users\Admin\Desktop\Automation-Projects\Mobile-App-Automation\resources\ios\message_test_locators.resx'
resx_reader_ios = ResxReader(resource_location_ios)

@pytest.mark.usefixtures("driver")
def test_send_message_ios(login,driver):
    """
    Test case to send a message on iOS app.
    """
    try:
        # Step 1: Accept terms and conditions if presented
        agree_terms_locator = resx_reader_ios.get_locator(key="agreeTerms")
        agree_terms_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, agree_terms_locator))
        )
        agree_terms_element.click()

        # Step 2: Login (reuse login fixture for pre-logged in session)
        login(driver)

        # Step 3: Navigate to chat screen
        chat_locator = resx_reader_ios.get_locator(key="chat")
        chat_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, chat_locator))
        )
        chat_element.click()

        # Step 4: Send message
        message_field_locator = resx_reader_ios.get_locator(key="messageField")
        message_field_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, message_field_locator))
        )
        message_field_element.send_keys("Hello, this is a test message!")

        send_button_locator = resx_reader_ios.get_locator(key="sendButton")
        send_button_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, send_button_locator))
        )
        send_button_element.click()

        # Step 5: Verify message is sent (Check if the message appears in chat)
        sent_message_locator = resx_reader_ios.get_locator(key="sentMessage")
        sent_message_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, sent_message_locator))
        )
        assert sent_message_element.is_displayed(), "Message was not sent successfully"
        
    except Exception as e:
        print(f"Test failed: {str(e)}")
        assert False, f"Test failed due to: {str(e)}"
