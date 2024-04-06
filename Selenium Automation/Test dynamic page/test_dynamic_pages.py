import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

class Upload(unittest.TestCase):
    def setUp(self):
        # Initialize the Firefox WebDriver
        self.driver = webdriver.Firefox()

    def tearDown(self):
        # Quit the Firefox WebDriver
        self.driver.quit()

    def test_dynamic_page_1(self):
        # Print the test case name
        print("Running test_dynamic_page_1")

        # Navigate to the dynamic loading page 1
        self.driver.get('http://the-internet.herokuapp.com/dynamic_loading/1')

        # Assert that the start button is displayed
        assert self.driver.find_element(By.CSS_SELECTOR, '#start button').is_displayed()

        # Assert that the finish element is not displayed
        assert not self.driver.find_element(By.ID, "finish").is_displayed()

        time.sleep(3)

        # Click the start button
        self.driver.find_element(By.CSS_SELECTOR, '#start button').click()

        # Introduce a delay to observe the loading process
        time.sleep(3)

        # Wait for the finish element to be visible
        WebDriverWait(self.driver, 6).until(
            expected_conditions.visibility_of_element_located((By.ID, "finish"))
        )

        # Assert that the finish element is displayed
        assert self.driver.find_element(By.ID, "finish").is_displayed()

        # Print the test case result
        print("test_dynamic_page_1 passed")

    def test_dynamic_page_2(self):
        # Print the test case name
        print("Running test_dynamic_page_2")

        # Navigate to the dynamic loading page 2
        self.driver.get('http://the-internet.herokuapp.com/dynamic_loading/2')

        # Assert that the start button is displayed
        assert self.driver.find_element(By.CSS_SELECTOR, '#start button').is_displayed()

        time.sleep(3)

        # Click the start button
        self.driver.find_element(By.CSS_SELECTOR, '#start button').click()

        # Introduce a delay to observe the loading process
        time.sleep(3)

        # Wait for the finish element to be visible
        WebDriverWait(self.driver, 6).until(
            expected_conditions.visibility_of_element_located((By.ID, "finish"))
        )

        # Assert that the finish element is displayed
        assert self.driver.find_element(By.ID, "finish").is_displayed()

        # Print the test case result
        print("test_dynamic_page_2 passed")

if __name__ == "__main__":
    unittest.main()
