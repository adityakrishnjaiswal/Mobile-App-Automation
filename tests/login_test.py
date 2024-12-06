import pytest
import sys
import os
from selenium.common.exceptions import TimeoutException, WebDriverException

# Add the project root to the Python path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.driver_setup import initialize_driver
from utils.resource_reader import ResxReader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv

# Specify the location of the .resx resource file containing locator information
resource_location = r'C:\Users\Admin\Desktop\Automation-Projects\Mobile-Automation\resources\login_test_locators.resx'
# Create an instance of the ResxReader to read locators from the resource file
resx_reader_instance = ResxReader(resource_location)

# Load environment variables from the .env file for test credentials
load_dotenv(r"C:\Users\Admin\Desktop\Automation-Projects\Mobile-Automation\resources\.env")
test_username = os.getenv("TEST_EMAIL")  # Get the test email from the environment variables
test_password = os.getenv("TEST_PASS")   # Get the test password from the environment variables

# Fixture to set up and tear down the WebDriver for the test module
@pytest.fixture(scope="module")
def driver():
    """Fixture to initialize the WebDriver for the test module."""
    driver = initialize_driver()  # Initialize the driver for the test session
    yield driver  # Provide the driver instance to the test
    try:
        if driver.session_id:  # Check if the session is still active
            driver.quit()  # Quit the driver after test completion
    except WebDriverException as e:
        print(f"Error during driver teardown: {e}")  # Print error if quitting fails

def test_login(driver):
    """Test case for logging into an application with different credentials."""
    try:
        # Step 1: Agree to Terms
        # Locate the "Agree to Terms" element and wait for it to be clickable
        agreeTerms_locator = resx_reader_instance.get_locator(key="agreeTerms")
        agreeTerms_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, agreeTerms_locator))
        )
        agreeTerms_element.click()  # Click the 'Agree to Terms' button or checkbox

        # Step 2: Click 'Get Started'
        # Locate the "Get Started" element and wait for it to be clickable
        getStarted_locator = resx_reader_instance.get_locator(key="getStarted")
        getStarted_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, getStarted_locator))
        )
        getStarted_element.click()  # Click the 'Get Started' button

        # Step 3: Deny Permissions if prompted
        # Locate the "Deny" element and wait for it to be clickable
        deny_locator = resx_reader_instance.get_locator(key="deny")
        deny_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, deny_locator))
        )
        deny_element.click()  # Click the 'Deny' button

        # Step 4: Enter Email Address
        # Locate the email field and wait for it to be present
        emailField_locator = resx_reader_instance.get_locator(key="emailField")
        emailField_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, emailField_locator))
        )
        emailField_element.send_keys(test_username)  # Input the email for login

        # Step 5: Click 'Next' button after entering email
        # Locate the "Next" button and wait for it to be clickable
        nextButton_locator = resx_reader_instance.get_locator(key="nextButton")
        nextButton_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, nextButton_locator))
        )
        nextButton_element.click()  # Click the 'Next' button

        # Step 6: Enter Password
        # Locate the password field and wait for it to be present
        passwordField_locator = resx_reader_instance.get_locator(key="passwordField")
        passwordField_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, passwordField_locator))
        )
        passwordField_element.send_keys(test_password)  # Input the password for login

        # Step 7: Click 'Sign In' button
        # Locate the "Sign In" button and wait for it to be clickable
        signInButton_locator = resx_reader_instance.get_locator(key="signInButton")
        signInButton_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, signInButton_locator))
        )
        signInButton_element.click()  # Click the 'Sign In' button

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
            start_x = (width/4) * 3  # Starting X coordinate for swipe
            start_y = (height/5) * 4  # Starting Y coordinate for swipe
            end_x = width/4  # Ending X coordinate for swipe
            end_y = (height/5) * 4  # Ending Y coordinate for swipe

            driver.swipe(start_x, start_y, end_x, end_y)  # Perform the swipe action

        # Step 14: Click 'Got It' button again if present
        gotItButton_locator = resx_reader_instance.get_locator(key="gotItButton")
        gotItButton_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, gotItButton_locator))
        )
        gotItButton_element.click()  # Click the 'Got It' button again

        try:
            # Step 17: Click 'OK' button again if needed
            okButton_locator = resx_reader_instance.get_locator(key="ok")
            okButton_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, okButton_locator))
            )
            okButton_element.click()  # Click the 'OK' button again
        except:
            pass

        # Step 15: Click 'Not Now' button if present
        notNow_locator = resx_reader_instance.get_locator(key="notNow")
        notNow_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, notNow_locator))
        )
        notNow_element.click()  # Click the 'Not Now' button

        # Step 16: Click 'Cancel' button again if needed
        cancelButton_locator = resx_reader_instance.get_locator(key="cancelButton")
        cancelButton_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, cancelButton_locator))
        )
        cancelButton_element.click()  # Click the 'Cancel' button again

        
        # Step 18: Verify if the 'Chat' element is present, indicating successful login
        chat_locator = resx_reader_instance.get_locator(key="chat")
        chat_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, chat_locator))
        )

        # Assert login success if 'Chat' element is found
        if chat_element:
            assert True, "Login Successful"

        print("Test passed: Logged in successfully.")

    except TimeoutException:
        # Handle case when an element is not found or not interactable within the timeout period
        print("Test failed: Timeout while waiting for an element.")
        assert False, "Test failed due to timeout."
