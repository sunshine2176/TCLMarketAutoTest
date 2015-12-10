# -*- coding: utf-8 -*-
from appium import webdriver
import time
import sys
from common.py_common_keyword.CommonFunctions import CommonFunctions


class onekey_report:
    def __init__(self):
        self.com = CommonFunctions()

    # 打开应用详情
    def openDetailpage(self):
        global app
        try:
            apps = self.com.driver.find_elements_by_id('com.tclmarket:id/name')
            for app in apps:
                if app.text != '':
                    app.click()
                    time.sleep(8)

                    appname = self.com.wait_for_element('com.tclmarket:id/name')
                    if appname.text == app.text:
                        print 'you have entered appdetailpage'
                        self.com.swipe_screen(percent=0.7)
                        time.sleep(3)
                        return True
                    else:
                        print 'you have entered wrong'
                        return False

        except:
            print 'No app in the page'
            return False

    def onekeyVerify(self):
        try:
            report = self.com.wait_for_element('com.tclmarket:id/one_key_submit')
            report.click()
            report_message = self.com.wait_for_element('com.tclmarket:id/report_message')
            report_items = self.com.driver.find_elements_by_id('com.tclmarket:id/linerlayout_two')
            for item in report_items:
                item.click()
            submit = self.com.wait_for_element('com.tclmarket:id/submit')
            report_message.send_keys(u'测试一件举报')
            submit.click()
            if report:
                print 'you back the detail page'
                return True
            else:
                print 'back  failed'
                return False
        except:
            s = sys.exc_info()
            print 'Error "%s" happend on line %d' % (s[1], s[2].tb_lineno)
            return False

    def run_onekey_report(self):
        return self.com.run_test_case(lambda: self.com.launch_app(),
                                          lambda: self.openDetailpage(),
                                          lambda: self.onekeyVerify())


if __name__ == '__main__':
    print onekey_report().run_onekey_report()
