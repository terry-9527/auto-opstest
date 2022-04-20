import unittest
from ddt import ddt, data

from common.base_page import BasePage
from common.my_logger import mylogger
from utils.read_data import readData
from pages.system_setting_page.cluster_info.cluster_info_page import ClusterInfoPage
from pages.system_setting_page.user_management.user.user_management_page import UserManagementPage
from utils.read_db import MysqlDb

filename = "clusterinfo.xlsx"

@ddt
class TestClusterInfo(BasePage):

    def setUp(self):
        self.page = ClusterInfoPage(self.driver)
        self.page1 = UserManagementPage(self.driver)
    def tearDown(self):
        self.page.wait()
        self.page.click_navigation_bar("系统设置")
        self.page.click_navigation_bar("首页")

    # 初始化数据数据
    MysqlDb().init_database("clusterinfo.txt")
    cases1 = readData().read_excel("新建集群信息", "clusterinfo.xlsx")

    @data(*cases1)
    # @unittest.skip
    def test_001_new_cluster(self, args):
        mylogger.info("--------------------测试用例开始执行--------------------")
        mylogger.info(f"用例{args[0]}:{args[1]}--->>测试数据：{args[2]}")

        self.page.new_clusterinfo(args[2]['miner_id'],customer=args[2]['customer'], machineroom=args[2]['machineroom'],
                             domain=args[2]['domain'], size=args[2]['size'], comment=args[2]['comment'])
        if args[0] not in ["add-clusterinfo-005", "add-clusterinfo-006", "add-clusterinfo-007"]:
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
        elif args[0] != "add-clusterinfo-007":
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
            self.page.click_span_button("取 消")
        else:
            actual1 = self.page.get_text(args[4]['xpath1'])
            self.checkAssertEqual(args[3]['msg1'], actual1)
            actual2 = self.page.get_text(args[4]['xpath2'])
            self.checkAssertEqual(args[3]['msg2'], actual2)
            self.page.click_span_button("取 消")
        mylogger.info("--------------------测试用例执行完毕--------------------")

    cases2 = readData().read_excel("编辑集群信息", "clusterinfo.xlsx")
    @data(*cases2)
    # @unittest.skip
    def test_002_edit_cluster(self, args):
        mylogger.info("--------------------测试用例开始执行--------------------")
        mylogger.info(f"用例{args[0]}:{args[1]}--->>测试数据：{args[2]}")
        self.page.edit_clusterinfo(args[2]['miner_id'], customer=args[2]['customer'], machineroom=args[2]['machineroom'],
                             domain=args[2]['domain'], size=args[2]['size'], comment=args[2]['comment'])
        actual = self.page.get_text(args[4]['xpath'])
        self.checkAssertEqual(args[3]['msg'], actual)
        mylogger.info("--------------------测试用例执行完毕--------------------")


    # @unittest.skip("跳过，进行调试")
    def test_003_bind_person_liabel(self):
        mylogger.info("--------------------测试用例开始执行--------------------")
        self.page.bind_person_liabel(minerid="f01000011", name="Nick")
        excepted = "添加负责人成功"
        actual = self.page.get_text("//span[text()='添加负责人成功']")
        self.checkAssertEqual(excepted, actual)
        self.page.wait()
        self.page.click_navigation_bar("系统设置")
        self.page.click_navigation_bar("首页")
        self.page.bind_person_liabel(minerid="f01000011", state="all")
        excepted = "添加负责人成功"
        actual = self.page.get_text("//span[text()='添加负责人成功']")
        self.checkAssertEqual(excepted, actual)
        mylogger.info("--------------------测试用例执行完毕--------------------")

    # 先创建集群后再对用户绑定对应的集群
    def test_004_bind_miner(self):
        mylogger.info("--------------------测试用例开始执行--------------------")
        # 绑定执行的集群
        minerid_list = ["f020000", "f030000"]
        self.page1.bind_miner(minerid_list, is_select=True)
        excepted = "关联集群成功"
        actual = self.page.get_text("//span[text()='关联集群成功']")
        self.checkAssertEqual(excepted, actual)
        self.page.wait()
        self.page.click_navigation_bar("用户管理")
        self.page.click_navigation_bar("系统设置")
        self.page.click_navigation_bar("首页")
        # 绑定所有的集群
        self.page1.bind_miner(select_all=True)
        excepted = "关联集群成功"
        actual = self.page.get_text("//span[text()='关联集群成功']")
        self.checkAssertEqual(excepted, actual)
        mylogger.info("--------------------测试用例执行结束--------------------")

if __name__ == '__main__':
    unittest.main(verbosity=2)


