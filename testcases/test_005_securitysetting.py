from common.base_page import BasePage
from pages.system_setting_page.security_policy.security_setting_page import SecuritySettingPage



class TestSecurityPolicy(BasePage):


    def test_setting_security_policy(self):
        page = SecuritySettingPage(self.driver)
        page.setting_security_policy(times=10)