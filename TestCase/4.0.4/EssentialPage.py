# -*- coding: utf-8 -*-
# AppStore3-1171&1172 1.点击必备按钮，检查是否进入到必备页面，返回，检查是否返回到上一级页面
# 2.进入到必备页面，滑动app列表，向上滑动到加载完毕
from common.py_common_keyword.CommonFunctions import CommonFunctions
import time


class EssentialPage:
    commonfn = CommonFunctions()

    def __init__(self):
        pass

    def verification(self):
        self.commonfn.element_clk(r'com.tclmarket:id/remark3')
        self.commonfn.wait_for_element(r'com.tclmarket:id/header_text')
        assert self.commonfn.driver.find_element_by_id(r'com.tclmarket:id/header_text').text == u'新机必备'
        print 'done verification'
        return True

    def sliding_screen_up(self):
        newapp_list = ''
        while True:
            try:
                app_list = []
                buttons = self.commonfn.driver.find_elements_by_id('com.tclmarket:id/name')
                for b in buttons:
                    app = b.text
                    app_list.append(app)

                if app_list[-1] != newapp_list:
                    newapp_list = app_list[-1]
                    print 'loading app up successfully'
                    self.commonfn.swipe_screen(direction='up')
                    time.sleep(5)
                else:
                    print 'you load all app on the page'
                    return True
                    break
            except (Exception, TypeError), e:
                print e
                return False

        # def sliding_screen_down(self):
        # newapp_list = ''
        # try:
        #     while True:
        #         app_list = []
        #         buttons = self.commonfn.driver.find_elements_by_id('com.tclmarket:id/name')
        #         for b in buttons:
        #             app = b.text
        #             app_list.append(app)
        #
        #         if app_list[0] != newapp_list:
        #             newapp_list = app_list[0]
        #             print r'loading app down successfully'
        #             self.commonfn.swipe_screen(direction='down')
        #             time.sleep(5)
        #         else:
        #             print 'till the top'
        #             break
        # except (Exception, TypeError), e:
        #         print e
        # try:
        #     for i in range(1, 5, 1):
        #         if i < 5:
        #             self.commonfn.swipe_screen(direction='down')
        #             print r'swipe up'
        #             time.sleep(1)
        #         else:
        #             print 'swipe up failed'
        #             break
        # except(Exception, TypeError), e:
        #     print e
        # return True

    def run_checking_setting(self):
        return self.commonfn.run_test_case(lambda: self.commonfn.launch_app('4.0.4'),
                                    lambda: self.verification(),
                                    lambda: self.sliding_screen_up())


if __name__ == '__main__':
    test = EssentialPage()
    test.run_checking_setting()
