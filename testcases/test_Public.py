import unittest
from ddt import ddt,data
from common.base_page import BasePage
from pages.job_management_page.Common_module import CustemorPage
from utils.read_data import readData
import yaml

class operation_info(BasePage):
   # cass = readData().read_yaml("view_memory.yaml")
    # 操作新建模板
    def test_001_newly_build(self):
        page = CustemorPage(self.driver)
        page.operation_info()


if __name__ == '__main__':
    unittest.main(verbosity=2)