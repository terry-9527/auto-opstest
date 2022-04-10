import random

from selenium.webdriver.common.keys import Keys

from common.keywords import KeyWords
from common.my_logger import mylogger
from utils.read_db import MysqlDb


class ApprovalProcessPage(KeyWords):
    system_setting = ('xpath', '//span[text()="新 建"]')
    # 名称输入框 //label[@title="名称"]/../..//input
    name_input = ('xpath', '//label[@title="名称"]/../..//input')
    # 审核人1 input
    first_approval_input = ('xpath', '//label[@title="审核人1"]/../../div[2]/div/div/div/div')
    # first_approval_input = ('xpath', '//label[@title="审核人1"]/../..//input')
    second_approval_input = ('xpath', '//label[@title="审核人2"]/../../div[2]/div/div/div/div')
    # second_approval_input = ('xpath', '//label[@title="审核人2"]/../..//input')
    three_approval_input = ('xpath', '//label[@title="审核人3"]/../../div[2]/div/div/div/div')
    # three_approval_input = ('xpath', '//label[@title="审核人3"]/../..//input')
    # 通知人 input
    notifier_input = ('xpath', '//label[@title="通知人"]/../../div[2]/div/div/div/div')
    # 通知方式 input
    notify_type_input = ('xpath', '//label[@title="通知方式"]/../../div[2]/div/div/div/div')
    # 通知人label
    notifier = ('xpath', '//label[@title="通知人"]')
    # 通知方式label
    notify_type = ('xpath', '//label[@title="通知方式"]')
    # test001 对应的 编辑、查看、删除、关联操作按钮
    edit_button = ('xpath', '//*[@class="ant-table-container"]//span[contains(text(),"test001")]/../..//span[text()="编辑"]')
    check_button = ('xpath', '//*[@class="ant-table-container"]//span[contains(text(),"test001")]/../..//span[text()="查看"]')
    delete_button = ('xpath', '//*[@class="ant-table-container"]//span[contains(text(),"test001")]/../..//span[text()="删除"]')
    bind_button = ('xpath', '//*[@class="ant-table-container"]//span[contains(text(),"test001")]/../..//span[text()="关联操作"]')


    def add_process(self, process_name, approve1=None, approve2=None, approve3=None, notifiers=None):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("审批流")
        self.click_span_button("新 建")
        self.input_text(content=process_name, text="名称")
        self.div_selector(self.first_approval_input, name=approve1)
        self.wait()
        self.div_selector(self.second_approval_input, name=approve2, which_index=2)
        self.wait()
        self.div_selector(self.three_approval_input, name=approve3, which_index=3)
        self.wait()
        # self.click_element(*self.notifier_input)
        # 选择通知方式
        # self.click_element(*self.notify_type_input)
        # self.wait(1)
        # self.locator(*self.notify_type_input).send_keys(Keys.ENTER)
        # self.wait(1)
        # self.locator(*self.notify_type_input).send_keys(Keys.ARROW_DOWN)
        # self.wait(1)
        # self.locator(*self.notify_type_input).send_keys(Keys.ENTER)
        # self.click_element(*self.notify_type)
        # self.wait(1)
        self.click_span_button("保 存")



    # 编辑审批流
    def edit_process(self, process_name, approve1=None, approve2=None, approve3=None, notifiers=None, type=None):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("审批流")
        self.click_span_button("新 建")
        self.input_text(content=process_name, text="名称")
        self.div_selector(self.first_approval_input, name=approve1)
        self.wait()
        self.div_selector(self.second_approval_input, name=approve2, which_index=2)
        self.wait()
        self.div_selector(self.three_approval_input, name=approve3, which_index=3)
        self.wait()
        self.click_span_button("保 存")

    # 查看审批流
    def check_process(self):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("审批流")
        self.click_element(*self.check_button)
        self.wait()
        self.click_navigation_bar("首页")

    # 删除审批流
    def delete_process(self):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("审批流")
        self.click_element(*self.delete_button)
        self.wait()
        self.click_span_button("确 定")


    # 关联操作页面--复选框
    checkbox_button = ('xpath', '//span[text()="主机管理(页面)"]/../../span[3]')
    # checkbox_button = ('css', 'span.ant-tree-checkbox-inner')

    # 绑定关联操作
    def bind_action(self):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("审批流")
        self.click_element(*self.bind_button)
        all_checkbox = self.locator(*self.checkbox_button)
        if not all_checkbox.get_attribute("class").endswith("checked"):
            all_checkbox.click()
        self.click_span_button("确 定")
        self.wait()
