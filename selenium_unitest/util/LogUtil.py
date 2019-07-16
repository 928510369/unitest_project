#!/user/bin/env python3
# -*- coding: utf-8 -*-
#editor whp
import logging
import datetime,os
# log工具类
class LogUtil(object):
    def __init__(self):
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # 控制台流
        # con_handle=logging.StreamHandler()
        # logger.addHandler(con_handle)

        # 文件流


        path_dir_top=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path_dir=os.path.join(path_dir_top,"log","logs")
        current_date=datetime.datetime.now().strftime("%Y-%m-%d")
        file_name=os.path.join(path_dir,current_date)+".log"
        print(file_name)
        self.file_handle=logging.FileHandler(
            filename=file_name,
            mode='a', encoding="utf-8")
        self.file_handle.setLevel(logging.INFO)
        fomatter=logging.Formatter(
            ' %(asctime)s %(module)s --->%(filename)s %(funcName)s ---> 第 %(lineno)d 行 %(levelname)s : %(message)s ')
        self.logger.addHandler(self.file_handle)
        self.file_handle.setFormatter(fomatter)

        # logging.debug("test")
        # 关闭控制台流
        # con_handle.close()
        # 关闭文件流
        # self.file_handle.close()

        # logger.removeHandler(con_handle)
        # self.logger.removeHandler(self.file_handle)
    def get_logger(self):
        return self.logger

    def close_handle(self):
        self.file_handle.close()

        # logger.removeHandler(con_handle)
        self.logger.removeHandler(self.file_handle)
if __name__ == '__main__':
    lu=LogUtil()