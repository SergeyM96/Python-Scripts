from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class RadioButtonsAndCheckboxes():

    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        bmwRadioBtn = driver.find_element(By.ID,"bmwradio")
        bmwRadioBtn.click()

        time.sleep(2)
        benzRadioBtn = driver.find_element(By.ID,"benzradio")
        benzRadioBtn.click()

        time.sleep(2)
        bmwCheckbox = driver.find_element(By.ID,"bmwcheck")
        bmwCheckbox.click()

        time.sleep(2)
        benzCheckbox = driver.find_element(By.ID,"benzcheck")
        benzCheckbox.click()

        # True if selected, False is not selected
        print("BMW Radio button is selected? " + str(bmwRadioBtn.is_selected()))
        print("Benz Radio button is selected? " + str(benzRadioBtn.is_selected()))
        print("BMW Checkbox is selected? " + str(bmwCheckbox.is_selected()))
        print("Benz Checkbox is selected? " + str(benzCheckbox.is_selected()))

ff = RadioButtonsAndCheckboxes()
ff.test()
