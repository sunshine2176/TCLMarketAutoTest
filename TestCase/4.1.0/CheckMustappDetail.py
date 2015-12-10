# -*- coding:utf-8 -*-
from common.py_common_keyword.CommonFunctions import CommonFunctions
from common.py_common_keyword.CommonFunctions_wll import CommonFunctions_wll


class CheckMustappDetail:
    def __init__(self):
        self.com = CommonFunctions_wll()

    def Check_Mustapp_Detail(self):
        return self.com.run_test_case(lambda: self.com.launch_app(),
                                      lambda: self.com.Launch_LabelPage(u'必备'),
                                      lambda: self.com.Check_App_Detail()
                                      )


if __name__ == '__main__':
    test = CheckMustappDetail()
    test.Check_Mustapp_Detail()
