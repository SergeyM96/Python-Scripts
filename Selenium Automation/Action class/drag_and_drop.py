from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class DragAndDropExample:

    def test_drag_and_drop(self):
        # Define the base URL for the example
        base_url = "https://jqueryui.com/droppable/"

        # Initialize the Firefox WebDriver
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)

        # Set an implicit wait time to handle dynamic page elements
        driver.implicitly_wait(3)

        # Switch to the iframe containing the draggable elements
        driver.switch_to.frame(0)

        # Find the draggable and droppable elements
        from_element = driver.find_element(By.ID, "draggable")
        to_element = driver.find_element(By.ID, "droppable")

        # Introduce a delay to ensure elements are loaded before actions
        time.sleep(2)

        try:
            # Initialize ActionChains
            actions = ActionChains(driver)

            # Perform the drag-and-drop action
            actions.drag_and_drop(from_element, to_element).perform()

            # Print success message
            print("Drag And Drop Element Successful")

            # Introduce a delay to observe the result
            time.sleep(2)
        except:
            # Print failure message if drag-and-drop fails
            print("Drag And Drop failed on element")


drag_and_drop = DragAndDropExample()
drag_and_drop.test_drag_and_drop()
