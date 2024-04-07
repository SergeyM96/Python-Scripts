import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Checkboxes(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome browser
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Close the browser after the test is completed
        self.driver.quit()

    def test_list_values_for_different_approaches(self):
        driver = self.driver
        # Navigate to the checkboxes page
        driver.get('http://the-internet.herokuapp.com/checkboxes')
        # Wait for the page to load
        time.sleep(2)

        # Find all the checkboxes on the page
        checkboxes = driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
        # Wait for the checkboxes to load
        time.sleep(2)

        # Print the 'checked' attribute of each checkbox using .get_attribute('checked')
        print("With .get_attribute('checked')")
        for checkbox in checkboxes:
            print(checkbox.get_attribute('checked'))

        # Print the selected state of each checkbox using .is_selected()
        print("\nWith .is_selected")
        for checkbox in checkboxes:
            print(checkbox.is_selected())

        # Manually check the first checkbox
        checkboxes[0].click()
        # Wait for the checkbox to be checked
        time.sleep(2)

        # Verify the state of the checkboxes after the manual interaction
        assert checkboxes[-1].get_attribute('checked') == 'true'
        assert checkboxes[-1].is_selected()
        assert checkboxes[0].get_attribute('checked') == 'true'
        assert checkboxes[0].is_selected()

        # Print a success message if all assertions pass
        print("Test succeeded.")


if __name__ == "__main__":
    unittest.main()
