from common.keywords import KeyWords
import unittest

class operation_info(KeyWords):
    Target_cluster = ('xpath', '//form/div[2]/div[2]/div/div/div/div/span[2]')
    select_host = ('xpath', '//span[text()="+选择主机"]')
    checkinfo = ('css','input.ant-checkbox-input')
    determine= ('xpath','//span[text()="确 认"]/..')
    choiceinfo =('xpath','//span[text()="选 择"]')
    parameter = ('xpath', '//label[@title="脚本参数"]/../../div/div/div')
    duration = ('xpath', '//label[@title="超时时长"]/../../div/div/div/input')
    name = ('xpath', '//label[@title="备注"]/../../div[2]/div')
    cancel = ('xpath','//span[text()="取 消"]')
    quern1 = ('xpath','//div[4]/div/div[2]/div/div[2]/div[2]/footer/button[2]')


    # 点击勾选脚本
    Tick_script=('css','.ant-radio-input')


    def Correct_operation(self, name=None,parameter=None,duration=None,remarks=None):
        self.click_navigation_bar("作业管理")
        self.click_navigation_bar(" 任务管理")
        self.wait(2)
        self.click_span_button("添加任务")
        self.wait()
        self.input_text(type="input", text="任务名称", content=name)
        self.div_selector(self.Target_cluster, name="内部f060975")
        self.input_host(self.select_host, host="KJ2020100610006")
        self.click_elements(*self.determine, list_number=0)
        self.wait(2)
        self.input_host(self.choiceinfo, choice="text.yaml")
        self.click_elements(*self.determine, list_number=1)
        self.wait(2)
        self.input_text(type="placeholder",text="脚本执行时传入的参数，如/test.sh",content=parameter)
        self.input_text(*self.duration,content=duration)
        self.input_text(type="placeholder",text="请输入任务描述或脚本说明",content=remarks)
        self.click_span_button("保 存")


    # 处理单独提示断言
    def select_boxinfo(self,type=None,host=None,choice=None, state=False):
        self.click_navigation_bar("作业管理")
        self.click_navigation_bar(" 任务管理")
        self.wait()
        self.click_span_button("添加任务")
        self.input_text(type="input", text="任务名称", content="测试")
        if type:
            self.div_selector(self.Target_cluster, name=type)
        self.input_host(self.select_host, host=host)
        if type:
            self.click_span_button("确 认")
            self.wait()
        if state:
            self.input_host(self.choiceinfo,choice=choice)
            self.wait(2)
            self.click_elements(*self.determine,list_number=1)





