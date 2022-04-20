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
    def tearDown(self):
        self.page.wait()
        self.page.click_navigation_bar("用户管理")
        self.page.click_navigation_bar("系统设置")
        self.page.click_navigation_bar("首页")

    # 初始化数据库
    MysqlDb().init_database("usermanagement.txt")

    cases1 = readData().read_excel("adduser", filename)

    @data(*cases1)
    # @unittest.skip("跳过")
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
        if args[0] in ["add-user-01", "add-user-02", "add-user-03", "add-user-04"]:
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
        else:
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
            self.page.click_span_button("取 消")
        mylogger.info("--------------------测试用例执行结束--------------------")

    # @unittest.skip("跳过")
    def test_002_check_userino(self):
        self.page.check_userinfo()

    cases2 = readData().read_excel("edituser", filename)

    @data(*cases2)
    # @unittest.skip("跳过")
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
        actual = self.page.get_text(args[4]['xpath'])
        self.checkAssertEqual(args[3]['msg'], actual)
        mylogger.info("--------------------测试用例执行结束--------------------")

    # @unittest.skip("跳过")
    def test_004_bind_role(self):
        mylogger.info("--------------------测试用例开始执行--------------------")
        self.page.bind_role(rolename="role001-111")
        excepted = "关联角色成功"
        actual = self.page.get_text("//span[text()='关联角色成功']")
        self.checkAssertEqual(excepted, actual)
        mylogger.info("--------------------测试用例执行结束--------------------")

    @unittest.skip("跳过")
    def test_005_bind_miner(self):
        mylogger.info("--------------------测试用例开始执行--------------------")
        # 绑定执行的集群
        minerid_list = ["f020000", "f030000"]
        self.page.bind_miner(minerid_list, is_select=True)
        excepted = "关联集群成功"
        actual = self.page.get_text("//span[text()='关联集群成功']")
        self.checkAssertEqual(excepted, actual)
        self.page.wait()
        self.page.click_navigation_bar("用户管理")
        self.page.click_navigation_bar("系统设置")
        self.page.click_navigation_bar("首页")
        # 绑定所有的集群
        self.page.bind_miner(select_all=True)
        excepted = "关联集群成功"
        actual = self.page.get_text("//span[text()='关联集群成功']")
        self.checkAssertEqual(excepted, actual)
        mylogger.info("--------------------测试用例执行结束--------------------")

    cases3 = readData().read_excel("searchuser", filename)

    @data(*cases3)
    # @unittest.skip("跳过")
    def test_006_search_userinfo(self, args):
        mylogger.info("--------------------测试用例开始执行--------------------")
        mylogger.info(f"用例{args[0]}:{args[1]}--->>测试数据：{args[2]}")
        self.page.search(username=args[2]["username"], customername=args[2]["customername"])
        mylogger.info("--------------------测试用例执行结束--------------------")


if __name__ == '__main__':
    unittest.main(verbosity=2)
