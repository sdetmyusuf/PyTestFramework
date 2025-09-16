from pages.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    first_name_xpath = "//input[@name='firstname']"
    last_name_xpath = "//input[ @ name = 'lastname']"
    email_xpath = "//input[ @ name = 'email']"
    telephone_xpath = "//input[ @ name = 'telephone']"
    p_word_xpath = "//input[@name='password']"
    conf_pword_xpath = "//input[@name='confirm']"
    cont_btn_xpath = "//input[@value='Continue']"
    error_message_regist_xpath = "//div[contains(text(), 'Warning: You must agree to the Privacy Policy!')]"


    def doRegistration (self, fname, lname, email, tphone, p_word,):
        print("=====================Registeration started==============")
        self.type_into(fname,"first_name_xpath", self.first_name_xpath)
        self.type_into(lname,"last_name_xpath", self.last_name_xpath)
        self.type_into(email, "email_xpath", self.email_xpath)
        self.type_into(tphone, "telephone_xpath", self.telephone_xpath)
        self.type_into(p_word, "p_word_xpath", self.p_word_xpath)
        self.type_into(p_word, "conf_pword_xpath", self.conf_pword_xpath)
        self.click_element("cont_btn_xpath", self.cont_btn_xpath)
        self.save_screenshot_page()

    def validateRegistration (self, registrationType):
        if registrationType.startswith("without privacy policy"):
            if self.validate_element_displayed("error_message_regist_xpath", self.error_message_regist_xpath):
                print("Invalid Registration checked without privacy policy")



