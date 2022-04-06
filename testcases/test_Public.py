import unittest
from common.base_page import BasePage
from pages.job_management_page.Common_module import CustemorPage
from utils.read_db import MysqlDb
from utils.read_data import readData
from ddt import ddt,data

@ddt
class operation_info(BasePage):
    # 初始化数据
    # MysqlDb().init_database("custemorinfo.txt")
    @unittest.skip('忽略')
    def test_001_newly_build(self):
        page = CustemorPage(self.driver)
        page.operation_info()


    file = readData().read_excel("公共模板", "commandinfo.xlsx") #[[],[],[]]
    @data(*file)
    @unittest.skip('忽略')
    def test_002_err_operation(self,args):
        print("用例id:{0},用例标题:{1},输入参数:{2}".format(args[0],args[1],args[2]))
        page = CustemorPage(self.driver)
        page.err_operation(args[2]["name"], args[2]["content1"], args[2]["remarks"])


    calse = readData().read_excel("公共模板", "commandinfo.xlsx")
    @data(*calse)
    def test_003_err_operation(self,args):
        page = CustemorPage(self.driver)
        page.err_operation(args[2]["name"], args[2]["content1"], args[2]["remarks"])







if __name__ == '__main__':
    unittest.main(verbosity=2)