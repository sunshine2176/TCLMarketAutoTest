#-*- coding: UTF-8 -*-  

import sys
import time
from common.py_common_keyword.CommonFunctions import CommonFunctions
from selenium.webdriver.common.by import By
from startOperate import startOperate
from baseFunc import baseFunc
 
class apk_scanning_page():
    '''
                      版本 应用商店4.0.1
                     编号  AppStore2-935 
                    标题    安装包扫描界面
      '''
    def __init__(self):
        self.common_fn = CommonFunctions()
    
                                    
    def app_homepage(self):
        try:
            downloadApps=self.common_fn.wait_for_elements(r'com.tclmarket:id/item_container',By.ID)
            isClick = False
            for app in downloadApps:
                downloadBtn = app.find_element(By.ID,r'com.tclmarket:id/action_text')
                if downloadBtn.text == u'下载':
                    downloadBtn.click()
                    appName = app.find_element(By.ID,r'com.tclmarket:id/name').text
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
                self.common_fn.element_clk(r'com.android.packageinstaller:id/ok_button')
                #print u'click the next button %d\n' % (i+1)
            time.sleep(30)
            #print u'finish clicking ok\n'
        except Exception as e:
            print e
            print u'something wrong with ok button\n'
            return False 
        try:
            self.common_fn.element_clk(r"com.android.packageinstaller:id/done_button")
            time.sleep(2)
            #print u'install the first app\n'         
        except:
            print u'fail to install the first app\n'     
            return False
        try:
            download_apps=self.common_fn.wait_for_elements(r'com.tclmarket:id/action',By.ID)
            download_apps[1].click()
            print u'start to download the second app\n'
            time.sleep(55)
        except:
            print u'fail to download the second app\n ' 
            return False
        try:    
            self.common_fn.wait_for_element(r'com.android.packageinstaller:id/cancel_button',time_out=90).click() 
            time.sleep(2)
            print u'refuse to install downloaded apk\n'
        except:
            print u'fail to refuse install\n'     
            return False
        finally:
            self.common_fn.driver.remove_app('com.tencent.qqlive') 
            
        try:
            manage_buttons=self.common_fn.wait_for_elements(r'com.tclmarket:id/text',By.ID)
            if manage_buttons[4].text==u'管理':
                manage_buttons[4].click()
                time.sleep(2)
                print u'go into manage page\n'
            else:
                print u'manageButton[4].text do not equal to 管理'
                return False
            try:
                action_buttons=self.common_fn.wait_for_elements(r'com.tclmarket:id/manage_image',By.ID)
                action_texts=self.common_fn.wait_for_elements(r'com.tclmarket:id/manage_text',By.ID)
                if action_texts[3].text==u'安装包扫描' :
                    action_buttons[3].click()
                    print u'get apks scanning page\n'
                else:
                    print u'not get apks scanning page\n'
                    return False 
                try:
                    title=self.common_fn.wait_for_elements(r'com.tclmarket:id/header_text',By.ID)
                    base = baseFunc()
                    if title and len(title) == 1 and u'已安装' in title[0].text:
                        base.uninstallAPP(appName)
                        return True
                    elif title and len(title) == 2 and u'已安装' in title[0].text and u'未安装' in title[1].text:
                        #print u'installed apk is right\n'
                        base.uninstallAPP(appName)
                        return True
                    else:
                        print u'没有发现已安装或未安装列表'
                        return False 
                except:
                    print u'not find apks\n'  
                    s = sys.exc_info()
                    print 'Error "%s" happend on line %d' % (s[1],s[2].tb_lineno)                   
                    return False 
            except:
                print u'not find apks scanning button\n'
                s = sys.exc_info()
                print 'Error "%s" happend on line %d' % (s[1],s[2].tb_lineno)
                return False
        except:
            print u'not find manage button\n'
            s = sys.exc_info()
            print 'Error "%s" happend on line %d' % (s[1],s[2].tb_lineno)            
            return False
        
       
    def run(self):
        start = startOperate()
        return self.common_fn.run_test_case(lambda: self.common_fn.launch_app('4.0.1'),
                                     lambda: start.baseOperate(),
                                     lambda: self.app_homepage())
if __name__ =="__main__":
    test=apk_scanning_page()
    test.run()
      
            
                                
                                           
     
