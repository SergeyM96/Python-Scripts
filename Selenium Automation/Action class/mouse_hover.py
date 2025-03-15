from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class MouseHovering():

    def test1(self):
        # Set the base URL
        baseUrl = "https://www.letskodeit.com/practice"

        # Initialize the Firefox driver
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Scroll the page to bring the element into view
        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(2)

        # Find the element to hover over
        element = driver.find_element(By.ID, "mousehover")

        # Define the locator for the item to click
        itemToClickLocator = ".//div[@class='mouse-hover-content']//a[text()='Top']"

        try:
            # Initialize ActionChains
            actions = ActionChains(driver)

            # Hover over the element
            actions.move_to_element(element).perform()
            print("Mouse Hovered on element")

            # Small delay to observe the hover action
            time.sleep(1)

            # Find and click the item
            topLink = driver.find_element(By.XPATH, itemToClickLocator)
            actions.move_to_element(topLink).click().perform()
            print("Item Clicked")
        except:
            print("Mouse Hover failed on element")


# Create an instance of the class and call the test1 method
ff = MouseHovering()
ff.test1()
