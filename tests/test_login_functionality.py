import time
import pytest
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from tests.BaseTest import BaseTest
from utilities import ExcelReaderUtil
# from utilities.DataProcessorUtil import DataProcessor
# from utilities.ExcelReaderPandas import readExcelUsingPandas


class TestLoginFunctionality(BaseTest):
    # def __init__(self, file_path, sheet_name):
    #     self.data = readExcelUsingPandas(file_path, sheet_name)
    @pytest.mark.parametrize("username,password", ExcelReaderUtil.getDataFromExcell("ExcelFiles/LoginData.xlsx", "LoginData"))
    def test_check_login_invalid_creds(self, username, password):
        home_page = HomePage(self.driver)

        home_page.loginTestInDifferentScenarios(username, password)
        time.sleep(2)
        # self.driver.find_element(By.XPATH, "//a//span[contains(text(), 'My Account')]").click()
        # self.driver.find_element(By.XPATH, "(//ul//li//a[contains(text(), 'Login')])[1]").click()
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("")
        # self.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("Password@123")
        # self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        # time.sleep(2)
        # assert self.driver.find_element(By.XPATH, "//div[contains(text(), 'Warning: No match for E-Mail Address and/or Password.')]").is_displayed()