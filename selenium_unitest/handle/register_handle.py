#!/user/bin/env python3
# -*- coding: utf-8 -*-
#editor whp
from selenium_project.selenium_unitest.Pages.register_page import Register_Page
from selenium_project.selenium_unitest.util.get_code import GetCode


class Register_Handle(object):
    def __init__(self,driver):
        self.driver=driver
        self.register_p=Register_Page(self.driver)

    def send_user_email(self,email):
        self.register_p.get_user_email().send_keys(email)
        #.send_keys(email)
    def send_user_username(self,usertname):
        self.register_p.get_user_username().send_keys(usertname)

    def send_user_password(self,password):
        self.register_p.get_user_password().send_keys(password)

    def send_user_code(self,filename):
        code_get=GetCode(self.driver)
        code_text=code_get.get_check_img(filename).get_check_code(filename)
        self.register_p.get_user_code().send_keys(code_text)

    def click_register_btn(self):
        self.register_p.get_register_btn().click()

    # def user_send(self):
    #     pass
    def get_user_text(self,key,str):
        try:
            if key=="email_error":
                error_text_ele=self.register_p.get_eamil_error()
                text =self.register_p.get_eamil_error().text
            elif key=="username_error":
                text =self.register_p.get_nickname_error().text

            elif key=="password_error":
                text =self.register_p.get_password_error().text

            else:
                text=self.register_p.get_code_error().text
        except Exception:
            text=None
        return text

    def get_registerbtn_text(self):
        return self.register_p.get_register_btn()