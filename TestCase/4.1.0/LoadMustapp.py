# -*- coding: utf-8 -*-
from common.py_common_keyword.CommonFunctions import CommonFunctions
from common.py_common_keyword.CommonFunctions_wll import CommonFunctions_wll


class LoadMustapp:
    def __init__(self):
        self.com = CommonFunctions_wll()

    def Load_Must_app(self):
        return self.com.run_test_case(lambda: self.com.launch_app(),
                                      lambda: self.com.Launch_LabelPage(u'必备'),
                                      lambda: self.com.swipe_page_to_end())


if __name__ == '__main__':
    test = LoadMustapp()
    print test.Load_Must_app()
