import random
from selenium import webdriver
from common.windows_popup import WinAuto
from common.keywords import KeyWords


class HostManagementPage(KeyWords):
    """
    页面元素定位信息
    """
    # 下载模板按钮
    download_button = ('xpath', '//form/div[4]//a')
    # 审核提示弹窗的原因文本输入框
    reason_input = ('xpath', '//textarea')
    # 拒绝审批按钮
    refuse_approve_button = ('xpath', '//div[@class="ant-modal-footer"]/button[1]')
    # 确定走审批流程按钮
    confirm_approve_button = ('xpath', '//div[@class="ant-modal-footer"]/button[2]')
    # 编辑按钮
    edit_button = ('css', 'span.anticon.edit-icon-btn')
    # 导入设备信息+按钮 send_keys(r"E:\auto-opstest\testdatas\f01234.csv")
    import_button = ('xpath', '//*[@class="cluster-upload"]/button')
    # 导入方式选项定位 button.ant-btn-text
    import_type = ('css', 'button.ant-btn-text')
    # 上传文件弹出框确定按钮
    confirm_upload_button = ('xpath', '//div[@class="ant-modal-footer"]//button[2]')
    # 所属客户下拉input
    customer_input = ('xpath', '//label[@title="所属客户"]/../../div[2]/div')
    # 软件角色下拉input
    software_role_input = ('xpath', '//*[@class="ant-modal-content"]//form/div[3]/div[2]')
    # 下拉选项
    div_option = ('css', 'div.ant-select-item-option-content')
    # 添加主机确定按钮
    confirm_addhost_button = ('xpath', '//div[@class="ant-modal-footer"]//button[2]')
    # 添加主机取消按钮
    cancel_addhost_button = ('xpath', '//div[@class="ant-modal-footer"]//button[1]')
    # 主机列表查询
    # 搜索输入框 //input[@placeholder="集群SN/IP"]
    search_input = ('xpath', '//input[@placeholder="集群SN/IP"]')
    # 搜索按钮
    search_button = ('xpath', '//input[@placeholder="集群SN/IP"]/../span')
    # 更多条件下拉按钮
    condition_button = ('xpath', '//form/div[2]/div/div/div')
    # 条件搜索框中软件角色下拉div
    role_select = ('xpath', '//form/div[1]/div[2]/div/div/div')
    div_select = ('xpath', '//div[@class="ant-select-item-option-content"]')
    # 条件搜索框中机器状态下拉div
    machine_status_select = ('xpath', '//form/div[2]/div[2]/div/div/div')
    # 条件搜索框中工作状态下拉div
    work_status_select = ('xpath', '//form/div[3]/div[2]/div/div/div')

    # 定义一个空列表存放客户名
    customer_list = []

    def click_button_list(self, button_name):
        xpath = ('xpath', '//form/div[4]//button')
        name_list = {
            "关机": "2",
            "重启": "3",
            "移除": "4",
            "启动lotus": "5",
            "重启lotus": "6",
            "停止lotus": "7"
        }
        self.click_elements(*xpath, int(name_list[button_name]))

    # 选择复选框 //tbody/tr
    def choice_checkbox(self, times=1, sn=None, minerid="f01234"):
        """
        选择复选框，默认随机选择其中一台，也可以选择指定设备sn
        :param times: 默认勾选一台机器
        :param sn: 勾选具体的一台设备，输入sn
        :return:
        """
        self.click_navigation_bar("工作台")
        self.click_navigation_bar("主机管理")
        self.select_cluster(minerid)
        if not sn:
            xpath = ('xpath', '//tbody//input[@type="checkbox"]')
            # 查询设备总数量
            numbers = len(self.locators(*xpath))
            while times > 0:
                num = random.choice(list(range(numbers)))
                # num = 7
                if self.locators(*xpath)[num].is_selected():
                    times += 0
                else:
                    times -= 1
                    self.locators(*xpath)[num].click()
                    self.wait()
        else:
            checkbox_xpath = ('xpath', f'//span[text()="{sn}"]/../../..//input')
            self.click_element(*checkbox_xpath)

    # 审核弹窗操作
    def approve_alert(self, comment, is_confirm=True, approve_state="no"):
        """
        处理走审批流弹窗功能
        :param comment: 输入原因原由
        :param is_confirm: 默认为True，点击确定，审批走向下一级
        """
        if approve_state == "yes":
            self.input_text(*self.reason_input, comment)
            self.wait(0.5)
            if is_confirm:
                # print(len(self.locators(*self.confirm_approve_button)))
                self.click_element(*self.confirm_approve_button)
                self.wait()
            else:
                self.click_element(*self.refuse_approve_button)
                self.wait()
        elif approve_state == "no":
            if is_confirm:
                self.click_element(*self.confirm_approve_button)
                self.wait()
            else:
                self.click_element(*self.refuse_approve_button)
                self.wait()
        self.click_navigation_bar("首页")
        self.click_navigation_bar("工作台")

    def set_machine_fault_status(self, sn, state=False, minerid="f01234"):
        """
        z更改设备故障状态
        :param sn: 输入机器设备的SN码
        :param state: 需要设置的故障状态，默认是设置为否
        :return:
        """
        self.click_navigation_bar("工作台")
        self.click_navigation_bar("主机管理")
        self.select_cluster(minerid)
        # trlist = self.locator("xpath","//tr[@data-row-key][8]//td[2]//span[2]")
        sn_list = []
        trlenght = len(self.locators("xpath", "//tr[@data-row-key]"))
        for i in range(1, trlenght + 1):
            text = self.locator("xpath", f"//tr[@data-row-key][{i}]//td[2]//span[2]").get_attribute("textContent")
            # 获取到当前页面所有的SN码
            sn_list.append(text)
        index = sn_list.index(sn)
        edit_div = ('xpath', f'//span[text()="{sn}"]/../../../td[9]/div')
        # 鼠标移动到指定的元素上
        self.move(*edit_div)
        self.wait(0.5)
        # 获取到输入的SN索引，根据索引判断点击第几个编辑按钮
        self.click_elements(*self.edit_button, index)
        self.wait(0.5)
        select_input = ('xpath', f'//span[text()="{sn}"]/../../../td[9]/div')
        self.click_element(*select_input)
        self.wait(0.5)
        status_option = ('css', 'div.ant-select-item-option-content')
        # 判断设置的故障机状态，False设置为否，True设置为是
        if not state:
            self.click_elements(*status_option, 0)
        else:
            self.click_elements(*status_option, 1)

    def select_cluster(self, minerid):
        xpath = ('xpath', f'//ul[@class="cluster-list"]//li[text()="内部 {minerid}"]')
        self.click_element(*xpath)

    def upload_deviceinfo(self, filepath=None, import_type="批量导入", minerid=None, sn=None, module=None, customer=None,
                          software_role=None):
        """
        上传导入设备信息文件,默认是批量导入
        :param filepath: csv设备信息文件所在路径
        :param type: 导入方式，默认批量导入
        :return:
        """
        self.click_navigation_bar("工作台")
        self.click_navigation_bar("主机管理")
        self.select_cluster(minerid)
        self.move(*self.import_button)
        if import_type == "批量导入":
            self.click_elements(*self.import_type, 1)
            self.wait()
            self.click_span_button("选 择")
            self.wait(2)
            # 用pywinauto处理Windows弹窗
            window = WinAuto("#32770", "打开")
            self.wait()
            window.file_input(filepath)
            self.wait()
            window.open_button_click()
            self.wait()
            # 点击文件弹窗确定按钮
            self.click_element(*self.confirm_upload_button)
            self.click_navigation_bar("工作台")
            self.driver.refresh()
        if import_type == "添加主机":
            self.click_elements(*self.import_type, 0)
            self.add_host_alert(sn, module, customer, software_role)

    def add_host_alert(self, sn, module, customer, software_role):
        """
        处理单台设备信息上传
        :param sn: 设备SN码
        :param module: 产品型号
        :param customer:
        :param software_role:
        :return:
        """
        self.input_text(content=sn, text="主机SN")
        self.input_text(content=module, text="产品型号")
        # 选择所属用户
        if customer:
            self.click_element(*self.customer_input)
            self.wait(0.5)
            els1 = self.locators(*self.div_option)
            for el in els1:
                self.customer_list.append(el.text)
            num = self.customer_list.index(customer)
            self.click_elements(*self.div_option, num)
        else:
            self.click_element(*self.customer_input)
        if software_role:
            # 选择软件角色
            self.click_element(*self.software_role_input)
            self.wait(0.5)
            els2 = self.locators(*self.div_option)
            software_role_list = []
            for el in els2:
                software = el.text
                if software not in self.customer_list:
                    software_role_list.append(el.text)
            num = software_role_list.index(software_role)
            self.click_elements(*self.div_option, num)
            self.wait(0.5)
        if sn and module and customer and software_role:
            self.click_element(*self.confirm_addhost_button)
        else:
            self.click_element(*self.confirm_addhost_button)
            self.wait()
            self.click_element(*self.cancel_addhost_button)

    def download_template(self):
        """
        下载模板，下载默认文件名称为：批量导入机器.csv
        :return:
        """
        self.click_navigation_bar("工作台")
        self.click_navigation_bar("主机管理")
        self.click_element(*self.download_button)

    # 查看设备详情
    def deviceinfo_detail(self, minerid=None, sn=None):
        self.click_navigation_bar("工作台")
        self.click_navigation_bar("主机管理")
        self.select_cluster(minerid)
        # 查询设备详情按钮
        detail_button = ('xpath', f'//span[text()="{sn}"]/../../../td[12]/button')
        self.click_element(*detail_button)
        self.wait()

    def search_deviceinfo(self, minerid="f060975", sn=None, ip=None, role=None, machine_status=None, work_status=None):
        self.click_navigation_bar("工作台")
        self.click_navigation_bar("主机管理")
        self.select_cluster(minerid)
        if role or machine_status or work_status:
            self.wait()
            self.click_elements(*self.condition_button, 0)
            # 清空上一次的搜索
            self.click_span_button("清 空")
            # 选择软件角色
            self.wait()
            if role:
                self.div_selector(self.role_select, self.div_select, name=role)
            # 选择故障状态
            if machine_status:
                self.div_selector(self.machine_status_select, self.div_select, name=machine_status)
            # 选择工作状态
            if work_status:
                self.div_selector(self.work_status_select, self.div_select, name=work_status)
            self.click_span_button("确 定")
            self.click_elements(*self.condition_button, 0)
        # 先清空输入框的内容
        self.clear(*self.search_input)
        if sn:
            self.input_text(*self.search_input, content=sn)
            self.click_element(*self.search_button)
        if ip:
            self.input_text(*self.search_input, content=ip)
            self.click_element(*self.search_button)
