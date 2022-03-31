from selenium.webdriver.common.keys import Keys

from common.keywords import KeyWords

# 用户名标签a
user_button = ('xpath', '//main//a')
# 下拉选项option
div_option = ('css', 'button.dropdown__son__btn')

class PersonalInfoPage(KeyWords):
    """
    页面元素定位信息
    """
    # 名称编辑按钮
    name_edit_button = ('xpath', '//label[@title="用户名"]/../..//span[2]')
    name_input = ('xpath', '//label[@title="用户名"]/../../div[2]//input')
    # 名称确认编辑按钮
    confirm_edit_name = ('xpath', '//label[@title="用户名"]/../..//button[1]')
    # 名称X按钮
    cancel_edit_name = ('xpath', '//label[@title="用户名"]/../..//button[2]')

    # 邮箱编辑按钮
    email_edit_button = ('xpath', '//label[@title="邮箱"]/../..//span[2]')
    email_input = ('xpath', '//label[@title="邮箱"]/../../div[2]//input')
    # 邮箱确认编辑按钮
    confirm_edit_email = ('xpath', '//label[@title="邮箱"]/../..//button[1]')
    # 邮箱X按钮
    cancel_edit_email = ('xpath', '//label[@title="邮箱"]/../..//button[2]')

    def check_personal_info(self, name=None, email=None):
        self.click_navigation_bar("首页")
        self.div_selector(user_button, div_option, name="个人信息")
        # 编辑名称
        if name:
            self.click_element(*self.name_edit_button)
            self.input_text(*self.name_input, content=name)
            self.wait()
            self.click_element(*self.confirm_edit_name)
        # 编辑Email
        if email:
            self.click_element(*self.email_edit_button)
            self.input_text(*self.email_input, content=email)
            self.wait()
            self.click_element(*self.confirm_edit_email)


class MyApprovalPage(KeyWords):
    """
    页面元素定位信息
    """
    # 审批状态下拉框input
    status_input = ('xpath', '//form/div[1]/div')
    div_select = ("css", "div.ant-select-item-option-content")
    # 搜索输入框
    search_input = ('xpath', '//input[@placeholder="输入关键字进行搜索"]')
    # 搜索图标按钮
    search_button = ('xpath', '//input[@placeholder="输入关键字进行搜索"]/../span')

    def search_approval_process(self, status=None, start_time=None, end_time=None, text=None):
        self.click_navigation_bar("首页")
        self.div_selector(user_button, div_option, name="我的审批")
        if status:
            self.div_selector(self.status_input, self.div_select,name="审核失败")
        if start_time and end_time:
            self.input_text(content="2022-03-27 13:00:53", text="开始日期", type="placeholder")
            self.input_text(content="2022-03-28 13:00:53", text="结束日期", type="placeholder")
            self.locator('xpath', '//input[@placeholder="结束日期"]').send_keys(Keys.ENTER)
        if text:
            self.input_text(content=text, text="输入关键字进行搜索", type="placeholder")
            self.click_element(*self.search_button)
            self.wait()

