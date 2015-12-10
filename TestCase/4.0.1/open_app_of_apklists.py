#-*- coding: UTF-8 -*-  
'''
    版本 应用商店4.0.1
    编号 AppStore2-1011 
   标题	打开已安装的程序
'''

import sys
import time
from common.py_common_keyword.CommonFunctions import CommonFunctions
from selenium.webdriver.common.by import By
from startOperate import startOperate
from baseFunc import baseFunc

 
class open_app_of_apklists():
    def __init__(self):
        self.common_fn = CommonFunctions()
    
    def app_homePage(self):
        try:
            manage_buttons=self.common_fn.wait_for_elements(r'com.tclmarket:id/text',By.ID)
            if manage_buttons[4].text==u'管理':
                manage_buttons[4].click()
                time.sleep(2)
                print u'go into manage page\n'
            else:
                print u'manageButton[4].text do not equal to 管理'    
        except:
            print u'not find manage button\n'
            
            
    def app_installedList(self):
        try:
            self.app_homePage()
            installed_buttons=self.common_fn.wait_for_elements(r'com.tclmarket:id/manage_image',By.ID)
            installed_buttons[3].click()
            time.sleep(2)
            try:
                title=self.common_fn.wait_for_element(r'com.tclmarket:id/home_title')
                if title.text==u'安装包扫描':
                    print u'get apks list\n'
                    try:
                        appName = self.common_fn.wait_for_element(r'com.tclmarket:id/name').text
                        click_apps=self.common_fn.wait_for_elements(r'com.tclmarket:id/icon',By.ID)
                        click_apps[0].click()
                        print u'open app "%s" \n' % appName
                        self.common_fn.driver.keyevent('4')
                        base = baseFunc()
                        base.uninstallAPP(appName)    
                        return True
                    except Exception as e:
                        print e
                        print u'not find apps\n'
                        return False
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
                                     lambda: self.app_installedList()) 
    
if __name__ =="__main__":
    test=open_app_installed()
    test.run()         
            
                                
                                           
     
