# -*- coding: utf-8 -*-
# AppStore3-26 1.点击banner，返回。列表正常显示无问题
# 2.点击banner，下载第一个app
from common.py_common_keyword.CommonFunctions import CommonFunctions
import time
import sys


class DownloadAds:
    common_fn = CommonFunctions()

    def __init__(self):
        pass

    def entrybanner(self):
        print 'do entrybanner'
        try:
            self.common_fn.element_clk(r'com.tclmarket:id/banner1')
            print 'click the banner'
            if self.common_fn.wait_for_element(r'com.tclmarket:id/loading_error_info') == True:
                print self.common_fn.driver.find_element('com.tclmarket:id/loading_error_info').text
                return False
            else:
                time.sleep(2)
                self.common_fn.driver.find_element_by_id(r'com.tclmarket:id/actionbar_up').click()
                assert self.common_fn.driver.find_element_by_id(r'com.tclmarket:id/home_title').text == u'应用市场'
                return True
                print u'返回成功'
        except Exception, e:
            print e
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1],s[2].tb_lineno)
            return False

    def download_ads(self):
        print 'entry download_ads'
        try:
            assert self.common_fn.element_clk(r'com.tclmarket:id/banner1')
            assert self.common_fn.element_clk(r'com.tclmarket:id/action_button')
            time.sleep(2)
            return True
            # print u'判断是否开始下载或下载完成了'
            # if self.common_fn.wait_for_element(value=r'com.android.packageinstaller:id/cancel_button'):
            #     return True
            # else:
            #     print u'下载处出错'
        except Exception, e:
            print e
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
            return False

    def run_checking_setting(self):
        return self.common_fn.run_test_case(lambda: self.common_fn.launch_app('4.0.4'),
                                     lambda: self.entrybanner(),
                                     lambda: self.download_ads())


if __name__ == '__main__':
    test = DownloadAds()
    test.run_checking_setting()
