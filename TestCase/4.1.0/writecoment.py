# -*- coding: utf-8 -*-
from appium import webdriver
import time
from common.py_common_keyword.CommonFunctions import CommonFunctions


class writecoment:
    def __init__(self):
        self.com = CommonFunctions()

    # 打开应用详情ssss
    def openDetailpage(self):
        try:
            apps = self.com.driver.find_elements_by_id('com.tclmarket:id/name')
            for app in apps:
                if app.text != '':
                    app.click()
                    time.sleep(5)

                    appname = self.com.wait_for_element('com.tclmarket:id/name')
                    if appname.text == app.text:
                        print 'you have entered appdetailpage'
                        self.com.swipe_screen(percent=0.7)
                        time.sleep(3)
                        return True
                    else:
                        print 'you have entered wrong'
                        return False

        except:
            print 'No app in the page'
            return False

    def writecomment(self):
        try:
            comment = self.com.wait_for_element('com.tclmarket:id/remark_tv')
            comment.click()
            time.sleep(2)

            writeComment = self.com.wait_for_element('com.tclmarket:id/write_commment')
            writeComment.click()

            commentbox = self.com.wait_for_element('com.tclmarket:id/comment_content')
            submit = self.com.wait_for_element('com.tclmarket:id/submit_comment')
            submit.click()
            if commentbox:
                print 'network is well'
            else:
                print 'pelase check your network'
                return False

            commentbox.send_keys(u'等等')
            submit.click()
            time.sleep(2)
            if writeComment:
                print 'You have successfully submit comments'
                return True
            return False

        except:
            print 'writecomment error '
            return False

    def run_writecoment(self):
        return self.com.run_test_case(lambda: self.com.launch_app(),
                                      lambda: self.openDetailpage(),
                                      lambda: self.writecomment())


if __name__ == '__main__':
    print writecoment().run_writecoment()
