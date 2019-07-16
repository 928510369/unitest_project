#!/user/bin/env python3
# -*- coding: utf-8 -*-
#editor whp

import random
import time

from PIL import Image
from selenium import webdriver
import datetime
from selenium.webdriver.support import expected_conditions as Ec
from selenium_project.primary_test import ShowapiRequest
from selenium_project.selenium3py3_tests.find_elememt import FindElement

driver=webdriver.Chrome()
def init__driver(url):
    driver.get(url)
    time.sleep(2)
    driver.maximize_window()

def find_element(id):
    # driver.find_element_by_xpath()
    return driver.find_element_by_id(id)

def get_random_str(n):
    str="".join(random.sample("abcdefghi123456789",n))
    return str
def get_check_img(fi,pic_name):
    all_pic_name=r"E:\python\projects\pythonpractice\selenium_project\imgs\%s.png"%(pic_name)
    driver.save_screenshot(all_pic_name)
    img_ele=fi.get_element("user_code_img")
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

def get_check_code(path):
    r = ShowapiRequest("http://route.showapi.com/184-1", "99319", "05eee32b57f14ca693f0e88252b6a2c0")
    r.addBodyPara("image", "")
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addFilePara("image", path)  # 文件上传时设置
    res = r.post()
    # print(res.json())
    code=res.json()["showapi_res_body"]["Result"]  # 返回信息
    return code

def main():
    init__driver("http://www.5itest.cn/register")
    if not Ec.title_contains("注册"):
        print("初始化出错")
        return False
    fi = FindElement(driver)
    register_input=fi.get_element("user_email")
    random_str=get_random_str(6)
    register_input.send_keys(random_str+"@163.com")
    user_input=fi.get_element("user_nickname")
    user_input.send_keys(random_str)
    passwd_input=fi.get_element("user_password")
    passwd_input.send_keys("11111111")
    day=datetime.datetime.now().date()
    pic_name=str(day)+"-"+random_str
    # print(pic_name)
    image_addr=get_check_img(fi,pic_name)
    code=get_check_code(image_addr)
    print(code)
    code_input=fi.get_element("user_captcha")
    code_input.send_keys(code)
    submit_btn=fi.get_element("user_register")
    submit_btn.click()

if __name__=="__main__":
    main()

    #测试FindElement类
    # driver.get("http://www.5itest.cn/register")
    # fi=FindElement(driver)
    # ele=fi.find_element("user_email")
    # print(ele)
    # driver.close()