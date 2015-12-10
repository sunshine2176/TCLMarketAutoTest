#-*- coding: UTF-8 -*-  
'''
    版本 应用商店4.0.1
    编号 AppStore2-1103 
   标题	打开设置页面
'''

import sys
import time
from common.py_common_keyword.CommonFunctions import CommonFunctions
from selenium.webdriver.common.by import By
from startOperate import startOperate

 
class start_set_from_apkslist():
    def __init__(self):
        self.common_fn = CommonFunctions()
    
    def app_homepage(self):
        try:
            manage_buttons=self.common_fn.wait_for_elements(r'com.tclmarket:id/text',By.ID)
            if manage_buttons[4].text==u'管理':
                manage_buttons[4].click()
                time.sleep(2)
                print u'go into manage page\n'
            else:
                print u'manage_button[4].text do not equal to 管理'    
        except:
            print u'not find manage button\n'
            
            
    def apks_list(self):
        try:
            apks_list_buttons=self.common_fn.wait_for_elements(r'com.tclmarket:id/manage_image',By.ID)
            apks_list_buttons[3].click()
            time.sleep(2)
            print u'go into apks list page'
        except:
            print u'fail to go into apks list page'
                       
    def start_set_page(self):
        try:
            self.app_homepage()
            self.apks_list()
            set_button=self.common_fn.wait_for_element(r'com.tclmarket:id/actionbar_settings')
            set_button.click()
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
                                     lambda: self.start_set_page())                   
    
if __name__ =="__main__":
    test=start_set()
    test.run()          
            
                                
                                           
     
