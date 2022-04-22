import unittest
from common.base_page import BasePage
from pages.job_management_page.task_management import operation_info
from utils.read_db import MysqlDb
from utils.read_data import readData
from ddt import ddt, data
from common.my_logger import mylogger

textname = "commandinfo.xlsx"

@ddt()
class task_managementinfo(BasePage):


    def setUp(self):
        self.pent = operation_info(self.driver)
    def tearDown(self):
        self.pent.click_navigation_bar("作业管理")


    add_to = readData().read_excel("任务管理添加任务",textname)
    @data(*add_to)
    # @unittest.skip("忽略")
    def test_0001_add_take(self,args):
        mylogger.info("---------------------用例执行-------------------")
        if args[0] in ["add_text_001","add_text_002","add_text_003"]:
            self.pent.select_boxinfo(args[2]["type"],args[2]["host"],args[2]["choice"],args[2]["state"])
        else:
            self.pent.Correct_operation(args[2]["name"],args[2]["parameter"],args[2]["duration"],args[2]["remarks"])
        actual = self.pent.get_text(args[4]["xpath"])
        self.checkAssertEqual(args[3]["msg"],actual)
        if args[0] == "add_text_002":
            self.pent.click_elements(*self.pent.cancel,list_number=1)
        if args[0] == "add_text_003":
            self.pent.click_elements(*self.pent.cancel,list_number=2)

        mylogger.info("----------------------用例结束-----------------------")



if __name__ == '__main__':
    unittest.main(verbosity=2)