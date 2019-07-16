#!/user/bin/env python3
# -*- coding: utf-8 -*-
#editor whp

import ddt,unittest,functools,sys
import inspect
def get_current_function_name():
    return inspect.stack()[1][3]
# def idata(iterable):
#     """
#     Method decorator to add to your test methods.
#
#     Should be added to methods of instances of ``unittest.TestCase``.
#
#     """
#     DATA_ATTR="aa"
#     def wrapper(func):
#         setattr(func, DATA_ATTR, iterable)
#         return func
#     return wrapper

@ddt.ddt
class Ddt_Unitest_Case01(unittest.TestCase):
    # def __init__(self, methodName='runTest', param=None):
    #     super(Ddt_Unitest_Case, self).__init__(methodName)
    #     self.param = param
    def setUp(self):
        print("前置条件")
    def tearDown(self):
        print("后置输出")

    @ddt.data(
        [1,2],
        [3,4],
        [5,6]
    )
    @ddt.unpack
    def test_add(self,a,b):
        # print("%s.%s invoked" % (self.__class__.__name__, get_current_function_name()))
        print(a+b)
        # return a+b

if __name__ == '__main__':
    suite=unittest.TestSuite()
    s=Ddt_Unitest_Case01()
    print(dir(s))
    # func=getattr(s,"test_add")
    # func()
    # s.testadd(1,2)
    suite.addTest(Ddt_Unitest_Case01("test_add_1__1__2_"))
    unittest.TextTestRunner().run(suite)
    # unittest.main()
