import pytest
from faker import Faker


@pytest.mark.usefixtures("setup_teardown")
class BaseTest:

    def generateTestDataFaker (self):
        fake_data = Faker()
        user_first_name = fake_data.first_name()
        user_last_name = fake_data.last_name()
        user_email = user_first_name+"_"+user_last_name+"@gmail.com"
        user_tel = fake_data.phone_number()
        user_pwd = fake_data.password(8)

        dict = {"f_name": user_first_name, "l_name" : user_last_name,
                "u_email" :user_email, "u_tel" : user_tel, "u_pwd" : user_pwd}
        return dict