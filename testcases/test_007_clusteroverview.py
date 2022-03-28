import unittest

from common.base_page import BasePage
from ddt import ddt, data
from pages.workbench_page.cluster_overview.cluster_overview_page import ClusterOverviewPage


@ddt()
class TestClusterOverview(BasePage):
    # 准备测试数据
    input_data = ({"minerid": "f060975"}, {"customer": "内部"}, {"liabel": "Fide"})

    @data(*input_data)
    def test_search(self, args):
        self.page = ClusterOverviewPage(self.driver)
        self.page.search_cluster(**args)

if __name__ == '__main__':
    unittest.main()