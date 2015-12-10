# -*- coding: utf-8 -*-
from appium import webdriver
import os
import sys
import time
from common.py_common_keyword.CommonFunctions import CommonFunctions


class hoursSearch48:
    def __init__(self):
        self.com = CommonFunctions()

    def clickKeyword(self):
        global keyword

        button = self.com.wait_for_element('com.tclmarket:id/actionbar_search')
        button.click()
        time.sleep(5)

        try:
            button = self.com.wait_for_element('com.tclmarket:id/loading_error_info')
            if button.text == u'加载失败，请检查您的网络连接':
                return False

            return True
        except:
            buttons = self.com.wait_for_elements(value='android.widget.TextView')
            for number in range(len(buttons)):
                if buttons[number].text == u'48小时热门搜索':
                    keyword = buttons[number + 1].text
                    print 'keyword is %s' % keyword
                    time.sleep(5)
                    buttons[number + 1].click()
                    time.sleep(5)
                    return True

    def searchresultValidation(self):
        buttons = self.com.driver.find_elements_by_id('com.tclmarket:id/name')
        for i in buttons:
            app = i.text
            if keyword in app:
                print 'app is %s' % app
                return True
            else:
                print 'error happened on searchresultValidation'
                return False

    def loadPage(self):
        newapp_list = ''
        while True:
            self.searchresultValidation()
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
                print 'loadpage error'
                print '%s:%s' % (Exception.message, e)
                return False

    def run_hoursSearch48(self):
        return self.com.run_test_case(lambda: self.com.launch_app(),
                                      lambda: self.clickKeyword(),
                                      lambda: self.loadPage())

if __name__ == '__main__':
    print hoursSearch48().run_hoursSearch48()
