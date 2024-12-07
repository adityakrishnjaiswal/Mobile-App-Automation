# Mobile-App-Automation

This repository contains a Python-based framework for automating mobile application testing. The framework uses tools such as Selenium, Pytest, and Appium to interact with the mobile application and perform various automated test scenarios.

## Features

- **Automated Test Cases**: A suite of tests for login, navigation, and other workflows.
- **Resource Handling**: Locators are managed via `.resx` files for centralized and structured storage.
- **Environment Configuration**: `.env` file support for managing credentials and other sensitive data.
- **Test Reports**: Detailed test execution reports generated for each test run.
- **Reusable Utilities**: Modules for driver setup and resource file handling.
- **Cross-Platform Support**: Capable of testing Android and iOS applications.
- **Config Management**: Centralized configuration for Appium and Pytest settings.
- **APK Support**: Direct testing of APK files for Android applications.
- **Pytest Reporter**: Generates visually appealing and detailed test reports.

---

## Directory Structure

```
Mobile-App-Automation/
├── resources/
│   ├── login_test_locators.resx  # Locator definitions for tests
│   ├── .env                      # Environment variables for sensitive data
├── config/
│   ├── device_info.py            # Get Device Info
│   ├── desired_caps.py           # Desired Capabilities according to device 
├── apk/
│   ├── app-release.apk           # Application under test
├── tests/
│   ├── "Test Cases ".py          # Test cases
├── utils/
│   ├── driver_setup.py           # Driver initialization logic
│   ├── resource_reader.py        # Utility to read .resx resource files
├── reports/
│   ├── test_report.html          # Test execution report
├── README.md                     # Project documentation
├── requirements.txt              # Python dependencies
```

---

## Prerequisites

Ensure the following are installed on your system:

- Python 3.8+
- Appium Server
- Node.js
- Android SDK or Xcode (for Android/iOS testing)

Install Python dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Setup

1. **.env Configuration**:
   - Create a `.env` file in the `resources` directory.
   - Add the following variables:
     ```env
     TEST_EMAIL=your_test_email@example.com
     TEST_PASS=your_test_password
     ```

2. **Appium Configuration**:
   - Configure `desired_caps.py` & `device_info.py` in the `config/` folder with necessary capabilities.
   - Start the Appium server using the command:
     ```bash
     appium
     ```

---

## Running Tests

Run the tests using Pytest:

```bash
pytest tests/test_login.py --html=reports/test_report.html --self-contained-html
```

- `--html`: Generates a detailed HTML report.
- `--self-contained-html`: Ensures the report is self-contained for easy sharing.

To include pytest-reporter, install it and run with enhanced reporting:

```bash
pip install pytest-html
pytest tests/test_login.py --html=reports/detailed_report.html --self-contained-html
```

---

## Test Reports

After running the tests, you can find the report in the `reports/` directory as `test_report.html` or `detailed_report.html`. Open it in a browser to view:

- **Test Summary**: Displays pass/fail status for each test case.
- **Detailed Logs**: Includes screenshots and stack traces for failed tests.
- **Visualization**: Provides enhanced reporting with pytest-reporter.

---

## Key Modules

1. **Driver Setup**:
   - Located at `utils/driver_setup.py`.
   - Contains methods to initialize the WebDriver for Appium.

2. **Resource Reader**:
   - Located at `utils/resource_reader.py`.
   - Reads locators from `.resx` files for easy maintenance.

3. **Appium Config**:
   - Located at `config/appium_config.json`.
   - Holds desired capabilities for the Appium server.

4. **APK Files**:
   - Located in the `apk/` folder.
   - Contains the application APK file to be tested.

5. **Test Framework**:
   - Built with Pytest for structured and scalable test execution.

6. **Pytest Reporter**:
   - Generates interactive and detailed HTML reports.

---

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with clear documentation of changes.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For issues or feature requests, feel free to reach out:
- **Author**: Admin
- **Email**: adityakrishnjaiswal@gmail.com

