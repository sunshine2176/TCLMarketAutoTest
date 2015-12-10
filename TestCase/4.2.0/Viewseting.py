# -*- coding: utf-8 -*-
# AS4-1140:查看设置
# update by sunlei on 2015-12-7
# 更新进入排行和分类页方法  
import sys
import time
from selenium.webdriver.common.by import By
from common.py_common_keyword.CommonFunctions import CommonFunctions


# noinspection PyBroadException
class Viewseting:
    comFn = CommonFunctions()

    def __init__(self):
        self.title = []


    def get_object(self):
        time.sleep(20)
        try:
            self.title = self.comFn.driver.find_elements_by_class_name(r'android.widget.TextView')
            print u'获取元素对象成功'
            return True
        except:
            print u'获取元素对象失败'
            s = sys.exc_info()
            print 'Error %s happend on lineon %d' % (s[1],s[2].tb_lineno)
            return False

    def rank_page(self):
        try:
            for i in self.title:
                if i.text == u'排行':
                    i.click()
                    print u'成功进入排行页面'
                    return True
            return False
        except:
            print u'进入排行页面失败'
            return False

    def classify_page(self):
        time.sleep(5)
        try:
            for i in self.title:
                if i.text == u'分类':
                    i.click()
                    print u'成功进入分类页面'
                    return True
            return False
        except:
            print u'进入分类页面失败'
            s = sys.exc_info()
            print 'Error %s happend on lineon %d' % (s[1],s[2].tb_lineno)
            return False

    def launch_menu(self):
        time.sleep(2)
        try:
            network_error = self.comFn.wait_for_element(value=r'com.tclmarket:id/loading_error_info')
            if network_error.text == u'加载失败请检查您的网络连接...':
                print '加载失败请检查您的网络连接...'
                return False
        except:
            try:
                # self.comFn.driver.execute_script("mobile: keyevent",{ "keycode": 82 })
                self.comFn.driver.press_keycode(82)
                time.sleep(2)
                print u'启动menu成功'
                return True
            except:
                print u'启动menu失败'
                return False

    def quit_menu(self):
        time.sleep(2)
        try:
            # self.comFn.driver.press_keycode(4)
            self.comFn.driver.swipe(500, 200, 500, 300, 0.7)
            time.sleep(2)
            print u'退出menu成功'
            return True
        except:
            print u'退出menu失败'
            return False

    def seting_page(self):
        time.sleep(2)
        try:
            menu = self.comFn.wait_for_elements(value=r'com.tclmarket:id/menu_item_tv', by=By.ID)
            menu[1].click()
            time.sleep(2)
        except:
            print u'点击设置页面失败'
            s = sys.exc_info()
            print 'Error %s happend on lineon %d' % (s[1],s[2].tb_lineno)
            return False

        try:
            if self.comFn.wait_for_element(value=r'com.tclmarket:id/home_title').text == u'设置':
                print u'成功跳转到设置界面'
                return True
            else:
                print u'跳转到设置界面失败'
                return False
        except:
            print u'跳转到设置界面失败'
            return False

    def run_test(self):
        return self.comFn.run_test_case(lambda: self.comFn.launch_app(),
                                 lambda: self.get_object(),
                                 lambda: self.launch_menu(),
                                 lambda: self.quit_menu(),
                                 lambda: self.rank_page(),
                                 lambda: self.launch_menu(),
                                 lambda: self.quit_menu(),
                                 lambda: self.classify_page(),
                                 lambda: self.launch_menu(),
                                 lambda: self.seting_page()
                                 )


if __name__ == '__main__':
    test = Viewseting()
    test.run_test()
