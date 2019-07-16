#!/user/bin/env python3
# -*- coding: utf-8 -*-
#editor whp
from selenium_project.selenium_unitest.handle.register_handle import Register_Handle


class Business_Register(object):
    def __init__(self,driver):
        self.register_h=Register_Handle(driver)
    def send_base(self,email,username,password,file_name):
        self.register_h.send_user_email(email)
        self.register_h.send_user_username(username)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(file_name)
        self.register_h.click_register_btn()
    def Panduan_register_success(self):
        if self.register_h.get_registerbtn_text()==None:
            return True
        else:
            return False
    def all_ddt_register(self,email, username, password, file_name,assert_ele,assert_text):
        self.send_base(email, username, password, file_name)

        if self.register_h.get_user_text(assert_ele, assert_text) == None:
            print("成功")
            return True
        else:
            return False


    def register_success(self,email,username,password,file_name):
        self.send_base(email,username,password,file_name)
        if self.Panduan_register_success():
            print("登录成功")
            return False
        else:
            print("登录失败")
            return True
    def register_email_error(self,email,username,password,file_name):
        self.send_base(email,username,password,file_name)
        if self.register_h.get_user_text("email_error","请输入有效的电子邮件地址")==None:
            print("邮箱注册成功")
            return True
        else:
            return False
    def register_username_error(self,email,username,password,file_name):
        self.send_base(email,username,password,file_name)
        if self.register_h.get_user_text("username_error","字符长度必须大于等于4，一个中文字算2个字符")==None:
            print("用户名注册成功")
            return True
        else:
            return False
    def register_password_error(self,email,username,password,file_name):
        self.send_base(email,username,password,file_name)
        if self.register_h.get_user_text("password_error","最少需要输入 5 个字符")==None:
            print("密码注册成功")
            return True
        else:
            return False
    def register_code_error(self,email,username,password,file_name):
        self.send_base(email,username,password,file_name)
        if self.register_h.get_user_text("code_error","验证码错误")==None:
            print("验证码注册成功")
            return True
        else:
            return False

