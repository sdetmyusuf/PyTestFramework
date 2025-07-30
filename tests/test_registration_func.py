import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage
from tests.BaseTest import BaseTest


class TestSearchValidProd(BaseTest):


    def test_register_wo_agree(self):
        # register_page = RegisterPage(self.driver)
        home_page = HomePage(self.driver)
        data_dict = self.generateTestDataFaker()
        print("Printing from test_register_wo_agree------> Debug")
        print(data_dict["f_name"], data_dict["l_name"], data_dict["u_email"], data_dict["u_tel"],
                                     data_dict["u_pwd"])
        print("======checking data type=============")
        print(type(data_dict["f_name"]))
        home_page.clickMyAccount()
        print("Clicked on My Account")
        time.sleep(3)
        register_page = home_page.clickRegisterOption()
        time.sleep(4)

        register_page.doRegistration(data_dict["f_name"], data_dict["l_name"], data_dict["u_email"], data_dict["u_tel"],
                                     data_dict["u_pwd"])

        # self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(2)
        # assert self.driver.find_element(By.XPATH, "//div[contains(text(), 'Warning: You must agree to the Privacy Policy!')]").is_displayed()

    def test_register_wo_confirm_pwd(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a//span[contains(text(), 'My Account')]").click()
        self.driver.find_element(By.XPATH, "(//ul//li//a[contains(text(), 'Register')])[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("MoOne")
        self.driver.find_element(By.XPATH, "//input[ @ name = 'lastname']").send_keys("YusOne")
        self.driver.find_element(By.XPATH, "//input[ @ name = 'email']").send_keys("YusOne@gmail.com")
        self.driver.find_element(By.XPATH, "//input[ @ name = 'telephone']").send_keys("9090123456")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Password@123")
        # driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys("Password@123")
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(2)
        assert self.driver.find_element(By.XPATH, "//div[contains(text(), 'Warning: You must agree to the Privacy Policy!')]").is_displayed()

