from selenium.webdriver.common.keys import Keys

from common.keywords import KeyWords


class ClusterOverviewPage(KeyWords):
    """
    页面元素定位信息
    """

    # 搜索输入框
    search_input = ('xpath', '//main/div[3]//input')
    # 进入集群按钮
    entry_button = ('xpath', '//span[text()="进入集群"]')

    def search_cluster(self,minerid=None,customer=None,liabel=None):
        self.click_navigation_bar("工作台")
        self.click_navigation_bar("集群概览")
        if minerid:
            self.input_text(*self.search_input,minerid)
        if customer:
            self.input_text(*self.search_input,customer)
        if liabel:
            self.input_text(*self.search_input,liabel)
        self.locator(*self.search_input).send_keys(Keys.ENTER)
        self.wait()
        self.click_navigation_bar("工作台")

    def lookup_cluster(self, minerid):
        # //span[contains(text(),"f060975")]/../..//button
        self.click_navigation_bar("工作台")
        self.click_navigation_bar("集群概览")
        xpath = ('xpath', f'//span[contains(text(),"{minerid}")]/../..//button')
        self.click_element(*xpath)
        self.wait(2)