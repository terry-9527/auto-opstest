import random

from selenium import webdriver

from common.keywords import KeyWords
from utils.read_db import MysqlDb


class ClusterInfoPage(KeyWords):
    '''
    页面元素的定位信息
    '''
    # 系统设置
    system_setting = ('xpath', '//span[text()="系统设置"]')
    # 新建集群
    cluster_info = ('xpath', '//span[text()=" 集群信息"]')
    # 新建集群按钮
    new_cluster_button = ('xpath', '//span[text()="新建集群"]')
    # 集群ID输入框
    clusterid_input = ('xpath', '//form/div[1]//input')
    # 域名输入框
    domain_input = ('xpath', '//form/div[4]//input')
    # 备注输入框
    comment_input = ('xpath', '//form/div[6]//input')
    # 确定按钮
    confirm_button = ('xpath', '//span[text()="确 定"]')
    # 取消按钮
    cancel_button = ('xpath', '//span[text()="取 消"]')
    # 编辑按钮
    edit_button = ('xpath', '//tbody/tr[4]//span[text()="编辑"]')
    # 添加负责人按钮
    add_person_liable = ('xpath', '//tbody/tr[4]//span[text()="添加负责人"]')
    # div下拉框
    div_select = ('css', 'div.ant-select-item-option-content')
    # 所属客户输入框
    client_input = ('xpath', '//form/div[2]/div[2]/div[1]/div/div/div')
    # client_input = ('xpath', '//*[@id="rc_select_1"]')
    # 所在机房输入框
    machineroom_input = ('xpath', '//form/div[3]/div[2]/div[1]/div/div/div')
    # 山区大小输入框
    sector_size_input = ('xpath', '//form/div[5]/div[2]/div[1]/div/div/div')

    custemors = MysqlDb().query("select count(*) from t_client")[0][0]
    machinerooms = MysqlDb().query("select count(*) from t_machine_room")[0][0]
    total = custemors + machinerooms + 2


    # div下拉菜单选择
    def div_selector(self, input_path, number=0):
        self.click_element(*input_path)
        self.click_elements(*self.div_select, number)

    # 新建集群信息
    def new_clusterinfo(self, clusterid, domain=None, comment=None, confirm=True):
        self.click_element(*self.system_setting)
        self.click_element(*self.cluster_info)
        self.click_element(*self.new_cluster_button)
        self.wait(1)
        self.input_text(*self.clusterid_input, clusterid)
        # 选择所属客户下拉框
        self.wait(1)
        self.div_selector(self.client_input, random.randint(0,self.custemors-1))
        self.wait(1)
        self.div_selector(self.machineroom_input, random.randint(self.custemors,self.total-3))
        self.wait(1)
        self.input_text(*self.domain_input, domain)
        self.wait(1)
        self.div_selector(self.sector_size_input, random.randint(self.total-2, self.total-1))
        self.wait(1)
        self.input_text(*self.comment_input, comment)
        if confirm:
            self.click_element(*self.confirm_button)
        self.click_element(*self.cancel_button)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    page = ClusterInfoPage(driver)
