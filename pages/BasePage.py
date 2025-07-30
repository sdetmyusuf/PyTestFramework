from contextlib import nullcontext

from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def getElementByLocator (self, locator_name, locator_value):
        # element = None
        element = None
        if locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_name.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        elif locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        return element



    def type_into (self, text, locator_name, locator_value):
        element = self.getElementByLocator(locator_name, locator_value)
        element.send_keys(text)

    def click_element (self, locator_name, locator_value):
        element = self.getElementByLocator(locator_name, locator_value)
        element.click()

    def get_text_of_webelements (self, locator_name, locator_value):
        element = self.getElementByLocator(locator_name, locator_value)
        return element.text()

    def validate_element_displayed (self, locator_name, locator_value):
        element = self.getElementByLocator(locator_name, locator_value)
        if element.is_displayed():
            return True
        else:
            return False




