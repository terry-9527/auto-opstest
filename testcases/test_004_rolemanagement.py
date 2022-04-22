import unittest
from ddt import ddt, data
from common.base_page import BasePage
from common.my_logger import mylogger
from pages.system_setting_page.user_management.role.role_management_page import RoleManagementPage
from utils.read_data import readData
from utils.read_db import MysqlDb

filename = "usermanagement.xlsx"


@ddt
class TestRoleManagement(BasePage):

    def setUp(self):
        self.page = RoleManagementPage(self.driver)
    def tearDown(self):
        self.page.wait()
        self.page.click_navigation_bar("用户管理")
        self.page.click_navigation_bar("系统设置")
        self.page.click_navigation_bar("首页")

    # 初始化数据库
    MysqlDb().init_database("rolemanagement.txt")

    cases1 = readData().read_excel("addrole", filename)


    @unittest.skip("跳过")
    def test_004_delete_role(self):
        self.page = RoleManagementPage(self.driver)
        self.page.delete_role()

    @data(*cases1)
    # @unittest.skip
    def test_001_add_role(self, args):
        mylogger.info("--------------------测试用例开始执行--------------------")
        mylogger.info(f"用例{args[0]}:{args[1]}--->>测试数据：{args[2]}")
        self.page.handle_add_role_alert(args[2]['name'], args[2]['comment'], args[2]['customer'])
        if args[0] not in ["add-role-004","add-role-005"]:
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
        else:
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
            self.page.click_span_button("取 消")
        mylogger.info("--------------------测试用例执行结束--------------------")


    cases2 = readData().read_excel("editrole", filename)
    @data(*cases2)
    # @unittest.skip("跳过")
    def test_002_edit_role(self, args):
        mylogger.info("--------------------测试用例开始执行--------------------")
        mylogger.info(f"用例{args[0]}:{args[1]}--->>测试数据：{args[2]}")
        self.page.handle_edit_role_alert(args[2]['name'], args[2]['comment'], args[2]['customer'])
        if args[0] not in ["edit-role-005","edit-role-006"]:
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
        else:
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
            self.page.click_span_button("取 消")
        mylogger.info("--------------------测试用例执行结束--------------------")



    @unittest.skip("跳过")
    def test_006_add_role(self, args):
        self.page = RoleManagementPage(self.driver)
        self.page.add_role(args[2]['name'], args[2]['comment'], args[2]['is_save'])


    # @unittest.skip("跳过")
    def test_003_setting_role(self):
        mylogger.info("--------------------测试用例开始执行--------------------")
        self.page.setting_role_privilege()
        mylogger.info("--------------------测试用例执行结束--------------------")


    # @unittest.skip("跳过")
    def test_004_delete_role(self):
        mylogger.info("--------------------测试用例开始执行--------------------")
        self.page.delete_role()
        excepted = "删除角色成功"
        actual = self.page.get_text("//span[text()='删除角色成功']")
        self.checkAssertEqual(excepted, actual)
        mylogger.info("--------------------测试用例执行结束--------------------")


if __name__ == '__main__':
    suite = unittest.TestSuite()

    cases = unittest.TestLoader().loadTestsFromTestCase(TestRoleManagement)
    suite.addTest(cases)
    runner = unittest.TextTestRunner()
    runner.run(suite)


