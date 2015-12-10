# -*- coding:utf-8 -*-
from appium import webdriver
import time
import sys
from common.py_common_keyword.CommonFunctions import CommonFunctions


class favoritesApp:
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
                    time.sleep(5)
                    return True
                else:
                    print 'loading recommend app failure'
                    return False
        except:
            print 'No app in the page'
            return False

    # 登录并收藏应用
    def favoriteApp(self):
        try:
            shareicon = self.com.wait_for_element('com.tclmarket:id/left_btn_image')
            appname = self.com.wait_for_element('com.tclmarket:id/name')

            if appname.text == app.text:
                print 'you have entered appdetailpage'
            else:
                print 'you have entered wrong'
                return False

            shareicon.click()
            time.sleep(5)

            input_texts = self.com.driver.find_elements_by_class_name('android.widget.EditText')
            input_texts[0].send_keys(u'liling.wang@tcl.com')
            input_texts[1].send_keys(u'wll82441985')
            button = self.com.driver.find_element_by_class_name('android.widget.Button')
            button.click()
            time.sleep(8)

            shareicon = self.com.wait_for_element('com.tclmarket:id/left_btn_image')
            shareicon.click()
            time.sleep(5)
            back_button = self.com.wait_for_element('com.tclmarket:id/actionbar_up')
            if back_button:
                back_button.click()
                return True
            else:
                return False
        except:
            print 'favoriteApp error'
            return False

    # 验证收藏是否成功
    def checkFavoriteapp(self):
        try:
            tab = self.com.wait_for_element('com.tclmarket:id/tab_indicator')

            buttons = tab.find_elements_by_class_name('android.widget.TextView')

            for b in buttons:
                if u'我的' in b.text:
                    b.click()
                    time.sleep(3)
                    break
            F_button = self.com.wait_for_element('com.tclmarket:id/favorite')
            F_button.click()
            time.sleep(5)

            F_apps = self.com.driver.find_elements_by_id('com.tclmarket:id/name')
            if F_apps[0].text == app.text:
                print 'Successful collection application'
                return True
            else:
                print 'Collect application failure'
                return False
        except:
            print 'checkFavoriteapp error'
            return False

    def run_favoritesApp(self):
        return self.com.run_test_case(lambda: self.com.launch_app(),
                                      lambda: self.openDetailpage(),
                                      lambda: self.favoriteApp(),
                                      lambda: self.checkFavoriteapp())

if __name__ == '__main__':
    print favoritesApp().run_favoritesApp()
