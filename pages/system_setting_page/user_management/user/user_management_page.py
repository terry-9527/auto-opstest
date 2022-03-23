import random

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
    # 保存按钮
    save_button = ('xpath', '//span[text()="保 存"]')
    # 取消按钮
    cancel_button = ('xpath', '//span[text()="取 消"]')
    # 确定按钮
    confirm_button = ('xpath', '//span[text()="确 定"]')
    # 查看编辑按钮 terry001-autotest用户
    check_button = (
        'xpath', '//*[@class="ant-table-container"]//span[contains(text(),"terry001")]/../..//span[text()="查看"]')
    # 关联角色 //*[@class="ant-table-container"]//span[contains(text(),"terry001-")]
    bind_role_button = (
        'xpath', '//*[@class="ant-table-container"]//span[contains(text(),"terry001")]/../..//span[text()="关联角色"]')
    # 关联集群
    bind_cluster_button = (
        'xpath', '//*[@class="ant-table-container"]//span[contains(text(),"terry001")]/../..//span[text()="关联集群"]')
    # 关联角色 test 复选框
    one_role_checkbox = ('xpath', '//td[@title="test"]/..//input')
    # 角色全选框 checkbox
    all_roles_checkbox = ('xpath', '//th[@title="角色名"]/..//input')
    # 单个集群 f01000 checkbox
    one_miner_checkbox = ('xpath', '//td[@title="f01000"]/..//input')
    # 集群全选框 checkbox
    all_miners_checkbox = ('xpath', '//th[@title="集群"]/..//input')
    # 编辑按钮
    edit_button = ('xpath', '//span[text()="编 辑"]')
    # 输入用户名搜索框
    search_input = ('xpath', '//label[@title="用户"]/../..//input')
    # 搜索按钮 //form/div[2]/div[2]/div/div/span/span
    search_button = ('xpath', '//form/div[2]/div[2]/div/div/span/span')
    # 所属客户div 输入框
    search_customer = ('xpath', '//form/div[1]//div[@class="ant-select-selector"]')
    # 下拉div选项
    div_select = ('css', 'div.ant-select-item-option-content')

    def add_user(self, username, chinesename, phone, email, is_leader="False", is_approve="False", is_enable="True"):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("用户")
        self.click_element(*self.new_button)
        self.input_text(*self.username_input, username)
        self.input_text(*self.chinesename_input, chinesename)
        self.input_text(*self.phone_input, phone)
        self.input_text(*self.email_input, email)
        if is_leader == "False":
            if self.locator(*self.leader_checkbox).is_selected():
                self.click_element(*self.leader_checkbox)
        elif is_leader == "True":
            if not self.locator(*self.leader_checkbox).is_selected():
                self.click_element(*self.leader_checkbox)
        if is_approve == "False":
            if self.locator(*self.approve_checkbox).is_selected():
                self.click_element(*self.approve_checkbox)
        elif is_approve == "True":
            if not self.locator(*self.approve_checkbox).is_selected():
                self.click_element(*self.approve_checkbox)
        if is_enable == "False":
            if self.locator(*self.enable_checkbox).is_selected():
                self.click_element(*self.enable_checkbox)
        elif is_enable == "True":
            if not self.locator(*self.enable_checkbox).is_selected():
                self.click_element(*self.enable_checkbox)
        self.wait(1)
        self.click_element(*self.save_button)
        self.wait(1)

    # 点击查看用户信息详情
    def check_userinfo(self):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("用户")
        self.click_element(*self.check_button)
        self.wait(1)

    # 编辑用户信息
    def edit_userinfo(self, username, chinesename, phone, email):
        self.check_userinfo()
        self.click_element(*self.edit_button)
        self.input_text(*self.username_input, username)
        self.input_text(*self.chinesename_input, chinesename)
        self.input_text(*self.phone_input, phone)
        self.input_text(*self.email_input, email)
        self.wait(1)
        self.click_element(*self.leader_checkbox)
        self.wait(1)
        self.click_element(*self.approve_checkbox)
        self.wait(1)
        self.click_element(*self.save_button)
        self.wait(1)

    # 用户关联角色
    def bind_role(self, state="one", is_save=True):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("用户")
        self.click_element(*self.bind_role_button)
        self.wait(1)
        if state == "all":
            if not self.locator(*self.all_roles_checkbox).is_selected():
                self.click_element(*self.all_roles_checkbox)
        elif state == "one":
            if not self.locator(*self.one_role_checkbox).is_selected():
                self.click_element(*self.one_role_checkbox)
        if is_save:
            self.wait(1.5)
            self.click_element(*self.confirm_button)
        else:
            self.click_element(*self.cancel_button)

    # 用户关联集群
    def bind_miner(self, state="one", is_save=True):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("用户")
        self.click_element(*self.bind_cluster_button)
        self.wait(1)
        if state == "all":
            if not self.locator(*self.all_miners_checkbox).is_selected():
                self.click_element(*self.all_miners_checkbox)
        elif state == "one":
            if not self.locator(*self.one_miner_checkbox).is_selected():
                self.click_element(*self.one_miner_checkbox)
        if is_save:
            self.wait(1.5)
            self.click_element(*self.confirm_button)
        else:
            self.click_element(*self.cancel_button)

    # 输入用户名搜索用户，不支持模糊匹配
    def search_by_username(self, name=None):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("用户")
        self.input_text(*self.search_input, name)
        self.click_element(*self.search_button)
        self.wait(2)

    def search_by_customer(self):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("用户")
        self.click_element(*self.search_customer)
        els = self.locators(*self.div_select)
        self.click_elements(*self.div_select, random.randint(0, len(els) - 1))
        self.wait()

    def clear_input(self):
        self.driver.refresh()
        self.clear(*self.search_input)
        self.click_element(*self.search_button)
    def search(self,username=None, by_username=True, by_customer=True):
        if by_username and not by_customer:
            self.search_by_username(username)
            self.wait()
        elif by_customer and not by_username:
            self.search_by_customer()
            self.wait()
        elif by_username and by_customer:
            self.search_by_username(username)
            self.search_by_customer()
            self.wait()
