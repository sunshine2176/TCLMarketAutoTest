# -*- coding: utf-8 -*-
#case通用方法封装

import re
import os
import sys
import time
from appium import webdriver
from CommonFunctions import CommonFunctions
from selenium.webdriver.common.by import By

path = r'E:\app_market_apk\tclmarket-v4.2.0-201505120914.apk'
#new_list = []
class common_class(CommonFunctions):
    def __init__(self):
        CommonFunctions.__init__(self)   
        self.path = path
        self.menu = []
        self.title = []  
        self.icon_temp = []
        self.icon_list= []

    def Install_open_app(self):
        device = {
            'platformName' : 'Android',
            'deviceName': 'BEGQHUBY79EMS8BE',
            'version' : '4.4.2',
            'app': self.path,
            'app-package': 'com.tclmarket',
            'app-activity': r'.sz.activity.WelcomeActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True
            }
        try:
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub',device)
            print 'Install and open success!'
            return True
        except:
            print 'Install app fail!'
            return False
            #sys.exit() 

    def lunach(self):
        time.sleep(5)
        #try:
            #self.driver.find_element_by_id(r'com.tclmarket:id/zero_flow_update_mode_checkbox').click()
        #except:
            #print u'关闭零流量更新失败'
            #s = sys.exc_info()
            #print "Error '%s' happened on line %d" % (s[1],s[2].tb_lineno)
            #return False
            ##self.driver.quit()
        try:
            self.driver.find_element_by_id(r'com.tclmarket:id/start_experience_btn').click()
            time.sleep(13)
        except:
            print 'launch fail!'
            return False
            #self.driver.quit()

        try:
            self.driver.find_element_by_id(r'com.tclmarket:id/cancel').click()
            time.sleep(1)
            print u'点击跳过成功'            
            self.driver.find_element_by_id(r'com.tclmarket:id/negativeButton').click()
            print u'点击暂不更新成功' 
            self.driver.find_element_by_id(r'com.tclmarket:id/positiveButton').click()
            print u'创建快捷方式成功'
            return True
        except:
            try:
                self.driver.find_element_by_id(r'com.tclmarket:id/negativeButton').click()
                print u'点击暂不更新成功'
                self.driver.find_element_by_id(r'com.tclmarket:id/cancel').click()
                print u'点击跳过成功' 
                self.driver.find_element_by_id(r'com.tclmarket:id/positiveButton').click()
                print u'创建快捷方式成功' 
                return True
            except:
                self.driver.find_element_by_id(r'com.tclmarket:id/positiveButton').click()
                print u'创建快捷方式成功'  
                self.driver.find_element_by_id(r'com.tclmarket:id/negativeButton').click()
                print u'点击暂不更新成功'
                self.driver.find_element_by_id(r'com.tclmarket:id/cancel').click()
                print u'点击跳过成功' 
                return True
        
                   

    def entry_seting(self):
        """
        功能描述：进入seting界面
        """
        try:
            network_error = self.wait_for_element(r'com.tclmarket:id/loading_error_info',is_normal_screen=True)
            if network_error.text == u'资源获取失败请重新刷新获取信息...':
                print '资源获取失败请重新刷新获取信息...'
                return False
            else:
                print network_error.text
                return False
        except:
            try:
                self.driver.find_element_by_id(r'com.tclmarket:id/drawer_menu').click()
                time.sleep(1)
                self.driver.find_element_by_id(r'com.tclmarket:id/setting').click()
                time.sleep(1)
                print u'进入设置页面成功'
                return True
            except:
                print u'进入设置页面失败'
                return False
        
    
    def screen_swipe_2(self):
        try:
            x = self.driver.get_window_size()['width']  #获取界面宽度
            y = self.driver.get_window_size()['height']  #获取界面长度
            self.driver.swipe(x/2, y*4/5, x/2, 2*y/5,0)    #设置比例滑屏
            time.sleep(3)
            return True
        except:
            print u'滑屏失败！'
            return False
            #self.driver.quit()
            
            
    def get_elements(self): 
        '''
        功能描述：获取该页界面的元素，并去掉和上一页获取的重复的元素
                 例如：获取该界面的app并去重
        '''
        time.sleep(2)
        try:
            icon_text = []
            self.icon = self.driver.find_elements_by_class_name(r'android.widget.TextView')    
            for i in self.icon:
                icon_text.append(i.text)
            new_list = list(set(icon_text)-set(self.icon_temp))
            
            if new_list:
                for n in new_list:
                    self.icon_list.append(n)
                    print n
                self.icon_temp = icon_text
                return True
            else:
                print u'页面已加载完毕'
                #print self.icon_list
                print u'共找到%s 个活动主题' % len(self.icon_list)
                return False
                #self.driver.quit()                #断开与driver的连接，若重复断开，则会引起异常
                #sys.exit()                     此处退出会引起python也退出，导致robot不会执行下一个case，建议不使用
        except SystemExit:
            return False
            #sys.exit()
        except:
            print u'不能获取到图片'
            s=sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1],s[2].tb_lineno) 
            return False
            #self.driver.quit()
            #sys.exit(0)    


    def get_layout(self,by,value,time_out=20,poll_frequency=1):
        '''
        功能描述：获取“精品、排行、分类”的layout
        '''
        from selenium.webdriver.support.wait import WebDriverWait
        try:
            wait = WebDriverWait(self.driver, time_out, poll_frequency)           #self.driver为实参，调用WebDriverWait时，可以直接将实参传进来，作为默认值。
            #wait.until(lambda s:self.com_find_element(by, value, element_text=element_text)) #com_find_element函数已经使用了实参 self.driver
            self.layout =  wait.until(lambda s:s.find_element(value=value,by=by))     #此处的s只是形参。wait中，将形参driver传给 self._driver,在本文件170中，将实参self.driver传给了driver作为默认参数                    
            print self.layout
            print u'获取layout对象成功'
            return True
        except:
            print u'获取layout对象失败'
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1],s[2].tb_lineno)  
            return False     
        
    def get_objet(self,by,value,time_out=20,poll_frequency=1):
        '''
        根据获得的layout，获取对象元素
        '''
        try:
            from selenium.webdriver.support.wait import WebDriverWait
            wait = WebDriverWait(self.driver,time_out,poll_frequency)
            self.obj=wait.until(lambda x:self.layout.find_elements(value=value,by=by))
            print self.obj             
            print u'获得元素对象成功'
        except:
            print u'获得对象元素失败'
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1],s[2].tb_lineno)               
            
                     
              
    def rank_page(self):
        try:
            self.get_layout(By.ID,r'com.tclmarket:id/tab_indicator',10)            
            self.get_objet(By.CLASS_NAME,r'android.widget.TextView',10)
            self.obj[1].click()
            print u'成功进入排行页面'
            return True
        except:
            print u'进入排行页面失败'
            return False 
               
    def classify_page(self):
        try:
            self.get_layout(By.ID,r'com.tclmarket:id/tab_indicator',10)
            self.get_objet(By.CLASS_NAME,r'android.widget.TextView',10)            
            self.obj[2].click()
            print u'成功进入分类页面'
            return True
        except:
            print u'进入分类页面失败'
            s = sys.exc_info()
            print s[0]
            print s[1]
            return False
            #self.driver.quit()
            #sys.exit()     


    def launch_menu(self):
        time.sleep(2)
        try:
            network_error=self.driver.find_element_by_id(r'com.tclmarket:id/loading_error_info')
            if network_error.text == u'加载失败请检查您的网络连接...':
                print '加载失败请检查您的网络连接...'
                return False
        except:
            try:
                #self.driver.execute_script("mobile: keyevent",{ "keycode": 82 })
                self.driver.press_keycode(82)
                time.sleep(2)
                print u'启动menu成功'
                return True
            except:
                print u'启动menu失败'
                s = sys.exc_info()
                print "Error '%s' happened on line %d" % (s[1],s[2].tb_lineno)                 
                return False
           
                
    def quit_menu(self,direction='down', percent=0.15, duration=None):
        time.sleep(2)
        try:
           #self.driver.press_keycode(4)
            
            '''
            x = self.driver.get_window_size()['width']  #获取界面宽度
            y = self.driver.get_window_size()['height']  #获取界面长度
            self.driver.swipe(x/2, y*3/5, x/2, 13*y/20,0)
            '''
            self.swipe_screen(direction,percent,duration)
            time.sleep(2)
            print u'退出menu成功'
            return True
        except:
            print u'退出menu失败'
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1],s[2].tb_lineno) 
            return False
            #self.driver.quit()
            #sys.exit() 
            
    def get_menu_icon(self):
        '''
        获取menu菜单中的各种元素
        '''
        time.sleep(2)
        try:
            self.menu = self.driver.find_elements_by_id(r'com.tclmarket:id/menu_item_tv')
            print u"获取菜单元素成功"
            return True
        except:
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1],s[2].tb_lineno) 
            return False
            #self.driver.quit()          
            
    def download_page(self):
        '''
        点击进入menu中的 下载页面
        '''
        try:
            self.menu[0].click()
            time.sleep(1)
        except:
            print u'点击下载页面失败'
            return False
            #self.driver.quit()
            #sys.exit()  
                   
        try:
            if self.driver.find_element_by_id(r'com.tclmarket:id/home_title').text == u'下载队列':
                print u'成功跳转到下载任务界面'
                return True
            else:
                print u'跳转到下载任务界面失败'
                return False
                #self.driver.quit()
                #sys.exit()            
        except:
            print u'跳转到下载任务界面失败'
            return False
            #self.driver.quit()
            #sys.exit()      

    
    def seting_page(self):
        time.sleep(3)
        try:
            for m in self.menu:
                print m.text
            self.menu[1].click()
            time.sleep(2)
        except:
            print u'点击设置页面失败'
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1],s[2].tb_lineno)  
            return False
            #self.driver.quit()
            #sys.exit()  
                  
                  
        try:
            if self.driver.find_element_by_id(r'com.tclmarket:id/home_title').text == u'设置':
                print u'成功跳转到设置界面'
                return True
            else:
                print u'跳转到设置界面失败'
                return False
                #self.driver.quit()
                #sys.exit()            
        except:
            print u'跳转到设置界面失败'
            return False
            #self.driver.quit()
            #sys.exit()   
            
    def clearEditText(self,text):
        """
        功能描述：删除文本框中的内容
        1.将光标定位都文本末尾
        2.全选
        3.删除(退格键)
        """
        
        self.driver.press_keycode(123)
        for i in range(len(text)):
            self.driver.press_keycode(67)
        
            
    def network_check(self):
        """
        功能描述：检查当前页面的网络情况
        """
        network_error = self.driver.find_element_by_id(r'com.tclmarket:id/loading_error_info')
        if network_error.text == u'资源获取失败请重新刷新获取信息...':
            print '资源获取失败请重新刷新获取信息...'
            return False
        else:
            print network_error.text
            return False
            
    
    def mycount(self):
        """
        前提：启动功能菜单
        功能描述：
        点击进入我的账户
         
        """
        try:
            self.menu = self.driver.find_elements_by_id(r'com.tclmarket:id/menu_item_tv')
            self.menu[2].click()
            time.sleep(10)
        except:
            print u'点击我的账户失败'
            return False     
          
        try:
            time.sleep(2)
            tool_bar=self.driver.find_element_by_id(r"com.tcl.account:id/toolbar")
            authorize_element=tool_bar.find_element_by_class_name(r"android.widget.TextView")         
            
            if authorize_element.text=="Authorize":
                self.driver.find_element_by_id(r"com.tcl.account:id/switch_account").click()
                te=self.driver.find_elements_by_class_name(r'android.widget.EditText')
                time.sleep(1)
                text = te[0].text             
                if text:
                    self.clearEditText(text)
                    te[0].send_keys(u'zhoupei.he@tcl.com')
                    te[1].send_keys(u'a123456789')
                    self.driver.find_element_by_id(r'com.tcl.account:id/login_btn').click()
                else:
                    te[0].send_keys(u'zhoupei.he@tcl.com')
                    te[1].send_keys(u'a123456789')
                    self.driver.find_element_by_id(r'com.tcl.account:id/login_btn').click()               
            elif authorize_element.text=="Login":
                te=self.driver.find_elements_by_class_name(r'android.widget.EditText')
                time.sleep(1)          
                text = te[0].text
                print text
                if text:
                    self.clearEditText(text)
                    te[0].send_keys(u'zhoupei.he@tcl.com')
                    te[1].send_keys(u'a123456789')
                    self.driver.find_element_by_id(r'com.tcl.account:id/login_btn').click()
                else:
                    te[0].send_keys(u'zhoupei.he@tcl.com')
                    te[1].send_keys(u'a123456789')
                    self.driver.find_element_by_id(r'com.tcl.account:id/login_btn').click()              
               
            time.sleep(20)
            self.get_layout(By.ID,r'com.tclmarket:id/tab_indicator',10)            
            self.get_objet(By.CLASS_NAME,r'android.widget.TextView',10)
                                    
            if self.obj[0].text==u"精品": 
                print u'登录成功'
                return True
            else:
                print u'登录失败'
                return False
        except:
            try:
                te=self.wait_for_elements(r'android.widget.EditText',by=By.CLASS_NAME)
                print te
                te[0].send_keys(u'zhoupei.he@tcl.com')
                te[1].send_keys(u'a123456789')
                self.driver.find_element_by_class_name(r'android.widget.Button').click()
                time.sleep(10)
                self.get_layout(By.ID,r'com.tclmarket:id/tab_indicator',10)            
                self.get_objet(By.CLASS_NAME,r'android.widget.TextView',10)                
                if self.obj[0].text==u"精品": 
                    print u'登录成功'
                    return True
                else:
                    print u'登录失败'
                    return False                
            except:
                print u'登录异常，失败'
                s = sys.exc_info()
                print "Error '%s' happened on line %d" % (s[1],s[2].tb_lineno)                    
                return False  
        
    def entry_search_box(self):
        try:
            self.network_check()
        except:
            try:
                self.wait_for_element(r'com.tclmarket:id/home_container').click()
                time.sleep(1)
                return True
            except:
                print u'点击进入输入框失败'
                s = sys.exc_info()
                print "Error '%s' happened on line %d" % (s[1],s[2].tb_lineno)  
                return False

        

if __name__ =='__main__':
                
    test = common_class()
    test.Install_open_app()
    test.lunach()
    test.swipe_screen()