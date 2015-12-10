# -*- coding: utf-8 -*-
# AS4-58:活动页面验证

import sys
import time
from common.py_common_keyword.common_class import common_class


class check_activity:
    def __init__(self):
        self.con = common_class()
        self.icon_temp = []
        self.icon_list = []
        self.icon = []

    def entry_activity(self):
        time.sleep(2)
        try:
            self.con.network_check()
        except:
            try:
                time.sleep(2)
                ac = self.con.driver.find_element_by_id(r'com.tclmarket:id/remark_text3')
                if ac.text == u'专题':
                    ac.click()
                    time.sleep(3)
                    if self.con.driver.find_element_by_id(r'com.tclmarket:id/home_title').text == u'活动':
                        print u'成功进入活动页面'
                        return True
                    else:
                        print u'没有进入活动页面'
                        return False
                else:
                    ac.click()
                    print ac.text
                    return True
            except:
                print u'进入活动页面失败'
                s = sys.exc_info()
                print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
                return False

    def swipe_get_item(self, direction='up', percent=0.4, duration=None):
        try:
            time.sleep(5)
            self.icon = self.con.driver.find_elements_by_id(r'com.tclmarket:id/subject_name')
            while self.con.get_elements():
                self.con.swipe_screen(direction, percent, duration)
                time.sleep(3)
                self.icon = self.con.driver.find_elements_by_id(r'com.tclmarket:id/subject_name')

            return True
        except:
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
            return False

    def checkactivity(self):
        return self.con.run_test_case(lambda: self.con.launch_app(), lambda: self.entry_activity(),
                                      lambda: self.swipe_get_item())


if __name__ == '__main__':
    test = check_activity()
    test.checkactivity()
