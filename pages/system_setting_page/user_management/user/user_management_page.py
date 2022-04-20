from common.keywords import KeyWords
from common.my_logger import mylogger


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
    leader_checkbox = ('xpath', '//form/div[6]/div[2]/div/div/label/span')
    # 参与审批复选框
    approve_checkbox = ('xpath', '//form/div[8]/div[2]/div/div/label/span')
    # 启用复选框
    enable_checkbox = ('xpath', '//form//input[@type="checkbox"]')
    # enable_checkbox = ('xpath', '//form/div[10]/div[2]/div/div/label/span/input')
    # 保存按钮
    save_button = ('xpath', '//span[text()="保 存"]')
    # 取消按钮
    cancel_button = ('xpath', '//span[text()="取 消"]')
    # 确定按钮
    confirm_button = ('xpath', '//span[text()="确 定"]/..')
    # 查看编辑按钮 terry001-autotest用户
    check_button = (
        'xpath', '//*[@class="ant-table-container"]//span[contains(text(),"terry0001")]/../..//span[text()="查看"]')
    # 关联角色 //*[@class="ant-table-container"]//span[contains(text(),"terry001-")]
    bind_role_button = (
        'xpath', '//*[@class="ant-table-container"]//span[contains(text(),"terry0001")]/../..//span[text()="关联角色"]')
    # 关联集群
    bind_cluster_button = (
        'xpath', '//*[@class="ant-table-container"]//span[contains(text(),"terry0001")]/../..//span[text()="关联集群"]')
    # 角色全选框 checkbox
    all_roles_checkbox = ('xpath', '//th[@title="角色名"]/..//input')
    # 单个集群 f01000 checkbox
    one_miner_checkbox = ('xpath', '//td[@title="f01000"]/..//input')
    # 集群全选框 checkbox
    all_miners_checkbox = ('xpath', '//th[@title="集群"]/..//span//input')
    # 编辑按钮 terry001-autotest
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
        self.wait(0.5)
        if is_leader == "False":
            if self.locators(*self.enable_checkbox)[0].is_selected():
                self.click_elements(*self.enable_checkbox, list_number=0)
        elif is_enable == "True":
            if not self.locators(*self.enable_checkbox)[0].is_selected():
                self.click_elements(*self.enable_checkbox, list_number=0)
        if is_approve == "False":
            if self.locators(*self.enable_checkbox)[1].is_selected():
                self.click_elements(*self.enable_checkbox, list_number=1)
        elif is_enable == "True":
            if not self.locators(*self.enable_checkbox)[1].is_selected():
                self.click_elements(*self.enable_checkbox, list_number=1)
        if is_enable == "False":
            if self.locators(*self.enable_checkbox)[2].is_selected():
                self.click_elements(*self.enable_checkbox, list_number=2)
        elif is_enable == "True":
            if not self.locators(*self.enable_checkbox)[2].is_selected():
                self.click_elements(*self.enable_checkbox, list_number=2)
        mylogger.info("点进保存按钮")
        self.click_span_button("保 存")
        self.wait(0.5)

    # 点击查看用户信息详情
    def check_userinfo(self):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("用户")
        # 点击用户terry001-autotest 的查看按钮
        self.click_element(*self.check_button)

    # 编辑用户信息
    def edit_userinfo(self, username, chinesename, phone, email, is_leader="False", is_approve="False", is_enable="True"):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("用户")
        # 点击用户terry0001-autotest的查看按钮
        self.click_element(*self.check_button)
        self.wait()
        self.click_element(*self.edit_button)
        if username:
            self.input_text(*self.username_input, username)
        if chinesename:
            self.input_text(*self.chinesename_input, chinesename)
        if phone:
            self.input_text(*self.phone_input, phone)
        if email:
            self.input_text(*self.email_input, email)
        self.wait(0.5)
        if is_leader == "False":
            if self.locators(*self.enable_checkbox)[0].is_selected():
                self.click_elements(*self.enable_checkbox, list_number=0)
        elif is_enable == "True":
            if not self.locators(*self.enable_checkbox)[0].is_selected():
                self.click_elements(*self.enable_checkbox, list_number=0)
        if is_approve == "False":
            if self.locators(*self.enable_checkbox)[1].is_selected():
                self.click_elements(*self.enable_checkbox, list_number=1)
        elif is_enable == "True":
            if not self.locators(*self.enable_checkbox)[1].is_selected():
                self.click_elements(*self.enable_checkbox, list_number=1)
        if is_enable == "False":
            if self.locators(*self.enable_checkbox)[2].is_selected():
                self.click_elements(*self.enable_checkbox, list_number=2)
        elif is_enable == "True":
            if not self.locators(*self.enable_checkbox)[2].is_selected():
                self.click_elements(*self.enable_checkbox, list_number=2)
        mylogger.info("点进保存按钮")
        self.click_span_button("保 存")
        self.wait(0.5)



    # 用户关联角色
    def bind_role(self, rolename, state="one", is_save=True):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("用户")
        self.click_element(*self.bind_role_button)
        self.wait(1)
        if state == "all":
            if not self.locator(*self.all_roles_checkbox).is_selected():
                self.click_element(*self.all_roles_checkbox)
        elif state == "one":
            one_role_checkbox = ('xpath', f'//td[@title="{rolename}"]/../td[1]/label')
            if not self.locator(*one_role_checkbox).is_selected():
                self.click_element(*one_role_checkbox)
        if is_save:
            self.wait()
            self.click_span_button("确 定",type="button")
        else:
            self.click_element(*self.cancel_button)

    # 用户关联集群
    def bind_miner(self, minerid_list=None, is_select=True, select_all=False, is_save=True):
        """
        用户绑定集群
        :param minerid_list: 集群id列表
        :param is_select: 绑定还是去除绑定
        :param state: 是否全选
        :param is_save:
        :return:
        """
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("用户")
        self.click_element(*self.bind_cluster_button)
        self.wait()
        # 判断是否是全选操作
        if select_all:
            all_miners_checkbox = ('xpath', '//th[@title="集群"]/../th[1]/div/label/span')
            state = self.locator(*all_miners_checkbox).get_attribute("class")
            mylogger.info(state)
            if state != "ant-checkbox ant-checkbox-checked":
                self.click_element(*all_miners_checkbox)
        # 根据输入的minerid列表进行处理
        if minerid_list:
            for minerid in minerid_list:
                xpath = ('xpath', f'//td[text()="{minerid}"]/../td[1]/label/span')
                classname = self.locator(*xpath).get_attribute("class")
                if is_select:
                    if classname == "ant-checkbox":
                        self.click_element(*xpath)
                else:
                    if classname == "ant-checkbox ant-checkbox-checked":
                        self.click_element(*xpath)
        if is_save:
            self.wait()
            self.click_element(*self.confirm_button)
        else:
            self.click_element(*self.cancel_button)

    # 输入用户名搜索用户，不支持模糊匹配
    def _search_by_username(self, username=None):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("用户")
        if username:
            self.input_text(content=username, text="用户")
        self.click_element(*self.search_button)
        # self.click_navigation_bar("用户管理")
        # self.click_navigation_bar("系统设置")


    def _search_by_customer(self, customername=None):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("用户")
        if customername:
            self.div_selector(self.search_customer, name=customername)
            # self.click_navigation_bar("用户管理")
            # self.click_navigation_bar("系统设置")


    def search(self,username=None, customername=None, by_username=True, by_customer=True):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("用户")
        if username:
            self.input_text(content=username, text="用户")
        self.click_element(*self.search_button)
        if customername:
            self.div_selector(self.search_customer, name=customername)

        # if by_username and not by_customer:
        #     mylogger.info(f"输入{username}进行搜索")
        #     self._search_by_username(username)
        #     self.wait()
        # elif by_customer and not by_username:
        #     mylogger.info(f"按所属客户{customername}进行搜索")
        #     self._search_by_customer()
        #     self.wait()
        # elif by_username and by_customer:
        #     mylogger.info(f"输入{username}和按所属客户{customername}进行搜索")
        #     self._search_by_username(username)
        #     self._search_by_customer(customername)
        #     self.wait()