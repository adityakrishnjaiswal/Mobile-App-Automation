import adbutils

# Initialize the ADB client to communicate with the ADB server.
adb = adbutils.AdbClient(host="127.0.0.1", port=5037)

def get_device_info():
    """
    Retrieve device information from connected Android devices using ADB.

    This function connects to the ADB server and retrieves the list of connected devices. 
    For each device, it extracts the serial number and Android OS version.

    Returns:
        tuple: A tuple containing the device serial number and OS version.
    """
    # Get the list of connected devices.
    devices = adb.device_list()

    # Check if any devices are connected.
    if not devices:
        print("No Physical Device is Available, Connecting to Browserstack")
        return None
    
    else:
        # Extract the device information.
        for device in devices:
            # Get the device serial number.
            device_name = device.serial  

            # Get the Android OS version from the device properties.
            os_version = device.prop.get("ro.build.version.release")  

            # Return the information as a tuple.
        return device_name, os_version

get_device_info()