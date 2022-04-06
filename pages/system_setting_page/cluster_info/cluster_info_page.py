from selenium import webdriver
from common.keywords import KeyWords
from common.my_logger import mylogger


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
    # 编辑按钮 f01000
    edit_button = ('xpath', '//tr//span[contains(text(),"f0100")]/../..//span[text()="编辑"]')
    # 添加负责人按钮
    add_person_liable_button = ('xpath', '//tr//span[contains(text(),"f0100")]/../..//span[text()="添加负责人"]')
    # div下拉框
    div_select = ('css', 'div.ant-select-item-option-content')
    # 所属客户输入框
    client_input = ('xpath', '//form/div[2]/div[2]/div[1]/div/div/div')
    # 所在机房输入框
    machineroom_input = ('xpath', '//form/div[3]/div[2]/div[1]/div/div/div')
    # 山区大小输入框
    sector_size_input = ('xpath', '//form/div[5]/div[2]/div[1]/div/div/div')
    # 添加集群负责人，全选复选框
    checkbox_all = ('xpath', '//th[@title="用户"]/../th[1]//input')
    # admin用户复选框
    checkbox_one = ('xpath', '//td[@title="admin"]/../td[1]//input')
    #


    def new_clusterinfo(self, clusterid, customer=None, machineroom=None, domain=None, size=None, comment=None, is_save=True):
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("集群信息")
        self.click_element(*self.new_cluster_button)
        self.input_text(*self.clusterid_input, clusterid)
        # 选择所属客户下拉框
        if customer:
            self.div_selector(self.client_input, self.div_select, name=customer)
        else:
            self.click_element(*self.client_input)
        if machineroom:
            self.div_selector(self.machineroom_input, self.div_select, name=machineroom)
        else:
            self.click_element(*self.machineroom_input)
        if size:
            self.div_selector(self.sector_size_input, name=size)
        else:
            self.click_element(*self.sector_size_input)
        self.input_text(*self.domain_input, domain)
        self.input_text(*self.comment_input, comment)
        if is_save:
            self.wait()
            self.click_element(*self.confirm_button)
        self.click_element(*self.cancel_button)

    # 编辑集群信息
    def edit_clusterinfo(self, clusterid, customer=None, machineroom=None, domain=None, size=None, comment=None, is_save=True):
        # self.click_element(*self.system_setting)
        # self.click_element(*self.cluster_info)
        self.click_navigation_bar("系统设置")
        self.click_navigation_bar("集群信息")
        self.click_element(*self.edit_button)
        self.wait(1)
        mylogger.info(f"输入集群ID：{clusterid}")
        self.input_text(*self.clusterid_input, clusterid)
        # 选择所属客户下拉框
        if customer:
            mylogger.info(f"选择所属客户{customer}")
            self.div_selector(self.client_input, self.div_select, name=customer)
        else:
            self.click_element(*self.client_input)
        if machineroom:
            mylogger.info(f"选择所在机房{machineroom}")
            self.div_selector(self.machineroom_input, self.div_select, name=machineroom)
        else:
            self.click_element(*self.machineroom_input)
        if size:
            mylogger.info(f"选择扇区大小{size}")
            self.div_selector(self.sector_size_input, name=size)
        else:
            self.click_element(*self.sector_size_input)
        mylogger.info(f"输入域名{domain}")
        self.input_text(*self.domain_input, domain)
        mylogger.info(f"输入备注{comment}")
        self.input_text(*self.comment_input, comment)
        if is_save:
            self.wait()
            mylogger.info("点击确定按钮")
            self.click_element(*self.confirm_button)
        else:
            mylogger.info("点击取消按钮")
            self.click_element(*self.cancel_button)

    # 添加集群负责人
    def bind_person_liabel(self,state="one"):
        self.click_element(*self.system_setting)
        self.click_element(*self.cluster_info)
        self.wait(1)
        self.click_element(*self.add_person_liable_button)
        if state == "one":
            self.wait(1)
            self.click_element(*self.checkbox_one)
        else:
            self.wait(1)
            self.click_element(*self.checkbox_all)
        self.wait(1.5)
        self.click_element(*self.confirm_button)





if __name__ == '__main__':
    driver = webdriver.Chrome()
    page = ClusterInfoPage(driver)
    page.div_list()
