from common.keywords import KeyWords
from selenium import webdriver


class MachineRoomInfoPage(KeyWords):
    '''
    页面元素的定位信息
    '''
    # 系统设置
    system_setting = ('xpath', '//*[@id="app"]/div/aside/ul/li[5]/div/span[2]')
    # 机房信息
    machineroom_info = ('xpath', '//*[@id="sub_menu_4_$$_SystemSettings-popup"]/li[1]/span')
    # 新建机房
    new_button = ('xpath', '//span[text()="新建机房"]')
    # 机房名称输入框
    roomname = ('xpath', '//label[@title="机房名称"]/../..//input')
    # 机房所在地输入框
    address = ('xpath', '//label[@title="机房所在地"]/../..//input')
    # 域名输入框
    domain = ('xpath', '//label[@title="域名"]/../..//input')
    # 算力机是否可调度复选框
    scheduling_checkbox = ('xpath', '//input[@id="scheduling"]')
    # 取消按钮
    cancle_button = ('xpath', '//span[text()="取 消"]')
    # 确定按钮
    confirm_button = ('xpath', '//span[text()="确 定"]')
    # 退出X按钮
    quit_button = ('xpath', '//span[@class="ant-modal-close-x"]')
    # 新建机房成功提示信息 //span[text()="新建机房成功"]
    success_msg = ('xpath', '//span[text()="新建机房成功"]')
    # "我知道了"按钮
    success_confirm_button = ('xpath', '//span[text()="我知道了"]')
    # 机房名为空错误提示信息 //div[text()="请输入机房名称"]
    machineroom_noname = ('xpath', '//div[text()="请输入机房名称"]')
    # 机房所在地为空错误提示信息 //div[text()="请输入机房名称"]
    machineroom_noaddress = ('xpath', '//div[text()="请输入机房所在地"]')
    # 重复的机房名称错误信提示信息 //span[contains(text(),"机房错误")]
    duplicatename_error = ('xpath', '//span[contains(text(),"创建机房错误")]')
    # 编辑按钮框css定位信息 .ant-table-tbody>tr:nth-child(2)>td:nth-child(5)>button:nth-child(1)
    edit_button = ('css_selector', '.ant-table-tbody>tr:nth-child(5)>td:nth-child(5)>button:nth-child(1)')
    # 权限分配按钮css定位信息 .ant-table-tbody>tr:nth-child(2)>td:nth-child(5)>button:nth-child(2)
    assign_permission_button = ('css_selector', '.ant-table-tbody>tr:nth-child(5)>td:nth-child(5)>button:nth-child(1)')

    # 新建机房信息
    def new_machine_room(self):
        self.click_element(*self.system_setting)
        self.wait(2)
        self.click_element(*self.machineroom_info)
        self.wait(2)
        self.click_element(*self.new_button)
        self.wait(2)
        self.input_text(*self.roomname, "test002")
        self.wait(1)
        self.input_text(*self.address, "深圳市福田区新洲南楼金享楼2栋6楼")
        self.wait(1)
        self.input_text(*self.domain, "https://www.arsyun.com")
        self.click_element(*self.confirm_button)


if __name__ == "__main__":
    pass
