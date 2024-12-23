# Mobile-App-Automation Framework

This repository provides a robust Python-based framework for automating mobile application testing using  **Appium** ,  **Selenium** , and  **Pytest** . It is designed to facilitate the testing of Android and iOS applications by interacting with the mobile application UI to execute predefined test scenarios, such as login, navigation, and functional workflows.

## Key Features

* **Automated Test Cases** : Comprehensive suite of tests covering core mobile application workflows including login, navigation, and other essential functionality.
* **Centralized Resource Management** : All locators and identifiers are managed via `.resx` files to ensure easy maintenance and scalability.
* **Secure Environment Configuration** : Support for managing sensitive data like credentials through `.env` files to maintain security.
* **Cross-Platform Compatibility** : Supports testing on both Android and iOS platforms.
* **Test Reports** : Detailed HTML-based reports generated post-execution, allowing easy access to test results, including success, failure, and error logs.
* **Reusable Utilities** : Centralized modules for driver setup, configuration management, and resource file handling.
* **APK Testing** : Direct testing of Android APK files for Android applications, streamlining the testing process.
* **Pytest Integration** : Seamless integration with Pytest for structured test execution, with enhanced reporting capabilities via `pytest-html`.

---

## Directory Structure

```plaintext
Mobile-App-Automation/
├── resources/
│   ├── login_test_locators.resx  # Locator definitions for tests
│   ├── .env                      # Environment variables (credentials, sensitive data)
├── config/
│   ├── device_info.py            # Device information setup for testing
│   ├── desired_caps.py           # Desired capabilities configuration for Appium
├── apk/
│   ├── app-release.apk           # Application APK to be tested
├── tests/
│   ├── test_login.py             # Login-related test case
│   ├── test_navigation.py        # Navigation test case
├── utils/
│   ├── driver_setup.py           # Initializes and configures the Appium WebDriver
│   ├── resource_reader.py        # Utility for reading locators from .resx files
├── reports/
│   ├── test_report.html          # Test execution HTML report
├── README.md                     # Project documentation
├── requirements.txt              # List of Python dependencies
```

---

## Prerequisites

Before setting up the framework, ensure the following prerequisites are met:

* **Python 3.8+** (or a later version)
* **Appium Server** (for running the Appium tests)
* **Node.js** (required by Appium)
* **Android SDK** or **Xcode** (for Android/iOS testing respectively)

To install the required Python dependencies, execute the following command:

```bash
pip install -r requirements.txt
```

---

## Environment Setup

1. **Configure the `.env` File** :

* Create a `.env` file in the `resources/` directory.
* Add your credentials and other environment variables such as:
  ```env
  TEST_EMAIL=your_test_email@example.com
  TEST_PASS=your_test_password
  ```

1. **Appium Configuration** :

* Set up device-specific capabilities in `desired_caps.py` and `device_info.py` (located in the `config/` folder).
* Launch the Appium server using the following command:
  ```bash
  appium
  ```

---

## Running the Tests

### Basic Test Run:

To execute the test cases with  **Pytest** , run the following command:

```bash
pytest tests/test_login.py --html=reports/test_report.html --self-contained-html
```

* `--html`: Generates a comprehensive HTML test report.
* `--self-contained-html`: Ensures that the report is fully self-contained, making it easy to share and view across platforms.

### Enhanced Reporting with `pytest-html`:

To include detailed reporting features, you can use  **pytest-html** . First, ensure the module is installed:

```bash
pip install pytest-html
```

Then run the test cases with enhanced reporting:

```bash
pytest tests/test_login.py --html=reports/detailed_report.html --self-contained-html
```

This will provide a rich HTML report with additional details such as screenshots for failed tests, stack traces, and more.

---

## Test Reports

Post-test execution, the results will be available in the `reports/` directory:

* **test_report.html** (or `detailed_report.html` if using enhanced reporting) contains a detailed breakdown of test execution, including:
  * **Test Summary** : Overview of passed and failed tests.
  * **Detailed Logs** : Logs, screenshots, and stack traces for any failed tests.
  * **Interactive Visuals** : An interactive view of the tests with status indicators and other metrics.

---

## Key Modules

1. **Driver Setup** (`utils/driver_setup.py`):
   * Responsible for initializing the Appium WebDriver and setting up connections for both Android and iOS platforms.
2. **Resource Reader** (`utils/resource_reader.py`):
   * A utility that allows easy retrieval of locators from `.resx` files, ensuring the locators are always up to date and centrally managed.
3. **Appium Configuration** (`config/desired_caps.py`):
   * Contains the configuration settings (desired capabilities) for launching the mobile application on the desired platform and device.
4. **APK Files** (`apk/`):
   * Stores the APK file for Android application testing. You can easily replace it with the appropriate APK for your app.
5. **Test Cases** (`tests/`):
   * Contains the Pytest-based test cases that define and execute your automated tests, including login, navigation, and any other workflows.
6. **Test Reporting** :

* The `pytest-html` plugin is used for generating clean and visually appealing HTML reports, which include detailed test outcomes, logs, and screenshots.

---

## Contributing

We welcome contributions to improve the framework. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Implement the changes and ensure all tests pass.
4. Submit a pull request with clear documentation on the changes you made.

---

## License

This project is licensed under the  **MIT License** . See the `LICENSE` file for further details.

---

## Contact

For inquiries, support, or contributions, feel free to reach out to:

* **Author** : Aditya Krishn Jaiswal
* **Email** : [adityakrishnjaiswal@gmail.com](mailto:adityakrishnjaiswal@gmail.com)

---

## Acknowledgements

* **Appium** : For providing the open-source mobile automation platform.
* **Pytest** : For the powerful testing framework that makes test execution and reporting easy.
* **Selenium** : For its web automation capabilities, which extend to mobile web testing.
