import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class JavaScriptAlerts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_example_1(self):
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/javascript_alerts')
        time.sleep(5)
        driver.find_element(By.TAG_NAME, 'button').click()
        time.sleep(5)
        popup = driver.switch_to.alert
        popup.accept()
        time.sleep(5)
        result = driver.find_element(By.ID, 'result')
        time.sleep(5)
        # Check if the result text matches the expected result
        if result.text == 'You successfully clicked an alert':
            print("You successfully clicked an alert")
        else:
            print("Expected result not found")


if __name__ == "__main__":
    unittest.main()
