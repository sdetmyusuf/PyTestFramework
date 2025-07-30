import time

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.RegisterPage import RegisterPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    desktop_xpath = "//a[contains(text(), 'Desktops')]"
    laptop_xpath = "//a[contains(text(), 'Laptops')]"
    components_xpath = "//a[contains(text(), 'Components')]"
    tablets_xpath = "//a[contains(text(), 'Tablets')]"
    software_xpath = "//a[contains(text(), 'Software')]"
    phones_xpath = "//a[contains(text(), 'Phones')]"
    cameras_xpath = "//a[contains(text(), 'Cameras')]"
    mpthree_xpath = "//a[contains(text(), 'MP3')]"
    search_box_xpath = "//input[@placeholder='Search']"
    search_button_xpath = "//button[@class='btn btn-default btn-lg']"
    my_account_xpath = "//a//span[contains(text(), 'My Account')]"
    login_option_xpath = "(//ul//li//a[contains(text(), 'Login')])[1]"
    register_option_xpath = "(//ul//li//a[contains(text(), 'Register')])[1]"
    login_email_xpath = "//input[@id='input-email']"
    login_pwd_xpath = "//input[@id='input-password']"
    login_btn_xpath = "//input[@value='Login']"
    inc_login_warn = "//div[contains(text(), 'Warning: No match for E-Mail Address and/or Password.')]"

    def clickMyAccount (self):
        self.click_element("my_account_xpath", self.my_account_xpath)

    def clickRegisterOption (self):
        self.click_element("register_option_xpath", self.register_option_xpath)
        return RegisterPage(self.driver)

    def validateAllComponenst (self):
        is_disp = self.driver.find_element(By.XPATH, self.desktop_xpath).is_displayed()
        self.driver.find_element(By.XPATH, self.laptop_xpath).is_displayed()
        self.driver.find_element(By.XPATH, self.components_xpath).is_displayed()
        self.driver.find_element(By.XPATH, self.software_xpath).is_displayed()
        self.driver.find_element(By.XPATH, self.phones_xpath).is_displayed()
        self.driver.find_element(By.XPATH, self.cameras_xpath).is_displayed()
        self.driver.find_element(By.XPATH, self.mpthree_xpath).is_displayed()
        if is_disp:
            print("All components are verified")

    def searchValidProduct (self, prod_name):
        self.driver.find_element(By.XPATH, self.search_box_xpath).is_displayed()
        self.type_into(prod_name, "search_box_xpath", self.search_box_xpath)
        self.click_element("search_button_xpath", self.search_button_xpath)
        time.sleep(2)
        # self.driver.find_element(By.XPATH, self.search_box_xpath).send_keys(prod_name)
        # self.driver.find_element(By.XPATH, self.search_button_xpath).click()


    def loginTestInDifferentScenarios(self, username, password):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.my_account_xpath).click()
        self.driver.find_element(By.XPATH, self.login_option_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.login_email_xpath).send_keys(username)
        self.driver.find_element(By.XPATH, self.login_pwd_xpath).send_keys(password)
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()
        time.sleep(2)
        assert self.driver.find_element(By.XPATH, self.inc_login_warn).is_displayed()


