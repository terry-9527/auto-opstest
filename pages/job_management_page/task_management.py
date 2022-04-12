from common.keywords import KeyWords


class operation_info(KeyWords):
    Target_cluster = ('css', '.ant-select-selection-item')
    select_host = ('xpath', '//span[text()="+选择主机"]')



    def Correct_operation(self):
        self.click_navigation_bar("作业管理")
        self.click_navigation_bar(" 任务管理")
        self.click_span_button("添加任务")
        self.input_text(type="input", text="任务名称", content="测试")
        self.div_selector(self.Target_cluster, name="内部f060975")
        self.input_host(self.select_host, host="KJ2020100610006")



