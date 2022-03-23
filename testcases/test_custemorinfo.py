import unittest
from ddt import ddt,data
from common.base_page import BasePage
from pages.system_setting_page.customer_info.custemor_info import CustemorPage
from utils.read_data import readData
from utils.read_db import MysqlDb


@ddt
class TestCustemorInfo(BasePage):
    # 初始化数据
    MysqlDb().init_database("custemorinfo.txt")

    cases = readData().read_excel("新建客户信息","custemorinfo.xlsx")
    @data(*cases)
    #@unittest.skip("忽略")
    def test_001_new_custemorinfo(self,args):
        print("用例id:{0},用例标题:{1},输入参数:{2}".format(args[0],args[1],args[2]))
        page = CustemorPage(self.driver)
        page.new_custemorinfo(args[2]['name'], args[2]['comment'])

    file = readData().read_excel("编辑客户信息","custemorinfo.xlsx")
    @data(*file)
    #@unittest.skip('忽略')
    def test_002_edit_custemorinfo(self,args):
        print("用例id:{0},用例标题:{1},输入参数:{2}".format(args[0], args[1], args[2]))
        page = CustemorPage(self.driver)
        page.edit_custemor(args[2]['name'], args[2]['comment'])

    def test_003_delete_custemorinfo(self):
        page = CustemorPage(self.driver)
        page.delete_name()



if __name__ == '__main__':
    unittest.main(verbosity=2)

