import unittest

from common.base_page import BasePage
from ddt import ddt, data

from common.my_logger import mylogger
from pages.workbench_page.cluster_overview.cluster_overview_page import ClusterOverviewPage


@ddt()
class TestClusterOverview(BasePage):

    def setUp(self):
        self.page = ClusterOverviewPage(self.driver)
    # 准备测试数据
    input_data = [{"minerid": "f060975"}, {"customer": "内部"}, {"liabel": "Fide"}]

    @data(*input_data)
    @unittest.skip
    def test_search(self, args):
        mylogger.info("--------------------测试用例开始执行--------------------")
        self.page.search_cluster(**args)

    def test_lookup_cluster(self):
        mylogger.info("--------------------测试用例开始执行--------------------")
        self.page.lookup_cluster(minerid="f060975")
        actual = self.page.get_text("//span[text()='f060975']")
        self.checkAssertEqual("f060975", actual)
        mylogger.info("--------------------测试用例执行结束--------------------")

if __name__ == '__main__':
    unittest.main()