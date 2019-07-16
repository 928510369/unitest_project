#!/user/bin/env python3
# -*- coding: utf-8 -*-
#editor whp
from PIL import Image

from selenium_project.selenium_unitest.util.ShowapiRequest import ShowapiRequest
from selenium_project.selenium_unitest.util.find_elememt import FindElement
import time

class GetCode(object):
    def __init__(self,driver):
        self.driver=driver
        self.Find_element=FindElement(self.driver)
    def get_check_img(self, filename):

        self.driver.save_screenshot(filename)
        img_ele = self.Find_element.get_element("user_code_img")
        left = img_ele.location["x"]
        top = img_ele.location["y"]
        width = img_ele.size["width"]
        height = img_ele.size["height"]
        right = left + width
        bottom = top + height
        im = Image.open(filename)
        img = im.crop((left, top, right, bottom))
        img.save(filename)
        time.sleep(2)
        return self
    #获取验证数字信息
    def get_check_code(self,file_name):
        r = ShowapiRequest("http://route.showapi.com/184-1", "99319", "05eee32b57f14ca693f0e88252b6a2c0")
        r.addBodyPara("image", "")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_name)  # 文件上传时设置
        res = r.post()
        # print(res.json())
        code = res.json()["showapi_res_body"]["Result"]  # 返回信息
        return code