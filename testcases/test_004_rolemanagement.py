import unittest
from ddt import ddt,data
from common.base_page import BasePage
from pages.system_setting_page.user_management.role.role_management_page import RoleManagementPage
from utils.read_data import readData
from utils.read_db import MysqlDb

filename = "usermanagement.xlsx"
@ddt
class TestRoleManagement(BasePage):
    # 初始化数据库
    MysqlDb().init_database("usermanagement.txt")

    cases = readData().read_excel("role",filename)
    @data(*cases)
    def test_add_role(self, args):
        self.page = RoleManagementPage(self.driver)
        self.page.add_role(args[2]['name'], args[2]['comment'], args[2]['is_save'])

    @data(*cases)
    @unittest.skip("跳过")
    def test_002_edit_role(self):
        pass

    @data(*cases)
    # @unittest.skip("跳过")
    def test_003_setting_role(self):
        self.page = RoleManagementPage(self.driver)
        self.page.setting_role()

    @unittest.skip("跳过")
    def test_004_delete_role(self):
        self.page = RoleManagementPage(self.driver)
        self.page.delete_role()

    @unittest.skip("跳过")
    def test_005_delete_role(self):
        self.page = RoleManagementPage(self.driver)
        self.page.delete_role()


    @unittest.skip("跳过")
    def test_006_add_role(self, args):
        self.page = RoleManagementPage(self.driver)
        self.page.add_role(args[2]['name'], args[2]['comment'], args[2]['is_save'])





if __name__ == '__main__':
    suite = unittest.TestSuite()
    cases = unittest.TestLoader().loadTestsFromTestCase(TestRoleManagement)
    suite.addTest(cases)
    runner = unittest.TextTestRunner()
    runner.run(suite)

