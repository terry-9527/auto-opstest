from common.keywords import KeyWords
import random

class CustemorPage(KeyWords):
    '''
    页面元素的定位信息
    '''
    # 作业管理
    job_managemen = ('xpath', '//span[text()="作业管理"]')
    # 命令执行
    command_imp = ('xpath', '//span[text()="命令执行"]')
    # 目标集群
    Target_cluster = ('css_selector', '.ant-select-selection-item')
    # 点击集群
    click_info = ('css_selector', '.ant-select-item-option-content')
    # 执行主机
    Execution_host = ('xpath', '//span[text()="+ 选择主机"]')
    # 点击主机
    click_host = ('css_selector', 'input.ant-radio-input')
    # 点击确认
    click_confirm = ('xpath', '//span[text()="确 认"]')
    # 点击取消
    #click_cancel = ('xpath', '//span[text()="取 消"]')
    # 选择模板
    choice_info = ('xpath', '//span[text()="+ 选择模板"]')
    # 点击模板
    check_model = (' ', 'input.ant-radio-input')
    # 确认模板
    confirm_model = ('xpath', '//span[text()="确 认"]')
    # 点击取消
    #click_cancel2 = ('xpath', '//span[text()="取 消"]')
    # 开始执行
    start_execution = ('xpath', '//span[text()="开始执行"]')

    # 工作台
    workbench_info = ('xpatg', '//span[text()="工作台"]')
    # 主机管理
    host_info = ('xpath', '//span[text()="主机管理"]')
    # 点击否
    no_info = ('css_selector', '.edit-icon-btn')
    # 点击
    # jia_hao = ('xpath', '//button[@class="ant-btn ant-dropdown-trigger"]')
    jia_hao = ('css_selector', '.ant-dropdown-trigger')

    def new_commandinfo(self):
        self.click_navigation_bar("作业管理")
        self.click_navigation_bar("命令执行")
        # 点击目标集群
        self.click_element(*self.Target_cluster)
        self.wait(1)
        # 点选择集群
        self.click_elements(*self.click_info,list_number=1)
        self.wait(1)
        # 点击选择主机
        self.click_element(*self.Execution_host)
        # 点击勾选主机
        self.click_elements(*self.click_host,random.randint(0,7))
        self.wait(2)
        # 点击确定
        self.click_elements(*self.click_confirm,list_number=0)
        # 点击选择模板
        self.click_element(*self.choice_info)
        # 点击模板
        self.click_elements(*self.check_model,list_number=1)
        # 确定选择模板
        self.click_elements(*self.confirm_model,list_number=1)
        # 开始执行
        self.click_element(*self.start_execution)


    def err_operation(self, target=None, target2=None):

        self.click_navigation_bar("作业管理")
        self.click_navigation_bar("命令执行")
        if target:
            # 点击目标集群
            self.click_element(*self.Target_cluster)
            self.wait(1)
        if target2:
            # 点选择集群
            self.click_elements(*self.click_info, list_number=1)
            self.wait(1)
            # 点击选择主机
            self.click_element(*self.Execution_host)
            # 点击勾选主机
            self.click_elements(*self.click_host, random.randint(0, 7))
        # 开始执行
        self.click_element(*self.start_execution)



