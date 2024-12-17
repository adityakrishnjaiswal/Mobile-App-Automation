import pytest
import sys
import os
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

# Add the project root to the Python path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Import the required functions and classes
from utils.driver_setup import initialize_driver
from utils.resource_reader import ResxReader

# Load locators from the .resx resource file
resource_location = r'C:\Users\Admin\Desktop\Automation-Projects\Mobile-App-Automation\resources\ios\login_test_locators.resx'
resx_reader_instance = ResxReader(resource_location)

# Fixture to initialize and tear down the WebDriver for the test module
@pytest.fixture(scope="module")
def driver():
    """
    Fixture to initialize the WebDriver for the test module.

    Yields:
        driver (WebDriver): A WebDriver instance for interacting with the mobile app.
    """
    driver = initialize_driver("ios")  # Step 1: Initialize WebDriver
    yield driver  # Step 2: Provide the WebDriver instance to the test
    try:
        if driver.session_id:  # Ensure the session is still active
            driver.quit()  # Step 3: Quit the driver to release resources
    except WebDriverException as e:
        # Handle any errors during teardown
        print(f"Error during driver teardown: {e}")

# Fixture to handle the login process
@pytest.fixture
def login(driver):
    """
    Logs into the application using credentials stored in environment variables.

    Args:
        driver (WebDriver): Selenium WebDriver instance.

    Steps:
        1. Accept terms and conditions.
        2. Enter login credentials and proceed.
        3. Handle any additional prompts.
    """
    # Step 1: Load environment variables for credentials
    load_dotenv(r"C:\Users\Admin\Desktop\Automation-Projects\Mobile-App-Automation\resources\.env")
    test_username = os.getenv("TEST_EMAIL")  # Retrieve email from .env
    test_password = os.getenv("TEST_PASS")   # Retrieve password from .env

    try:
        # Step 2: Accept Terms and Conditions
        cancel_locator = resx_reader_instance.get_locator(key="cancel")
        cancel_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, cancel_locator))
        )
        cancel_element.click()
        try:
        # Step 3: Click 'Get Started' button
            accountField_locator = resx_reader_instance.get_locator(key="accountField")
            accountField_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, accountField_locator))
            )
            accountField_element.click()
            accountField_element.send_keys(test_username)

        except:
            
            
            useAnotherAccount_locator = resx_reader_instance.get_locator(key="useAnotherAccount")
            useAnotherAccount_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, useAnotherAccount_locator))
            )
            useAnotherAccount_element.click()

            accountField_locator = resx_reader_instance.get_locator(key="accountField")
            accountField_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, accountField_locator))
            )
            accountField_element.click()
            accountField_element.send_keys(test_username)

        # Step 5: Click 'Next' button
        nextButton_locator = resx_reader_instance.get_locator(key="nextButton")
        nextButton_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, nextButton_locator))
        )
        nextButton_element.click()

        # Step 6: Enter password
        passwordField_locator = resx_reader_instance.get_locator(key="passwordField")
        passwordField_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, passwordField_locator))
        )
        passwordField_element.click()
        passwordField_element.send_keys(test_password)

        # Step 7: Click 'Sign In' button
        signInButton_locator = resx_reader_instance.get_locator(key="signInButton")
        signInButton_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, signInButton_locator))
        )
        signInButton_element.click()

        # Step 8: Handle 'Next' buttons in additional prompts
        for i in range(2):  # Loop for handling multiple 'Next' clicks
            dontAllow_locator = resx_reader_instance.get_locator(key="dontAllow")
            dontAllow_element = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, dontAllow_locator))
            )
            dontAllow_element.click()

        # Step 11: Click 'Get Started' button again if necessary
        getStarted_locator = resx_reader_instance.get_locator(key="getStarted")
        getStarted_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, getStarted_locator))
        )
        getStarted_element.click()

    except TimeoutException:
        # Handle timeout errors
        print("Test failed: Timeout while waiting for an element.")
        assert False, "Test failed due to timeout."
    except Exception as e:
        # Handle unexpected errors
        print(f"Test failed: {str(e)}")
        assert False, f"Test failed due to: {str(e)}"