from config.device_info import get_device_info
from appium.options.common.base import AppiumOptions
import os
from dotenv import load_dotenv

load_dotenv(r"C:\Users\Admin\Desktop\Automation-Projects\Mobile-App-Automation\resources\.env")

# Retrieve device information (device name and platform OS version) from the configuration.
deviceInfo = get_device_info()
if deviceInfo == None:
    deviceName = "Samsung Galaxy S24"
    platformOS = "14.0"
    appPath = os.getenv("APP_URL")
    bsUser = os.getenv("BS_USER")
    bsKey = os.getenv("BS_KEY")
    server_url = f"http://hub-cloud.browserstack.com/wd/hub"
else:
    deviceName, platformOS = deviceInfo

    # Path to the mobile application (APK file) to be tested.
    appPath = r"C:\Users\Admin\Desktop\Automation-Projects\Mobile-App-Automation\apk\Teams-Test.apk"
    server_url = "http://localhost:4723"

def get_desired_capabilities():
    """
    Generate and return desired capabilities for the Appium session.

    This function sets up the desired capabilities required to initialize an Appium session. 
    The capabilities specify the platform, device, app, and additional settings for the test environment.

    Returns:
        AppiumOptions: An object containing the desired capabilities for Appium.
    """
    # Create an instance of AppiumOptions to define desired capabilities.
    options = AppiumOptions()

    # Load desired capabilities.
    options.load_capabilities({
        "platformName": "Android",  # Target platform for the test.
        "appium:deviceName": deviceName,  # Name of the device under test.
        "appium:app": appPath,  # Path to the application (APK) to be tested.
        "appium:appPackage": "com.microsoft.teams",  # Application package name.
        "appium:appActivity": "com.microsoft.skype.teams.Launcher",  # Main activity to launch the app.
        "appium:automationName": "UiAutomator2",  # Automation framework to use for Android testing.
        "appium:noReset": False,  # Ensure the app state is reset before the session.
        "appium:platformVersion": platformOS,  # Version of the Android platform on the device.
        "appium:disableIdLocatorAutocompletion": True,  # Disable automatic ID locator completion.
        "appium:autoGrantPermissions": True,  # Automatically grant app permissions during installation.
        "appium:interactiveDebugging":True,
        "appium:video":True
    })

    return options, server_url, bsUser, bsKey
