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
resource_location = r'C:\Users\Admin\Desktop\Automation-Projects\Mobile-App-Automation\resources\login_test_locators.resx'
resx_reader_instance = ResxReader(resource_location)

# Load environment variables for test credentials
load_dotenv(r"C:\Users\Admin\Desktop\Automation-Projects\Mobile-App-Automation\resources\.env")
test_username = os.getenv("TEST_EMAIL")  # Email for login
test_password = os.getenv("TEST_PASS")   # Password for login

# Fixture to set up and tear down the WebDriver for the test module
@pytest.fixture(scope="module")
def driver():
    """Fixture to initialize the WebDriver for the test module."""
    driver = initialize_driver()  # Initialize WebDriver
    yield driver  # Provide driver instance to the test
    try:
        if driver.session_id:  # Ensure the session is active before quitting
            driver.quit()  # Quit the driver after tests
    except WebDriverException as e:
        print(f"Error during driver teardown: {e}")

# Reusable login function for all test cases
def login(driver, username, password):
    """
    Logs into the application using the provided username and password.

    Args:
        driver (WebDriver): Selenium WebDriver instance.
        username (str): The email or username for login.
        password (str): The password for login.
    """
    try:
        # Step 1: Agree to Terms
        agreeTerms_locator = resx_reader_instance.get_locator(key="agreeTerms")
        agreeTerms_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, agreeTerms_locator))
        )
        agreeTerms_element.click()

        # Step 2: Click 'Get Started'
        getStarted_locator = resx_reader_instance.get_locator(key="getStarted")
        getStarted_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, getStarted_locator))
        )
        getStarted_element.click()

        # Step 3: Enter Email Address
        emailField_locator = resx_reader_instance.get_locator(key="emailField")
        emailField_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, emailField_locator))
        )
        emailField_element.send_keys(username)

        # Step 4: Click 'Next' button
        nextButton_locator = resx_reader_instance.get_locator(key="nextButton")
        nextButton_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, nextButton_locator))
        )
        nextButton_element.click()

        # Step 5: Enter Password
        passwordField_locator = resx_reader_instance.get_locator(key="passwordField")
        passwordField_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, passwordField_locator))
        )
        passwordField_element.send_keys(password)

        # Step 6: Click 'Sign In' button
        signInButton_locator = resx_reader_instance.get_locator(key="signInButton")
        signInButton_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, signInButton_locator))
        )
        signInButton_element.click()

        # Step 8: Handle additional prompts (e.g., "Next" buttons)
        for i in range(2):  # Click the "Next" button twice if needed
            nextButton_locator = resx_reader_instance.get_locator(key="nextButton")
            nextButton_element = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, nextButton_locator))
            )
            nextButton_element.click()  # Click the 'Next' button

        # Step 9: Dismiss "Got It" messages if they appear
        for i in range(2):  # Click the "Got It" button twice if present
            gotItButton_locator = resx_reader_instance.get_locator(key="gotItButton")
            gotItButton_element = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, gotItButton_locator))
            )
            gotItButton_element.click()  # Click the 'Got It' button

        # Step 10: Handle the 'Cancel' button if present (optional)
        cancelButton_locator = resx_reader_instance.get_locator(key="cancelButton")
        cancelButton_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, cancelButton_locator))
        )
        cancelButton_element.click()  # Click the 'Cancel' button if needed

        # Step 11: Click 'Get Started' button again if necessary
        getStarted_locator = resx_reader_instance.get_locator(key="getStarted")
        getStarted_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, getStarted_locator))
        )
        getStarted_element.click()  # Click the 'Get Started' button again

        # Step 12: Check for a viewpager element for additional navigation (if present)
        viewpager_locator = resx_reader_instance.get_locator(key="viewpagerIndicator")
        viewpager_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, viewpager_locator))
        )

        if viewpager_element:
            # Step 13: Swipe screen to navigate (if necessary)
            # Get the window size and calculate coordinates for swipe action
            screen_size = driver.get_window_size()
            width = screen_size['width']
            height = screen_size['height']
            start_x = width * 0.8  # Starting X coordinate for swipe
            start_y = (height / 5) * 4  # Starting Y coordinate for swipe
            end_x = width * 0.2  # Ending X coordinate for swipe
            end_y = (height / 5) * 4  # Ending Y coordinate for swipe

            driver.swipe(start_x, start_y, end_x, end_y)  # Perform the swipe action

        # Step 14: Click 'Got It' button again if present
        gotItButton_locator = resx_reader_instance.get_locator(key="gotItButton")
        gotItButton_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, gotItButton_locator))
        )
        gotItButton_element.click()

        try:
            # Step 15: Click 'OK' button again if needed
            okButton_locator = resx_reader_instance.get_locator(key="ok")
            okButton_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, okButton_locator))
            )
            okButton_element.click()  # Click the 'OK' button again
        except:
            pass  # Ignore if the "OK" button is not present
        
        # Step 16: Verify if the 'Chat' element is present, indicating successful login
        chat_locator = resx_reader_instance.get_locator(key="chat")
        chat_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, chat_locator))
        )

        # Assert login success if 'Chat' element is found
        if chat_element.is_enabled():
            return True
        else:
            return False
    except TimeoutException:
        # Handle case when an element is not found or not interactable within the timeout period
        print("Test failed: Timeout while waiting for an element.")
        assert False, "Test failed due to timeout."  # Log failure
    except Exception as e:
        # Handle any other exceptions and fail the test
        print(f"Test failed: {str(e)}")
        assert False, f"Test failed due to: {str(e)}"  # Log failure due to other errors

# Test case using the reusable login function
def test_login(driver):
    """Test case to validate login functionality."""
    is_logged_in = login(driver, test_username, test_password)
    if is_logged_in == True:
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Results found!"}}')
    else:
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Chat element not enabled."}}')
        assert False, "Chat element was not enabled, test failed."