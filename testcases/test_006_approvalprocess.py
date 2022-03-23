import unittest

from common.base_page import BasePage
from pages.system_setting_page.approval_process.approval_process_page import ApprovalProcessPage


class TestApprovalProcess(BasePage):

    @unittest.skip
    def test_001_add_process(self):
        page = ApprovalProcessPage(self.driver)
        page.add_process("test001", approve1="Jacky", approve2="terry003-autotest", approve3="Hugo",
                         notifiers=["Nick", "lemontree", "Hunter", "Morgan"])

    @unittest.skip
    def test_002_check_process(self):
        page = ApprovalProcessPage(self.driver)
        page.check_process()

    @unittest.skip
    def test_003_edit_process(self):
        page = ApprovalProcessPage(self.driver)
        page.edit_process("test003", approve1="Nick", approve2="terry003-autotest", approve3="Hugo",
                          notifiers=["Nick", "lemontree", "Hunter", "Morgan"])

    @unittest.skip
    def test_004_bind_action(self):
        page = ApprovalProcessPage(self.driver)
        page.bind_action()
        # 关联操作成功
        # self.kd.text_assert_equal("操作成功", location=("xpath", "//span[text()='关联操作成功']"))
        # self.checkAssertEqual("操作成功1","操作成功",'结果对比失败')
        # print("--------------------------------------------------")
        # self.checkAssertEqual("操作成功2","操作成功",'结果对比失败')

    @unittest.skip
    def test_005_delete_process(self):
        page = ApprovalProcessPage(self.driver)
        page.delete_process()


if __name__ == '__main__':
    unittest.main(verbosity=2)
