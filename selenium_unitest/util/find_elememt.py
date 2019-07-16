#!/user/bin/env python3
# -*- coding: utf-8 -*-
#editor whp
from selenium_project.selenium_unitest.util.read_ini import ReadIni


class FindElement:
    def __init__(self,driver):
        self.driver=driver
        self.cf=ReadIni()
    def get_element(self,key):
        try:
            by=str(self.cf.get_value(key).split(">")[0])
            value=str(self.cf.get_value(key).split (">")[1])
        except Exception as e:
            print("无该属性")
            return False
        # print(by,value)
        try:
            if by=="id":
                return self.driver.find_element_by_id(value)
            elif by=="name":
                return self.driver.find_element_by_name(value)
            elif by=="xpath":
                return self.driver.find_element_by_xpath(value)
            else:
                print("请以id,name,xpath来书写配置文件")
                return False
        except Exception:
            print("%s元素定位出错"%(value))
            return None