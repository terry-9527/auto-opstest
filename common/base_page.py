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
        cls.driver.add_cookie({"name":"public-jwt","value":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo2LCJ1c2VyX25hbWUiOiJ0ZXJyeSIsImJ1ZmZlcl90aW1lIjo4NjQwMCwiZXhwIjoxNjQ5MjExMTE4LCJpc3MiOiJhcnNQdWJsaWMiLCJuYmYiOjE2NDg2MDUzMTh9.eDFhGkdzOwmKK5AZLoW0fVBROQPMVhvUlPd1TtCxAQI"})
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