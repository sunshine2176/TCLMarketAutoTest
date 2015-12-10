#-*- coding: UTF-8 -*-  
'''
    版本 应用商店4.0.1
    编号 AppStore2-934 
   标题	卸载已安装程序
'''

import sys
import time
from common.py_common_keyword.CommonFunctions import CommonFunctions
from selenium.webdriver.common.by import By
from startOperate import startOperate
 
class uninstalled_app():
    
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
                        uninstall_name = self.common_fn.wait_for_element(r'com.tclmarket:id/name').text
                        uninstall_button=self.common_fn.wait_for_element(r'com.tclmarket:id/actionOne')
                        uninstall_button.click()
                        try:
                            uninstall_title=self.common_fn.wait_for_element(r'android:id/alertTitle')
                            if uninstall_title.text==uninstall_name:
                                print u'uninstall apps\n'
                                return True
                            else:
                                print u'can not uninstall apps\n'  
                                return False
                        except:
                            s = sys.exc_info()
                            print 'Error %s happend on line %d' % (s[1],s[2].tb_lineno)
                            return False
                        
                    except:
                        s = sys.exc_info()
                        print 'Error %s happend on line %d' % (s[1],s[2].tb_lineno)
                        print u'not find uninstall buttons\n'
                        return False
                else:
                    return False
            except:
                s = sys.exc_info()
                print 'Error %s happend on line %d' % (s[1],s[2].tb_lineno)
                return False   
        except:
            s = sys.exc_info()
            print 'Error %s happend on line %d' % (s[1],s[2].tb_lineno)
            print u'fail to go into installed apps page\n'
            return False
                       
      
    def run(self):
        start = startOperate()
        return self.common_fn.run_test_case(lambda: self.common_fn.launch_app('4.0.1'),
                                     lambda: start.baseOperate(),
                                     lambda: self.app_installedList())       
    
if __name__ =="__main__":
    test=app_uninstalled()
    test.run()         
            
                                
                                           
     
