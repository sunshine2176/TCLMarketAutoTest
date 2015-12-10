#-*- coding: UTF-8 -*-  
'''
    版本 应用商店4.0.1
    编号 AppStore2-1068 
   标题	启动搜索功能
'''

import sys
import time
from common.py_common_keyword.CommonFunctions import CommonFunctions
from selenium.webdriver.common.by import By
from baseFunc import baseFunc
from startOperate import startOperate
 
class startSearchPage():
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
                self.common_fn.element_clk(r'com.android.packageinstaller:id/ok_button',timeout=50)
                print u'click the next button %d\n' % (i+1)
            time.sleep(30)
            print u'finish clicking ok\n'
        except:
            print u'something wrong with ok button\n'
        try:
            doneButton=self.common_fn.element_clk(r"com.android.packageinstaller:id/done_button",timeout=30)
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
            
            downloadTaskButtons=self.common_fn.wait_for_elements(r'com.tclmarket:id/manage_image',By.ID)
            downloadTaskButtons[0].click()
            time.sleep(2)
            
            print u'go into download task page'
        except:
            print u'fail to go into download task page'
                        
    def startSearchPage(self):
        try:
            self.appHomePage()
            self.appDownloadTask()
            appName = self.common_fn.wait_for_element(r'com.tclmarket:id/name').text
            searchButton=self.common_fn.wait_for_element(r'com.tclmarket:id/actionbar_search')
            searchButton.click()
            time.sleep(2)
            try:
                findAppButton=self.common_fn.wait_for_element(r'com.tclmarket:id/search_editor')
                if findAppButton.text==u'搜您喜欢的应用':
                    print u'get search page\n'
                    try:
                        gobackButton=self.common_fn.wait_for_element(r'com.tclmarket:id/actionbar_up')
                        gobackButton.click()
                        time.sleep(2)
                        try:
                            title=self.common_fn.wait_for_element(r'com.tclmarket:id/home_title')
                            if title:
                                print u'goback to download task page\n'
                                base = baseFunc()
                                base.uninstallAPP(appName)                                
                                return True
                            else:
                                print u'fail to goback to download task page\n'    
                                return False
                        except:
                            s = sys.exc_info()
                            print 'Error %s happend on line %d' % (s[1],s[2].tb_lineno)
                            return False        
                    except:
                        print u'not find gobackButton\n'    
                        return False
                else:
                    print u'fail to get search page\n'
                    return False
            except:
                print u'not get the findAppButton'        
                return False
        except:
            print u'fail to find search button\n'
            return False
        finally:
            self.common_fn.driver.remove_app('com.tencent.qqlive')        
            
    def run(self):
        start = startOperate()
        return self.common_fn.run_test_case(lambda: self.common_fn.launch_app('4.0.1'),
                                     lambda: start.baseOperate(),
                                     lambda: self.startSearchPage()) 
       
       
    
if __name__ =="__main__":
    test=startSearchPage()
    test.run()
                                
                                           
     
