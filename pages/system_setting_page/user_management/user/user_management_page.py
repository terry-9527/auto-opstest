from selenium import webdriver

from common.keywords import KeyWords


class UserManagementPage(KeyWords):
    '''
    用户所有页面元素定位信息
    '''
    # 新建按钮
    new_button = ('xpath', '//span[text()="新 建"]')
    # 用户名输入框
    username_input = ('xpath', '//label[@title="用户名"]/../..//input')
    # 中文名输入框
    chinesename_input = ('xpath', '//label[@title="中文名"]/../..//input')
    # 手机号输入框
    phone_input = ('xpath', '//label[@title="手机号"]/../..//input')
    # 邮箱输入框
    email_input = ('xpath', '//label[@title="邮箱"]/../..//input')
    # 密码输入框
    password_input = ('xpath', '//label[@title="密码"]/../..//input')
    # 分组div下拉框
    group_input = ('xpath', '//form/div[2]/div[2]/div[1]/div/div/div/span[2]')
    # 所属客户div下拉框
    customer_input = ('xpath', '//form/div[4]/div[2]/div[1]/div/div/div/span[2]')
    # Leader复选框
    leader_checkbox = ('xpath', '//label[@title="Leader"]/../..//input')
    # 参与审批复选框
    approve_checkbox = ('xpath', '//label[@title="参与审批"]/../..//input')
    # 启用复选框
    enable_checkbox = ('xpath', '//label[@title="启用"]/../..//input')

    def add_user(self, username, chinesename, phone, email, ):
        self.click_navigation_bar("系统设置")
        self.wait(1)
        self.click_navigation_bar("用户管理")
        self.wait(1)
        self.click_navigation_bar("用户")
        self.wait(1)
        self.click_element(*self.new_button)
        self.wait(1)
        self.input_text(*self.username_input, username)
        self.wait(1)
        self.input_text(*self.chinesename_input, chinesename)
        self.wait(1)
        self.input_text(*self.phone_input, phone)
        self.wait(1)
        self.input_text(*self.email_input, email)
        # self.input_text(*self.password_input)








if __name__ == '__main__':
    driver = webdriver.Chrome()
    page = UserManagementPage(driver)
    page.add_user()
