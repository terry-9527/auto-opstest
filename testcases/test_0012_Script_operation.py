import unittest
from common.base_page import BasePage
from pages.job_management_page.Public_script import CustemorPage
from utils.read_db import MysqlDb
from utils.read_data import readData
from ddt import ddt, data
from common.my_logger import mylogger
@ddt()
class Correct_operation(BasePage):
    # 添加脚本类型
    name = readData().read_excel("添加脚本类型名称", "commandinfo.xlsx")
    @data(*name)
    # @unittest.skip('忽略')
    def test_0001_add_type(self, args):
        mylogger.info("------------------用例执行开始--------------------")
        mylogger.info(f"用例{args[0]}:{args[1]}--->>测试数据：{args[2]}")
        self.oper = CustemorPage(self.driver)
        self.oper.add_type(args[2]["text"])
        self.oper.sure_cancel()
        if args[0] =="add-clusterinfo-001":
            actual = self.oper.get_text(args[4]["xpath"])
            self.checkAssertEqual(args[3]["msg"], actual)
            self.oper.click_navigation_bar("作业管理")
        else:
            actual = self.oper.get_text(args[4]["xpath"])
            self.checkAssertEqual(args[3]["msg"], actual)
            self.oper.sure_cancel(judge=False)
        mylogger.info("--------------------用例执行结束-----------------")


    # 添加脚本
    Script_add = readData().read_excel("公共脚本", "commandinfo.xlsx")
    @data(*Script_add)
    def test_0002_add_script(self, args):
        mylogger.info("------------------------用例执行----------------------")
        mylogger.info(f"用例{args[0]}:{args[1]}--->>测试数据：{args[2]}")
        self.opne = CustemorPage(self.driver)
        self.opne.New_script(args[2]["type"],args[2]["choice"],args[2]["edition"],args[2]["describe"])
        if args[0] != "add-clusterinfo-003":
            Assert1 = self.opne.get_text(args[4]["xpath"])
            self.checkAssertEqual(args[3]["msg"], Assert1)
        else:
            actual1 =self.opne.get_text(args[4]["xpath1"])
            actual2 =self.opne.get_text(args[4]["xpath2"])
            self.checkAssertEqual(args[3]["msg1"],actual1)
            self.checkAssertEqual(args[3]["msg2"],actual2)
        mylogger.info("--------------------------用例结束-------------------------")



    # 管理脚本类型
    edit = readData().read_excel("管理脚本类型", "commandinfo.xlsx")
    @data(*edit)
    # @unittest.skip('忽略')
    def test_0003_edit_type(self,args):
        mylogger.info("-------------------用例开始执行------------------")
        mylogger.info("用例id:{0},用例标题:{1},输入参数:{2}".format(args[0], args[1], args[2]))
        self.opse = CustemorPage(self.driver)
        self.opse.script_operinfo(args[2]["text"])
        Assert1 = self.opse.get_text(args[4]["xpath"])
        self.checkAssertEqual(args[3]["msg"],Assert1)





if __name__ == '__main__':
    unittest.main(verbosity=2)