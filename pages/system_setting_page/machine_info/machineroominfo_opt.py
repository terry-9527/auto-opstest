'''
机房信息页面元素的相关操作
'''
from WebUI_ops.common import keywords
from WebUI_ops.common.keywords import KeyWords
from WebUI_ops.page_location.enginroom.machineroominfo_lct import MachineRoomInfoLocation
from WebUI_ops.page_operation.login_opt.login_opt import LoginOperation
from WebUI_ops.page_operation.system_setting.userinfo.userinfo_opt import UserInfoOperation
from demo import random_phone


class MachineRoomInfoOperation(KeyWords):

    def __init__(self, driver):
        super(MachineRoomInfoOperation, self).__init__(driver)
        self.lct = MachineRoomInfoLocation()

    # 点击机房信息
    def click_engin_room_info(self):
        self.click_element(*self.lct.engin_room_info)

    # 点击新建机房
    def click_new_engin_room(self):
        self.click_element(*self.lct.new_engin_room)

    # 输入机房名称
    def input_engin_room_name(self, roomname):
        self.force_clear(*self.lct.roomname)
        self.input_text(*self.lct.roomname, roomname)

    # 输入机房所在地
    def input_address(self, address):
        self.force_clear(*self.lct.address)
        self.input_text(*self.lct.address, address)

    # 输入域名
    def input_domain(self, domain):
        self.force_clear(*self.lct.domain)
        self.input_text(*self.lct.domain, domain)

    # 算力机是否可调度复选框
    def click_scheduling_checkbox(self,check=False):
        if check:
            self.click_element(*self.lct.scheduling_checkbox)

    # 点击确定按钮
    def click_confirm_button(self):
        self.click_element(*self.lct.confirm_button)

    # 点击取消按钮
    def click_cancle_button(self):
        self.click_element(*self.lct.cancle_button)

    # 点击退出X按钮
    def click_quit_button(self):
        self.click_element(*self.lct.quit_button)

    # 创建成功后点击"我知道了"确定按钮
    def click_success_confirm_button(self):
        self.click_element(*self.lct.success_confirm_button)

    # 获取新建机房成功弹框文本信息
    def get_success_msg(self):
        msg = self.locator(*self.lct.success_msg).get_attribute('textContent')
        return msg
    # 获取机房名称重复错误提示信息
    def get_duplicatename_error_msg(self):
        msg = self.locator(*self.lct.duplicatename_error).get_attribute('textContent')
        return msg

    # 机房名称为空错误信息
    def get_machineroom_noname_msg(self):
        msg = self.locator(*self.lct.machineroom_noname).get_attribute('textContent')
        return msg

    # 机房地址为空错误信息
    def get_machineroom_noaddress_msg(self):
        msg = self.locator(*self.lct.machineroom_noaddress).get_attribute('textContent')
        return msg
    # 点击编辑按钮
    def click_edit_button(self):
        self.locator(*self.lct.edit_button).click()

    # 点击编辑按钮
    def click_assign_permission_button(self):
        self.locator(*self.lct.assign_permission_button).click()


if __name__ == '__main__':
    url = "https://opstest.arsyun.com/#/"
    driver = keywords.init_driver("Chrome")
    lg = LoginOperation(driver)
    lg.open_browser(url)
    lg.login("18276762767", "aa123456")
    lg.wait(2)
    ui = UserInfoOperation(driver)
    ui.click_system_setting()
    ui.wait(2)
    opt1 = MachineRoomInfoOperation(driver)
    opt1.click_engin_room_info()
    opt1.wait(2)
    opt1.click_edit_button()
    # opt1.click_new_engin_room()
    # opt1.wait(2)
    # opt1.input_engin_room_name("test0001")
    # opt1.wait(1)
    # opt1.input_address("新洲南路")
    # opt1.wait(1)
    # opt1.input_domain("https://opttest.arsyun.com")
    # opt1.wait(1)
    # opt1.click_scheduling_checkbox()
    # opt1.wait(1)
    # opt1.click_confirm_button()
    # opt1.wait(2)
    # opt1.click_success_confirm_button()
    # opt1.wait(2)
    # opt1.click_edit_button()
    # opt1.wait(2)
    # opt1.click_element('xpath', '//input[@id="machine_name"]')
    # opt1.wait(2)
    # opt1.clear('xpath', '//input[@id="machine_name"]')
    # driver.find_element_by_xpath('//input[@id="machine_name"]').clear()
    # driver.execute_script('document.querySelector("#machine_name").value=""')
    # opt1.input_engin_room_name("test0002")
    # opt1.wait(1)
    # opt1.input_address("新洲南路2")
    # opt1.wait(1)
    # opt1.click_confirm_button()
    # opt1.click_assign_permission_button()
    # opt1.close_browser()
    # phone = random_phone()