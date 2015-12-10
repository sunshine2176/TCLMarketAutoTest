#-*- coding: UTF-8 -*-  

import sys
import time
from common.py_common_keyword.CommonFunctions import CommonFunctions
from selenium.webdriver.common.by import By
from startOperate import startOperate


 
class share_app():
    '''
                                版本 应用商店4.0.1
                               编号 AppStore2-931 
                              标题    分享应用程序
    '''
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
            
            
    def app_update_task(self):
        try:
            self.app_homepage()
            download_task_buttons=self.common_fn.wait_for_elements(r'com.tclmarket:id/manage_image',By.ID)
            download_task_buttons[1].click()
            time.sleep(2)
            print u'go into update task page'
            try:
                app_list_buttons=self.common_fn.wait_for_elements(r'com.tclmarket:id/fold_tag',By.ID)
                if app_list_buttons:
                    app_list_buttons[0].click()
                    try:
                        ignore_button=self.common_fn.wait_for_element(r'com.tclmarket:id/bottom_action_middle')
                        ignore_button.click()
                        time.sleep(2)
                        try:
                            alert_title=self.common_fn.wait_for_element(r'android:id/alertTitle')
                            ok_button=self.common_fn.wait_for_element(r'android:id/button1')
                            if alert_title.text==u'忽略更新':
                                ok_button.click()
                                print u'ignore app update\n'
                            else:
                                print u'the alert is not about ignore\n'
                        except:
                            print u'not get alert page\n' 
                            s = sys.exc_info()
                            print 'Error %s happend on line %d' % (s[1],s[2].tb_lineno)
                    except:
                        print u'not get ignore page\n'
                else:
                    print u'not find any apps to be updated\n' 
                if app_list_buttons:
                    app_list_buttons[0].click()
                    try:
                        share_button=self.common_fn.wait_for_element(r'com.tclmarket:id/bottom_action_left')
                        share_button.click()
                        time.sleep(2)
                        try:
                            alert_title=self.common_fn.wait_for_element(r'android:id/title')
                            if alert_title.text==u'分享':
                                print u'get share list\n'
                                try:
                                    shareBtn=self.common_fn.wait_for_elements(r'android:id/text1',By.ID)
                                    for bluetooth_share in shareBtn:
                                        if bluetooth_share.text == 'Bluetooth':
                                            bluetooth_share.click()
                                            time.sleep(2)
                                            break
                                    try:
                                        open_alert=self.common_fn.wait_for_element(r'com.android.bluetooth:id/content')
                                        if open_alert:
                                            print u'get open bluetooth alert\n'
                                            turn_on_button=self.common_fn.wait_for_element(r'android:id/button1')
                                            turn_on_button.click()
                                            time.sleep(2)
                                    except:
                                        print u'not get open bluetooth alert\n'  
                                        s = sys.exc_info()
                                        print 'Error %s happend on line %d' % (s[1],s[2].tb_lineno)   
                                    
                                    try:
                                        if self.common_fn.driver.current_activity == u'.bluetooth.DevicePickerActivity':
                                            print u'the app can be shared by bluetooth\n'
                                        else:
                                            pass
                                    except:
                                        print u'not get the title\n'    
                                        s = sys.exc_info()
                                        print 'Error %s happend on line %d' % (s[1],s[2].tb_lineno)                                        
                                except:
                                    print u'not get bluetooth share button\n'
                                    s = sys.exc_info()
                                    print 'Error %s happend on line %d' % (s[1],s[2].tb_lineno)                                         
                            else:
                                print u'the alert is not about share\n'
                        except:
                            print u'not get alert page\n'  
                            s = sys.exc_info()
                            print 'Error %s happend on line %d' % (s[1],s[2].tb_lineno)                            
                    except:
                        print u'not get share button\n'
                    try:
                        self.common_fn.driver.back()
                        time.sleep(5)
                        self.common_fn.swipe_screen()
                        try:
                            action_buttons=self.common_fn.wait_for_elements(r'com.tclmarket:id/fold_tag_btn',By.ID)
                            text_buttons=self.common_fn.wait_for_elements(r'com.tclmarket:id/actionOne_text',By.ID)
                            if text_buttons[-1].text==u'取消忽略':
                                print u'get ignored app\n'
                                action_buttons[-1].click()
                                try:
                                    ignore_share=self.common_fn.wait_for_element(r'com.tclmarket:id/bottom_action_left')
                                    ignore_share.click()
                                    time.sleep(2)
                                    try:
                                        alert_title=self.common_fn.wait_for_element(r'android:id/title')
                                        if alert_title.text==u'分享':
                                            print u'get share list\n'
                                            return True  
                                        else:
                                            return False
                                    except:
                                        print u'not get bluetooth share button\n'
                                        s = sys.exc_info()
                                        print 'Error %s happend on line %d' % (s[1],s[2].tb_lineno)                                        
                                except Exception as e:
                                    print e
                                    print u'not find share button\n'    
                            elif text_buttons[-1].text ==u'更新':
                                print u'no ignored app\n'
                                return True
                            else:
                                return False
                        except:
                            print u'no app\n'
                            s = sys.exc_info()
                            print 'Error %s happened on lineno %d' % (s[1],s[2].tb_lineno)
                            return False
                    except:
                        print u'fail to swipe\n'  
                        s = sys.exc_info()
                        print 'Error %s happened on lineno %d' % (s[1],s[2].tb_lineno)                        
                        return False
                else:
                    
                    print u'only one app to be updated\n'  
                    return False
            except:
                print u'not get ignore button'                
        except:
            print u'fail to go into update task page'   
            return False
            
    def run(self):
        start = startOperate()
        return self.common_fn.run_test_case(lambda: self.common_fn.launch_app('4.0.1'),
                                     lambda: start.baseOperate(),
                                     lambda: self.app_update_task())             
    
if __name__ =="__main__":
    test=share_app()
    test.run()         
            
                                
                                           
     
