"""
执行用例总入口
"""
import os
import unittest
from unittestreport import TestRunner
from BeautifulReport import BeautifulReport
from datetime import datetime
from utils.handle_path import report_dir,testdata_dir,testcase_dir


class runTestCase:

    def load_all_case(self, filename=None):
        """
        加载用例目录下的所有测试用例文件的测试用例
        默认加载testcases目录下所有的测试用例
        :return:
        """
        # 获取测试用例目录
        files = os.listdir(testcase_dir)
        case_list = []
        if not filename:
            # 遍历目录下所有的文件
            for file in files:
                if file.endswith(".py") and file.startswith("test"):
                    discover = unittest.defaultTestLoader.discover(testcase_dir, pattern=file, top_level_dir=None)
                    case_list.append(discover)
            return case_list
        elif not filename in files:
            print("用例文件不存在")
        else:
            case_suits = unittest.defaultTestLoader.discover(testcase_dir, pattern=filename, top_level_dir=None)
            return case_suits

    def run_all_cases(self, filename=None):
        case_suits = run.load_all_case(filename)
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = now + "-report"
        if case_suits:
            # 方式一
            # BeautifulReport(case_suits).report(
            #                                     description="运维系统web自动化测试报告",
            #                                     report_dir=report_dir,
            #                                     filename=filename,
            #                                     theme="theme_candy"
            #                                    )
            # 方式二
            runner = TestRunner(case_suits,
                                filename=filename,
                                report_dir=report_dir,
                                title="运维系统web自动化测试报告",
                                templates=1,
                                tester="Terry",
                                desc="运维系统项目web自动化测试报告")
            runner.run()


if __name__ == "__main__":
    run = runTestCase()
    run.run_all_cases(filename="test_007_approvalprocess.py")
    s = "sfsdfsdfsdf"


