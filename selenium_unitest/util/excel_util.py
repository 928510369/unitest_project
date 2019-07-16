#!/user/bin/env python3
# -*- coding: utf-8 -*-
#editor whp
import xlrd
from xlutils.copy import copy


class ExcelUtil(object):
    def __init__(self,excel_path=None,index=None):
        if excel_path==None:
            self.excel_path="E:\python\projects\pythonpractice\selenium_project\selenium_unitest\data\keyword.xls"
        else:
            self.excel_path=excel_path
        if index==None:
            index=0
        self.data=xlrd.open_workbook(self.excel_path)
        self.table=self.data.sheets()[index]

    def get_datas(self):
        result=[]
        rows=self.get_rows()
        if rows:
            for i in range(self.get_rows()):
                result.append(self.table.row_values(i))
            return result
        return None
    def get_rows(self):

        rows=self.table.nrows
        if rows>=1:
            return rows
        return None
    def get_cell_value(self,row,col):
        if row<self.get_rows():
            data=self.table.cell(row,col).value
            return data
        else:
            return None
    def write_cell_value(self,row,value):

        read_value=xlrd.open_workbook(self.excel_path)
        write_data=copy(read_value)
        write_data.get_sheet(0).write(row,9,value)
        write_data.save(self.excel_path)

if __name__ == '__main__':

    ex=ExcelUtil()
    ex.get_datas()
    print(ex.get_cell_value(7,8))
    ex.write_cell_value(1,"test")
