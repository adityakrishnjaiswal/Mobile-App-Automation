import xml.etree.ElementTree as ET

class ResxReader:
    """
    A class to read and parse .resx files for locators or key-value pairs.

    Attributes:
        locators (dict): A dictionary containing keys and their corresponding values parsed from the .resx file.
    """

    def __init__(self, resx_file):
        """
        Initialize the ResxReader with the given .resx file.

        Args:
            resx_file (str): The path to the .resx file to be parsed.
        """
        self.locators = self._parse_resx(resx_file)

    def _parse_resx(self, resx_file):
        """
        Parse the .resx file and return a dictionary of locators.

        This method uses the ElementTree XML API to read the .resx file, extracting 
        key-value pairs where:
            - 'name' attribute of 'data' tags serves as the key.
            - 'value' tag nested within the 'data' tag serves as the value.

        Args:
            resx_file (str): The path to the .resx file.

        Returns:
            dict: A dictionary containing the parsed locators.
        """
        # Parse the XML file
        tree = ET.parse(resx_file)
        root = tree.getroot()

        # Extract locators from the 'data' tags
        locators = {}
        for data in root.findall('data'):
            key = data.get('name')  # Extract the 'name' attribute as the key
            value = data.find('value').text  # Extract the text of the 'value' tag as the value
            locators[key] = value

        return locators

    def get_locator(self, key: str):
        """
        Retrieve a locator by its key.

        Args:
            key (str): The key of the locator to retrieve.

        Returns:
            str: The value associated with the key, or None if the key is not found.
        """
        return self.locators.get(key)

# Example usage
path = r'C:\Users\Admin\Desktop\Automation-Projects\Mobile-Automation\resources\login_test_locators.resx'
reader = ResxReader(path)
