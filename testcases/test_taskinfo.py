import unittest
from common.base_page import BasePage
from pages.job_management_page.Command_info import CustemorPage
from utils.read_data import readData
from ddt import ddt,data

@ddt
class Test_taskInfo(BasePage):

    # 初始化数据
    # MysqlDb().init_database("custemorinfo.txt")
    fide = readData().read_excel("命令执行","commandinfo.xlsx")
    @unittest.skip('忽略')
    def test_001_run_taskinfo(self):
        page = CustemorPage(self.driver)
        page.new_commandinfo()


    cases =readData().read_excel("命令执行","commandinfo.xlsx")
    @data(*cases)
    @unittest.skip('忽略')
    def test_002_err_takinfo(self,args):
        self.page = CustemorPage(self.driver)
        self.page.err_operation(target=args[2]['target'], target2=args[2]['target2'])
        # self.assertEqual(args[3]['errmsg'],self.page .locators(*self.page .errmsg1)[0].get_attribute('textContent'))
        self.assertEqual(args[3]['errmsg'],self.page .locators(args[4]['type'],args[4]['xpath'])[0].get_attribute('textContent'))

    def test_003_host_takinfo(self):
        pas = CustemorPage(self.driver)
        pas.host_management()









if __name__ == '__main__':
    unittest.main(verbosity=2)