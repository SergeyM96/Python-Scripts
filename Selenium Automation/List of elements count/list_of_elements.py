from selenium import webdriver
from selenium.webdriver.common.by import By


class ListOfElements():

    # Method to test finding elements by class name and tag name
    def test(self):
        # URL of the webpage to be tested
        baseUrl = "https://www.letskodeit.com/practice"

        # Create a new Firefox WebDriver instance
        driver = webdriver.Chrome()

        # Open the provided URL in the browser
        driver.get(baseUrl)

        # Find elements by class name
        elementListByClassName = driver.find_elements(By.CLASS_NAME, "inputs")

        # Get the length of the list of elements found by class name
        length1 = len(elementListByClassName)

        # Check if elements are found by class name
        if elementListByClassName is not None:
            # Print the size of the list of elements found by class name
            print("ClassName -> Size of the list is: " + str(length1))

        # Find elements by tag name
        elementListByTagName = driver.find_elements(By.TAG_NAME, "td")

        # Get the length of the list of elements found by tag name
        length2 = len(elementListByTagName)

        # Check if elements are found by tag name
        if elementListByTagName is not None:
            # Print the size of the list of elements found by tag name
            print("TagName -> Size of the list is: " + str(length2))

        # Quit the WebDriver, closing the browser window
        driver.quit()


# Create an instance of the ListOfElements class
ff = ListOfElements()

# Call the test method to execute the test
ff.test()
