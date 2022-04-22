import unittest
from common.base_page import BasePage
from pages.job_management_page.Command_info import CustemorPage
from utils.read_data import readData
from ddt import ddt,data
from common.my_logger import mylogger

@ddt
class Test_taskInfo(BasePage):

    def setUp(self):
        self.page = CustemorPage(self.driver)

    def tearDown(self):
        self.page.click_navigation_bar(" 任务管理")
        self.page.click_navigation_bar("作业管理")



    # 初始化数据
    # MysqlDb().init_database("custemorinfo.txt")
    fide = readData().read_excel("命令执行","commandinfo.xlsx")
    @data(*fide)
    # @unittest.skip('忽略')
    def test_001_run_taskinfo(self,args):
        mylogger.info("---------------------用例执行开始--------------------")
        self.page.new_commandinfo(args[2]["colony"],args[2]["host"],args[2]["template"],args[2]["states"],args[2]["start"],
                                  args[2]["section"])
        if args[0] not in ["add-clusterinfo-001","add-clusterinfo-005"]:
            actual = self.page.get_text(args[4]["xpath"])
            self.checkAssertEqual(args[3]["msg"],actual)
        if args[0] == "add-clusterinfo-005":
            judge1 = self.page.get_text(args[4]["xpath1"])
            judge2 = self.page.get_text(args[4]["xpath2"])
            judge3 = self.page.get_text(args[4]["xpath3"])
            self.checkAssertEqual(args[3]["msg1"],judge1)
            self.checkAssertEqual(args[3]["msg2"],judge2)
            self.checkAssertEqual(args[3]["msg3"],judge3)
        if args[0] =="add-clusterinfo-003":
            self.page.click_elements(*self.page.cancel,list_number=0)
        if args[0] =="add-clusterinfo-004":
            self.page.click_elements(*self.page.cancel,list_number=1)




if __name__ == '__main__':
    unittest.main(verbosity=2)