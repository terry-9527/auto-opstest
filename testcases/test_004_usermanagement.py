import unittest
from ddt import ddt, data
from common.base_page import BasePage
from common.my_logger import mylogger
from pages.system_setting_page.user_management.user.user_management_page import UserManagementPage
from utils.read_data import readData
from utils.read_db import MysqlDb

filename = "usermanagement.xlsx"


@ddt
class TestUserManagement(BasePage):

    def setUp(self):
        self.page = UserManagementPage(self.driver)

    # 初始化数据库
    # MysqlDb().init_database("usermanagement.txt")

    cases1 = readData().read_excel("adduser", filename)

    @data(*cases1)
    @unittest.skip("跳过")
    def test_001_add_user(self, args):
        mylogger.info("--------------------测试用例开始执行--------------------")
        mylogger.info(f"用例{args[0]}:{args[1]}--->>测试数据：{args[2]}")
        username = args[2]['username']
        chinesename = args[2]['chinesename']
        phone = args[2]['phone']
        email = args[2]['email']
        is_leader = args[2]['is_leader']
        is_approve = args[2]['is_approve']
        is_enable = args[2]['is_enable']
        self.page.add_user(username, chinesename, phone, email, is_leader, is_approve, is_enable)
        self.page.handle_save()
        if args[0] not in ["add-user-001", "add-user-002", "add-user-003", "add-user-004"]:
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
        else:
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
            self.page.handle_save(is_save=False)
        mylogger.info("--------------------测试用例执行结束--------------------")

    @unittest.skip("跳过")
    def test_002_check_userino(self):
        self.page.check_userinfo()

    cases2 = readData().read_excel("edituser", filename)

    @data(*cases2)
    @unittest.skip("跳过")
    def test_003_edit_userinfo(self, args):
        mylogger.info("--------------------测试用例开始执行--------------------")
        mylogger.info(f"用例{args[0]}:{args[1]}--->>测试数据：{args[2]}")
        username = args[2]['username']
        chinesename = args[2]['chinesename']
        phone = args[2]['phone']
        email = args[2]['email']
        is_leader = args[2]['is_leader']
        is_approve = args[2]['is_approve']
        is_enable = args[2]['is_enable']
        self.page.edit_userinfo(username, chinesename, phone, email, is_leader, is_approve, is_enable)
        self.page.handle_save()
        actual = self.page.get_text(args[4]['xpath'])
        self.checkAssertEqual(args[3]['msg'], actual)
        mylogger.info("--------------------测试用例执行结束--------------------")

    # @unittest.skip("跳过")
    def test_003_bind_role(self):
        self.page.bind_role()

    @unittest.skip("跳过")
    def test_004_bind_miner(self):
        self.page.bind_miner(state="all")

    @unittest.skip
    def test_006_search_userinfo(self):
        self.page.search("terry001-modify", by_username=True, by_customer=True)
        self.page.clear_input()
        self.page.search("terry001-modify", by_username=True, by_customer=False)
        self.page.clear_input()
        self.page.search("terry001-modify", by_username=False, by_customer=True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
