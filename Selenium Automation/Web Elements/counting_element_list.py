from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElementsList:

   def testListOfElements(self):

       base_url = "https://www.letskodeit.com/practice"
       driver = webdriver.Firefox()
       driver.maximize_window()
       driver.get(base_url)

       # Set an implicit wait of 10 seconds
       driver.implicitly_wait(10)

       # Find all the radio buttons with the name "cars" using XPath
       radio_buttons_list = driver.find_elements(
           By.XPATH, "//input[contains(@type,'radio') and contains(@name,'cars')]"
       )

       # Get the size of the list of radio buttons
       size = len(radio_buttons_list)
       print("Size of the list: " + str(size))

       # Loop through the radio buttons and click on the ones that are not selected
       for radio_button in radio_buttons_list:
           is_selected = radio_button.is_selected()

           if not is_selected:
               radio_button.click()
               time.sleep(2)


ff = WorkingWithElementsList()
ff.testListOfElements()