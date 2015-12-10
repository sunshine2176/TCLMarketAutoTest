# -*- coding:utf-8 -*-
import time
from common.py_common_keyword.CommonFunctions import CommonFunctions


class commentpageVerify:
    def __init__(self):
        self.com = CommonFunctions()

    # 打开应用详情
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

    def commentpafeVerify(self):
        try:
            comment = self.com.wait_for_element('com.tclmarket:id/remark_tv')
            comment.click()
            time.sleep(5)
            writeComment = self.com.wait_for_element('com.tclmarket:id/write_commment')
            grade = self.com.wait_for_element('com.tclmarket:id/avgscore_lyout')

            if writeComment and grade:
                print 'You enter commentpage successfully'
                return True
            else:
                print 'Enter the commentpage failure'
                return False
        except:
            print 'commentpafe verify failure'
            return False

    def run_commentpafeVerify(self):
        return self.com.run_test_case(lambda: self.com.launch_app(),
                                      lambda: self.openDetailpage(),
                                      lambda: self.commentpafeVerify())


if __name__ == '__main__':
    print commentpageVerify().run_commentpafeVerify()