from selenium import webdriver
import unittest
from common.keywords import KeyWords


class BasePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.kd = KeyWords(cls.driver)
        cls.driver.get("https://opstest.arsyun.com")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        # cls.kd.login("18276762767", "aa123456")
        cls.driver.add_cookie({"name":"public-jwt","value":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo2LCJ1c2VyX25hbWUiOiJGaWRlIiwiYnVmZmVyX3RpbWUiOjg2NDAwLCJleHAiOjE2NDg2MjM0NDYsImlzcyI6ImFyc1B1YmxpYyIsIm5iZiI6MTY0ODAxNzY0Nn0.HtJ8b5k0smpSe9pFVUKEsGD7Nkj9KYndR5AOkdi7I2g"})
        cls.driver.get("https://opstest.arsyun.com")

    def setUp(self):
        pass

    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        cls.kd.wait(2)
        cls.driver.quit()

    # def test01(self):
    #     print("ssssss")



if __name__ == "__main__":
    basepage = BasePage()