import unittest
from ddt import ddt,data

from common.base_page import BasePage
from utils.read_data import readData
from utils.read_db import MysqlDb
from common.my_logger import mylogger
from pages.system_setting_page.machineroom_info.machineroom_info_page import MachineRoomInfoPage

filename = "machineroominfo.xlsx"

@ddt
class TestMachineRoomInfo(BasePage):
    def setUp(self):
        self.page = MachineRoomInfoPage(self.driver)
    def tearDown(self):
        self.page.click_navigation_bar("系统设置")
        self.page.click_navigation_bar("首页")

    # MysqlDb().init_database("systemsetting.txt")
    cases1 = readData().read_excel("新建机房信息", filename)

    @data(*cases1)
    @unittest.skip
    def test_01_new_machineroom_info(self, args):
        mylogger.info("--------------------测试用例开始执行--------------------")
        mylogger.info(f"用例{args[0]}:{args[1]}--->>测试数据：{args[2]}")
        self.page.handle_new_machineroom_alert(args[2]['machineroom_name'], args[2]['address'], args[2]['domain'],
                                  args[2]['comment'], args[2]['check'])
        if args[0] not in ["add-machineroom-004","add-machineroom-005","add-machineroom-006","add-machineroom-007"]:
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
        elif args[0] == "add-machineroom-006":
            actual1 = self.page.get_text(args[4]['xpath1'])
            actual2 = self.page.get_text(args[4]['xpath2'])
            self.checkAssertEqual(args[3]['msg1'], actual1)
            self.checkAssertEqual(args[3]['msg2'], actual2)
            self.page.click_span_button("取 消")
        else:
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
            self.page.click_span_button("取 消")
        mylogger.info("--------------------测试用例执行完毕--------------------")

    cases2 = readData().read_excel("编辑机房信息", filename)

    @data(*cases2)
    # @unittest.skip
    def test_02_edit_machineroom_info(self, args):
        self.page.handle_edit_machineroom_alert(args[2]['machineroom_name'], args[2]['address'], args[2]['domain'],
                                    args[2]['comment'], args[2]['check'])
        if args[0] in ["edit-machineroom-007","edit-machineroom-008"]:
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
            self.page.click_span_button("取 消")
        else:
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)

        mylogger.info("--------------------测试用例执行完毕--------------------")

if __name__ == "__main__":
    unittest.main(verbosity=2)
