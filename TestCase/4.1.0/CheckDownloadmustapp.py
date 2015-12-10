# -*- coding=utf-8 -*-
import sys
from common.py_common_keyword.CommonFunctions import CommonFunctions
from common.py_common_keyword.CommonFunctions_wll import CommonFunctions_wll


class CheckDownloadmustapp:
    def __init__(self):
        self.com = CommonFunctions_wll()

    def Download_must_app(self):
        return self.com.run_test_case(lambda: self.com.launch_app(),
                                      lambda: self.com.Launch_LabelPage(u"必备"),
                                      lambda: self.com.Check_App_Status(),
                                      lambda: self.com.Check_Downloading(),
                                      lambda: self.com.Check_Installing())


if __name__ == '__main__':
    test = CheckDownloadmustapp()
    test.Download_must_app()
