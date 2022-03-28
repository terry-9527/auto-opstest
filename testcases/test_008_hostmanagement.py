from selenium import webdriver

from common.base_page import BasePage
from common.keywords import KeyWords
from pages.workbench_page.host_management.host_management_page import HostManagementPage
import unittest
from utils.read_data import readData
from ddt import ddt, data

filename = "hostmanagement.xlsx"


@ddt
class TestHostManagement(BasePage):

    @classmethod
    def setUpClass(cls):
        # 设置Chrome浏览器profile配置项 download.default_directory：设置下载路径 profile.default_content_settings.popups：设置为 0 禁止弹出窗口
        cls.options = webdriver.ChromeOptions()
        cls.prefs = {'profile.default_content_settings.popups': 0,
                     'download.default_directory': 'E:\\auto-opstest\\download'}
        cls.options.add_experimental_option('prefs', cls.prefs)
        cls.driver = webdriver.Chrome(chrome_options=cls.options)
        cls.kd = KeyWords(cls.driver)
        cls.driver.get("https://opstest.arsyun.com")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.add_cookie({"name": "public-jwt",
                               "value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo2LCJ1c2VyX25hbWUiOiJ0ZXJyeSIsImJ1ZmZlcl90aW1lIjo4NjQwMCwiZXhwIjoxNjQ5MDMzODkxLCJpc3MiOiJhcnNQdWJsaWMiLCJuYmYiOjE2NDg0MjgwOTF9.sOIhEcHMAVKacR6DRRzoQjfQizZoNWxjfuvozTpSsXI"})
        cls.driver.get("https://opstest.arsyun.com")

    # 批量导入设备信息
    @unittest.skip
    def test_001_batch_import(self):
        self.page = HostManagementPage(self.driver)
        self.page.upload_deviceinfo(filepath=r"E:\auto-opstest\testdatas\f01234.csv", import_type="批量导入",
                                    minerid="f01234")

    # lotus操作和主机操作
    cases = readData().read_excel("主机管理", filename)

    @unittest.skip
    @data(*cases)
    def test_002_lotus_operation(self, args):
        self.page = HostManagementPage(self.driver)
        # 判断是否走审批流程,yes表示走审批流，no表示不走审批流
        if args[2]['button_name'] == "移除":
            self.page.set_machine_fault_status(args[2]['sn'], state=True, minerid=args[2]['minerid'])
        self.page.choice_checkbox(times=2, sn=args[2]['sn'], minerid=args[2]['minerid'])
        self.page.click_button_list(args[2]['button_name'])
        self.page.approve_alert(args[2]['reason_comment'], is_confirm=args[2]['is_confirm'],
                                approve_state=args[2]['approve_state'])
        self.page.wait(1)

    # 单个导入设备信息
    cases = readData().read_excel("单个设备导入", filename)

    @unittest.skip
    @data(*cases)
    def test_003_upload(self, args):
        self.page = HostManagementPage(self.driver)
        self.page.upload_deviceinfo(import_type=args[2]['import_type'], minerid=args[2]['minerid'], sn=args[2]['sn'],
                                    module=args[2]['module'],
                                    customer=args[2]['customer'], software_role=args[2]['software_role'])
        self.page.wait()

    # 下载导入模板
    @unittest.skip
    def test_004_down_template(self):
        self.page = HostManagementPage(self.driver)
        self.page.download_template()

    @unittest.skip
    def test_005_deviceinfo(self):
        self.page = HostManagementPage(self.driver)
        self.page.deviceinfo_detail(minerid="f060975", sn="KJ21011310004")



    cases = readData().read_excel("搜索", filename)
    # @unittest.skip
    @data(*cases)
    def test_006_search(self, args):
        self.page = HostManagementPage(self.driver)
        self.page.search_deviceinfo(minerid=args[2]['minerid'], sn=args[2]['sn'], ip=args[2]['ip'], role=args[2]['role'],
                                    machine_status=args[2]['machine_status'], work_status=args[2]['work_status'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
