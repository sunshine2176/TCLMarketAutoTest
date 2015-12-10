#-*- coding: UTF-8 -*-  
'''
    版本 应用商店4.0.1
    编号 AppStore2-1069 
   标题	打开设置页面
'''

import sys
import time
from common.py_common_keyword.CommonFunctions import CommonFunctions
from selenium.webdriver.common.by import By
from startOperate import startOperate



 
class startSetPage():
    def __init__(self):
        self.common_fn = CommonFunctions()
    
        
    def appHomePage(self):
        try:
            downloadApps=self.common_fn.wait_for_elements(r'com.tclmarket:id/action',By.ID)
            downloadApps[0].click()
            print u'start to download an app\n'
            time.sleep(30)
        except:
            print u'fail to download the first app\n ' 
        try:
            for i in range(4):
                OKButton=self.common_fn.wait_for_element(r'com.android.packageinstaller:id/ok_button')
                OKButton.click()
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
            
            
    def appDownloadTask(self):
        try:
            downloadTaskButtons=self.common_fn.wait_for_elements(r'com.tclmarket:id/manage_image',By.ID)
            downloadTaskButtons[0].click()
            time.sleep(2)
            print u'go into download task page'
        except:
            print u'fail to go into download task page'
                      
    def startSetPage(self):
        try:
            #self.appHomePage()
            self.appDownloadTask()
            setButton=self.common_fn.wait_for_element(r'com.tclmarket:id/actionbar_settings')
            setButton.click()
            time.sleep(2)
            try:
                title=self.common_fn.wait_for_element(r'com.tclmarket:id/home_title')
                if title.text==u'设置':
                    print u'get set page\n'
                    return True
                else:
                    return False
            except:
                print u'not get the title\n'     
                return False
        except:
            print u'fail to find set button\n'
            return False
             
       
    def run(self):
        start = startOperate()
        return self.common_fn.run_test_case(lambda: self.common_fn.launch_app('4.0.1'),
                                     lambda: start.baseOperate(),
                                     lambda: self.startSetPage())        
    
if __name__ =="__main__":
    test=AppDownload()
    test.run()         
            
                                
                                           
     
