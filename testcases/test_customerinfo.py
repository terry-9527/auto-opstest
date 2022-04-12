import unittest
from ddt import ddt, data
from common.base_page import BasePage
from common.my_logger import mylogger
from pages.system_setting_page.customer_info.customerinfo_page import CustomerInfoPage
from utils.read_data import readData
from utils.read_db import MysqlDb

filename = "customerinfo.xlsx"


@ddt
class TestCustomerInfo(BasePage):

    def setUp(self):
        self.page = CustomerInfoPage(self.driver)

    # 初始化数据
    MysqlDb().init_database("customerinfo.txt")

    cases1 = readData().read_excel("新建客户信息", filename)

    @data(*cases1)
    # @unittest.skip("忽略")
    def test_001_new_custemorinfo(self, args):
        mylogger.info("--------------------测试用例开始执行--------------------")
        mylogger.info(f"用例{args[0]}:{args[1]}--->>测试数据：{args[2]}")
        self.page.handle_new_customerinfo_alert(args[2]['name'], args[2]['content'])
        self.page.handle_save()
        if args[0] not in ["add-customer-004"]:
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
        else:
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
            self.page.handle_save(is_save=False)
        mylogger.info("--------------------测试用例执行结束--------------------")

    cases2 = readData().read_excel("编辑客户信息", "customerinfo.xlsx")

    @data(*cases2)
    # @unittest.skip('忽略')
    def test_002_edit_custemorinfo(self, args):
        mylogger.info("--------------------测试用例开始执行--------------------")
        mylogger.info(f"用例{args[0]}:{args[1]}--->>测试数据：{args[2]}")
        self.page.handle_edit_customerinfo_alert(args[2]['name'], args[2]['content'])
        self.page.handle_save()
        actual = self.page.get_text(args[4]['xpath'])
        self.checkAssertEqual(args[3]['msg'], actual)
        mylogger.info("--------------------测试用例执行结束--------------------")

    # @unittest.skip
    def test_003_delete_custemorinfo(self):
        self.page.delete_customer()
        excepted = "删除客户成功"
        actual = self.page.get_text("//span[text()='删除客户成功']")
        self.checkAssertEqual(excepted, actual)
        sql = "SELECT COUNT(*) FROM `t_client` WHERE `NAME`='test002' AND `deleted_at` IS NULL"
        num = MysqlDb().query(sql)
        self.checkAssertEqual(0, num[0][0])
        mylogger.info("--------------------测试用例执行结束--------------------")


if __name__ == '__main__':
    unittest.main(verbosity=2)
