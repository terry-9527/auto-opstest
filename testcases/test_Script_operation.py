import unittest
from common.base_page import BasePage
from pages.job_management_page.Public_script import CustemorPage

class Correct_operation(BasePage):

    def test_0001_operation(self):
        page = CustemorPage(self.driver)
        page.New_script()


if __name__ == '__main__':
    unittest.main(verbosity=2)