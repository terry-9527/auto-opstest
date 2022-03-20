import unittest

from common.base_page import BasePage
from pages.system_setting_page.user_management.user.user_management_page import UserManagementPage


class TestUserManagement(BasePage):


    def test_001_user(self):
        page = UserManagementPage(self.driver)
        page.add_user()


if __name__ == '__main__':
    unittest.main(verbosity=2)
