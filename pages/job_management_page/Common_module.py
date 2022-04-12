from common.keywords import KeyWords
from common.my_logger import mylogger

class CustemorPage(KeyWords):
    # 作业管理
    job_management = ('xpath', '//span[text()="作业管理"]')
    # 点击新建
    newly_build = ('xpath', '//span[text()="新建"]')
    # 点击添加模板
    add_temolate = ('xpath', '//span[text()="添加模板类型"]')
    # 输入
    input_info = ('xpath', '//label[@title="模板类型"]/../../div/div/div/div/div/span')
    # 取消
    button = ('xpath', '//div[@class="ant-modal-footer"]/button[1]/span')
    # 管理模板类型编辑
    testinfo = ('xpath', '//*[contains(text(),"ssssssaaa")]/../../td[2]/button[1]')
    # 点击输入框
    inputinfo = ('xpath', '//tbody[@class="ant-table-tbody"]/tr[5]/td/span/input')
    # 保存
    preservation = ('xpath', '//span[@class="ant-input-suffix"]/a[1]')
    # 关闭
    stop = ('xpath', '//span[@aria-label="close"]')

    # # 下拉框定位
    # fliter_box = ('css', 'div.ant-select-selector')
    # # 模板内容
    # content_info = ('xpath', '//label[@title="模板内容"]/../../div/div/div/textarea')
    # # 保存新建
    # preservation = ('xpath', '//span[text()="保 存"]')

    # 模板内容写入yaml脚本

    script1 = """
---
- hosts: all
  remote_user: root
  tasks:
    - name: "查询内存"
      shell: free -h
      register: check
    - name: show
      debug: var=check.stdout verbosity=0
    
    """

    # 添加模板类型
    def app_type(self, text=None):
        self.click_navigation_bar("作业管理")
        self.click_navigation_bar(" 公共模板")
        self.click_span_button(text="新建")
        self.click_element(*self.add_temolate)
        self.wait(1)
        if text:
            self.input_text(self, type="placeholder" , text="模板类型名称", content=text)
            self.wait(2)
    # 添加模板类型（确定/取消）
    def determine_cancel(self,state=True):
        if state:
            mylogger.info("点击确定")
            self.click_span_button(text="确 定")
            self.wait(1)
        else:
            mylogger.info("点击取消")
            self.click_element(*self.button)
            self.wait(1)
            self.click_navigation_bar("作业管理")


    # 编辑模板
    def edit_template(self,test=None):
        self.click_navigation_bar("作业管理")
        self.click_navigation_bar(" 公共模板")
        self.click_span_button(text="新建")
        self.click_span_button(text="管理模板类型")
        self.click_element(*self.testinfo)
        # self.clear(*self.inputinfo)
        if test:
            self.input_text(*self.inputinfo,content=test)
        self.click_element(*self.preservation)




    # 新建模板
    def add_operation(self, type=True, name=None, content1=None, remarks=None):
        self.click_navigation_bar("作业管理")
        self.wait(1)
        self.click_navigation_bar(" 公共模板")
        self.wait(1)
        self.click_span_button(text="新建")
        self.click_navigation_bar("作业管理")
        # if text:
        #     self.input_text(self, type="placeholder", text="模板类型名称", content=text)
        # self.click_span_button(text="确 定")
        if type:
            self.div_selector(self.input_info,  name=type)
        if name:
            self.input_text(self, type="input", text="模板名称", content=name)
        if content1=='no':
            self.input_text(self, type="textarea", text="模板内容", content=content1)
        elif content1=='yes':
            self.input_text(self, type="textarea", text="模板内容", content=self.script1)
        if remarks:
            self.input_text(self, type="input", text="备注", content=remarks)
        self.click_span_button(text="保 存")