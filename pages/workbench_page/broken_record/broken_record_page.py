import random
import time
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import Keys
from common.keywords import KeyWords


class BrokenRecordPage(KeyWords):
    """
    页面元素定位信息
    """
    # 新建弹窗元素
    # 日期输入框
    date_input = ('xpath', '//input[@placeholder="选择故障发生日期"]')
    # 选择集群select
    miner_select = ('xpath', '//label[@title="集群"]/../../div[2]/div')
    type_select = ('xpath', '//label[@title="故障分类"]/../../div[2]/div')
    level_select = ('xpath', '//label[@title="故障等级"]/../../div[2]/div')
    status_select = ('xpath', '//label[@title="处理状态"]/../../div[2]/div')
    div_select = ('css', 'div.ant-select-item-option-content')
    # 搜索栏页面元素定位信息
    # 故障分类input
    type_input = ('xpath', '//form/div[1]/div/div/div/div[1]')
    # 故障等级input
    level_input = ('xpath', '//form/div[1]/div/div/div/div[2]')
    # 处理状态
    status_input = ('xpath', '//form/div[1]/div/div/div/div[3]')
    # 搜索输入框,支持集群ID和客户进行搜索
    search_input = ('xpath', '//input[@placeholder="集群ID\客户"]')
    # 搜索图标按钮
    search_button = ('xpath', '//input[@placeholder="集群ID\客户"]/../span')

    # 新建故障记录
    def add_record(self, minerid, description=None, reason=None, sort="软件问题", level="中", status="进行中"):
        self.click_navigation_bar("工作台")
        self.click_navigation_bar("故障记录")
        self.click_span_button("新建记录")
        self.click_element(*self.date_input)
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.input_text(content=now, text="日期")
        self.div_selector(self.miner_select, self.div_select, name=minerid)
        if description:
            self.input_text(content=description, text="故障描述", type="textarea")
        if reason:
            self.input_text(content=reason, text="故障原因", type="textarea")
        if sort:
            self.div_selector(self.type_select, self.div_select, name=sort)
        if level:
            self.div_selector(self.level_select, self.div_select, name=level)
        if status:
            self.div_selector(self.status_select, self.div_select, name=status)
        self.click_span_button("确 定")

    # 编辑按钮 默认选择故障别表中第一条故障信息
    edit_button = ('xpath', '//tbody/tr[2]/td[10]/button[1]')
    def edit_record(self, minerid, description=None, reason=None, sort=None, level=None, status=None):
        self.click_navigation_bar("工作台")
        self.click_navigation_bar("故障记录")
        self.click_element(*self.edit_button)
        # 处理弹窗里面的内容
        self.click_element(*self.date_input)
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.input_text(content=now, text="日期")
        self.div_selector(self.miner_select, self.div_select, name=minerid)
        if description:
            self.input_text(content=description, text="故障描述", type="textarea")
        if reason:
            self.input_text(content=reason, text="故障原因", type="textarea")
        if sort:
            self.div_selector(self.type_select, self.div_select, name=sort)
        if level:
            self.div_selector(self.level_select, self.div_select, name=level)
        if status:
            self.div_selector(self.status_select, self.div_select, name=status)
        self.click_span_button("确 定")

    # 删除按钮 多个
    delete_buttons = ('xpath', '//span[text()="删除"]')
    def delete_record(self, times=1):
        """
        删除后页面会自动刷新，导致旧元素获取不到，引起旧元素引用异常的错误，还需进行优化该方法，暂时先留着
        :param times:
        :return:
        """
        self.click_navigation_bar("工作台")
        self.click_navigation_bar("故障记录")

        elements = self.locators(*self.delete_buttons)
        for i in range(len(elements)):
            if times > 0:
                self.click_elements(*self.delete_buttons, 0)
                self.click_span_button("确 定")
                times -= 1

    def search_record(self, type=None, level=None, status=None, text=None, start_time=None, end_time=None):
        self.click_navigation_bar("工作台")
        self.click_navigation_bar("故障记录")
        self.click_span_button("清 空")
        if type:
            self.div_selector(self.type_input, self.div_select, name=type)
        if level:
            self.div_selector(self.level_input, self.div_select, name=level)
        if status:
            self.div_selector(self.status_input, self.div_select, name=status)
        if text:
            self.input_text(*self.search_input, content=text)
            self.click_element(*self.search_button)
        if start_time and end_time:
            self.input_text(content=start_time, text="开始日期", type="placeholder")
            self.input_text(content=end_time, text="结束日期", type="placeholder")
            self.locator('xpath', '//input[@placeholder="结束日期"]').send_keys(Keys.ENTER)
        self.wait()
