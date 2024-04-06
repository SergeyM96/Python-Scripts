# Selenium File Download Test (Chrome)

This Python script is designed to test the file download functionality of a web page using Selenium WebDriver with Chrome.

## Description

The script automates the following steps:

1. Sets up a temporary directory for downloads.
2. Configures Chrome WebDriver to automatically download files to the temporary directory without prompting.
3. Opens a web page using Selenium WebDriver.
4. Locates and clicks on a download link on the web page.
5. Waits for the download to complete.
6. Verifies that the downloaded file exists and is not empty.
7. Cleans up after the test by closing the browser instance and removing the temporary download directory.

## Prerequisites

- Python 3.x
- Selenium WebDriver for Python
- Google Chrome browser
- ChromeDriver (WebDriver for Chrome)

## Usage

1. Install Python if not already installed.
2. Install Selenium WebDriver for Python using pip: `pip install selenium`
3. Ensure that Google Chrome browser is installed on your system.
4. Download ChromeDriver from the [ChromeDriver website](https://chromedriver.chromium.org/) and place it in your system PATH.
5. Run the script using Python: `python download_test.py`

## Notes

- This script assumes that the download link is located on a web page with the URL `http://the-internet.herokuapp.com/download`. You may need to modify the URL to match your specific test environment.
- Ensure that the Chrome WebDriver (ChromeDriver) is correctly installed and accessible.
- Customize the test case to match the structure and behavior of the download link on your web page.
- Adjust the wait time (`time.sleep()`) if necessary to accommodate slower download speeds.



