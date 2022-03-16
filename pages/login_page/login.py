from common.keywords import KeyWords
from selenium import webdriver


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
        # self.click_element(*self.send_button)
        # self.input_text(*self.code_input, content=verifycode)
        self.click_element(*self.login_button)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    lg = LoginPage(driver)
    # lg.login("18276762767", "aa123456", "888888")
