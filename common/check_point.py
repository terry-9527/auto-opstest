"""
# File       : checkPoint.py
# Time       ：2021/4/20 14:05
# Author     ：DY
# version    ：V1.0.0
# Description：重写unittest断言方法,解决断言失败不再继续执行的问题
"""
import unittest

from common.keywords import KeyWords

from common.my_logger import mylogger


class CheckPoint(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super(CheckPoint, self).__init__(methodName)
        self._testMethodName = methodName
        self.flag = 0
        self.msg = []

    # 基本的布尔断言：要么正确，要么错误的验证
    def checkAssertEqual(self, excepted, actual, msg=None):
        """    验证arg1=arg2，不等则fail"""
        mylogger.info("开始进行断言------------>>")
        try:
            mylogger.info(f"预期结果：{excepted} <<=====>> 实际结果：{actual}")
            self.assertEqual(excepted, actual, msg)
            mylogger.info("---------------断言通过，结束断言---------------")
        except Exception as e:
            self.flag += 1
            self.msg.append("\n{}".format(msg))
            mylogger.info("---------------断言失败，结束断言---------------")
            raise e

    def checkAssertNotEqual(self, arg1, arg2, msg=None):
        """    验证arg1 != arg2, 相等则fail"""
        try:
            self.assertNotEqual(arg1, arg2, msg)
        except Exception as e:
            self.flag += 1
            self.msg.append("\n{}".format(msg))
            print(e)

    def checkAssertTrue(self, expr, msg=None):
        """验证expr是true，如果为false，则fail"""
        try:
            self.assertTrue(expr, msg)
        except Exception as e:
            self.flag += 1
            self.msg.append("\n{}".format(msg))
            print(e)

    def checkAssertFalse(self, expr, msg=None):
        """    验证expr是false，如果为true，则fail"""
        try:
            self.assertFalse(expr, msg)
        except Exception as e:
            self.flag += 1
            self.msg.append("\n{}".format(msg))
            print(e)

    def checkAssertIs(self, arg1, arg2, msg=None):
        """验证arg1、arg2是同一个对象，不是则fail"""
        try:
            self.assertIs(arg1, arg2, msg)
        except Exception as e:
            self.flag += 1
            self.msg.append("\n{}".format(msg))
            print(e)

    def checkAssertIsNot(self, arg1, arg2, msg=None):
        """验证arg1、arg2不是同一个对象，是则fail"""
        try:
            self.assertIsNot(arg1, arg2, msg)
        except Exception as e:
            self.flag += 1
            self.msg.append("\n{}".format(msg))
            print(e)

    def checkAssertIsNone(self, expr, msg=None):
        """    验证expr是None，不是则fail"""
        try:
            self.assertIsNone(expr, msg)
        except Exception as e:
            self.flag += 1
            self.msg.append("\n{}".format(msg))
            print(e)

    def checkAssertIsNotNone(self, expr, msg=None):
        """    验证expr不是None，是则fail"""
        try:
            self.assertIsNotNone(expr, msg)
        except Exception as e:
            self.flag += 1
            self.msg.append("\n{}".format(msg))
            print(e)

    def checkAssertIn(self, arg1, arg2, msg=None):
        """    验证arg1是arg2的子串，不是则fail"""
        try:
            self.assertIn(arg1, arg2, msg)
        except Exception as e:
            self.flag += 1
            self.msg.append("\n{}".format(msg))
            print(e)

    def checkAssertNotIn(self, arg1, arg2, msg=None):
        """验证arg1不是arg2的子串，是则fail"""
        try:
            self.assertNotIn(arg1, arg2, msg)
        except Exception as e:
            self.flag += 1
            self.msg.append("\n{}".format(msg))
            print(e)

    def checkAssertIsInstance(self, arg1, arg2, msg=None):
        """验证obj是cls的实例，不是则fail"""
        try:
            self.assertIsInstance(arg1, arg2, msg)
        except Exception as e:
            self.flag += 1
            self.msg.append("\n{}".format(msg))
            print(e)

    def checkAssertNotIsInstance(self, arg1, arg2, msg=None):
        """验证obj不是cls的实例，是则fail"""
        try:
            self.assertNotIsInstance(arg1, arg2, msg)
        except Exception as e:
            self.flag += 1
            self.msg.append("\n{}".format(msg))
            print(e)

    # 比较断言：比较两个变量的值
    def checkAssertGreater(self, first, second, msg=None):
        """　验证first > second，否则fail"""
        try:
            self.assertGreater(first, second)
        except Exception as e:
            self.flag += 1
            self.msg.append("\n{}".format(msg))
            print(e)

    def checkAssertGreaterEqual(self, first, second, msg=None):
        """验证first >= second，否则fail"""
        try:
            self.assertGreaterEqual(first, second)
        except Exception as e:
            self.flag += 1
            self.msg.append("\n{}".format(msg))
            print(e)

    def checkAssertLess(self, first, second, msg=None):
        """验证first < second，否则fail"""
        try:
            self.assertLess(first, second)
        except Exception as e:
            self.flag += 1
            self.msg.append("\n{}".format(msg))
            print(e)

    def checkAssertLessEqual(self, first, second, msg=None):
        """验证first <= second，否则fail"""
        try:
            self.assertLessEqual(first, second)
        except Exception as e:
            self.flag += 1
            self.msg.append("\n{}".format(msg))
            print(e)

    def checkTestResult(self):
        """获取用例执行结果"""
        return self.assertEqual(self.flag, 0, "{}".format(self.msg))
