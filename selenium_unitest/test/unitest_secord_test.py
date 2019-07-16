#!/user/bin/env python3
# -*- coding: utf-8 -*-
#editor whp
import unittest
class SecordTestCase01(unittest.TestCase):

    def setUp(self):
        print("前置条件")
    def tearDown(self):
        print("后置输出")
    def test_001(self):
        print("测试01")
    # @unittest.skip("不执行")
    def test_002(self):
        print("测试02")

if __name__=="__main__":
    #unittest.main()#执行所有case
    suite= unittest.TestSuite()
