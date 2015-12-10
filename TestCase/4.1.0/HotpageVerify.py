# -*- coding:utf-8 -*-
from common.py_common_keyword.CommonFunctions import CommonFunctions
import time
import sys


class HotpageVerify:
    def __init__(self):
        self.com = CommonFunctions()

    def loadHotapps(self):
        try:
            # frame = self.com.driver.find_element_by_id('com.tclmarket:id/remark_layout')
            # buttons = frame.find_elements_by_class_name('android.widget.RelativeLayout')
            # for button in buttons:
            #     b = button.find_element_by_class_name('android.widget.TextView')
            #     if b.text == u'飙升':
            #         b.click()
            #         time.sleep(5)
            #         break
            # return True
            hot_button = self.com.wait_for_element(value='com.tclmarket:id/remark_text1', element_text=u'最热')
            if hot_button:
                hot_button.click()
                return True
            return False


        except:
            print 'No hot labels'
            s = sys.exc_info()
            print 'Error "%s" happend on line %d' % (s[1], s[2].tb_lineno)
            return False

    def hotpageVerify(self):
        time.sleep(2)
        hot_title = self.com.wait_for_element(value='com.tclmarket:id/home_title', element_text=u'最热')
        if hot_title:
            apps = self.com.driver.find_elements_by_id('com.tclmarket:id/name')
            for app in apps:
                if app.text != '':
                    print 'hotpage display normally'
                    return True
                else:
                    print 'There is no app in hotpage.'

        return False

    def run_hotpageVerify(self):
        return self.com.run_test_case(lambda: self.com.launch_app(),
                                      lambda: self.loadHotapps(),
                                      lambda: self.hotpageVerify())
if __name__ == '__main__':
    print HotpageVerify().run_hotpageVerify()
