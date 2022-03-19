from selenium import webdriver
import unittest
from common.keywords import KeyWords
from utils.read_db import MysqlDb


class BasePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.kd = KeyWords(cls.driver)
        # cls.kd.login("18276762767", "aa123456")
        cls.driver.add_cookie({"name":"public-jwt","value":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxNSwidXNlcl9uYW1lIjoidGVycnkiLCJidWZmZXJfdGltZSI6ODY0MDAsImV4cCI6MTY0Nzg0ODQ5MSwiaXNzIjoiYXJzUHVibGljIiwibmJmIjoxNjQ3MjQyNjkxfQ.YUzAK-tVbRteqnSnSIW8iHZO--4krVlqgLPhZ471c9Q"})
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