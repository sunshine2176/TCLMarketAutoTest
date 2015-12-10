#-*- coding: UTF-8 -*-  
'''
    版本 应用商店4.0.1
    编号 AppStore2-1009 
   标题	打开已安装程序
'''

import sys
import time
from common.py_common_keyword.CommonFunctions import CommonFunctions
from selenium.webdriver.common.by import By
from startOperate import startOperate

 
class open_installed_app():
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
            installed_buttons[2].click()
            time.sleep(2)
            try:
                title=self.common_fn.wait_for_element(r'com.tclmarket:id/home_title')
                if title.text==u'已安装':
                    print u'get installed apps list\n'
                    try:
                        
                        appName = self.common_fn.wait_for_elements(r'com.tclmarket:id/name',By.ID)[5].text
                        click_apps=self.common_fn.wait_for_elements(r'com.tclmarket:id/fold_tag',By.ID)
                        click_apps[5].click()
                        open_button=self.common_fn.wait_for_element(r'com.tclmarket:id/bottom_action_left')
                        open_button.click()  
                        
                        print u'open app "%s" \n' % appName
                        self.common_fn.driver.keyevent('4')
                        return True
                    except Exception as e:
                        
                        print u'not find apps\n'
                        s = sys.exc_info()
                        print 'Error %s happend on line %d' % (s[1],s[2].tb_lineno)                        
                else:
                    pass
            except:
                pass        
        except:
            print u'fail to go into installed apps page\n'
            s = sys.exc_info()
            print 'Error %s happend on line %d' % (s[1],s[2].tb_lineno)
                       
      
    def run(self):
        start = startOperate()
        return self.common_fn.run_test_case(lambda: self.common_fn.launch_app('4.0.1'),
                                     lambda: start.baseOperate(),
                                     lambda: self.app_installedList()) 
    
if __name__ =="__main__":
    test=app_uninstalled()
    test.run()           
            
                                
                                           
     
