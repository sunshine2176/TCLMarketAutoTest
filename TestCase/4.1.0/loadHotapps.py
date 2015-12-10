# -*- coding:utf-8 -*-
import time
import sys
from common.py_common_keyword.CommonFunctions import CommonFunctions


class loadHotapps:
    def __init__(self):
        self.com = CommonFunctions()

    def loadHotapps(self):
        try:
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

    def loadApps(self):
        newapp_list = ''
        while True:
            try:
                app_list = []
                time.sleep(2)
                buttons = self.com.driver.find_elements_by_id('com.tclmarket:id/name')
                for b in buttons:
                    app = b.text
                    app_list.append(app)

                if app_list[-1] != newapp_list:
                    newapp_list = app_list[-1]
                    print 'loading app successfully'
                    self.com.swipe_screen()
                    time.sleep(10)
                else:
                    print 'you load all app on the page'
                    return True
            except:
                print 'loadApps error'
                s = sys.exc_info()
                print 'Error "%s" happend on line %d' % (s[1], s[2].tb_lineno)
                return False

    def run_loadHotapps(self):
        return self.com.run_test_case(lambda: self.com.launch_app(),
                                      lambda: self.loadHotapps(),
                                      lambda: self.loadApps())
if __name__ == '__main__':
    print loadHotapps().run_loadHotapps()