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


# 初始化浏览器，若传入的浏览器驱动存在，则启动对应的浏览器，否则默认启动谷歌浏览器

def init_driver(driver_type):
    try:
        driver = getattr(webdriver, driver_type)()
        return driver
    except Exception as e:
        print("输入的浏览器驱动不可用，正在为您启动Google浏览器", e)
        driver = webdriver.Chrome()
        return driver


class KeyWords():

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

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
            print("定位元素失败,定位方式{0},定位信息{1},失败原因:{2}".format(locator_type, location, e))

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
            elif locator_type.upper() == "CSS_SELECTOR":
                elements = self.driver.find_elements(By.CSS_SELECTOR, location)
                return elements
        except Exception as e:
            print("定位元素失败,定位方式{0},定位信息{1},失败原因:{2}".format(locator_type, location, e))

    # 输入内容：input_text
    def input_text(self, locator_type, location, content):
        self.clear(locator_type, location)
        self.locator(locator_type, location).send_keys(content)

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

    # 获取元素的文本
    def get_text(self, locator_type, location):
        text = self.locator(locator_type, location)
        return text

    # 设置等待时间
    def wait(self, second):
        time.sleep(second)

    # 关闭浏览器
    def close_browser(self):
        self.driver.quit()


if __name__ == '__main__':
    url = "https://www.baidu.com"
    driver = webdriver.Chrome()
    kd = KeyWords(driver)
    kd.open_browser(url)
    kd.input_text('name', 'wd', '倚天屠龙记')
    kd.click_element('id', 'su')
    kd.wait(2)
    kd.clear('name', 'wd')
    kd.wait(2)
    kd.close_browser()
