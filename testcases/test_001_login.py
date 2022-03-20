import unittest
from selenium import webdriver
from ddt import ddt, data, unpack

from common.base_page import BasePage
from pages.login_page.login_page import LoginPage
from utils.read_data import readData


@ddt
class TestLogin(BasePage):

    def setUp(self):
        self.kd.wait(3)
        self.driver.delete_all_cookies()
    case = readData().read_excel("login", "logincase.xlsx")

    @data(*case)
    def test_login(self, args):
        print("用例编号:{0},用例标题:{1},传入数据:{2},预期结果:{3}".format(args[0], args[1], args[2], args[3]))
        login = LoginPage(self.driver)
        login.login(args[2]['phone'], args[2]['password'])

        print("{0} pass".format(args[0]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
