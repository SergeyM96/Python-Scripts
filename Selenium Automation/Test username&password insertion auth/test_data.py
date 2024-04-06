import csv
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):

    def setUp(self):
        # Set up Chrome WebDriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        # Quit the browser instance
        self.driver.quit()

    def test_login_with_multiple_users(self):
        driver = self.driver
        with open('user_data.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Open the login page
                driver.get('http://the-internet.herokuapp.com/login')
                print(f"Opened login page for user: {row['username']}")
                time.sleep(4)  # Wait for 2 seconds to see the login page

                # Enter username and password
                driver.find_element(By.ID, 'username').send_keys(row['username'])
                driver.find_element(By.ID, 'password').send_keys(row['password'])
                driver.find_element(By.ID, 'login').submit()
                print("Submitted login form")
                time.sleep(4)  # Wait for 2 seconds to see the form submission

                # Wait for the flash message to appear
                WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.CLASS_NAME, "flash")))
                print("Flash message appeared")

                # Assert the expected message is present in the flash message
                flash_message = driver.find_element(By.CLASS_NAME, 'flash').text
                assert row['notification_message'] in flash_message, f"Expected: {row['notification_message']}, Actual: {flash_message}"
                print(f"Assertion passed: {row['notification_message']} in {flash_message}")
                time.sleep(2)  # Wait for 2 seconds to see the assertion result

if __name__ == "__main__":
    unittest.main()