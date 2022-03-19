import unittest
from ddt import ddt,data
from common.base_page import BasePage
from pages.system_setting_page.cluster_info.cluster_info_page import ClusterInfoPage
from utils.read_data import readData
from utils.read_db import MysqlDb

@ddt
class TestClusterInfo(BasePage):
    # 初始化数据数据
    MysqlDb().init_database("clusterinfo.txt")


    cases = readData().read_excel("新建集群信息","clusterinfo.xlsx")
    @data(*cases)
    def test_new_cluster(self, args):
        c = ClusterInfoPage(self.driver)
        c.new_clusterinfo(args[2]['miner_id'], domain=args[2]['domain'], comment=args[2]['comment'], confirm=args[2]['confirm'])




if __name__ == '__main__':
    unittest.main(verbosity=2)