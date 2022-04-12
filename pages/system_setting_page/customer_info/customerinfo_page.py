from common.keywords import KeyWords
from common.my_logger import mylogger


class CustomerInfoPage(KeyWords):
    '''
    页面元素的定位信息
    '''
    # 系统设置
    system_setting = ('xpath', '//span[text()="系统设置"]')
    # 客户信息
    machineroom_info = ('xpath', '//span[text()=" 客户信息"]')
    # 新建客户按钮
    new_custemor = ('xpath', '//span[text()="新建客户"]')
    # 客户名称输入框
    name_input = ('xpath', '//form/div[1]/div[2]/div/div/input')
    # 备注输入框
    comment_input = ('xpath', '//form/div[2]/div[2]/div/div/input')
    # 客户test001的编辑按钮
    edit_button = ('xpath', '//span[contains(text(),"test001")]/../..//button[1]')
    # 客户test002的删除按钮
    delete_button = ('xpath', '//span[contains(text(),"test002")]/../..//button[2]')


    def handle_new_customerinfo_alert(self, name=None, content=None):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar(" 客户信息")
        self.click_navigation_bar("系统设置")
        self.click_span_button("新建客户")
        if name:
            self.input_text(content=name,text="客户简称")
        if content:
            self.input_text(content=content,text="备注")

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

    def handle_edit_customerinfo_alert(self, name, content):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar(" 客户信息")
        self.click_navigation_bar("系统设置")
        self.click_element(*self.edit_button)
        if name:
            self.input_text(content=name,text="客户简称")
            self.wait(0.5)
        if content:
            self.input_text(content=content,text="备注")
            self.wait(0.5)



    def delete_customer(self):

        self.click_navigation_bar("系统设置")
        mylogger.info("----------刷新浏览器----------")
        self.driver.refresh()
        self.wait()
        self.click_navigation_bar(" 客户信息")
        mylogger.info("点击删除按钮")
        self.click_element(*self.delete_button)
        self.wait()
        mylogger.info("点击确定按钮，确认删除客户")
        self.click_span_button("确 定")


