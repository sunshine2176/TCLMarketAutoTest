# -*- coding=utf-8 -*-
from common.py_common_keyword.CommonFunctions import CommonFunctions
from common.py_common_keyword.CommonFunctions_wll import CommonFunctions_wll


class CheckMustPage:
    def __init__(self):
        self.com = CommonFunctions_wll()

    def Check_Mustpage(self):
        return self.com.run_test_case(lambda: self.com.launch_app(),
                                      lambda: self.com.Launch_LabelPage(u'必备'))


if __name__ == '__main__':
    test = CheckMustPage()
    test.Check_Mustpage()
