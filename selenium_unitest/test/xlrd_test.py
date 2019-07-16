#!/user/bin/env python3
# -*- coding: utf-8 -*-
#editor whp
import xlrd
class ExcelUtil(object):
    def __init__(self,excel_path=None,index=None):
        if excel_path==None:
            excel_path="E:\python\projects\pythonpractice\selenium_project\selenium_unitest\data\casedata.xlsx"
        if index==None:
            index=0
        self.data=xlrd.open_workbook(excel_path)
        self.table=self.data.sheets()[index]
        self.rows=self.table.nrows
    def get_datas(self):
        result=[]
        for i in range(self.rows):
            result.append(self.table.row_values(i))
        print(result)
    def get_rows(self):
        return self.table.nrows
if __name__ == '__main__':

    ex=ExcelUtil()
    ex.get_datas()
