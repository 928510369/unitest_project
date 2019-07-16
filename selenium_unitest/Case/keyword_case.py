#!/user/bin/env python3
# -*- coding: utf-8 -*-
#editor whp


import sys,os,ddt
# sys.path.append("../../../")#../../../


sys.path.append(r"E:\python\projects\pythonpractice")#加入所需项目的上一级
from selenium_project.selenium_unitest.util.ActionMethod import ActionMethod
from selenium_project.selenium_unitest.util.excel_util import ExcelUtil

class KeyWordCase(object):
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel=ExcelUtil("E:\python\projects\pythonpractice\selenium_project\selenium_unitest\data\keyword.xls")
        rows=handle_excel.get_rows()

        # 拿到行数
        # 循环行数,去执行每一行的case
        # 是否执行
            # 拿到执行方法
            # 拿到操作元素
            # 拿到输入数据
            # 是否有输入数据
                # 执行方法(操作元素,输入数据)
            #没有数据
        # 执行方法(操作元素）
        for i in range(1,rows):

            # 测试插入失败
            # handle_excel.write_cell_value(i, "pass")
            # continue



            is_run=handle_excel.get_cell_value(i,2)
            if is_run=="yes":
                method=handle_excel.get_cell_value(i,4)#执行方法
                send_value=handle_excel.get_cell_value(i,5)#输入的数据
                handle_value=handle_excel.get_cell_value(i,6)#操作元素
                except_result_method=handle_excel.get_cell_value(i,7)
                except_result=handle_excel.get_cell_value(i,8)
                self.run_method(method,send_value,handle_value)
                if except_result!="":

                    res_list=self.get_except_result_value(except_result)
                    if res_list[0]=="text":
                        result=self.run_method(except_result_method)
                        print("1111111----?",res_list[1],result)
                        if res_list[1] in result:
                            print("1111111----?")
                            handle_excel.write_cell_value(i,"pass")
                        else:
                            handle_excel.write_cell_value(i, "fail")
                    elif res_list[0]=="element":
                        result=self.run_method(except_result_method,res_list[1])
                        if result:
                            handle_excel.write_cell_value(i, "pass")
                        else:
                            handle_excel.write_cell_value(i, "fail")
                    else:
                        print("暂未添加判断")



            else:
                continue
    #获得预期结果
    def get_except_result_value(self,data):
        return data.split("=")

    #运行方法
    def run_method(self,method,send_value="",handle_value=""):

        method_value=getattr(self.action_method,method)
        print(method)
        if send_value!="" and handle_value!="":
            res=method_value(handle_value,send_value)
        elif send_value!="" and handle_value=="":
            res=method_value(send_value)
        elif send_value=="" and handle_value!="":
            res=method_value(handle_value)
        else:
            res=method_value()
        return res
if __name__ == '__main__':
    kc=KeyWordCase()
    kc.run_main()





