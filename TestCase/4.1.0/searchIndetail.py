# -*- coding: utf-8 -*-
from appium import webdriver
import time
from common.py_common_keyword.CommonFunctions import CommonFunctions


class searchIndetail:
    def __init__(self):
        self.com = CommonFunctions()

    #打开应用详情
    def openDetailpage(self):
        global app
        try:
            apps=self.com.driver.find_elements_by_id('com.tclmarket:id/name')
            for app in apps:
                if app.text!='':
                    app.click()
                    time.sleep(5)

                    appname=self.com.wait_for_element('com.tclmarket:id/name')
                    if appname.text==app.text:
                        print 'you have entered appdetailpage'
                        return True
                    else:
                        print 'you have entered wrong'
                        return False

        except:
            print 'No app in the page'
            return False

    def opensearch(self):
        try:
            search=self.com.wait_for_element('com.tclmarket:id/actionbar_search')
            search.click()
            time.sleep(5)

            frame=self.com.wait_for_element('com.tclmarket:id/keywordflow')
            keywords=frame.find_elements_by_class_name('android.widget.TextView')
            apps=self.com.driver.find_elements_by_id('com.tclmarket:id/name')

            for k in keywords:
                if k.text!='':
                    print u'48小时热门搜索 is ok'
                    break
                else:
                    print u'48小时热门搜索 Load Fail'
                    return False

            for a in apps:
                if a.text !='':
                    print u'search chats is ok'
                    break
                else:
                    print u'search chats Load Fail'
                    return False

            backicon=self.com.wait_for_element('com.tclmarket:id/actionbar_up')
            backicon.click()

            appname=self.com.wait_for_element('com.tclmarket:id/name')
            if appname.text==app.text:
                print 'You successfully returns page for details'
                return True
            else:
                print 'you have entered wrong'
                return False
        except:
            print 'searchpage Load Fail'
            return False

    def run_searchIndetail(self):
        return self.com.run_test_case(lambda: self.com.launch_app(),
                                      lambda: self.openDetailpage(),
                                      lambda: self.opensearch())
        
if __name__ == '__main__':
    print searchIndetail().run_searchIndetail()