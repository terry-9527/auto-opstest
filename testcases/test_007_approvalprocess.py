import unittest

from common.base_page import BasePage
from pages.system_setting_page.approval_process.approval_process_page import ApprovalProcessPage


class TestApprovalProcess(BasePage):

    def setUp(self):
        self.page = ApprovalProcessPage(self.driver)

    @unittest.skip
    def test_001_add_process(self):
        #
        # self.page.add_process("自定义审批流001", approve1="Jacky", notifiers=["Nick", "Hugo"])
        self.page.add_process("test001", approve1="Jacky", approve2="Fide", approve3="Hugo", notifiers=["Nick", "Hugo"])

    @unittest.skip
    def test_002_check_process(self):
        self.page.check_process()

    @unittest.skip
    def test_003_edit_process(self):
        self.page.edit_process("test003", approve1="Nick", approve2="terry003-autotest", approve3="Hugo",
                          notifiers=["Nick", "lemontree", "Hunter", "Morgan"])

    # @unittest.skip
    def test_004_bind_action(self):
        self.page.bind_action()


    @unittest.skip
    def test_005_delete_process(self):
        self.page.delete_process()


if __name__ == '__main__':
    unittest.main(verbosity=2)
