import time
import logging
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open the DemoQA registration page
    url = "https://demoqa.com/automation-practice-form"
    driver.get(url)
    driver.maximize_window()

    # Define test data
    test_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "mobile": "1234567890",
        "message": "The automated form filler was created by S. Morozov"
    }

    # Function to add random wait time (human-like behavior)
    def random_wait():
        time.sleep(random.uniform(2, 5))

    # Fill in the registration form
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys(test_data["first_name"])
    random_wait()

    driver.find_element(By.ID, "lastName").send_keys(test_data["last_name"])
    random_wait()

    driver.find_element(By.ID, "userEmail").send_keys(test_data["email"])
    random_wait()

    # Select Gender (Male)
    gender_male = driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']")
    driver.execute_script("arguments[0].click();", gender_male)
    random_wait()

    driver.find_element(By.ID, "userNumber").send_keys(test_data["mobile"])
    random_wait()

    # Scroll down to make the submit button visible
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    random_wait()

    # Enter custom message
    driver.find_element(By.ID, "currentAddress").send_keys(test_data["message"])
    random_wait()

    # Click the Submit button
    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].click();", submit_button)  # Use JavaScript to ensure click

    # Confirm successful submission
    time.sleep(3)
    if "Thanks for submitting the form" in driver.page_source:
        print("✅ Registration successful!")
    else:
        print("❌ Registration may have failed.")

except Exception as e:
    logging.error(f"An error occurred: {e}")

finally:
    # Close the browser
    time.sleep(5)
    driver.quit()
