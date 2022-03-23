from common.keywords import KeyWords



class SecuritySettingPage(KeyWords):


    # 最大连续无效登录次数输入框
    max_login_times = ('xpath', '//form/div[4]//input')
    # 第1次锁定有效时长div下拉输入框
    first_lock_input = ('xpath', '//form[1]/div[5]//div[@class="ant-select-selector"]')
    # 第2次锁定有效时长div下拉输入框
    second_lock_input = ('xpath', '//form[1]/div[6]//div[@class="ant-select-selector"]')
    # 第3次锁定有效时长div下拉输入框
    three_lock_input = ('xpath', '//form[1]/div[7]//div[@class="ant-select-selector"]')
    # root密码有效期div下拉输入框
    rootpwd_validity_input = ('xpath', '//form[2]//span[@class="ant-select-selection-item"]')
    # 提交设置按钮
    submit_button = ('xpath', '//form[2]//button[@type="submit"]')
    div_select = ('css', 'div.ant-select-item-option-content')
    # div_select2 = ('css', '//form[2]//span[@class="ant-select-selection-item"]')

    # 安全策略设置
    def setting_security_policy(self, times=3, is_submit=True):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("安全策略")
        self.force_clear(*self.max_login_times)
        self.input_text(*self.max_login_times,times)
        self.div_selector(self.first_lock_input, self.div_select, number=random.choice(range(5)))
        self.div_selector(self.second_lock_input, self.div_select, number=random.choice(range(5,10)))
        self.div_selector(self.three_lock_input, self.div_select, number=random.choice(range(10,15)))
        self.div_selector(self.rootpwd_validity_input, self.div_select, number=random.choice(range(15,18)))
        if is_submit:
            self.wait()
            self.click_element(*self.submit_button)