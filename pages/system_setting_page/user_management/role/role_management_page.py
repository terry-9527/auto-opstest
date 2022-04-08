from common.keywords import KeyWords
from common.my_logger import mylogger


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
    customer_input = ('xpath', '//form/div[3]/div[2]/div[1]/div/div/div')
    # 编辑按钮 role001角色
    edit_button = ('xpath', '//span[contains(text(),"role001")]/../../td[6]//button[1]')
    # 删除按钮 role003
    # delete_button = ('xpath', '//span[contains(text(),"role003")]/../../td[6]//button[2]')


    # 设置角色权限按钮
    # role_setting_button = ('xpath', '//span[contains(text(),"role001")]/../../td[3]//a')
    # 复选框
    # checkbox = ('xpath', '//main/div[3]//span[@class="ant-tree-checkbox-inner"]')
    checkbox = ('css', 'span.ant-tree-title')
    # 保存按钮
    save_button = ('xpath', '//span[text()="保 存"]')
    # 最后一个权限名称 下单设置(页面)
    last_name = ('xpath', '//*[@id="app"]/div/main/div[3]/div/div/div/div[3]/div[1]/div/div/div[17]/span[4]/span')

    def handle_add_role_alert(self, name, comment, customer):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("角色")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("系统设置")
        self.click_span_button("新建角色")
        if name:
            self.input_text(*self.role_input, name)
            self.wait()
        if comment:
            self.input_text(*self.comment_input, comment)
            self.wait()
        if customer:
            self.div_selector(self.customer_input, name=customer)
            self.wait()

    # 处理是否保存
    def handle_save(self, is_save=True):
        if is_save:
            mylogger.info("点进确定按钮")
            self.click_span_button("确 定")
            self.wait()
        else:
            mylogger.info("点进取消按钮")
            self.wait(0.5)
            self.click_span_button("取 消")

    def handle_edit_role_alert(self, name, comment, customer):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("角色")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("系统设置")
        self.click_element(*self.edit_button)
        self.input_text(*self.role_input, name)
        self.wait(0.5)
        self.input_text(*self.comment_input, comment)
        self.wait(0.5)
        if customer:
            self.div_selector(self.customer_input, name=customer)
            self.wait(0.5)



    def delete_role(self, is_delete=True, rolename="role003"):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("角色")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("系统设置")
        mylogger.info(f"点击{rolename}角色删除按钮")
        # 删除按钮 role003
        delete_button = ('xpath', f'//span[contains(text(),"{rolename}")]/../../td[6]//button[2]')
        self.click_element(*delete_button)
        if is_delete:
            mylogger.info("确定删除角色")
            self.click_span_button("确 定")
            self.wait(1)
        else:
            mylogger.info("取消删除角色")
            self.click_span_button("取 消")
            self.wait(1)

    def setting_role_privilege(self, is_save=True, rolename="role001"):
        """目前只考虑设置所有的权限"""
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("角色")
        self.click_navigation_bar("用户管理")
        self.click_navigation_bar("系统设置")
        mylogger.info(f"开始为角色{rolename}设置权限")
        role_setting_button = ('xpath', f'//span[contains(text(),"{rolename}")]/../../td[3]//a')
        self.click_element(*role_setting_button)
        self.wait(1)
        checkboxs1 = self.locators(*self.checkbox)
        menu_list1 = []
        for name in checkboxs1:
            menu_list1.append(name.get_attribute("textContent"))
            self.double_click(name)
        # 滚动到底部进行勾选
        target = self.locator(*self.last_name)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.wait(1)
        checkboxs2 = self.locators(*self.checkbox)
        for name in checkboxs2:
            self.double_click(name)
        if is_save:
            self.click_element(*self.save_button)
            mylogger.info("权限设置成功")
            self.wait(1)
