# -*- coding: utf-8 -*-
import time
import sys
from common.py_common_keyword.CommonFunctions import CommonFunctions


class versionVerify:
    def __init__(self):
        self.com = CommonFunctions()

    # 获取应用列表中应用的版本号
    def getVersion(self):
        global version_NO
        try:
            versions = self.com.driver.find_elements_by_id('com.tclmarket:id/version')
            for v in versions:
                version = v.text
                version_no = version.split('|')[0]
                version_NO = version_no[1:-1]
                print version_NO
                return True
        except:
            print 'getVersion Failed'
            return False

    # 打开应用详情
    def openDetailpage(self):
        global app
        try:
            apps = self.com.driver.find_elements_by_id('com.tclmarket:id/name')
            for app in apps:
                if app.text != '':
                    app.click()
                    time.sleep(8)

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

    def checkVersion(self):
        try:
            fr = self.com.wait_for_element('com.tclmarket:id/version_info_content')
            v = fr.find_element_by_id('com.tclmarket:id/version_name')
            UT = fr.find_element_by_id('com.tclmarket:id/update_time')
            DL = fr.find_element_by_id('com.tclmarket:id/download_times')
            ok = fr.find_element_by_id('com.tclmarket:id/one_key_submit')

            version = v.text
            update = UT.text
            download = DL.text
            one_key = ok.text

            versioncode = version.split(u'：')[-1]
            print versioncode

            if versioncode == version_NO and update and download and one_key:
                print 'Version information in detail page is OK'
                return True
            else:
                print 'Version information in detail page is Failed'
                return False
        except:
            s = sys.exc_info()
            print 'Error "%s" happend on line %d' % (s[1], s[2].tb_lineno)
            return False

    def run_versionVerify(self):
        return self.com.run_test_case(lambda: self.com.launch_app(),
                                      lambda: self.getVersion(),
                                      lambda: self.openDetailpage(),
                                      lambda: self.checkVersion())


if __name__ == '__main__':
    print versionVerify().run_versionVerify()
