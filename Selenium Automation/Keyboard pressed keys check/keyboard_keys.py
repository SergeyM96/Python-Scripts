import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


class KeyboardKeys(unittest.TestCase):

    def setUp(self):
        # Use Chrome browser
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Close the browser after the test is completed
        self.driver.quit()

    def test_example_1(self):
        # Initialize driver
        driver = self.driver

        # Open the webpage
        driver.get('http://the-internet.herokuapp.com/key_presses')

        # Wait for page to load
        time.sleep(3)

        # Simulate pressing the space key
        driver.find_element(By.ID, 'target').send_keys(Keys.SPACE)

        # Wait for the action to take effect
        time.sleep(3)

        # Locate the result element
        target = driver.find_element(By.ID, 'result')

        # Wait for the result to be updated
        time.sleep(4)

        # Check if SPACE key press is registered
        if target.text == 'You entered: SPACE':
            print("SPACE key press successful")
        else:
            print("SPACE key press failed")

        # Simulate pressing the TAB key
        ActionChains(driver).send_keys(Keys.TAB).perform()

        # Wait before checking if TAB was pressed
        time.sleep(3)

        # Check if TAB key press is registered
        if target.text == 'You entered: TAB':
            print("TAB key press successful")
        else:
            print("TAB key press failed")


if __name__ == "__main__":
    unittest.main()
