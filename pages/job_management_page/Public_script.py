from common.keywords import KeyWords
from common.windows_popup import WinAuto
from common.my_logger import mylogger


class CustemorPage(KeyWords):

    # 脚本类型
    type_info = ('xpath', '//label[@title="脚本类型"]/../../div[2]/div/div/div/div')
    # 添加脚本类型确定
    sure = ('xpath', '//input[@placeholder="脚本类型名称"]/../../div[3]/button[2]/span')
    # 添加脚本类型取消
    cancel = ('xpath','//input[@placeholder="脚本类型名称"]/../../div[3]/button[1]/span')
    # 编辑
    edix = ('xpath', '//tbody[@class="ant-table-tbody"]/tr[2]/td[2]/button[1]/span')
    # 定位编辑输入框
    inputinfo = ('xpath','//input[@type="text"]/../span/../input')
    # 编辑保存
    storage = ('xpath', '//span[@class="ant-input-suffix"]/a[1]')
    # 编辑取消
    disappear =('xpath', '//span[@class="ant-input-suffix"]/a[2]')
    # 管理取消
    disappear2 = ('xpath','//div[2]/div[3]/button[1]/span')
    # 本地ym脚本参数化
    yamll = r"C:\Users\Administrator\Desktop\text.yaml"
    # 本地文件选择
    local = ('xpath','//span[text()="本地选择"]')

    # 添加脚本类型
    def add_type(self, name=None):
        self.click_navigation_bar("作业管理")
        self.click_navigation_bar(" 公共脚本")
        self.click_span_button("添加脚本")
        self.click_span_button("添加脚本类型")
        if name:
            self.input_text(type="placeholder", text="脚本类型名称", content=name)

    #添加脚本类型确定/取消
    def sure_cancel(self,judge=True):
        if judge:
            mylogger.info("点击确定")
            self.click_element(*self.sure)
            self.wait()
        else:
            mylogger.info("点击取消")
            self.click_element(*self.cancel)
            self.wait()
            self.click_navigation_bar("作业管理")


    # 管理脚本类型
    def script_operinfo(self, text=None):
        self.click_navigation_bar("作业管理")
        self.click_navigation_bar(" 公共脚本")
        self.click_span_button("添加脚本")
        self.click_span_button("管理脚本类型")
        self.click_element(*self.edix)
        self.input_text(*self.inputinfo,content=text)
        self.click_element(*self.storage)
        self.click_span_button("确 定")
        self.wait(2)
        self.click_navigation_bar("作业管理")





    def New_script(self, type=None, choice=None, edition=None, describe=None):
        self.click_navigation_bar("作业管理")
        self.click_navigation_bar(" 公共脚本")
        self.click_span_button("添加脚本")
        self.wait()
        if type:
            self.div_selector(self.type_info, name=type)

        if choice:
            self.click_span_button(choice)
            self.wait(2)
            # 用pywinauto处理Windows弹窗
            window = WinAuto("#32770", "打开")
            self.wait()
            window.file_input(self.yamll)
            self.wait()
            window.open_button_click()

        if edition:
            self.input_text(self, type="input", text="版本号", content=edition)
        if describe:
            self.input_text(self, type="textarea", text="脚本描述", content=describe)
        self.click_span_button("保 存")
        self.click_navigation_bar("作业管理")