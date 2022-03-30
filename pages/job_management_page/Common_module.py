from common.keywords import KeyWords

class CustemorPage(KeyWords):
    # 作业管理
    job_management = ('xpath', '//span[text()="作业管理"]')
    # 点击新建
    newly_build = ('xpath', '//span[text()="新建"]')
    # 点击添加模板
    add_temolate = ('xpath', '//span[text()="添加模板类型"]')
    # 输入
    input_info = ('css', '.ant-input')
    # 下拉框定位
    fliter_box = ('css', '#rc_select_0')

    def operation_info(self):
        self.click_navigation_bar("作业管理")
        self.click_navigation_bar(" 公共模板")
        self.click_span_button(text="新建")
        self.click_element(*self.add_temolate)
        self.input_text(*self.input_info[3], content ="测试")
        self.click_span_button(text="确 定")
        self.div_selector(self.fliter_box, name="测试")
        # self.input_text(self, content="查看内存", text="模板名称")
        # self.input_text(self ,content="111", text="模板内容")
        # self.input_text(self, content="测试", text="备注")