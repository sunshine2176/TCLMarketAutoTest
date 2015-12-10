#-*- coding: UTF-8 -*-  
'''
    版本 应用商店4.0.1
    编号 AppStore2-924 
   标题	开启已经安装好的应用程序
'''

import sys,os
import time
from common.py_common_keyword.CommonFunctions import CommonFunctions
from baseFunc import baseFunc
from selenium.webdriver.common.by import By
from startOperate import startOperate
 
class installedAppOpen():
    def __init__(self):
        self.common_fn = CommonFunctions()
     
    def appHomePage(self):
        try:
            
            downloadApps=self.common_fn.wait_for_elements(r'com.tclmarket:id/item_container',By.ID)
            isClick = False
            for app in downloadApps:
                downloadBtn = app.find_element(By.ID,r'com.tclmarket:id/action_text')
                if downloadBtn.text == u'下载':
                    downloadBtn.click()
                    isClick = True
                    break
            if not isClick:
                raise Exception('do not have download app at installedAppOpen')
            print u'start to download an app\n'
            time.sleep(50)
        except:
            print u'fail to download the first app\n ' 
        try:
            for i in range(4):
                self.common_fn.element_clk(r'com.android.packageinstaller:id/ok_button',timeout=30)
                print u'click the next button %d\n' % (i+1)
            time.sleep(30)
            print u'finish clicking ok\n'
        except:
            print u'something wrong with ok button\n'
        try:
            doneButton=self.common_fn.wait_for_element(r"com.android.packageinstaller:id/done_button")
            doneButton.click()
            time.sleep(2)
            print u'install the first app\n'         
        except:
            print u'fail to install the first app\n'           
        try:
            manageButtons=self.common_fn.wait_for_elements(r'com.tclmarket:id/text',By.ID)
            if manageButtons[4].text==u'管理':
                manageButtons[4].click()
                time.sleep(2)
                print u'go into manage page\n'
            else:
                print u'manageButton[4].text do not equal to 管理'    
        except:
            print u'not find manage button\n'
            s = sys.exc_info()
            print 'Error %s happend on line %d' % (s[1],s[2].tb_lineno)
            
            
    def appDownloadTask(self):
        try:
            self.appHomePage()
            downloadTaskButtons=self.common_fn.wait_for_elements(r'com.tclmarket:id/manage_image',By.ID)
            downloadTaskButtons[0].click()
            time.sleep(2)
            print u'go into download task page'
            try:
                appName = self.common_fn.wait_for_element(r'com.tclmarket:id/name').text
                actionButton=self.common_fn.wait_for_element(r'com.tclmarket:id/actionOne')
                textButton=self.common_fn.wait_for_element(r'com.tclmarket:id/actionOne_text')
                if textButton.text==u'打开':
                    actionButton.click()
                    time.sleep(5)
                    print u'open the app\n'
                    self.common_fn.driver.keyevent('4')
                    base = baseFunc()
                    base.uninstallAPP(appName)
                    return True
                else:
                    print u'not find the open button\n'
                    return False
            except Exception as e:
                print e
                print u'fail to open the app\n'      
                return False
        except:
            print u'fail to go into download task page'
            s = sys.exc_info()
            print 'Error %s happend on lineno %d' % (s[1],s[2].tb_lineno)
            return False
        finally:
            self.common_fn.driver.remove_app('com.tencent.qqlive')        
    
              
    def run(self):
        start = startOperate()
        return self.common_fn.run_test_case(lambda: self.common_fn.launch_app('4.0.1'),
                                     lambda: start.baseOperate(),
                                     lambda: self.appDownloadTask())    
       
    
if __name__ =="__main__":
    test=installedAppOpen()
    test.run()            
            
                                
                                           
     
