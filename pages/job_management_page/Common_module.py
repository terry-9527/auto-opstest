from common.keywords import KeyWords

class CustemorPage(KeyWords):
    # 作业管理
    job_management = ('xpath', '//span[text()="作业管理"]')
    # 点击新建
    newly_build = ('xpath', '//span[text()="新建"]')
    # 点击添加模板
    add_temolate = ('xpath', '//span[text()="添加模板类型"]')
    # 输入
    input_info = ('xpath', '//label[@title="模板类型"]/../../div/div/div/div/div/span')
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


    def operation_info(self):
        self.click_navigation_bar("作业管理")
        self.click_navigation_bar(" 公共模板")
        self.click_span_button(text="新建")
        self.click_element(*self.add_temolate)
        self.input_text(self, type="placeholder" , text="模板类型名称", content="测试")
        self.click_span_button(text="确 定")
        self.div_selector(self.input_info,  name='测试')
        self.input_text(self, type="input", text="模板名称", content="查看内存")
        self.input_text(self, type="textarea", text="模板内容", content=self.script1)
        self.input_text(self, type="input", text="备注", content="测试")
        self.click_span_button(text="保 存")

    def err_operation(self, name=None, content1=None, remarks=None):
        self.click_navigation_bar("作业管理")
        self.wait(2)
        self.click_navigation_bar(" 公共模板")
        self.wait(2)
        self.click_span_button(text="新建")
        # self.click_element(*self.add_temolate)
        # self.input_text(self, type="placeholder" , text="模板类型名称", content="测试")
        # self.click_span_button(text="确 定")
        self.div_selector(self.input_info,  name="测试")
        if name:
            self.input_text(self, type="input", text="模板名称", content=name)
        if content1=='no':
            self.input_text(self, type="textarea", text="模板内容", content=None)
        elif content1=='yes':
            self.input_text(self, type="textarea", text="模板内容", content=self.script1)
        if remarks:
            self.input_text(self, type="input", text="备注", content=remarks)
        self.click_span_button(text="保 存")