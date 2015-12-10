# -*- coding: utf-8 -*-
import time
from common.py_common_keyword.CommonFunctions import CommonFunctions


class loadApp:
    def __init__(self):
        self.com = CommonFunctions()

    def loadApp(self):
        newapp_list = ''
        while True:
            try:
                app_list = []
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
            except Exception, e:
                print 'you load all app on the page error'
                print '%s:%s' % (e.message, e)
                return False

    def run_loadApp(self):
        return self.com.run_test_case(lambda: self.com.launch_app(),
                                      lambda: self.loadApp())


if __name__ == '__main__':
    print loadApp().run_loadApp()
