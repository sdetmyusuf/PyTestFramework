import time
import pytest
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from pages.SearchPage import SearchPage
from tests.BaseTest import BaseTest


class TestSearchProducts(BaseTest):
    def test_search_valid_product (self):
        home_page = HomePage(self.driver)
        home_page.validateAllComponenst()
        home_page.searchValidProduct("HP LP3065")
        # self.driver.find_element(By.XPATH, "//input[@name='search']").send_keys("HP")
        time.sleep(3)
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        # time.sleep(3)
        assert self.driver.find_element(By.XPATH, "//a[contains(text(), 'HP LP3065')]").is_displayed()
        time.sleep(3)


    def test_search_invalid_product (self):
        home_page = HomePage(self.driver)
        search_page = SearchPage(self.driver)
        home_page.validateAllComponenst()
        home_page.searchValidProduct("Test")
        search_page.validateUserSearch("Test")
        # self.driver.find_element(By.XPATH, "//input[@name='search']").send_keys("Test")
        # time.sleep(3)
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        # time.sleep(3)


    def test_message_on_successfull_search(self):
        search_page = SearchPage(self.driver)
        search_page.validateUserSearch("iPod Classic")


