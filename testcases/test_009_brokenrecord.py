from selenium import webdriver

from common.base_page import BasePage
from common.keywords import KeyWords
from pages.workbench_page.broken_record.broken_record_page import BrokenRecordPage
import unittest
from utils.read_data import readData
from ddt import ddt, data

filename = "brokenrecord.xlsx"


@ddt
class TestHostManagement(BasePage):
    cases = readData().read_excel("新建故障记录", filename)

    @unittest.skip
    @data(*cases)
    def test_001_add_record(self, args):
        # print(args)
        self.page = BrokenRecordPage(self.driver)
        self.page.add_record(minerid=args[2]['minerid'], description=args[2]['description'], reason=args[2]['reason'],
                             sort=args[2]['sort'], level=args[2]['level'], status=args[2]['status'])

    cases = readData().read_excel("编辑故障记录", filename)
    # @unittest.skip
    @data(*cases)
    def test_002_edit_record(self, args):
        self.page = BrokenRecordPage(self.driver)
        self.page.edit_record(minerid=args[2]['minerid'], description=args[2]['description'], reason=args[2]['reason'],
                             sort=args[2]['sort'], level=args[2]['level'], status=args[2]['status'])


    @unittest.skip
    def test_003_delete_record(self):
        self.page = BrokenRecordPage(self.driver)
        self.page.delete_record(times=6)



    cases = readData().read_excel("搜索", filename)
    @unittest.skip
    @data(*cases)
    def test_004_search(self, args):
        self.page = BrokenRecordPage(self.driver)
        self.page.search_record(type=args[2]['type'], level=args[2]['level'], status=args[2]['status'],
                                text=args[2]['text'], start_time=args[2]['start_time'], end_time=args[2]['end_time'])


if __name__ == '__main__':
    unittest.main()
