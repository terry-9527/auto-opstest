from ddt import ddt, data, unpack
from common.base_page import BasePage
from pages.system_setting_page.machineroom_info.machineroom_info_page import MachineRoomInfoPage
import unittest
from utils.read_data import readData
from utils.read_db import MysqlDb


@ddt
class TestMachineRoomInfo(BasePage):

    MysqlDb().init_database("systemsetting.txt")
    cases = readData().read_excel("新建机房信息","machineroominfo.xlsx")
    @data(*cases)
    def test_01_new_machineroom_info(self,args):
        self.page = MachineRoomInfoPage(self.driver)
        self.page.new_machineroom(args[2]['machineroom_name'], args[2]['address'], args[2]['domain'], args[2]['comment'], args[2]['check'])
        # self.checkAssertEqual(args[3]['msg'], "新建机房成功", filename="machineroominfo.xlsx", caseid=args[0])
        self.page.text_assert_equal(args[3]['msg'])


    cases = readData().read_excel("编辑机房信息","machineroominfo.xlsx")
    @data(*cases)
    @unittest.skip
    def test_02_edit_machineroom_info(self,args):
        self.page = MachineRoomInfoPage(self.driver)
        self.page.endit_machineroom(args[2]['machineroom_name'], args[2]['address'], args[2]['domain'], args[2]['comment'], args[2]['check'])



if __name__ == "__main__":
    unittest.main(verbosity=2)