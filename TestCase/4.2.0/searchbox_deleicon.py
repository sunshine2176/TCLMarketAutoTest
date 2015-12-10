# -*- coding: utf-8 -*-
# AS4-1291:搜索输入框中删除按钮验证

import sys
from common.py_common_keyword.common_class import common_class


class searchbox_deleicon():
    def __init__(self):
        self.con = common_class()
        self.content = u'hkdshsad中'

    def input_content(self):
        try:
            inputElement = self.con.driver.find_element_by_id(r'com.tclmarket:id/search_editor')
            inputElement.send_keys(self.content)
            input_content = self.con.driver.find_element_by_id(r'com.tclmarket:id/search_editor')
            print u'搜索框中输入的内容为: %s' % input_content.text
            return True
        except:
            print u'输入内容失败'
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
            return False

    def dele_content(self):
        try:
            self.con.network_check()
        except:
            try:
                if len(self.content) >= 1:
                    self.con.driver.find_element_by_id(r'com.tclmarket:id/clear_btn').click()
                    print u'删除‘%s’成功' % self.content
                    return True
                else:
                    print u'已全部删除字符'
                    return True

            except:
                print u'删除字符失败'
                s = sys.exc_info()
                print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
                return False

    def searchboxdeleicon(self):
        return self.con.run_test_case(lambda: self.con.launch_app(),
                                      lambda: self.con.entry_search_box(),
                                      lambda: self.input_content(),
                                      lambda: self.dele_content()
                                      )


if __name__ == '__main__':
    test = searchbox_deleicon()
    test.searchboxdeleicon()
