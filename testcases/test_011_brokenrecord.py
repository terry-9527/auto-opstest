import unittest
from ddt import ddt, data

from common.base_page import BasePage
from common.my_logger import mylogger
from pages.workbench_page.broken_record.broken_record_page import BrokenRecordPage
from utils.read_data import readData

filename = "brokenrecord.xlsx"


@ddt
class TestHostManagement(BasePage):

    def setUp(self):
        self.page = BrokenRecordPage(self.driver)

    cases = readData().read_excel("新建故障记录", filename)

    # @unittest.skip
    @data(*cases)
    def test_001_add_record(self, args):
        mylogger.info("--------------------测试用例开始执行--------------------")
        mylogger.info(f"用例{args[0]}:{args[1]}--->>测试数据：{args[2]}")
        self.page.add_record(minerid=args[2]['minerid'], description=args[2]['description'], reason=args[2]['reason'],
                             sort=args[2]['sort'], level=args[2]['level'], status=args[2]['status'])
        if args[0] not in ["add-record-006", "add-record-007"]:
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
            self.page.click_navigation_bar("工作台")
        else:
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
            self.page.wait()
            self.page.click_span_button("取 消")
            self.page.click_navigation_bar("工作台")
        mylogger.info("--------------------测试用例执行结束--------------------")

    cases = readData().read_excel("编辑故障记录", filename)

    # @unittest.skip
    @data(*cases)
    def test_002_edit_record(self, args):
        mylogger.info("--------------------测试用例开始执行--------------------")
        mylogger.info(f"用例{args[0]}:{args[1]}--->>测试数据：{args[2]}")
        self.page.edit_record(minerid=args[2]['minerid'], description=args[2]['description'], reason=args[2]['reason'],
                              sort=args[2]['sort'], level=args[2]['level'], status=args[2]['status'])
        actual = self.page.get_text(args[4]['xpath'])
        self.checkAssertEqual(args[3]['msg'], actual)
        self.page.click_navigation_bar("工作台")
        self.page.click_navigation_bar("首页")
        self.page.wait()
        mylogger.info("--------------------测试用例执行结束--------------------")

    cases = readData().read_excel("搜索", filename)

    # @unittest.skip
    @data(*cases)
    def test_003_search(self, args):
        mylogger.info("--------------------测试用例开始执行--------------------")
        self.page.search_record(type=args[2]['type'], level=args[2]['level'], status=args[2]['status'],
                                text=args[2]['text'], start_time=args[2]['start_time'], end_time=args[2]['end_time'])
        mylogger.info("--------------------测试用例执行结束--------------------")

    # @unittest.skip
    def test_004_delete_record(self):
        mylogger.info("--------------------测试用例开始执行--------------------")
        self.page.delete_record(all_delete=True)
        excepted = "删除记录成功"
        actual = self.page.get_text("//span[text()='删除记录成功']")
        self.checkAssertEqual(excepted, actual)
        mylogger.info("--------------------测试用例执行结束--------------------")


if __name__ == '__main__':
    unittest.main()
