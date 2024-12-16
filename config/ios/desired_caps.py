from appium.options.common.base import AppiumOptions
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv(r"C:\Users\Admin\Desktop\Automation-Projects\Mobile-App-Automation\resources\.env")


deviceName = "iPhone 14 Pro"
platformOS = "16"
appPath = os.getenv("IOS_APP_URL")
bsUser = os.getenv("BS_USER")
bsKey = os.getenv("BS_KEY")
server_url = f"http://hub-cloud.browserstack.com/wd/hub"



def get_desired_capabilities():
    """
    Generate and return desired capabilities for the Appium session (iOS).

    This function sets up the desired capabilities required to initialize an Appium session.
    The capabilities specify the platform, device, app, and additional settings for the test environment.

    Returns:
        AppiumOptions: An object containing the desired capabilities for Appium.
    """
    # Create an instance of AppiumOptions to define desired capabilities
    options = AppiumOptions()

    # Load desired capabilities
    options.load_capabilities({
        "platformName": "iOS",  # Target platform for the test
        "appium:deviceName": deviceName,  # Name of the device under test
        "appium:platformVersion": platformOS,  # Version of the iOS platform on the device
        "appium:automationName": "XCUITest",  # Automation framework to use for iOS testing
        "appium:app": appPath,  # Path to the application (IPA) to be tested
        "appium:noReset": False,  # Ensure the app state is reset before the session
        "appium:fullReset": False,  # Avoid resetting the device completely
        "appium:newCommandTimeout": 300,  # Timeout for Appium commands
        "appium:usePrebuiltWDA": False,  # Use prebuilt WebDriverAgent (WDA)
        "appium:bundleId": "com.microsoft.dmx.Teamspace-df",  # Bundle ID of the app to test
        "appium:video": True,  # Enable video recording of the session
        "appium:interactiveDebugging": True  # Enable debugging during test execution
    })

    return options, server_url, bsUser, bsKey
