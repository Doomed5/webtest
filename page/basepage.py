import os
import time

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.handler_log import my_log
from common.handle_path import ERRO_IMAGE_DIR

"""
BasePage:封装的是一个所有的页面的父类，在父类中封装一些页面常用的操作方法
    1、查找元素
    2、点击元素
    3、输入内容
    4、清空输入框
    5、获取元素文本
    6、获取元素属性
    7、等待元素可见
    8、等待元素存在
    9、等待元素可点击
    10、iframe切换
    11、错误截图
"""


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_element(self, loc, desc=None):
        """
        查找元素
        :param loc: 元素定位器
        :param desc: 元素的描述
        :return:
        """
        try:
            ele = self.driver.find_element(*loc)
        except Exception as e:
            my_log.error("查找元素--【{}】--失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("查找元素--【{}】--成功".format(desc))
        return ele

    def click_element(self, loc, desc=None):
        """
        点击元素
        :param loc: 元素定位器
        :param desc: 元素描述
        :return:
        """
        try:
            self.driver.find_element(*loc).click()
        except Exception as e:
            my_log.error("点击元素--【{}】--失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("点击元素--【{}】--成功".format(desc))

    def input_send_keys(self, loc, value, desc=None):
        """
        输入框输入值
        :param loc: 元素定位器
        :param value: 输入值
        :param desc: 元素描述
        :return:
        """
        try:
            self.driver.find_element(*loc).send_keys(value)
        except Exception as e:
            my_log.error("输入框--【{}】--输入元素失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("输入框--【{}】--输入元素成功".format(desc))

    def clear_input(self, loc, desc=None):
        """
        输入框清空
        :param loc: 元素定位器
        :param desc: 元素描述
        :return:
        """

        try:
            self.driver.find_element(*loc).clear()
        except Exception as e:
            my_log.error("输入框--【{}】--清空失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("输入框--【{}】--清空成功".format(desc))

    def get_element_text(self, loc, desc=None):
        """
        获取元素文本
        :param loc: 元素定位器
        :param desc: 元素描述
        :return:
        """
        try:
            res = self.driver.find_element(*loc).text
        except Exception as e:
            my_log.error("获取元素--【{}】--文本失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("获取元素--【{}】--文本成功".format(desc))
        return res

    def get_element_attribute(self, loc, attr, desc=None):
        """

        :param loc: 元素定位器
        :param attr: 元素属性
        :param desc: 元素描述
        :return:
        """
        try:
            res = self.driver.find_element(*loc).get_attribute(attr)
        except Exception as e:
            my_log.error("获取元素--【{}】--属性失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("获取元素--【{}】--属性成功".format(desc))
        return res

    def wait_element_visibility(self, loc, desc=None, timeout=10):
        """
        等待元素可见
        :param loc: 元素定位器
        :param desc: 元素描述
        :param timeout: 超时时间
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout, 0.5).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            my_log.error("等待元素可见--【{}】--失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("等待元素可见--【{}】--成功".format(desc))

    def wait_element_presence(self, loc, desc=None, timeout=10):
        """
        等待元素存在
        :param loc: 元素定位器
        :param desc: 元素描述
        :param timeout: 超时时间
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout, 0.5).until(EC.presence_of_element_located(loc))
        except Exception as e:
            my_log.error("等待元素存在--【{}】--失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("等待元素存在--【{}】--成功".format(desc))

    def wait_element_clickable(self, loc, desc=None, timeout=10):
        """
        等待元素可点击
        :param loc: 元素定位器
        :param desc: 元素描述
        :param timeout: 超时时间
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout, 0.5).until(EC.element_to_be_clickable(loc))
        except Exception as e:
            my_log.error("等待元素可点击--【{}】--失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("等待元素可点击--【{}】--成功".format(desc))

    def switch_to_iframe_loc(self, loc, desc=None):
        """
        通过frame标签的定位表达式进行iframe切换
        :param loc:
        :param desc:
        :return:
        """
        try:
            WebDriverWait(self.driver, 20, 0.5).until(EC.frame_to_be_available_and_switch_to_it(loc))
        except Exception as e:
            my_log.error("等待iframe标签可见并进行切换--【{}】--失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("等待iframe标签可见并进行切换--【{}】--成功".format(desc))

    def switch_to_iframe_name(self, name, desc=None):
        """
        通过iframe的name属性进行切换
        :param name:
        :param desc:
        :return:
        """
        try:
            self.driver.switch_to.frame(name)
        except Exception as e:
            my_log.error("切换iframe--【{}】--失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("切换iframe--【{}】--成功".format(desc))

    def error_save_screenshot(self, desc=None):

        i_date = time.strftime("%Y-%m-%d_%H_%M_%S")
        filename = i_date + desc + '.png'
        filepath = os.path.join(ERRO_IMAGE_DIR, filename)
        try:
            self.driver.save_screenshot(filepath)
        except Exception as e:
            my_log.error("对--【{}】--截图失败".format(desc))
            my_log.exception(e)
            raise e
        else:
            with open(filepath, 'rb') as f:
                content = f.read()
            allure.attach(content, '失败截图', allure.attachment_type.PNG)
            my_log.info("对--【{}】--截图成功".format(desc))
            my_log.info("图片保存为【{}】".format(filepath))
