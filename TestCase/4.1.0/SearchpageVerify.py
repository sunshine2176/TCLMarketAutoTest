# -*- coding: utf-8 -*-
import time
import sys
from selenium.webdriver.common.by import By
from common.py_common_keyword.CommonFunctions import CommonFunctions


class SearchpageVerify:
    def __init__(self):
        self.com = CommonFunctions()

    def searchpageVerify(self):

        button = self.com.wait_for_element('com.tclmarket:id/actionbar_search')
        button.click()
        time.sleep(5)
        try:
            frame = self.com.wait_for_element('com.tclmarket:id/keywordflow')
            keywords = frame.find_elements_by_class_name('android.widget.TextView')
            apps = self.com.wait_for_elements(value='com.tclmarket:id/name', by=By.ID)
            for k in keywords:
                if k.text != '':
                    print u'48小时热门搜索 is ok'
                else:
                    print u'48小时热门搜索 Load Fail'
                    return False
            for a in apps:
                if a.text != '':
                    print u'search chats is ok'
                else:
                    print u'search chats Load Fail'
                    return False

            backicon = self.com.wait_for_element('com.tclmarket:id/actionbar_up')
            backicon.click()
            banner = self.com.wait_for_element('com.tclmarket:id/banner1')
            if banner:
                print 'You have successfully from the search page'
                return True
            else:
                print 'wrong'
                return False
        except:

            print 'searchpage Load Fail'
            s = sys.exc_info()
            print 'Error "%s" happend on line %d' % (s[1], s[2].tb_lineno)
            return False

    def run_searchpageVerify(self):
        return self.com.run_test_case(lambda: self.com.launch_app(),
                                      lambda: self.searchpageVerify())


if __name__ == '__main__':
    print SearchpageVerify().run_searchpageVerify()
