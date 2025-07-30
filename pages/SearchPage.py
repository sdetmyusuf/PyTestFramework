from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    pron_not_searched = "//p[contains(text(), 'There is no product that matches')]"

    def validateUserSearch(self, prod_name):
        if self.driver.find_element(By.XPATH, self.pron_not_searched).is_displayed():
            print("the searched item was not found")
