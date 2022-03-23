import unittest
from ddt import ddt, data
from common.base_page import BasePage
from pages.system_setting_page.cluster_info.cluster_info_page import ClusterInfoPage
from utils.read_data import readData
from utils.read_db import MysqlDb


@ddt
class TestClusterInfo(BasePage):
    # 初始化数据数据
    MysqlDb().init_database("clusterinfo.txt")

    cases = readData().read_excel("新建集群信息", "clusterinfo.xlsx")

    @data(*cases)
    # @unittest.skip("跳过，进行调试")
    def test_001_new_cluster(self, args):
        page = ClusterInfoPage(self.driver)
        page.new_clusterinfo(args[2]['miner_id'], domain=args[2]['domain'], comment=args[2]['comment'],
                             is_save=args[2]['is_save'])

    cases = readData().read_excel("编辑集群信息", "clusterinfo.xlsx")

    @data(*cases)
    # @unittest.skip("跳过，进行调试")
    def test_002_edit_cluster(self, args):
        page = ClusterInfoPage(self.driver)
        page.edit_clusterinfo(args[2]['miner_id'], args[2]['custemor'], args[2]['machineroom'], args[2]['domain'],
                              args[2]['size'], args[2]['comment'], args[2]['is_save'])

    # @unittest.skip("跳过，进行调试")
    def test_003_bind_person_liabel(self):
        page = ClusterInfoPage(self.driver)
        page.bind_person_liabel()
        page.bind_person_liabel(state="all")


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    suit = unittest.TestSuite()
    unittest.TestLoader().loadTestsFromTestCase(TestClusterInfo)
    runner = unittest.TextTestRunner()
    runner.run(suit)
