import unittest
from ddt import ddt, data

from common.base_page import BasePage
from common.my_logger import mylogger
from utils.read_data import readData
from pages.system_setting_page.cluster_info.cluster_info_page import ClusterInfoPage
from utils.read_db import MysqlDb

filename = "clusterinfo.xlsx"

@ddt
class TestClusterInfo(BasePage):

    # 初始化数据数据
    MysqlDb().init_database("clusterinfo.txt")
    cases1 = readData().read_excel("新建集群信息", "clusterinfo.xlsx")

    @data(*cases1)
    # @unittest.skip
    def test_001_new_cluster(self, args):
        mylogger.info("--------------------测试用例开始执行--------------------")
        mylogger.info(f"用例{args[0]}:{args[1]}--->>测试数据：{args[2]}")
        page = ClusterInfoPage(self.driver)
        page.new_clusterinfo(args[2]['miner_id'],customer=args[2]['customer'], machineroom=args[2]['machineroom'],
                             domain=args[2]['domain'], size=args[2]['size'], comment=args[2]['comment'])
        page.handle_save()
        if args[0] not in ["add-clusterinfo-005", "add-clusterinfo-006", "add-clusterinfo-007"]:
            actual = page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
        elif args[0] != "add-clusterinfo-007":
            actual = page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
            page.handle_save(is_save=False)
        else:
            actual1 = page.get_text(args[4]['xpath1'])
            self.checkAssertEqual(args[3]['msg1'], actual1)
            actual2 = page.get_text(args[4]['xpath2'])
            self.checkAssertEqual(args[3]['msg2'], actual2)
            page.handle_save(is_save=False)
        mylogger.info("--------------------测试用例执行完毕--------------------")

    cases2 = readData().read_excel("编辑集群信息", "clusterinfo.xlsx")
    @data(*cases2)
    # @unittest.skip
    def test_002_edit_cluster(self, args):
        mylogger.info("--------------------测试用例开始执行--------------------")
        mylogger.info(f"用例{args[0]}:{args[1]}--->>测试数据：{args[2]}")
        page = ClusterInfoPage(self.driver)
        page.edit_clusterinfo(args[2]['miner_id'], customer=args[2]['customer'], machineroom=args[2]['machineroom'],
                             domain=args[2]['domain'], size=args[2]['size'], comment=args[2]['comment'])
        page.handle_save()
        actual = page.get_text(args[4]['xpath'])
        self.checkAssertEqual(args[3]['msg'], actual)
        mylogger.info("--------------------测试用例执行完毕--------------------")


    # @unittest.skip("跳过，进行调试")
    def test_003_bind_person_liabel(self):
        mylogger.info("--------------------测试用例开始执行--------------------")
        page = ClusterInfoPage(self.driver)
        page.driver.refresh()
        page.bind_person_liabel(minerid="f01000011", name="test001")
        excepted = "添加负责人成功"
        actual = page.get_text("//span[text()='添加负责人成功']")
        self.checkAssertEqual(excepted, actual)
        page.bind_person_liabel(minerid="f01000011", state="all")
        excepted = "添加负责人成功"
        actual = page.get_text("//span[text()='添加负责人成功']")
        self.checkAssertEqual(excepted, actual)
        mylogger.info("--------------------测试用例执行完毕--------------------")

if __name__ == '__main__':
    unittest.main(verbosity=2)


