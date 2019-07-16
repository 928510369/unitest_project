#!/user/bin/env python3
# -*- coding: utf-8 -*-
#editor whp

import configparser

class ReadIni(object):
    def __init__(self,path=None,node=None):
        if not path:
            self.path=r"E:\python\projects\pythonpractice\selenium_project\selenium_unitest\config\LocalElements.ini"
        if not node:
            self.node="RegisterElement"
        self.cf=self.load_ini(self.path)
    #加载文件
    def load_ini(self,path):
        cf=configparser.ConfigParser()
        # print(self.path)
        cf.read(path)

        return cf
    #获取信息
    def get_value(self,key):

        return self.cf.get(self.node,key)

