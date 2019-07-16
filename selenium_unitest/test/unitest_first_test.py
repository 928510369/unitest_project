#!/user/bin/env python3
# -*- coding: utf-8 -*-
#editor whp
import unittest
class FirstTestCase01(unittest.TestCase):

    def setUp(self):
        print("前置条件")
    def tearDown(self):
        print("后置输出")
    def test_01(self):
        print("测试1")
    # @unittest.skip("不执行")
    def test_02(self):
        print("测试2")

if __name__=="__main__":
    #unittest.main()#执行所有case
    suite= unittest.TestSuite()
    suite.addTest(FirstTestCase01('test_02'))
    suite.addTest(FirstTestCase01('test_01'))
    unittest.TextTestRunner().run(suite)