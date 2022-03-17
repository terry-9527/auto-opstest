"""
执行用例总入口
"""
import os
import unittest


class runTestCase:

    def load_all_case(self, filename=None):
        """
        加载用例目录下的所有测试用例文件的测试用例
        默认加载testcases目录下所有的测试用例
        :return:
        """
        # 获取测试用例目录
        case_path = os.path.join(os.path.abspath('..'), "testcases")
        files = os.listdir(case_path)
        case_list = []
        if not filename:
            # 遍历目录下所有的文件
            for file in files:
                if file.endswith(".py") and file.startswith("test"):
                    discover = unittest.defaultTestLoader.discover(case_path, pattern=file, top_level_dir=None)
                    case_list.append(discover)
            return case_list
        elif not filename in files:
            print("用例文件不存在")
        else:
            case_list = unittest.defaultTestLoader.discover(case_path, pattern=filename, top_level_dir=None)
            return case_list

    def run_all_case(self, filename=None):
        case = run.load_all_case(filename)
        if case:
            suite = unittest.TestSuite(case)
            runner = unittest.TextTestRunner()
            runner.run(suite)


if __name__ == "__main__":
    run = runTestCase()
    # case = run.load_all_case()
    # case = run.load_all_case(filename="test001.py")
    # suite = unittest.TestSuite(case)
    # runner = unittest.TextTestRunner()
    run.run_all_case("test_machineroominfo.py")
