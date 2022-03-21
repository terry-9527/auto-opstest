from common.keywords import KeyWords


class RoleManagementPage(KeyWords):
    '''
    用户所有页面元素定位信息
    '''
    # 新建角色
    new_role_button = ('xpath', '//span[text()="新建角色"]')
    # 角色名输入框
    role_input = ('xpath', '//label[@title="角色名"]/../..//input')
    # 备注输入框
    comment_input = ('xpath', '//label[@title="备注"]/../..//input')
    # 所属客户div下拉输入框
    customer_input = ('xpath', '//label[@title="所属客户"]/../..//input')
    # div 下拉框
    div_select = ('css', 'div.ant-select-item-option-content')
    # 确定按钮
    confirm_button = ('xpath', '//span[text()="确 定"]')
    # 取消按钮
    cancel_button = ('xpath', '//span[text()="取 消"]')
    # 编辑按钮 test001角色
    edit_button = ('xpath', '//*[@class="ant-table-container"]//span[text()="test001"]/../..//span[text()="编辑"]')
    # 删除按钮 test001
    delete_button = ('xpath', '//*[@class="ant-table-container"]//span[text()="test001"]/../..//span[text()="删除"]')
    # 删除弹窗确定按钮
    confirm_delete_button = ('xpath', '//div[@class="ant-modal-confirm-btns"]//span[text()="确 定"]')
    # 删除弹窗取消按钮
    cancel_delete_button = ('xpath', '//div[@class="ant-modal-confirm-btns"]//span[text()="取 消"]')
    # 设置角色权限按钮
    role_setting_button = ('xpath', '//*[@class="ant-table-container"]//span[text()="test001"]/../..//a[text()="设置"]')
    # 复选框
    checkbox = ('xpath', '//main/div[3]//span[@class="ant-tree-checkbox-inner"]')
    # 保存按钮
    save_button = ('xpath', '//span[text()="保 存"]')
    # 最后一个权限名称 下单设置(页面)
    last_name = ('xpath', '//*[@id="app"]/div/main/div[3]/div/div/div/div[3]/div[1]/div/div/div[17]/span[4]/span')



    def add_role(self, role_name, comment, is_save=True):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("角色")
        self.click_element(*self.new_role_button)
        self.input_text(*self.role_input, role_name)
        self.input_text(*self.comment_input, comment)
        if is_save:
            self.click_element(*self.confirm_button)
            self.wait(1)
        else:
            self.click_element(*self.cancel_button)
            self.wait(1)


    def edit_role(self, role_name, comment, is_save=True):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("角色")
        self.click_element(*self.edit_button)
        self.input_text(*self.role_input, role_name)
        self.input_text(*self.comment_input, comment)
        if is_save:
            self.click_element(*self.confirm_button)
            self.wait(1)
        else:
            self.click_element(*self.cancel_button)
            self.wait(1)

    def delete_role(self,is_delete=True):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("角色")
        self.click_element(*self.delete_button)
        if is_delete:
            self.click_element(*self.confirm_delete_button)
            self.wait(1)
        else:
            self.click_element(*self.cancel_delete_button)
            self.wait(1)


    def setting_role(self, is_save=True):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("角色")
        self.click_element(*self.role_setting_button)
        self.wait(1)
        checkboxs = self.locators(*self.checkbox)
        # print(len(checkboxs))
        for i in range(len(checkboxs)-2):
            if checkboxs[i].is_selected():
                continue
            checkboxs[i].click()
        # 拖动到页面最下端的元素
        target = self.locator(*self.last_name)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.wait(1)
        checkboxs = self.locators(*self.checkbox)
        # print(len(checkboxs))
        for i in range(17,25):
            if checkboxs[i].is_selected():
                continue
            checkboxs[i].click()
        if is_save:
            self.click_element(*self.save_button)
            self.wait(1)
