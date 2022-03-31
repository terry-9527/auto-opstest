'''
定义一个关键字类，封装公用的关键字函数：
打开浏览器： open_browser
定位元素: locator
输入内容：input_text
点击元素: click_element
等待时间：wait
退出浏览器： close_browser
清除输入框： clear
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# 初始化浏览器，若传入的浏览器驱动存在，则启动对应的浏览器，否则默认启动谷歌浏览器

# def init_driver(driver_type):
#     try:
#         driver = getattr(webdriver, driver_type)()
#         return driver
#     except Exception as e:
#         print("输入的浏览器驱动不可用，正在为您启动Google浏览器", e)
#         driver = webdriver.Chrome()
#         return driver
from utils.read_data import readData


class KeyWords():

    def __init__(self, driver):
        self.driver = driver
        # self.driver.get("https://opstest.arsyun.com")
        # self.driver.implicitly_wait(10)
        # self.driver.maximize_window()

    def click_navigation_bar(self, name):
        main_menu_navigation_bar = {
            "首页": 0,
            "工作台": 1,
            "集群概览": 2,
            "主机管理": 3,
            "公共算力": 4,
            "故障记录": 5,
            "作业管理": 6,
            "命令执行": 7,
            "任务管理": 8,
            "公共模板": 9,
            "公共脚本": 10,
            "系统设置": 11,
            "机房信息": 12,
            "集群信息": 13,
            "客户信息": 14,
            "用户管理": 15,
            "用户": 16,
            "角色": 17,
            "安全策略": 18,
            "审批流": 19
        }
        main_menu = ('css', '.ant-menu-title-content')
        for key in main_menu_navigation_bar:
            if key == name:
                self.click_elements(*main_menu, list_number=main_menu_navigation_bar[name])

    def div_selector(self, input_path, div_select=None, number=0, name=None):
        """
        div下拉框处理
        :param input_path: 下拉输入框定位信息，('xpath', '定位信息')
        :param div_select:  下拉选择项信息，('xpath', '定位信息')
        :param number:  默认点击选择第一个，从0开始
        :return:
        """
        self.click_element(*input_path)
        name_list = []
        if not div_select:
            div_select = ("css", "div.ant-select-item-option-content")
        elements = self.locators(*div_select)
        # print(elements)
        for el in elements:
            name_list.append(el.get_attribute('textContent'))
        # print(name_list)
        if name:
            self.click_elements(*div_select, list_number=name_list.index(name))
        else:
            self.click_elements(*div_select, list_number=number)
        return name_list

    def click_span_button(self, text):
        xpath = f"//span[text()=\'{text}\']"
        # xpath = f"//span[text()=\'{text}\'/..]"
        self.click_element(By.XPATH, xpath)

    # 打开浏览器
    def open_browser(self, url):
        self.driver.get(url)

    def locator(self, locator_type, location):
        """
        定位元素
        :param locator_type: 元素定位方式
        :param location: 定位信息
        :return: 返回元素对象
        """
        try:
            if locator_type.upper() == "ID":
                element = self.driver.find_element(By.ID, location)
                return element
            elif locator_type.upper() == "NAME":
                element = self.driver.find_element(By.NAME, location)
                return element
            elif locator_type.upper() == "CLASS_NAME":
                element = self.driver.find_element(By.CLASS_NAME, location)
                return element
            elif locator_type.upper() == "TAG_NAME":
                element = self.driver.find_element(By.TAG_NAME, location)
                return element
            elif locator_type.upper() == "LINK_TEXT":
                element = self.driver.find_element(By.LINK_TEXT, location)
                return element
            elif locator_type.upper() == "PARTIAL_LINK_TEXT":
                element = self.driver.find_element(By.PARTIAL_LINK_TEXT, location)
                return element
            elif locator_type.upper() == "XPATH":
                element = self.driver.find_element(By.XPATH, location)
                return element
            elif locator_type.upper() == "CSS_SELECTOR":
                element = self.driver.find_element(By.CSS_SELECTOR, location)
                return element
        except Exception as e:
            # print("定位元素失败,定位方式{0},定位信息{1},失败原因:{2}".format(locator_type, location, e))
            raise e

    def locators(self, locator_type, location):
        try:
            if locator_type.upper() == "ID":
                elements = self.driver.find_elements(By.ID, location)
                return elements
            elif locator_type.upper() == "NAME":
                elements = self.driver.find_elements(By.NAME, location)
                return elements
            elif locator_type.upper() == "CLASS_NAME":
                elements = self.driver.find_elements(By.CLASS_NAME, location)
                return elements
            elif locator_type.upper() == "TAG_NAME":
                elements = self.driver.find_elements(By.TAG_NAME, location)
                return elements
            elif locator_type.upper() == "LINK_TEXT":
                elements = self.driver.find_elements(By.LINK_TEXT, location)
                return elements
            elif locator_type.upper() == "PARTIAL_LINK_TEXT":
                elements = self.driver.find_elements(By.PARTIAL_LINK_TEXT, location)
                return elements
            elif locator_type.upper() == "XPATH":
                elements = self.driver.find_elements(By.XPATH, location)
                return elements
            elif locator_type.upper() == "CSS_SELECTOR" or locator_type.upper() == "CSS":
                elements = self.driver.find_elements(By.CSS_SELECTOR, location)
                return elements
        except Exception as e:
            # print("定位元素失败,定位方式{0},定位信息{1},失败原因:{2}".format(locator_type, location, e))
            raise e
    # 输入内容：input_text
    def input_text(self, locator_type=None, location=None, content=None, text=None, type="input"):
        # 处理普通的输入框
        if not text:
            self.clear(locator_type, location)
            self.locator(locator_type, location).send_keys(content)
        # 处理有文字标题说明的input输入框
        elif type == "input":
            xpath = f"//label[@title=\'{text}\']/../..//input"
            self.clear(By.XPATH, xpath)
            self.locator(By.XPATH, xpath).send_keys(content)
        # 处理属性是textarea文本输入框
        elif type == "textarea":
            xpath = f"//label[@title=\'{text}\']/../..//textarea"
            self.clear(By.XPATH, xpath)
            self.locator(By.XPATH, xpath).send_keys(content)
        # 处理输入中有占位文字的
        elif type == "placeholder":
            xpath = f"//input[@placeholder='{text}']"
            # self.clear(By.XPATH, xpath)
            self.locator(By.XPATH, xpath).send_keys(content)

    def click_delete_btn(self, locator_type, location, times=1):
        for i in range(times):
            self.locator(locator_type, location).send_keys(Keys.DELETE)

    # 清除输入框
    def clear(self, locator_type, location):
        self.locator(locator_type, location).clear()

    # 当clear()方法无法清空输入框内容时:
    def force_clear(self, locator_type, location):
        element = self.locator(locator_type, location)
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.DELETE)

    # 点击元素: click_element
    def click_element(self, locator_type, location):
        self.locator(locator_type, location).click()

    def click_elements(self, locator_type, location, list_number=1):
        self.locators(locator_type, location)[list_number].click()

    def move(self, locator_type, location):
        el = self.locator(locator_type, location)
        ActionChains(self.driver).move_to_element(el).perform()

    # 获取元素的文本
    def get_text(self, locator_type, location):
        text = self.locator(locator_type, location)
        return text

    def login(self, phone, password, verifycode=None):
        # 输入手机号、密码、点击获取验证码、输入手机验证码、点击登陆
        self.input_text('xpath', "//input[@placeholder='请输入手机号']", phone)
        self.input_text('xpath', "//input[@placeholder='请输入密码']", password)
        # self.click_element('xpath', "//button[@type='button']")
        # self.input_text('xpath', "//input[@placeholder='请输入验证码']", content=verifycode)
        self.click_element('xpath', "//button[@type='submit']")

    # 设置等待时间
    def wait(self, second=1):
        time.sleep(second)

    # 关闭浏览器
    def close_browser(self):
        self.driver.quit()

    # 断言普通文本text方法
    def text_assert_equal(self, filename, sheetname, case_id, expected_tuple, location=None):
        # //span[text()="编辑集群成功"] 文本默认的定位方式
        if not location:
            try:
                xpath = f"//span[text()=\'{expected_tuple[0]}\']"
                self.actual = self.locator(By.XPATH, xpath).get_attribute('textContent')
            except Exception as e:
                print(f"获取实际结果失败：{e}")
                errmsg = f"获取实际结果失败：{e}"
                readData().write_excel(filename, sheetname, case_id, testresult="FAILED", reason=errmsg)
                return (False, errmsg)
        else:
            try:
                self.actual = self.locator(By.XPATH,location).get_attribute('textContent')
            except Exception as e:
                print(f"获取实际结果失败：{e}")
                errmsg = f"获取实际结果失败：{e}"
                readData().write_excel(filename, sheetname, case_id, testresult="FAILED", reason=errmsg)
                return (False,errmsg)
        if expected_tuple == self.actual:
            print(f"{case_id}用例执行通过")
            readData().write_excel(filename, sheetname, case_id, testresult="PASS")
            return (True,)
        else:
            print(f"{case_id}用例结果对比失败====>>预期结果 != 实际结果 ===>> {expected_tuple} != {self.actual}")
            errmsg = f"结果对比失败：{expected_tuple} != {self.actual}"
            readData().write_excel(filename, sheetname, case_id, testresult="FAILED", reason=errmsg)
            return (False, errmsg)

    def text_assert_many_equal(self, filename, sheetname, case_id, expected_tuple, location):
        """
        多个文本进行断言
        :param filename: Excel表格文件名
        :param sheetname: 执行表的表名称
        :param case_id:    用例的ID
        :param expected_tuple: 预期结果
        :param location: 对应文本的定位方式，必须才用xpath定位方式
        :return:
        """
        reason_list = []
        test_result = "PASS"
        for i in range(len(location)):
            result = self.text_assert_equal(filename, sheetname, case_id, expected_tuple[i], location[i])
            if not result[0]:
                test_result = "FAIL"
                reason_list.append(result[1])
        readData().write_excel(filename, sheetname, case_id, testresult=test_result, reason=str(reason_list))



if __name__ == '__main__':
    url = "https://www.baidu.com"
    driver = webdriver.Chrome()
    kd = KeyWords(driver)
