import unittest
import time
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class DropDownGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dropdown Example")
        self.geometry("300x200")

        # Create a label for the dropdown
        self.label = tk.Label(self, text="Select an option from the dropdown:")
        self.label.pack(pady=20)

        # Create a StringVar to store the selected option
        self.dropdown_var = tk.StringVar(self)
        self.dropdown_var.set("Select an option")

        # Create the dropdown menu
        self.dropdown = tk.OptionMenu(self, self.dropdown_var, "Option 1", "Option 2")
        self.dropdown.pack(pady=10)

        # Create a button to run the test
        self.button = tk.Button(self, text="Run Test", command=self.run_test)
        self.button.pack(pady=20)

        # Initialize the DropDown instance
        self.dropdown_test = DropDown(self.dropdown_var)

    def run_test(self):
        # Call the setUp method of the DropDown instance
        self.dropdown_test.setUp()

        # Call the test_example_1 method of the DropDown instance
        self.dropdown_test.test_example_1()

        # Call the tearDown method of the DropDown instance
        self.dropdown_test.tearDown()


class DropDown(unittest.TestCase):
    def __init__(self, dropdown_var):
        super().__init__()
        # Store the selected option from the GUI
        self.dropdown_var = dropdown_var

    def setUp(self):
        # Configure the Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")

        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(options=chrome_options)

    def tearDown(self):
        # Close the Chrome driver
        self.driver.quit()

    def test_example_1(self):
        driver = self.driver
        # Navigate to the dropdown page
        driver.get('http://the-internet.herokuapp.com/dropdown')

        try:
            # Wait for the dropdown element to be present
            dropdown_list = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "dropdown"))
            )
        except NoSuchElementException:
            print("Dropdown element not found.")
            return

        # Find all the options in the dropdown
        options = driver.find_elements(By.TAG_NAME, 'option')

        # Loop through the options and click the selected one
        for opt in options:
            if opt.text == self.dropdown_var.get():
                opt.click()
                print(f"{opt.text} was clicked!")
                break

        # Wait for 2 seconds to see the action
        time.sleep(2)


if __name__ == "__main__":
    app = DropDownGUI()
    app.mainloop()
