from tests.BaseTest import BaseTest


class RoughTests(BaseTest):

    def test_fakerData (self):
        ret_dict = self.generateTestDataFaker()
        print(ret_dict["f_name"])