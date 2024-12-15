import sys
import os
from appium import webdriver
from selenium.webdriver.remote.client_config import ClientConfig
from appium.webdriver.appium_connection import AppiumConnection

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the desired capabilities function from the project's config
from config.android.desired_caps import get_desired_capabilities

# Define the Appium server URL

caps, server_url, bsuser, bskey = get_desired_capabilities()
# Configure the Appium client connection
# This ensures that the connection setup uses the latest recommended Appium client configuration
client_config = ClientConfig(remote_server_addr=server_url, username=bsuser, password=bskey)
command_executor = AppiumConnection(client_config=client_config)


# Function to initialize the Appium driver
def initialize_driver():
    """
    Create and return an Appium driver instance.

    This function:
    1. Fetches the desired capabilities using the `get_desired_capabilities` method.
    2. Initializes a Remote WebDriver instance using the configured command_executor.
    3. Returns the initialized driver instance for use in tests.
    """
    # Retrieve desired capabilities
    desired_caps = caps
    # Initialize the driver using the updated command_executor and desired capabilities
    driver = webdriver.Remote(command_executor=command_executor, options=desired_caps, keep_alive=True)
    return driver


