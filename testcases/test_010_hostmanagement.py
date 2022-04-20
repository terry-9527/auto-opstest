import os
import unittest
from ddt import ddt, data

from common.my_logger import mylogger
from utils.read_data import readData
from common.base_page import BasePage
from pages.workbench_page.host_management.host_management_page import HostManagementPage
from utils.handle_path import download_dir

filename = "hostmanagement.xlsx"
device_file = os.path.join(download_dir, "f01234.csv")

@ddt
class TestHostManagement(BasePage):

    def setUp(self):
        self.page = HostManagementPage(self.driver)

    # 批量导入设备信息
    # @unittest.skip
    def test_001_batch_import(self):
        self.page.upload_deviceinfo(filepath=device_file, import_type="批量导入", minerid="f01234")

    # 单个导入设备信息
    cases1 = readData().read_excel("单个设备导入", filename)

    # @unittest.skip
    @data(*cases1)
    def test_002_upload(self, args):
        mylogger.info("--------------------测试用例开始执行--------------------")
        mylogger.info(f"用例{args[0]}:{args[1]}--->>测试数据：{args[2]}")
        self.page.upload_deviceinfo(import_type=args[2]['import_type'], minerid=args[2]['minerid'], sn=args[2]['sn'],
                                    module=args[2]['module'],
                                    customer=args[2]['customer'], software_role=args[2]['software_role'])
        if args[0] == "import-deviceinfo-001":
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
            self.page.click_navigation_bar("工作台")
        else:
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
            self.page.click_span_button("取 消")
            self.page.click_navigation_bar("工作台")
        self.page.click_navigation_bar("首页")
        mylogger.info("--------------------测试用例执行结束--------------------")


    # lotus操作和主机操作
    cases2 = readData().read_excel("主机管理", filename)

    # @unittest.skip
    @data(*cases2)
    def test_003_lotus_operation(self, args):
        mylogger.info("--------------------测试用例开始执行--------------------")
        mylogger.info(f"用例{args[0]}:{args[1]}--->>测试数据：{args[2]}")
        # 判断是否走审批流程,yes表示走审批流，no表示不走审批流
        if args[2]['button_name'] == "移除"and args[0] == "opt-lotus-006":
            self.page.set_machine_fault_status(args[2]['sn'], state=True, minerid=args[2]['minerid'])
        if args[0] == "opt-lotus-007":
            self.page.chose_checkbox(times=2, sn=args[2]['sn'], minerid=args[2]['minerid'])
            self.page.click_button_list(args[2]['button_name'])
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
        else:
            self.page.chose_checkbox(times=2, sn=args[2]['sn'], minerid=args[2]['minerid'])
            self.page.click_button_list(args[2]['button_name'])
            self.page.approve_alert(args[2]['reason_comment'], is_confirm=args[2]['is_confirm'],
                                    approve_state=args[2]['approve_state'])
            actual = self.page.get_text(args[4]['xpath'])
            self.checkAssertEqual(args[3]['msg'], actual)
        self.page.click_navigation_bar("工作台")
        self.page.click_navigation_bar("首页")
        mylogger.info("--------------------测试用例执行结束--------------------")

    cases = readData().read_excel("搜索", filename)
    # @unittest.skip
    @data(*cases)
    def test_004_search(self, args):
        self.page.search_deviceinfo(minerid=args[2]['minerid'], sn=args[2]['sn'], ip=args[2]['ip'], role=args[2]['role'],
                                    machine_status=args[2]['machine_status'], work_status=args[2]['work_status'])


    # @unittest.skip
    def test_005_deviceinfo(self):
        self.page.deviceinfo_detail(minerid="f060975", sn="KJ2020100610004")

    # 下载导入模板
    # @unittest.skip
    def test_006_down_template(self):
        self.page.download_template()




if __name__ == '__main__':
    unittest.main(verbosity=2)
