import os
import time
import shutil
import tempfile
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class DownloadTest(unittest.TestCase):

    def setUp(self):
        """Set up test environment."""
        self.download_dir = tempfile.mkdtemp()  # Temporary directory for downloads

        options = Options()
        prefs = {"download.default_directory": self.download_dir}
        options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        """Clean up after test."""
        self.driver.quit()  # Close the browser instance
        shutil.rmtree(self.download_dir)  # Remove temporary download directory

    def test_download_file(self):
        """Test file download functionality."""
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/download')  # Open download page
        download_link = driver.find_element(By.CSS_SELECTOR, '.example a')  # Find download link

        download_link.click()  # Click on the download link

        time.sleep(1.0)  # Wait for download to complete (for slow download speeds)

        files = os.listdir(self.download_dir)  # List downloaded files
        files = [os.path.join(self.download_dir, f) for f in files]  # Add directory to each filename
        assert len(files) > 0, "No files were downloaded"  # Check if any files were downloaded
        assert os.path.getsize(files[0]) > 0, "Downloaded file was empty"  # Check if downloaded file is not empty

if __name__ == "__main__":
    unittest.main()
