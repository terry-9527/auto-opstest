from common.base_page import BasePage
from pages.user_page.user_page import PersonalInfoPage,MyApprovalPage
import unittest
from utils.read_data import readData
from ddt import ddt, data

# filename = "brokenrecord.xlsx"


class TestPersonalInfo(BasePage):

    @unittest.skip
    def test_001_edit_personal_info(self):
        self.page = PersonalInfoPage(self.driver)
        self.page.check_personal_info(name="terry", email="terry.wei@arsyun.com")

    @unittest.skip
    def test_002_search_approval_process(self):
        self.page = MyApprovalPage(self.driver)
        self.page.search_approval_process(status="审核中")

    def test_003_handle_process(self):
        self.page = MyApprovalPage(self.driver)
        self.page.handle_approval_process()


if __name__ == '__main__':
    unittest.main(verbosity=2)