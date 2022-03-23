import random

from selenium.webdriver.common.keys import Keys

from common.keywords import KeyWords
from utils.read_db import MysqlDb


class ApprovalProcessPage(KeyWords):
    system_setting = ('xpath', '//span[text()="新 建"]')
    # 名称输入框 //label[@title="名称"]/../..//input
    name_input = ('xpath', '//label[@title="名称"]/../..//input')
    # 审核人1 input
    first_approval_input = ('xpath', '//label[@title="审核人1"]/../..//input')
    second_approval_input = ('xpath', '//label[@title="审核人2"]/../..//input')
    three_approval_input = ('xpath', '//label[@title="审核人3"]/../..//input')
    # 通知人 input
    notifier_input = ('xpath', '//label[@title="通知人"]/../..//input')
    # 通知方式 input
    notify_type_input = ('xpath', '//label[@title="通知方式"]/../..//input')
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
        self.wait(1)
        self.click_navigation_bar("审批流")
        self.wait(1)
        self.click_span_button("新 建")
        self.input_text(content=process_name, text="名称")
        # 查询出参与审批的人数
        data = MysqlDb().query("select user_name from `t_user` where approve=1 group by id")
        approvename_list = []
        order = 1
        for i in range(len(data)):
            approvename_list.append(data[i][0])
        approve_list = list(filter(None, [approve1, approve2, approve3]))
        for name in approve_list:
            index = approvename_list.index(name)
            for i in range(len(approvename_list)):
                if order == 1:
                    if i == index:
                        self.click_element(*self.first_approval_input)
                        self.locator(*self.first_approval_input).send_keys(Keys.ENTER)
                        self.locator(*self.first_approval_input).send_keys(Keys.ARROW_DOWN)
                        order += 1
                        break
                    else:
                        self.locator(*self.first_approval_input).send_keys(Keys.ARROW_DOWN)
                elif order == 2:
                    if i == index:
                        self.click_element(*self.second_approval_input)
                        self.locator(*self.second_approval_input).send_keys(Keys.ENTER)
                        self.locator(*self.second_approval_input).send_keys(Keys.ARROW_DOWN)
                        order += 1
                        break
                    else:
                        self.locator(*self.second_approval_input).send_keys(Keys.ARROW_DOWN)
                elif order == 3:
                    if i == index:
                        self.click_element(*self.three_approval_input)
                        self.locator(*self.three_approval_input).send_keys(Keys.ENTER)
                        self.locator(*self.three_approval_input).send_keys(Keys.ARROW_DOWN)
                        break
                    else:
                        self.locator(*self.three_approval_input).send_keys(Keys.ARROW_DOWN)

        self.click_element(*self.notifier_input)
        users = MysqlDb().query("select user_name from `t_user` group by id")
        username_list = []
        for i in range(len(users)):
            username_list.append(users[i][0])
        for name in notifiers:
            name_index = username_list.index(name)
            for i in range(0, len(username_list)):
                if i == name_index:
                    self.locator(*self.notifier_input).send_keys(Keys.ENTER)
                    self.locator(*self.notifier_input).send_keys(Keys.ARROW_DOWN)
                    self.wait()
                else:
                    self.locator(*self.notifier_input).send_keys(Keys.ARROW_DOWN)
        self.click_element(*self.notifier)

        # 选择通知方式
        self.click_element(*self.notify_type_input)
        self.wait(1)
        self.locator(*self.notify_type_input).send_keys(Keys.ENTER)
        self.wait(1)
        self.locator(*self.notify_type_input).send_keys(Keys.ARROW_DOWN)
        self.wait(1)
        self.locator(*self.notify_type_input).send_keys(Keys.ENTER)
        self.click_element(*self.notify_type)
        self.wait(1)
        self.click_span_button("保 存")



    # 编辑审批流
    def edit_process(self, process_name, approve1=None, approve2=None, approve3=None, notifiers=None, type=None):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("审批流")
        self.wait(1)
        self.click_element(*self.edit_button)
        self.input_text(content=process_name, text="名称")
        # 查询出参与审批的人数
        data = MysqlDb().query("select user_name from `t_user` where approve=1 group by id")
        approvename_list = []
        order = 1
        for i in range(len(data)):
            approvename_list.append(data[i][0])
        approve_list = list(filter(None, [approve1, approve2, approve3]))
        for name in approve_list:
            index = approvename_list.index(name)
            print(index)
            for i in range(len(approvename_list)):
                if order == 1:
                    if i == index:
                        # self.click_element(*self.first_approval_input)
                        self.locators(*('css','span.ant-select-selection-item'))[0].click()
                        self.locator(*self.first_approval_input).send_keys(Keys.ENTER)
                        self.locator(*self.first_approval_input).send_keys(Keys.ARROW_DOWN)
                        order += 1
                        break
                    else:
                        self.locator(*self.first_approval_input).send_keys(Keys.ARROW_DOWN)
                elif order == 2:
                    if i == index:
                        # self.click_element(*self.second_approval_input)
                        self.locators(*('css', 'span.ant-select-selection-item'))[1].click()
                        self.locator(*self.second_approval_input).send_keys(Keys.ENTER)
                        self.locator(*self.second_approval_input).send_keys(Keys.ARROW_DOWN)
                        order += 1
                        break
                    else:
                        self.locator(*self.second_approval_input).send_keys(Keys.ARROW_DOWN)
                elif order == 3:
                    if i == index:
                        # self.click_element(*self.three_approval_input)
                        self.locators(*('css', 'span.ant-select-selection-item'))[2].click()
                        self.locator(*self.three_approval_input).send_keys(Keys.ENTER)
                        self.locator(*self.three_approval_input).send_keys(Keys.ARROW_DOWN)
                        break
                    else:
                        self.locator(*self.three_approval_input).send_keys(Keys.ARROW_DOWN)

        self.click_element(*self.notifier_input)
        users = MysqlDb().query("select user_name from `t_user` group by id")
        username_list = []
        for i in range(len(users)):
            username_list.append(users[i][0])
        for name in notifiers:
            name_index = username_list.index(name)
            for i in range(0, len(username_list)):
                if i == name_index:
                    self.locator(*self.notifier_input).send_keys(Keys.ENTER)
                    self.locator(*self.notifier_input).send_keys(Keys.ARROW_DOWN)
                    self.wait()
                else:
                    self.locator(*self.notifier_input).send_keys(Keys.ARROW_DOWN)
        self.click_element(*self.notifier)

        # 选择通知方式
        for i in range(random.choice([0,1])):
            self.click_element(*self.notify_type_input)
            self.wait(1)
            self.locator(*self.notify_type_input).send_keys(Keys.ENTER)
            self.wait(1)
            self.locator(*self.notify_type_input).send_keys(Keys.ARROW_DOWN)
            self.wait(1)
            self.locator(*self.notify_type_input).send_keys(Keys.ENTER)
            self.click_element(*self.notify_type)
        self.click_span_button("保 存")

    # 查看审批流
    def check_process(self):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("审批流")
        self.click_element(*self.check_button)
        self.wait()
        self.click_span_button("确 定")

    # 删除审批流
    def delete_process(self):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("审批流")
        self.click_element(*self.delete_button)
        self.wait()
        self.click_span_button("确 定")


    # 关联操作页面--复选框
    checkbox_button = ('css', 'span.ant-tree-checkbox-inner')

    # 绑定关联操作
    def bind_action(self):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("审批流")
        self.click_element(*self.bind_button)
        checkboxs = self.locators(*self.checkbox_button)
        print(len(checkboxs))
        for i in range(len(checkboxs)):
            self.wait(0.1)
            if not checkboxs[i].is_selected():
                checkboxs[i].click()
        self.wait()
        self.click_span_button("确 定")
