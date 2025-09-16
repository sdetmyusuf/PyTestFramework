from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    prod_not_searched_xpath = "//p[contains(text(), 'There is no product that matches')]"
    search_box_xpath = "(//input[@name='search'][@type='text'])[1]"
    product_search_success_msg_xpath = "//h2[text()='Products meeting the search criteria']"
    search_btn_xpath = "//button[@class='btn btn-default btn-lg']//i"

    def validateUserSearch(self, prod_name):
        self.type_into(prod_name, "search_box_xpath", self.search_box_xpath)
        self.click_element("search_btn_xpath", self.search_btn_xpath)
        if self.validate_element_displayed("product_search_success_msg_xpath", self.product_search_success_msg_xpath):
            print("The product is enlisted there...")




