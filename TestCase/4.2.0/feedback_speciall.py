# -*- coding: utf-8 -*-
#  AS4-898:提交特殊字符为反馈信息
import sys
import time
from common.py_common_keyword.common_class import common_class


class feedback_speciall:
    def __init__(self):
        self.con = common_class()

    def question_feedback(self, direction='up', percent=0.4, duration=None):
        while True:
            try:
                self.con.driver.find_element_by_id(r'com.tclmarket:id/question_feedback').click()
                break
            except:
                self.con.swipe_screen(direction, percent, duration)
                time.sleep(1)

        try:
            if self.con.driver.find_element_by_id(r'com.tclmarket:id/home_title').text == u'问题反馈':
                print u'进入问题反馈页面成功'
            else:
                print u'进入问题反馈页面失败'
                return False
        except:
            print u'进入问题反馈页面失败'
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
            return False

        try:
            content = self.con.driver.find_element_by_id(r'com.tclmarket:id/feedback_content')
            content.send_keys(u'！@#￥%……&*（）  23729  dhlkjlfd 5408483    好用 界面漂亮，资源多，下载快，资源多，下载快，占内存少    好')
            time.sleep(1)
            contact = self.con.driver.find_element_by_id(r'com.tclmarket:id/feedback_contact')
            contact.send_keys(u'gdfdj@hdfg.com')
            self.con.driver.find_element_by_id(r'com.tclmarket:id/send_feedback').click()
            time.sleep(2)
            if self.con.driver.find_element_by_id(r'com.tclmarket:id/home_title').text == u'问题反馈':
                print u'提交内容不完整，提交失败'
                return True
            elif self.con.driver.find_element_by_id(r'com.tclmarket:id/home_title').text == u'设置':
                print u'提交问题反馈成功'
                return True

        except:
            print u'问题反馈异常，失败'
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
            return False

    def feedbackspeciall(self):
        return self.con.run_test_case(lambda: self.con.launch_app(), lambda: self.con.entry_seting(),
                                      lambda: self.question_feedback())


if __name__ == '__main__':
    test = feedback_speciall()
    test.feedbackspeciall()
