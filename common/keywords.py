import datetime
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.handle_common import get_index
from utils.read_data import readData
from common.my_logger import mylogger


# 初始化浏览器，若传入的浏览器驱动存在，则启动对应的浏览器，否则默认启动谷歌浏览器

# def init_driver(driver_type):
#     try:
#         driver = getattr(webdriver, driver_type)()
#         return driver
#     except Exception as e:
#         print("输入的浏览器驱动不可用，正在为您启动Google浏览器", e)
#         driver = webdriver.Chrome()
#         return driver


class KeyWords():

    def __init__(self, driver):
        self.driver = driver
        self.wait_element = WebDriverWait(self.driver, 10)
        # self.driver.get("https://opstest.arsyun.com")
        # self.driver.implicitly_wait(10)
        # self.driver.maximize_window()



    # 等待元素出现
    def __wait_until(self, locator_type, location, many=False):
        mylogger.info("开始等待元素出现--->>")
        if many:
            try:
                element = self.wait_element.until(EC.visibility_of_any_elements_located((locator_type, location)))
                mylogger.info("-----元素已出现-----")
                return element
            except Exception as e:
                mylogger.error("-----等待时间内，元素未出现-----")
                raise e
        else:
            try:
                element = self.wait_element.until(EC.visibility_of_element_located((locator_type, location)))
                mylogger.info("-----元素已出现-----")
                return element
            except Exception as e:
                mylogger.error("-----等待时间内，元素未出现-----")
                raise e

    def locator(self, locator_type, location):
        """
        定位元素
        :param locator_type: 元素定位方式
        :param location: 定位信息
        :return: 返回元素对象
        """
        mylogger.info("元素定位开始--->>")
        mylogger.info("定位方式：{0},定位信息：{1}".format(locator_type, location))
        try:
            if locator_type.upper() == "ID":
                element = self.__wait_until(By.ID, location)
                mylogger.info("-----元素定位成功-----")
                return element
            elif locator_type.upper() == "NAME":
                element = self.__wait_until(By.NAME, location)
                mylogger.info("-----元素定位成功-----")
                return element
            elif locator_type.upper() == "CLASS_NAME":
                element = self.__wait_until(By.CLASS_NAME, location)
                mylogger.info("-----元素定位成功-----")
                return element
            elif locator_type.upper() == "TAG_NAME":
                element = self.__wait_until(By.TAG_NAME, location)
                mylogger.info("-----元素定位成功-----")
                return element
            elif locator_type.upper() == "LINK_TEXT":
                element = self.__wait_until(By.LINK_TEXT, location)
                mylogger.info("-----元素定位成功-----")
                return element
            elif locator_type.upper() == "PARTIAL_LINK_TEXT":
                element = self.__wait_until(By.PARTIAL_LINK_TEXT, location)
                mylogger.info("-----元素定位成功-----")
                return element
            elif locator_type.upper() == "XPATH":
                element = self.__wait_until(By.XPATH, location)
                mylogger.info("-----元素定位成功-----")
                return element
            elif locator_type.upper() == "CSS_SELECTOR":
                element = self.__wait_until(By.CSS_SELECTOR, location)
                mylogger.info("-----元素定位成功-----")
                return element
        except Exception as e:
            mylogger.exception("-----元素定位失败-----")
            raise e

    def locators(self, locator_type, location):
        mylogger.info("多元素定位开始--->>")
        mylogger.info("定位方式：{0},定位信息：{1}".format(locator_type, location))
        try:
            if locator_type.upper() == "ID":
                elements = self.driver.find_elements(By.ID, location)
                mylogger.info("-----多元素定位成功-----")
                return elements
            elif locator_type.upper() == "NAME":
                elements = self.driver.find_elements(By.NAME, location)
                mylogger.info("-----多元素定位成功-----")
                return elements
            elif locator_type.upper() == "CLASS_NAME":
                elements = self.driver.find_elements(By.CLASS_NAME, location)
                mylogger.info("-----多元素定位成功-----")
                return elements
            elif locator_type.upper() == "TAG_NAME":
                elements = self.driver.find_elements(By.TAG_NAME, location)
                mylogger.info("-----多元素定位成功-----")
                return elements
            elif locator_type.upper() == "LINK_TEXT":
                elements = self.driver.find_elements(By.LINK_TEXT, location)
                mylogger.info("-----多元素定位成功-----")
                return elements
            elif locator_type.upper() == "PARTIAL_LINK_TEXT":
                elements = self.driver.find_elements(By.PARTIAL_LINK_TEXT, location)
                mylogger.info("-----多元素定位成功-----")
                return elements
            elif locator_type.upper() == "XPATH":
                elements = self.driver.find_elements(By.XPATH, location)
                mylogger.info("-----多元素定位成功-----")
                return elements
            elif locator_type.upper() == "CSS_SELECTOR" or locator_type.upper() == "CSS":
                elements = self.driver.find_elements(By.CSS_SELECTOR, location)
                mylogger.info("-----多元素定位成功-----")
                return elements
        except Exception as e:
            mylogger.exception("-----多元素定位失败-----")
            raise e

    # 点击元素: click_element
    def click_element(self, locator_type, location):
        mylogger.info("开始点击元素--->>")
        self.locator(locator_type, location).click()
        mylogger.info("-----元素点击成功-----")

    def click_elements(self, locator_type, location, list_number=1):
        mylogger.info("点击多元素开始--->>")
        elements = self.locators(locator_type, location)
        mylogger.info("点击第{}个元素:".format(list_number + 1))
        elements[list_number].click()
        mylogger.info("-----元素点击成功-----")

    def double_click(self, element):
     ActionChains(self.driver).double_click(element).perform()

    # 清除输入框
    def clear(self, locator_type, location):
        mylogger.info("开始清除输入框内容--->>")
        try:
            self.locator(locator_type, location).clear()
            mylogger.info("-----输入框清除成功-----")
        except Exception as e:
            mylogger.error("-----清除输入框失败-----")
            raise e

    # 当clear()方法无法清空输入框内容时:
    def force_clear(self, locator_type, location):
        mylogger.info("开始强制清除输入框内容--->>")
        try:
            element = self.locator(locator_type, location)
            element.send_keys(Keys.CONTROL, 'a')
            element.send_keys(Keys.DELETE)
            mylogger.info("-----输入框清除成功-----")
        except Exception as e:
            mylogger.error("-----清除输入框失败-----")
            raise e

    def input_text(self, locator_type=None, location=None, content=None, text=None, type="input"):
        mylogger.info("文本框开始输入文本--->>")
        try:
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
            mylogger.info("-----文本输入成功，文本内容为：{}".format(content))
        except Exception as e:
            mylogger.info("-----文本输入失败-----")
            raise e
        finally:
            self.wait(0.5)

    def move(self, locator_type, location):
        mylogger.info("移动鼠标到指定元素开始--->>")
        try:
            el = self.locator(locator_type, location)
            ActionChains(self.driver).move_to_element(el).perform()
            mylogger.info("-----移动鼠标到指定元素成功-----")
        except Exception as e:
            mylogger.error("-----移动鼠标到指定元素失败-----")
            raise e

    # 获取元素的文本
    def get_text(self, location, locator_type="xpath"):
        mylogger.info("获取元素文本开始--->>")
        try:
            text = self.locator(locator_type, location).get_attribute("textContent")
            mylogger.info("-----获取元素文本属性值成功，文本内容：{}".format(text))
            return text
        except Exception as e:
            mylogger.error("-----获取元素文本属性值失败-----")
            raise e

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
            " 机房信息": 12,
            "集群信息": 13,
            " 客户信息": 14,
            "用户管理": 15,
            "用户": 16,
            "角色": 17,
            "安全策略": 18,
            "审批流": 19
        }
        main_menu = ('css', '.ant-menu-title-content')
        for key in main_menu_navigation_bar:
            if key == name:
                mylogger.info(f"点击导航栏：{name}")
                self.wait(0.5)
                self.click_elements(*main_menu, list_number=main_menu_navigation_bar[name])

    def div_selector(self, input_path, div_select=None, number=0, name=None, which_index=1):
        """
        div下拉框处理
        :param input_path: 下拉输入框定位信息，('xpath', '定位信息')
        :param div_select:  下拉选择项信息，('xpath', '定位信息')
        :param number:  默认点击选择第一个，从0开始
        :return:
        """
        mylogger.info("开始处理div下拉选择框--->>")
        self.click_element(*input_path)
        self.wait(0.5)
        name_list = []
        if not div_select:
            div_select = ("css", "div.ant-select-item-option-content")
        # 获取选项中所有名称列表
        elements = self.locators(*div_select)
        for el in elements:
            name_list.append(el.get_attribute('textContent'))
        if name:
            index = get_index(name_list, name, which_index)
            mylogger.info(index)
            self.click_elements(*div_select, list_number=index)
        else:
            self.click_elements(*div_select, list_number=number)
        mylogger.info(name_list)
        return name_list

    def click_span_button(self, text, type="button"):
        if type == "span":
            self.xpath = f"//span[text()=\'{text}\']"
        elif type == "button":
            self.xpath = f"//span[text()=\'{text}\']/.."
        elif type == "alert":
            if text == "确 定":
                self.xpath = f"//div[@class='ant-modal-confirm-btns']/button[2]"
            else:
                self.xpath = f"//div[@class='ant-modal-confirm-btns']/button[1]"
        mylogger.info(f"点击按钮为：{text} 按钮--->>")
        self.click_element(By.XPATH, self.xpath)

    # 打开浏览器
    def open_browser(self, url):
        mylogger.info("打开浏览器")
        self.driver.get(url)

    # 设置等待时间
    def wait(self, second=1):
        mylogger.info("开始等待{}秒".format(second))
        time.sleep(second)

    # 关闭浏览器
    def close_browser(self):
        mylogger.info("关闭浏览器")
        self.driver.quit()

    def get_verifycode(self, phone, type="login"):
        url = "https://opstest.arsyun.com/api/v5/public/sms/get"
        if type == "login":
            mylogger.info(f"获取{type}验证码")
            self.data = {
                "phone": f"{phone}",
                "sms_type": "login"
            }
        else:
            mylogger.info(f"获取{type}验证码")
            self.data = {
                "phone": f"{phone}",
                "sms_type": f"{type}"
            }
        res = requests.post(url, json=self.data)
        verify_code = res.json()['data']['sms_code']
        mylogger.info(f"成功获取验证码：{verify_code}")
        readData().write_config("verify_code", "code", value=verify_code)
        return verify_code


if __name__ == '__main__':
    url = "https://www.baidu.com"
    driver = webdriver.Chrome()
    kd = KeyWords(driver)
