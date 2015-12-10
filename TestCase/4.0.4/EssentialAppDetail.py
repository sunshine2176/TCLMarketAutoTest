# -*- coding: utf-8 -*-
# AppStore3-1173&1174 1.点击必备按钮，任意点击一个app，检查进入详情页面，返回，检查是否返回到上一级页面
# 2.进入到必备页面，下载app，并打开
from common.py_common_keyword.CommonFunctions import CommonFunctions
import time
import sys
from selenium.webdriver.support.ui import WebDriverWait

class EssentialAppDetail:
    commonfn = CommonFunctions()

    def __init__(self):
        pass

    def EntryDetail(self):
        print 'do EntryDetail'
        try:
            self.commonfn.element_clk(r'com.tclmarket:id/remark3')
            time.sleep(2)
            if self.commonfn.wait_for_element(r'com.tclmarket:id/header_text'):
                assert self.commonfn.driver.find_element_by_id(r'com.tclmarket:id/header_text').text == u'新机必备'
            self.commonfn.wait_for_element(r'com.tclmarket:id/actionbar_up').click()
            time.sleep(2)
            assert self.commonfn.driver.find_element_by_id(r'com.tclmarket:id/home_title').text == u'应用市场'
            return True
        except Exception, e:
            print e
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
            return False
            

    def DownloadDetail(self):
        print 'do downloaddetail'
        try:
            self.commonfn.element_clk(r'com.tclmarket:id/remark3')
            time.sleep(2)
            buttons = self.commonfn.driver.find_elements_by_id(r'com.tclmarket:id/action_button')
            print len(buttons)
            print u'click the download buttons'
            for b in buttons:
                if b.text == u'下载':
                    b.click()
                    time.sleep(2)
                    if not self.commonfn.driver.find_elements_by_id(r'com.tclmarket:id/action_button'):
                            self.commonfn.driver.keyevent(4)
                    elif b.text == u'暂停':
                        self.commonfn.wait_for_element(r'com.android.packageinstaller:id/cancel_button',time_out=180)
                        self.commonfn.driver.keyevent(4)
                    else:
                        print u'资源错误'
                else:
                    print u'该页面app已全部下载完'
                    break
            return True
        except Exception, e:
            print e
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
            return False
    def run_checking_testing(self):
        return self.commonfn.run_test_case(lambda: self.commonfn.launch_app('4.0.4'),
                                    lambda: self.EntryDetail(),
                                    lambda: self.DownloadDetail())

if __name__ == '__main__':
    test = EssentialAppDetail()
    test.run_checking_testing()


