import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class FramesTest(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        # Set up Chrome WebDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        """Clean up after the test."""
        # Quit the browser instance
        self.driver.quit()

    def test_frame_content(self):
        """Test the content inside frames."""
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/nested_frames')

        # Switch to the frame with name 'frame-top'
        driver.switch_to.frame('frame-top')
        # Switch to the frame with name 'frame-middle'
        driver.switch_to.frame('frame-middle')

        # Wait for 2 seconds to observe the content
        time.sleep(2)

        # Assert that the text content of the body element is 'MIDDLE'
        assert driver.find_element(By.TAG_NAME, 'body').text == "MIDDLE", "Content should be MIDDLE"

    def test_interacting_with_elements_inside_frame(self):
        """Test interacting with elements inside frames."""
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/tinymce')

        # Switch to the frame with id 'mce_0_ifr'
        driver.switch_to.frame('mce_0_ifr')

        # Find the editor element
        editor = driver.find_element(By.TAG_NAME, 'body')
        before_text = editor.text

        # Wait for 2 seconds to observe the editor
        time.sleep(2)

        # Clear the editor, type 'Hello World!', and get the new text
        editor.clear()
        editor.send_keys('Hello World!')
        after_text = editor.text

        # Wait for 2 seconds to observe the changes
        time.sleep(2)

        # Assert that the text before and after typing are different
        assert after_text != before_text, "Text before and after typing should be different"

        # Switch back to the main content
        driver.switch_to.default_content()
        # Wait for 2 seconds to observe the changes
        time.sleep(2)
        # Assert that the h3 element is not empty
        assert driver.find_element(By.CSS_SELECTOR, 'h3').text != "", "h3 element should not be empty"

if __name__ == "__main__":
    unittest.main()
