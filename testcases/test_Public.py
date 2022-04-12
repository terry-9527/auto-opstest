import unittest
from common.base_page import BasePage
from pages.job_management_page.Common_module import CustemorPage
from utils.read_db import MysqlDb
from utils.read_data import readData
from ddt import ddt, data
from common.my_logger import mylogger


@ddt
class operation_info(BasePage):
    # 初始化数据
    # MysqlDb().init_database("custemorinfo.txt")
    # 添加模板类型
    name = readData().read_excel("添加模板类型", "commandinfo.xlsx")
    @data(*name)
    @unittest.skip('忽略')
    def test_001_add_to(self, args):
        mylogger.info("----------------------用例执行开始-----------------")
        mylogger.info(f"用例{args[0]}:{args[1]}--->>测试数据：{args[2]}")
        self.pags = CustemorPage(self.driver)
        self.pags.app_type(args[2]["text"])

        self.pags.determine_cancel()
        if args[0] == "edit-clusterinfo-001":
            self.pags.text_assert_equal(args[0], args[3]["msg"], args[4]["xpath"])
        else:
            self.pags.text_assert_equal(args[0], args[3]["msg"], args[4]["xpath"])
            self.pags.determine_cancel(state=False)


    file = readData().read_excel("公共模板", "commandinfo.xlsx")  # [[],[],[]]
    @data(*file)
    @unittest.skip('忽略')
    def test_002_add_operation(self, args):
        mylogger.info("----------------用例执行开始-------------------")
        mylogger.info("用例id:{0},用例标题:{1},输入参数:{2}".format(args[0], args[1], args[2]))
        page = CustemorPage(self.driver)
        page.add_operation(args[2]["name"], args[2]["content1"], args[2]["remarks"])
    # calse = readData().read_excel("公共模板", "commandinfo.xlsx")
    # @data(*calse)
    # def test_003_err_operation(self,args):
    #     mylogger.info("----------------用例执行开始-------------------")
    #     mylogger.info("用例id:{0},用例标题:{1},输入参数:{2}".format(args[0],args[1],args[2]))
    #     page = CustemorPage(self.driver)
    #     page.err_operation(args[2]["name1"], args[2]["content2"], args[2]["remarks"])

    Admin = readData().read_excel("管理模板类型", "commandinfo.xlsx")
    @data(*Admin)
    # @unittest.skip('忽略')
    def test_003_add_Administration(self, args):
        mylogger.info("----------------------用例执行开始-------------------")
        mylogger.info("用例id:{0},用例标题:{1},输入参数:{2}".format(args[0], args[1], args[2]))
        oper = CustemorPage(self.driver)
        oper.edit_template(args[2]["test"])

        mylogger.info("----------------------用例执行结束-------------------")

if __name__ == '__main__':
    unittest.main(verbosity=2)
