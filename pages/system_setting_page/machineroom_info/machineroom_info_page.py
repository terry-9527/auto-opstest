from common.keywords import KeyWords
from common.my_logger import mylogger

class MachineRoomInfoPage(KeyWords):
    '''
    页面元素的定位信息
    '''
    # 系统设置
    system_setting = ('xpath', '//span[text()="系统设置"]')
    # 机房信息
    machineroom_info = ('xpath', '//span[text()=" 机房信息"]')
    # 新建机房
    new_button = ('xpath', '//span[text()="新建机房"]')
    # 机房名称输入框
    roomname = ('xpath', '//label[@title="机房名称"]/../..//input')
    # 机房所在地输入框
    address = ('xpath', '//label[@title="机房所在地"]/../..//input')
    # 域名输入框
    domain = ('xpath', '//label[@title="域名"]/../..//input')
    # 备注输入框
    comment = ('xpath', '//label[@title="备注"]/../..//input')
    # 算力机是否可调度复选框
    scheduling_checkbox = ('xpath', '//input[@type="checkbox"]/..')
    # 取消按钮
    cancle_button = ('xpath', '//span[text()="取 消"]')
    # 确定按钮
    confirm_button = ('xpath', '//span[text()="确 定"]')
    # 退出X按钮
    quit_button = ('xpath', '//span[@class="ant-modal-close-x"]')
    # "我知道了"按钮
    success_confirm_button = ('xpath', '//span[text()="我知道了"]')
    # machineroom0001机房的编辑按钮框
    edit_button = ('xpath', '//span[contains(text(),"machineroom0001")]/../..//td[5]//span')
    # 权限分配按钮css定位信息
    assign_permission_button = ('css_selector', '.ant-table-tbody>tr:nth-child(5)>td:nth-child(5)>button:nth-child(1)')

    # 新建机房弹窗处理
    def handle_new_machineroom_alert(self, name, address, domain=None, comment=None, checkbox="False"):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar(" 机房信息")
        self.click_element(*self.new_button)
        mylogger.info(f"输入机房名称：{name}")
        self.input_text(*self.roomname, name)
        mylogger.info(f"输入机房所在地址：{address}")
        self.input_text(*self.address, address)
        mylogger.info(f"输入域名：{domain}")
        self.input_text(*self.domain, domain)
        mylogger.info(f"输入备注：{comment}")
        self.input_text(*self.comment,comment)
        if checkbox == "True":
            if not self.locator(*self.scheduling_checkbox).is_selected():
                mylogger.info("算力机是否可调度复选框未勾选")
                self.click_element(*self.scheduling_checkbox)
                self.wait()
    # 新建是否保存
    def handle_save(self, is_save=True):
        if is_save:
            mylogger.info("点进确定按钮")
            self.click_element(*self.confirm_button)
            self.wait()
        else:
            mylogger.info("点进取消按钮")
            self.click_element(*self.cancle_button)


    # 编辑机房信息
    def handle_edit_machineroom_alert(self, name, address, domain=None, comment=None, checkbox="False"):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar(" 机房信息")
        self.click_element(*self.edit_button)
        mylogger.info(f"输入机房名称：{name}")
        self.input_text(*self.roomname, name)
        mylogger.info(f"输入机房所在地址：{address}")
        self.input_text(*self.address, address)
        mylogger.info(f"输入域名：{domain}")
        self.input_text(*self.domain, domain)
        mylogger.info(f"输入备注：{comment}")
        self.input_text(*self.comment,comment)
        if checkbox == "True":
            if not self.locator(*self.scheduling_checkbox).is_selected():
                mylogger.info("算力机是否可调度复选框未勾选")
                self.click_element(*self.scheduling_checkbox)
                self.wait()



if __name__ == "__main__":
    pass
