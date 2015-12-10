# -*- coding: utf-8 -*-
# AS4-1296:注销账户
import re
import os
import sys
import time
from appium import webdriver
from common.py_common_keyword.common_class import common_class


class check_logout:
    def __init__(self):
        self.con = common_class()

    def check_login(self):
        try:
            self.me = self.con.driver.find_elements_by_id(r'com.tclmarket:id/menu_item_tv')
            if self.me[2].text == u'注销账号':
                print u'我的账户变成注销账号，登录成功'
                return True
            else:
                print u'经检查，登录失败'
                return False
        except:
            print u'检查是否已登录，异常'
            return False

    def logout(self):
        try:
            self.me[2].click()
            time.sleep(2)
            self.con.driver.find_element_by_id(r'com.tclmarket:id/positiveButton').click()
            print u'点击退出登录成功'
            return True
        except:
            print u'点击退出登录失败'
            return False

    def check_logout_2(self):
        try:
            # print self.me[2].text
            if self.me[2].text == u'我的账户':
                print u'注销账号变成我的账户，注销成功'
                return True
            else:
                print u'经检查，注销失败'
                return False
        except:
            print u'检查是否已注销，异常'
            return False

    def checklogout(self):
        return self.con.run_test_case(lambda: self.con.launch_app(),
                                      lambda: self.con.launch_menu(),
                                      lambda: self.con.mycount(),
                                      lambda: self.con.rank_page(),
                                      lambda: self.con.launch_menu(),
                                      lambda: self.check_login(),
                                      lambda: self.con.quit_menu(),
                                      lambda: self.con.classify_page(),
                                      lambda: self.con.launch_menu(),
                                      lambda: self.logout(),
                                      lambda: self.con.launch_menu(),
                                      lambda: self.check_logout_2()
                                      )


if __name__ == '__main__':
    test = check_logout()
    test.checklogout()
    