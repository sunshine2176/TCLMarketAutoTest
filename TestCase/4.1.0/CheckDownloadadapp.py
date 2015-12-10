# -*- coding=utf-8 -*-
from common.py_common_keyword.CommonFunctions_wll import CommonFunctions_wll


class CheckDownloadadapp:

    def __init__(self):
        self.com = CommonFunctions_wll()

    def Check_Download_ad_app(self):
        return self.com.run_test_case(lambda: self.com.launch_app(),
                                      lambda: self.com.Check_ad_Page(),
                                      lambda: self.com.Check_App_Status(),
                                      lambda: self.com.Check_Downloading(),
                                      lambda: self.com.Check_Installing())


if __name__ == '__main__':
    test = CheckDownloadadapp()
    print test.Check_Download_ad_app()
