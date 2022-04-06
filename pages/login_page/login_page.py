from common.keywords import KeyWords
from selenium import webdriver
import requests





class LoginPage(KeyWords):
    # 手机号码输入框
    phone = ('xpath', "//input[@placeholder='请输入手机号']")
    # 密码输入框
    password = ('xpath', "//input[@placeholder='请输入密码']")
    # 验证码输入框
    code_input = ('xpath', "//input[@placeholder='请输入验证码']")
    # 发送验证码按钮
    send_button = ('xpath', "//button[@type='button']")
    # 登陆按钮
    login_button = ('xpath', "//button[@type='submit']")

    def login(self, phone, password, verifycode=None):
        # 输入手机号、密码、点击获取验证码、输入手机验证码、点击登陆
        self.input_text(*self.phone, content=phone)
        self.input_text(*self.password, content=password)
        self.click_element(*self.send_button)
        code = self.get_verifycode(phone)
        self.input_text(*self.code_input, content=code)
        self.click_element(*self.login_button)
        self.wait(8)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://opstest.arsyun.com/")
    driver.maximize_window()
    lg = LoginPage(driver)
    lg.login("18222223333", "ars@12345678")
    lg.wait(8)
    lg.close_browser()
