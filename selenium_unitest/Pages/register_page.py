#!/user/bin/env python3
# -*- coding: utf-8 -*-
#editor whp
from selenium_project.selenium_unitest.util.find_elememt import FindElement


class Register_Page(object):
    def __init__(self,driver):
        self.__F=FindElement(driver)
    def get_user_email(self):

        return self.__F.get_element("user_email")
    def get_user_username(self):
        return self.__F.get_element("user_nickname")
    def get_user_password(self):
        return self.__F.get_element("user_password")
    def get_user_code(self):
        return self.__F.get_element("user_captcha")
    def get_register_btn(self):
        return self.__F.get_element("user_register")
    def get_eamil_error(self):
        return self.__F.get_element("user_email_error")
    def get_nickname_error(self):
        return self.__F.get_element("user_nickname_error")
    def get_password_error(self):
        return self.__F.get_element("user_password_error")
    def get_code_error(self):
        return self.__F.get_element("user_code_error")
