#-*- coding: UTF-8 -*-  
'''
    版本 应用商店4.0.1
    编号 AppStore2-989
	标题 下载并查看广告位app
'''

import sys,os
import time
from common.py_common_keyword.CommonFunctions import CommonFunctions
from selenium.webdriver.common.by import By
from startOperate import startOperate
import ConfigParser
 
class DownloadAdApp():
    def __init__(self):
        self.common_fn = CommonFunctions()
         
    def appdownload(self):
        try:
            adButtons=self.common_fn.wait_for_elements(r'android.widget.ImageView')
        except:
            time.sleep(3)
            adButtons=self.common_fn.wait_for_elements(r'android.widget.ImageView')
        adButtons[1].click()
        time.sleep(5)
        print u'get adButton\n'
        try:
            download_keys=self.common_fn.wait_for_elements(r'com.tclmarket:id/action_text',By.ID)
            download_values=self.common_fn.wait_for_elements(r'com.tclmarket:id/action',By.ID)
            if download_keys:
                for i in range(len(download_keys)):

                    if download_keys[i].text==u'下载':
                        download_values[i].click()
                        print u'start to download the app\n'
                        break
                    elif download_keys[i].text==u'继续':
                        download_values[i].click()
                        print u'continue to download the app\n'
                        
                    elif download_keys[i].text==u'安装':
                        download_values[i].click()
                        print u'start to setup the app\n'
                        
                    elif download_keys[i].text==u'更新':
                        download_values[i].click()
                        print u'start to update the app\n'
                        
                    elif download_keys[i].text==u'打开':
                        print u'the app has downloaded'
                        
                    else: 
                        download_values[i].click()
                        print u'stop download the app'
            else:
                print u'not find any download buttons\n' 
                return False
        except:
            print u'fail to download single app\n'
            return False
                            
        try:
            button=self.common_fn.wait_for_element(r'com.tclmarket:id/download_all_button')
            if button.text==u"下载全部":
                button.click()
                time.sleep(5)
                print u'all ad apps are downloading\n'
                self.cleanAPP()
                return True
            else:
                print u'not find "download all"button\n'
                return False
        except:
            print u'download fail'
            return False
        finally:
            self.common_fn.driver.remove_app('com.tencent.qqlive')        
        
    def cleanAPP(self):
        """清除全部下载任务"""
        try:
            config_file = os.path.join(self.common_fn.program_path, 'config/conf.ini')
            config = ConfigParser.ConfigParser()
            config.readfp(open(config_file))
            packageName = config.get("Device", "app-package")
            os.system('adb shell pm clear %s' % packageName)
            return True
        except:
            s = sys.exc_info()
            print 'Error "%s" happend on line %d' % (s[1],s[2].tb_lineno)
            
                
    def run(self):
        start = startOperate()
        return self.common_fn.run_test_case(lambda: self.common_fn.launch_app('4.0.1'),
                                     lambda: start.baseOperate(),
                                     lambda: self.appdownload())        
   
    
if __name__ =="__main__":
    test=DownloadAdApp()
    test.run()
                                
                                           
     
