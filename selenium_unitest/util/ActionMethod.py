#!/user/bin/env python3
# -*- coding: utf-8 -*-
#editor whp
from time import sleep

from selenium import webdriver

from selenium_project.selenium_unitest.util.find_elememt import FindElement


class ActionMethod(object):
    def __init__(self):
        pass

    # 打开浏览器
    def open_browser(self,name="Chrome"):
        if name=="Chrome":
            self.driver=webdriver.Chrome()
        elif name=="Firefox":
            self.driver=webdriver.Firefox()
        else:
            self.driver=webdriver.Edge()
        self.driver.maximize_window()

    # 输入url
    def get_url(self,url):
        self.driver.get(url)

    # 输入元素
    def send_value(self,key,value):
        element=self.get_element(key)
        element.send_keys(value)

    # 点击元素
    def click_element(self,key):
        element = self.get_element(key)
        element.click()
    # 等待时间
    def sleep_time(self,times):
        times=int(times)
        sleep(times)

    # 定位元素
    def get_element(self,key):
        self.F_ele = FindElement(self.driver)
        element=self.F_ele.get_element(key)
        return element

    def close_browser(self):
        self.driver.close()

    def get_title(self):
        # print(self.driver.title)
        return self.driver.title



