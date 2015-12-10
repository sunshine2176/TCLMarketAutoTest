#-*- coding: UTF-8 -*-  
'''
    版本 应用商店4.0.1
    编号 AppStore2-922 
   标题	下载任务界面验证
'''

import sys,os
import time
from common.py_common_keyword.CommonFunctions import CommonFunctions
from selenium.webdriver.common.by import By
from startOperate import startOperate


 
class appManage():
    def __init__(self):
        self.common_fn = CommonFunctions()
    
    def appHomePage(self):
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
            self.appHomePage()
            downloadTaskButtons=self.common_fn.wait_for_elements(r'com.tclmarket:id/manage_image',By.ID)
#             taskNums=self.common_fn.wait_for_elements(r'com.tclmarket:id/num')
#             print 'download tasks:'+taskNums[0].text
            downloadTaskButtons[0].click()
            time.sleep(2)
            print u'go into download task page'
            try:
                gobackButton=self.common_fn.wait_for_element(r'com.tclmarket:id/go_to_home')
                if gobackButton:
                    gobackButton.click()
                    print u'find goback button\n'
                    try:
                        downloadApps=self.common_fn.wait_for_elements(r'com.tclmarket:id/action',By.ID)
                        downloadApps[0].click()
                        downloadApps[1].click()
                        print u'start to download an app\n'
                        downloadApps[0].click()
                        downloadApps[1].click()
                        print u'stop downloading\n'
                        self.appHomePage()    
                        taskNums=self.common_fn.wait_for_elements(r'com.tclmarket:id/num',By.ID)
                        taskNum=taskNums[0].text
                        print 'download tasks:'+taskNum
                        downloadTaskButtons[0].click()
                        try:
                            listTasks=self.common_fn.wait_for_elements(r'com.tclmarket:id/actionOne',By.ID)
                            print listTasks
                            print 'task number is'+str(len(listTasks))
                            if taskNum==str(len(listTasks)):
                                print u'task number is right\n'
                                return True
                            else:
                                print u'task number is not right\n'  
                                return False
                        except Exception as e:
                            print u'not find task from list\n' 
                            print e   
                            return False
                        
                    except:
                        print u'can not download an app\n'
                        s = sys.exc_info()  
                        print 'Error "%s" happend on line %d' % (s[1],s[2].tb_lineno)                         
                        return False
                else:
                    print u'not find goback button\n'
                    s = sys.exc_info()
                    print 'Error "%s" happend on line %d' % (s[1],s[2].tb_lineno)                     
                    return False
            except:
                print u'not find gobackButton\n'
                s = sys.exc_info()
                print 'Error "%s" happend on line %d' % (s[1],s[2].tb_lineno)                 
                return False
        except:
            print u'fail to go into download task page'
            s = sys.exc_info()
            print 'Error "%s" happend on line %d' % (s[1],s[2].tb_lineno)            
            return False
        finally:
            self.common_fn.driver.remove_app('com.tencent.qqlive')        
    
    def run(self):
        start = startOperate()
        return self.common_fn.run_test_case(lambda: self.common_fn.launch_app('4.0.1'),
                                     lambda: start.baseOperate(),
                                     lambda: self.appDownloadTask())

if __name__ =="__main__":
    test=appManage()
    test.run()           
            
                                
                                           
     
