# -*- coding: utf-8 -*-
#  AS4-895:问题反馈界面验证
import sys
print '\n'.join(sys.path)

#print str(sys.path).join()


import time
from common.py_common_keyword.common_class import common_class


class check_feedback:
    def __init__(self):
        self.con = common_class()
        self.icon_temp = []
        self.icon_list = []

    def question_feedback(self, direction='up', percent=0.8, duration=None):
        try:
            self.con.swipe_screen(direction, percent, duration)
            self.con.driver.find_element_by_id(r'com.tclmarket:id/question_feedback').click()
            time.sleep(1)
            if self.con.driver.find_element_by_id(r'com.tclmarket:id/home_title').text == u'问题反馈':
                print u'进入问题反馈页面成功'
                return True
        except:
            print u'进入问题反馈页面失败'
            return False

    def checkfeedback(self):
        return self.con.run_test_case(lambda: self.con.launch_app(), lambda: self.con.entry_seting(),
                                      lambda: self.question_feedback())


if __name__ == '__main__':
    test = check_feedback()
    test.checkfeedback()
