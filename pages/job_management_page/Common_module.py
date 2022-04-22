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
    # input_info = ('xpath', '//*[contains(text(),"测试-223s22")]')
    # 取消
    button = ('xpath', '//div[@class="ant-modal-footer"]/button[1]/span')
    # 管理模板类型编辑
    testinfo = ('xpath', '//*[contains(text(),"测试")]/../../td[2]/button[1]')
    # 点击输入框
    inputinfo = ('xpath', '//tbody[@class="ant-table-tbody"]/tr[5]/td/span/input')
    # 保存
    preservation = ('xpath', '//span[@class="ant-input-suffix"]/a[1]')
    # 关闭
    stopinfo = ('xpath', '//span[@aria-label="close"]')
    # 删除
    delete = ('xpath', '//td[@title="测试"]/../td[2]/button[2]/span')


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
        mylogger.info("点击作业管理")
        self.click_navigation_bar("作业管理")
        self.click_navigation_bar(" 公共模板")
        self.click_span_button(text="新建")
        self.click_element(*self.add_temolate)
        self.wait(1)
        if text:
            self.input_text(self, type="placeholder" , text="模板类型名称", content=text)
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


    # 管理模板编辑模板
    def edit_template(self,test=None):
        self.click_navigation_bar("作业管理")
        self.click_navigation_bar(" 公共模板")
        self.click_span_button(text="新建")
        self.click_span_button(text="管理模板类型")
        self.click_element(*self.testinfo)
        self.input_text(*self.inputinfo,content=test)
        self.click_element(*self.preservation)
        self.click_element(*self.stopinfo)
        self.wait()
        self.click_navigation_bar("作业管理")


    # 管理模板删除操作
    def delete_info(self):
        self.click_navigation_bar("作业管理")
        self.click_navigation_bar(" 公共模板")
        self.click_span_button(text="新建")
        self.click_span_button(text="管理模板类型")
        self.click_element(*self.delete)





    # 新建模板
    def add_operation(self, type=None, name=None, content1=None, remarks=None):
        self.click_navigation_bar("作业管理")
        self.wait()
        self.click_navigation_bar(" 公共模板")
        self.wait()
        self.click_span_button(text="新建")
        self.wait(2)
        if type:
            self.div_selector(self.input_info, name=type)
        else:
            self.div_selector(self.input_info, name=type)
        if name:
            self.input_text(self, type="input", text="模板名称", content=name)
        if content1=='no':
            self.input_text(self, type="textarea", text="模板内容", content=content1)
        elif content1=='yes':
            self.input_text(self, type="textarea", text="模板内容", content=self.script1)
        if remarks:
            self.input_text(self, type="input", text="备注", content=remarks)
        self.click_span_button(text="保 存")
        self.wait(2)
        self.click_navigation_bar("作业管理")
