from selenium import webdriver
import unittest

from common.check_point import CheckPoint
from common.keywords import KeyWords
from pages.login_page.login_page import LoginPage
from utils.read_data import readData


class BasePage(CheckPoint):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.kd = KeyWords(cls.driver)
        cls.driver.get("https://opstest.arsyun.com")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.login = LoginPage(cls.driver)
        cls.phone = readData().read_config("test_account", "phone2")
        cls.password = readData().read_config("test_account", "password2")
        cls.login.login(cls.phone, cls.password)
        # cls.driver.add_cookie({"name":"public-jwt","value":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo5LCJ1c2VyX25hbWUiOiJ0ZXJyeTAwMiIsImJ1ZmZlcl90aW1lIjo4NjQwMCwiZXhwIjoxNjUwNTMwNDU1LCJpc3MiOiJhcnNQdWJsaWMiLCJuYmYiOjE2NDk5MjQ2NTV9.phqsgRr3GrqCH7VVid4WVS7uVA33e-ndE2QTI8kbyOs"})
        # cls.driver.get("https://opstest.arsyun.com")

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # cls.kd.wait(2)
        cls.kd.close_browser()

    # def test01(self):
    #     print("ssssss")



if __name__ == "__main__":
    basepage = BasePage()