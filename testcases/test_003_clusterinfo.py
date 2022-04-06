import unittest
from ddt import ddt, data

from common.base_page import BasePage
from utils.read_data import readData
from pages.system_setting_page.cluster_info.cluster_info_page import ClusterInfoPage


filename = "clusterinfo.xlsx"

@ddt
class TestClusterInfo(BasePage):
    # 初始化数据数据
    # MysqlDb().init_database("clusterinfo.txt")

    cases = readData().read_excel("新建集群信息", "clusterinfo.xlsx")

    @data(*cases)
    @unittest.skip
    def test_001_new_cluster(self, args):
        page = ClusterInfoPage(self.driver)
        page.new_clusterinfo(args[2]['miner_id'],customer=args[2]['customer'], machineroom=args[2]['machineroom'],
                             domain=args[2]['domain'], size=args[2]['size'], comment=args[2]['comment'], is_save=args[2]['is_save'])
        # 文本断言
        # page.text_assert_equal(filename, args[0], args[3]['msg'], args[4])
        # 测试结果写入表格中
        # readData().write_excel(filename, case_id=args[0], testresult="Failed", reason="结果对比失败")

    cases = readData().read_excel("编辑集群信息", "clusterinfo.xlsx")
    @data(*cases)
    # @unittest.skip
    def test_002_edit_cluster(self, args):
        page = ClusterInfoPage(self.driver)
        page.edit_clusterinfo(args[2]['miner_id'],customer=args[2]['customer'], machineroom=args[2]['machineroom'],
                             domain=args[2]['domain'], size=args[2]['size'], comment=args[2]['comment'], is_save=args[2]['is_save'])
        page.text_assert_equal(args[0], args[3]['msg'], args[4]['xpath'])

    @unittest.skip("跳过，进行调试")
    def test_003_bind_person_liabel(self):
        page = ClusterInfoPage(self.driver)
        page.bind_person_liabel()
        page.bind_person_liabel(state="all")


if __name__ == '__main__':
    unittest.main(verbosity=2)


