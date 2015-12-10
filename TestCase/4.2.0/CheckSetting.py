# -*- coding: utf-8 -*-
# AS4-891:设置界面验证
import sys
import time
from common.py_common_keyword.CommonFunctions import CommonFunctions


class CheckSetting:
    def __init__(self):
        pass

    common_fn = CommonFunctions()
    icon_temp = []
    icon_list = []

    def entry_seting(self):

        """
        功能描述：
        参数:无
        返回值：无
        :rtype : object
        """
        items = []
        items2 = []
        try:
            network_error = self.common_fn.driver.find_element_by_id(r'com.tclmarket:id/loading_error_info')
            if network_error.text == u'加载失败请检查您的网络连接...':
                print '加载失败请检查您的网络连接...'
                return False

        except:
            try:
                self.common_fn.driver.find_element_by_id(r'com.tclmarket:id/drawer_menu').click()
                time.sleep(1)
                self.common_fn.driver.find_element_by_id(r'com.tclmarket:id/setting').click()
                time.sleep(1)
                print u'进入设置页面成功'
            except:
                exc = sys.exc_info()
                print exc[0], ':', exc[1]
                print u'进入设置页面失败'
                return False

            try:
                time.sleep(10)
                items = self.common_fn.driver.find_elements_by_class_name(r'android.widget.TextView')
                self.common_fn.swipe_screen(direction='up')
                # self.common_fn.driver.swipe(516, 1200, 516, 300, 0)
                time.sleep(10)
                items2 = self.common_fn.driver.find_elements_by_class_name(r'android.widget.TextView')
                print len(items)
                print len(items2)
                # if len(items) == 23:
                #     print u'设置界面第一页加载成功'
                # else:
                #     print u'设置界面第一页加载失败'
                #
                # if len(items2) == 18:
                #     print u'设置界面第二页加载成功'
                # else:
                #     print u'设置界面第二页加载失败'

                if len(items) == 22 and len(items2) == 16:
                    print u'设置界面加载成功'
                    return True
                else:
                    print u'设置界面加载失败'
                    return False

            except:
                print u'设置界面加载失败'
                exc = sys.exc_info()
                print exc[0], ':', exc[1]
                return False

    def run_check_setting(self):
        """
        功能描述：运行用例逻辑
        参数:无
        返回值：无
        """
        return self.common_fn.run_test_case(lambda: self.common_fn.launch_app(),
                                            lambda: self.entry_seting())
        # try:
        #     print 'start test'
        #     assert self.common_fn.launch_app('4.2.0')
        #     assert self.entry_seting()
        #     print 'end test'
        #     return True
        # except:
        #     a = sys.exc_info()
        #     print a[0]
        #     print a[1]
        #     return False
        # finally:
        #     self.common_fn.appQuit()


if __name__ == '__main__':
    test = CheckSetting()
    test.run_check_setting()
