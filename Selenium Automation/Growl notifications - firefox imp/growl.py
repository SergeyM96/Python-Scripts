import unittest
from selenium import webdriver
import time

class Growl(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome browser
        self.driver = webdriver.Firefox()

    def tearDown(self):
        # Close the browser after the test is completed
        self.driver.quit()

    def test_example_1(self):
        driver = self.driver
        # Navigate to the homepage
        driver.get('http://the-internet.herokuapp.com')
        time.sleep(2)  # Wait for the page to load

        # Check for jQuery on the page, add it if needed
        print("Checking for jQuery on the page...")
        driver.execute_script(
            "if (!window.jQuery) {"
            "var jquery = document.createElement('script');"
            "jquery.type = 'text/javascript';"
            "jquery.src = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js';"
            "document.getElementsByTagName('head')[0].appendChild(jquery);}"
        )
        time.sleep(2)  # Wait for jQuery to load

        # Verify that jQuery is now available
        print("Verifying that jQuery is available...")
        has_jquery = driver.execute_script("return typeof jQuery != 'undefined';")
        assert has_jquery, "jQuery is not available on the page."

        # Use jQuery to add jquery-growl to the page
        print("Adding jquery-growl to the page...")
        driver.execute_script("$.getScript('http://the-internet.herokuapp.com/js/vendor/jquery.growl.js')")
        time.sleep(2)  # Wait for jquery-growl to load

        # Use jQuery to add jquery-growl styles to the page
        print("Adding jquery-growl styles to the page...")
        driver.execute_script(
            "$('head').append('"
            "<link rel=stylesheet "
            "href=http://the-internet.herokuapp.com/css/jquery.growl.css "
            "type=text/css />');"
        )
        time.sleep(2)  # Wait for the styles to load

        # jquery-growl - no frills(decorations, features etc`)
        print("Displaying a jquery-growl message with no frills...")
        driver.execute_script("$.growl({ title: 'GET', message: '/' });")
        time.sleep(2)  # Wait for the growl to be displayed

        # jquery-growl - colorized output
        print("Displaying a jquery-growl error message...")
        driver.execute_script("$.growl.error({ title: 'ERROR', message: 'Replace with your error message' });")
        time.sleep(2)  # Wait for the growl to be displayed
        print("Displaying a jquery-growl notice message...")
        driver.execute_script("$.growl.notice({ title: 'Notice', message: 'Replace with your notice message' });")
        time.sleep(2)  # Wait for the growl to be displayed
        print("Displaying a jquery-growl warning message...")
        driver.execute_script("$.growl.warning({ title: 'Warning!', message: 'Replace with your warning message' });")
        time.sleep(2)  # Wait for the growl to be displayed

        print("Test completed successfully.")

if __name__ == "__main__":
    unittest.main()