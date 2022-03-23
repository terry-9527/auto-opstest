import unittest
from ddt import ddt, data
from common.base_page import BasePage
from pages.system_setting_page.user_management.user.user_management_page import UserManagementPage
from utils.read_data import readData
from utils.read_db import MysqlDb


@ddt
class TestUserManagement(BasePage):
    # 初始化数据库
    MysqlDb().init_database("usermanagement.txt")

    cases = readData().read_excel("adduser", 'usermanagement.xlsx')

    @data(*cases)
    # @unittest.skip("跳过")
    def test_001_add_user(self, args):
        username = args[2]['username']
        chinesename = args[2]['chinesename']
        phone = args[2]['phone']
        email = args[2]['email']
        is_leader = args[2]['is_leader']
        is_approve = args[2]['is_approve']
        is_enable = args[2]['is_enable']
        self.page = UserManagementPage(self.driver)
        self.page.add_user(username, chinesename, phone, email, is_leader, is_approve, is_enable)

    # @unittest.skip("跳过")
    def test_002_check_userino(self):
        self.page = UserManagementPage(self.driver)
        self.page.check_userinfo()

    # @unittest.skip("跳过")
    def test_003_bind_role(self):
        self.page = UserManagementPage(self.driver)
        self.page.bind_role()

    # @unittest.skip("跳过")
    def test_004_bind_miner(self):
        self.page = UserManagementPage(self.driver)
        # self.page.bind_miner()
        self.page.bind_miner(state="all")


    cases = readData().read_excel("edituser", 'usermanagement.xlsx')
    @data(*cases)
    # @unittest.skip("跳过")
    def test_005_edit_userinfo(self,args):
        username = args[2]['username']
        chinesename = args[2]['chinesename']
        phone = args[2]['phone']
        email = args[2]['email']
        self.page = UserManagementPage(self.driver)
        self.page.edit_userinfo(username, chinesename, phone, email)


    def test_006_search_userinfo(self):
        self.page = UserManagementPage(self.driver)
        self.page.search("terry001-modify",by_username=True,by_customer=True)
        self.page.clear_input()
        self.page.search("terry001-modify",by_username=True,by_customer=False)
        self.page.clear_input()
        self.page.search("terry001-modify",by_username=False,by_customer=True)






if __name__ == '__main__':
    unittest.main(verbosity=2)
