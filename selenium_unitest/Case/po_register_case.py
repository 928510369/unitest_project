#!/user/bin/env python3
# -*- coding: utf-8 -*-
#editor whp
import unittest

import sys,os
# sys.path.append("../../../")#../../../


sys.path.append(r"E:\python\projects\pythonpractice")#加入所需项目的上一级

from HTMLTestRunner_PY3 import HTMLTestRunner
from selenium_project.selenium_unitest.business.business_register import Business_Register
from selenium_project.selenium_unitest.util.LogUtil import LogUtil
from selenium import webdriver



class Register_function(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("所有case的前置")
        cls.code_file_name=os.path.join(os.path.dirname(os.getcwd())+"/imgs/"+"code.png")
        cls.logger_ut=LogUtil()
        cls.logger=cls.logger_ut.get_logger()


    @classmethod
    def tearDownClass(cls):
        cls.logger_ut.close_handle()
        print("所有case执行的后置")
        # cls.logger.info("aaaa")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.5itest.cn/register")
        self.RegisterB = Business_Register(self.driver)

    def tearDown(self):
        for method_name,error in self._outcome.errors:
            if error:
                case_name=self._testMethodName
                print(error)
                file_path=os.path.join(os.path.dirname(os.getcwd())+"/report/"+case_name+".png")
                print(file_path)
                self.driver.save_screenshot(file_path)
        self.driver.close()

    def test_login_email_error(self):
        email_error=self.RegisterB.register_email_error("a1111.com", "1111", "111111",self.code_file_name)
        self.assertFalse(email_error,"邮箱验证case成功")
    def test_login_username_error(self):
        username_error=self.RegisterB.register_username_error("a1111@163.com","ss","111111",self.code_file_name)
        self.assertFalse(username_error,"用户名验证case成功")

    def test_login_password_error(self):
        password_error=self.RegisterB.register_password_error("a1111@163.com","111111","1111",self.code_file_name)
        self.assertFalse(password_error,"密码验证case成功")

    def test_login_code_error(self):
        code_error=self.RegisterB.register_code_error("a1111@163.com","1111","111111",self.code_file_name)
        self.assertFalse(code_error,"验证码验证case成功")


    def test_login_success(self):
        self.logger.info("aaaa")
        success=self.RegisterB.register_success("a111111@163.com", "b111111", "11111111", self.code_file_name)
        self.assertFalse(success,"注册case失败")


if __name__=="__main__":

    file_path=os.path.join(os.path.dirname(os.getcwd())+"/report/"+"first_case.html")
    print("1----->",file_path)
    # unittest.main()#所有case执行
    f=open(file_path,'wb')
    suite=unittest.TestSuite()
    # suite.addTest(Register_function("test_login_email_error"))

    # suite.addTest(Register_function("test_login_username_error"))
    # suite.addTest(Register_function("test_login_password_error"))
    # suite.addTest(Register_function("test_login_code_error"))
    suite.addTest(Register_function("test_login_success"))
    textrunner=HTMLTestRunner(stream=f,title="This is first report ",description="这是第一次运行报告")
    textrunner.run(suite)
    f.close()
