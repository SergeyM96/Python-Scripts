import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class Hovers(unittest.TestCase):

    def setUp(self):
        # Initialize Chrome browser
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Close the browser after the test is completed
        self.driver.quit()

    def test_example_1(self):
        driver = self.driver
        # Navigate to the hovers page
        driver.get('http://the-internet.herokuapp.com/hovers')
        # Wait for the page to load
        time.sleep(2)

        # Find all the avatar elements on the page
        avatars = driver.find_elements(By.CLASS_NAME, 'figure')

        # Iterate through each avatar and hover over it
        for i, avatar in enumerate(avatars):
            print(f"Hovering over avatar {i+1}...")
            # Hover over the avatar using ActionChains
            ActionChains(driver).move_to_element(avatar).perform()
            # Wait for the caption to be displayed
            time.sleep(2)

            # Check if the caption is displayed
            avatar_caption = avatar.find_element(By.CLASS_NAME, 'figcaption')
            if avatar_caption.is_displayed():
                print("Test succeeded.")
            else:
                print("Test failed.")

            # Wait for 2 seconds before moving to the next avatar
            time.sleep(2)

if __name__ == "__main__":
    unittest.main()