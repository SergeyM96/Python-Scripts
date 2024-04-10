from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ClickAndSendKeys:

   def test(self):

       # Set the base URL for the website
       base_url = "https://letskodeit.teachable.com"

       # Create a new instance of the Firefox WebDriver
       driver = webdriver.Firefox()

       # Maximize the window
       driver.maximize_window()

       # Navigate to the base URL
       driver.get(base_url)

       # Find the login link and click on it
       login_link = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
       login_link.click()

       # Use an explicit wait to ensure the email field is present
       email_field = WebDriverWait(driver, 20).until(
           EC.presence_of_element_located((By.ID, "email"))
       )
       email_field.click()
       email_field.send_keys("test")


       time.sleep(5)

       # Find the password field and enter the password
       password_field = driver.find_element(By.ID, "password")
       password_field.click()
       password_field.send_keys("test")


       time.sleep(5)

       # Find the login button and click on it
       login_button = driver.find_element(By.NAME, "commit")
       login_button.click()


       time.sleep(5)

       # Close the browser
       driver.quit()


ff = ClickAndSendKeys()
ff.test()