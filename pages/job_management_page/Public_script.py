from common.keywords import KeyWords
from common.windows_popup import WinAuto


class CustemorPage(KeyWords):

    # 脚本类型
    type_info = ('xpath', '//label[@title="脚本类型"]/../../div[2]/div/div/div/div')

    def New_script(self, filepath=None):
        self.click_navigation_bar("作业管理")
        self.click_navigation_bar(" 公共脚本")
        self.click_span_button("添加脚本")
        self.wait()
        self.div_selector(self.type_info, name="测试")
        self.click_span_button("本地选择")
        self.wait(2)
        # 用pywinauto处理Windows弹窗
        window = WinAuto("#32770", "打开")
        self.wait()
        window.file_input(r"C:\Users\Administrator\Desktop\text.yaml")
        self.wait()
        window.open_button_click()
        self.wait()
        self.input_text(self, type="input", text="版本号", content="4.10-v")
        self.input_text(self, type="textarea", text="脚本描述", content="查询节点")
        self.click_span_button("保 存")