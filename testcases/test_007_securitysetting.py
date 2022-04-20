from common.base_page import BasePage
from common.my_logger import mylogger
from pages.system_setting_page.security_policy.security_setting_page import SecuritySettingPage



class TestSecurityPolicy(BasePage):


    def test_setting_security_policy(self):
        mylogger.info("--------------------测试用例开始执行--------------------")
        self.page = SecuritySettingPage(self.driver)
        self.page.setting_security_policy(times=10)
        excepted = "修改密码策略成功"
        actual = self.page.get_text("//span[text()='修改密码策略成功']")
        self.checkAssertEqual(excepted, actual)
        mylogger.info("--------------------测试用例执行结束--------------------")

