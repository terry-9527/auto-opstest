import unittest

from ddt import ddt,data
from common.base_page import BasePage
from common.my_logger import mylogger
from pages.system_setting_page.approval_process.approval_process_page import ApprovalProcessPage
from utils.read_data import readData
from utils.read_db import MysqlDb

filename = "approvalprocess.xlsx"

@ddt
class TestApprovalProcess(BasePage):

    def setUp(self):
        self.page = ApprovalProcessPage(self.driver)

    MysqlDb().init_database("approvalprocess.txt")
    cases1 = readData().read_excel("新建审批流", filename)
    # @unittest.skip
    @data(*cases1)
    def test_001_add_process(self, args):
        mylogger.info("--------------------测试用例开始执行--------------------")
        mylogger.info(f"用例{args[0]}:{args[1]}--->>测试数据：{args[2]}")
        self.page.add_process(args[2]['process_name'], approve1=args[2]['approve1'], approve2=args[2]['approve2'], approve3=args[2]['approve3'])

        if args[0] not in ["add-approve-004","add-approve-005","add-approve-006"]:
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
        else:
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
            self.page.click_span_button("取 消")
        mylogger.info("--------------------测试用例执行结束--------------------")

    # @unittest.skip
    def test_002_check_process(self):
        self.page.check_process()

    @unittest.skip
    def test_003_edit_process(self):
        self.page.edit_process("test003", approve1="Nick", approve2="terry003-autotest", approve3="Hugo",
                          notifiers=["Nick", "lemontree", "Hunter", "Morgan"])

    # @unittest.skip
    def test_004_bind_action(self):
        self.page.bind_action(all_select=True)
        excepted = "关联操作成功"
        actual = self.page.get_text("//span[text()='关联操作成功']")
        self.checkAssertEqual(excepted, actual)

    # @unittest.skip
    def test_005_delete_process(self):
        mylogger.info("--------------------测试用例开始执行--------------------")
        # 该审批流模板已关联接口, 不能删除
        self.page.bind_action(process_name="process001", all_select=True)
        self.page.delete_process(process_name="process001")
        excepted = "该审批流模板已关联接口, 不能删除"
        actual = self.page.get_text("//span[text()='该审批流模板已关联接口, 不能删除']")
        self.checkAssertEqual(excepted, actual)
        # 模板没关联,可以删除
        self.page.bind_action(process_name="process003", all_select=False)
        self.page.delete_process()
        excepted = "删除成功"
        actual = self.page.get_text("//span[text()='删除成功']")
        self.checkAssertEqual(excepted, actual)
        mylogger.info("--------------------测试用例执行结束--------------------")


if __name__ == '__main__':
    unittest.main(verbosity=2)
