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
    click_host = ('css_selector', '.ant-radio-inner')
    # 点击确认
    click_confirm = ('xpath', '//span[text()="确 认"]')
    # 点击取消
    click_cancel = ('xpath', '//span[text()="取 消"]')
    # 选择模板
    click_model = ('xpath', '//span[text()="+ 选择模板"]')
    # 点击模板
    check_model = ('css_selector', '.ant-radio-input')
    # 确认模板
    confirm_model = ('xpath', '//span[text()="确 认"]')
    # 点击取消
    click_cancel2 = ('xpath', '//span[text()="取 消"]')
    # 开始执行
    start_execution = ('xpath', '//span[text()="开始执行"]')


    def new_commandinfo(self):
        self.click_navigation_bar("作业管理")
        self.click_navigation_bar("命令执行")
        self.click_element(*self.Target_cluster)
        self.click_elements(*self.click_info,random.randint(0,2))