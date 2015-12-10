#-*- coding: UTF-8 -*-  
'''
    版本 应用商店4.0.1
    编号 AppStore2-933 
   标题	已安装界面验证
'''

import sys
import time
from common.py_common_keyword.CommonFunctions import CommonFunctions
from selenium.webdriver.common.by import By
from startOperate import startOperate

 
class installedAppPage():
    def __init__(self):
        self.common_fn = CommonFunctions()
              
    def appHomePage(self):
        try:
            manageButtons=self.common_fn.wait_for_elements(r'com.tclmarket:id/text',By.ID)
            if manageButtons[4].text==u'管理':
                manageButtons[4].click()
                time.sleep(2)
                print u'go into manage page\n'
                return True
            else:
                print u'manageButton[4].text do not equal to 管理'   
                return False
        except:
            print u'not find manage button\n'
            return False
            
            
    def appInstalledList(self):
        try:
            self.appHomePage()
            installedButtons=self.common_fn.wait_for_elements(r'com.tclmarket:id/manage_image',By.ID)
            installedButtons[2].click()
            time.sleep(2)
            try:
                title=self.common_fn.wait_for_element(r'com.tclmarket:id/home_title')
                if title.text==u'已安装':
                    print u'get installed apps list\n'
                    return True
                else:
                    return False
            except:
                return False    
        except:
            print u'fail to go into installed apps page\n'
            return False
                     
    def run(self):
        start = startOperate()
        return self.common_fn.run_test_case(lambda: self.common_fn.launch_app('4.0.1'),
                                     lambda: start.baseOperate(),
                                         lambda: self.appInstalledList())          
    
if __name__ =="__main__":
    test=AppInstalled()
    test.run()          
            
                                
                                           
     
