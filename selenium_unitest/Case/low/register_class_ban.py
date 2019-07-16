#!/user/bin/env python3
# -*- coding: utf-8 -*-
#editor whp
import random
import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as Ec
from selenium_project.primary_test import ShowapiRequest
from selenium_project.selenium3py3_tests.find_elememt import FindElement

class RegisterFunction(object):
    def __init__(self,url):
        self.driver=webdriver.Chrome()
        self.Find_element=FindElement(self.driver)
        self.img_path="E:\python\projects\pythonpractice\selenium_project\imgs"
        self.init_driver(self.driver,url)
    def init_driver(self,driver,url):
        self.driver.get(url)
        time.sleep(2)
        self.driver.maximize_window()
    def find_element(self,key):
        return self.Find_element.get_element(key)
    def element_send_keys(self,key,keys):
        self.find_element(key).send_keys(keys)
    #获取随机数
    def get_random_str(self,n):
        str = "".join(random.sample("abcdefghi123456789", n))
        return str
    #获取验证码图片
    def get_check_img(self, pic_name):
        all_pic_name = r"%s\%s.png" % (self.img_path,pic_name)
        self.driver.save_screenshot(all_pic_name)
        img_ele = self.Find_element.get_element("user_code_img")
        left = img_ele.location["x"]
        top = img_ele.location["y"]
        width = img_ele.size["width"]
        height = img_ele.size["height"]
        right = left + width
        bottom = top + height
        im = Image.open(all_pic_name)
        img = im.crop((left, top, right, bottom))
        img.save(all_pic_name)
        return all_pic_name
    #获取验证数字信息
    def get_check_code(self,path):
        r = ShowapiRequest("http://route.showapi.com/184-1", "99319", "05eee32b57f14ca693f0e88252b6a2c0")
        r.addBodyPara("image", "")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", path)  # 文件上传时设置
        res = r.post()
        # print(res.json())
        code = res.json()["showapi_res_body"]["Result"]  # 返回信息
        return code
    def main(self):
        if not Ec.title_contains("注册"):

            print("初始化出错")
            return False
        random_str=self.get_random_str(6)
        self.element_send_keys("user_email",random_str+"@163.com")
        self.element_send_keys("user_nickname",random_str)
        self.element_send_keys("user_password","11111111")
        all_img_code=self.get_check_img(random_str)
        text=self.get_check_code(all_img_code)
        self.element_send_keys("user_captcha",text)
        register_btn=self.Find_element.get_element("user_register")
        register_btn.click()
if __name__=="__main__":
    regifunc=RegisterFunction("http://www.5itest.cn/register")
    regifunc.main()