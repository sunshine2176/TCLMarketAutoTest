#-*- coding: UTF-8 -*-  
'''
    版本 应用商店4.0.1
    编号 AppStore2-1102
   标题	启动搜索功能
'''

import sys
import time
from common.py_common_keyword.CommonFunctions import CommonFunctions
from selenium.webdriver.common.by import By
from startOperate import startOperate


class start_search_from_apks():
    
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
                print u'manageButton[4].text do not equal to 管理'    
        except:
            print u'not find manage button\n'
            
            
    def apks_list(self):
        try:
            
            download_task_buttons=self.common_fn.wait_for_elements(r'com.tclmarket:id/manage_image',By.ID)
            download_task_buttons[3].click()
            time.sleep(2)
            print u'go into apks list page\n'
        except:
            print u'fail to go into apks list page\n'
                   
    def start_search_page(self):
        try:
            self.app_homepage()
            self.apks_list()
            search_button=self.common_fn.wait_for_element(r'com.tclmarket:id/actionbar_search')
            search_button.click()
            time.sleep(2)
            try:
                findApp_button=self.common_fn.wait_for_element(r'com.tclmarket:id/search_editor')
                if findApp_button.text==u'搜您喜欢的应用':
                    print u'get search page\n'
                    try:
                        goback_button=self.common_fn.wait_for_element(r'com.tclmarket:id/actionbar_up')
                        goback_button.click()
                        time.sleep(2)
                        try:
                            title=self.common_fn.wait_for_element(r'com.tclmarket:id/home_title')
                            if title:
                                print u'goback to apks list page\n'
                                return True
                            else:
                                print u'fail to goback to apks list page\n'    
                                return False
                        except:
                            s = sys.exc_info()
                            print 'Error %s happend on line %d' % (s[1],s[2].tb_lineno)
                            return False
                    except:
                        print u'not find gobackButton\n'  
                        s = sys.exc_info()
                        print 'Error %s happend on line %d' % (s[1],s[2].tb_lineno)
                        return False                        
                else:
                    print u'fail to get search page\n'
                    s = sys.exc_info()
                    print 'Error %s happend on line %d' % (s[1],s[2].tb_lineno)
                    return False                    
            except:
                print u'not get the findAppButton' 
                s = sys.exc_info()
                print 'Error %s happend on line %d' % (s[1],s[2].tb_lineno)
                return False                
        except:
            print u'fail to find search button\n'
            s = sys.exc_info()
            print 'Error %s happend on line %d' % (s[1],s[2].tb_lineno)
            return False            
    
    def run(self):
        start = startOperate()
        return self.common_fn.run_test_case(lambda: self.common_fn.launch_app('4.0.1'),
                                     lambda: start.baseOperate(),
                                     lambda: self.start_search_page())  
    
if __name__ =="__main__":
    test=start_search()
    test.run()          
            
                                
                                           
     
