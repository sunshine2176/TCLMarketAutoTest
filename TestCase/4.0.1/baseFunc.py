#coding:utf-8

from selenium.webdriver.common.by import By
from common.py_common_keyword.CommonFunctions import CommonFunctions
import sys
import time

class baseFunc:
    """基本功能类"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.common_fn = CommonFunctions()
        
    #----------------------------------------------------------------------
    def uninstallAPP(self,name):
        """卸载指定应用"""
        isHome = False
        while not isHome:
            self.common_fn.driver.keyevent('4')
            time.sleep(2)
            if self.common_fn.driver.current_activity == '.activity.MarketHomeActivity':
                isHome = True
        print 'uninstall app'
        time.sleep(5)
        tabs = self.common_fn.com_find_element(r'android:id/tabs')
        tabs.find_element(By.NAME,u'管理').click()
        action_buttons=self.common_fn.wait_for_elements(r'com.tclmarket:id/manage_image',By.ID)
        action_texts=self.common_fn.wait_for_elements(r'com.tclmarket:id/manage_text',By.ID)
        if action_texts[2].text==u'已安装' :
            action_buttons[2].click()
            time.sleep(2)
            print u'get installed apks page\n'
            self.findByName(name)
        else:   
            print u'not get installed apks page\n'
            return False        

            #print self.common_fn.com_find_element(name,By.NAME)

        #----------------------------------------------------------------------
    def findByName(self,name):
        """查找指定应用列表"""
        try:
            isLast = False
            lastAPP = ''
            while not isLast:
                apps = self.common_fn.wait_for_elements(r'android.widget.RelativeLayout',By.CLASS_NAME)
                for i in range(len(apps)):
                    #print '------------',apps[i].find_element(By.ID,r'com.tclmarket:id/name').text
                    try:
                        if apps[i].find_element(By.ID,r'com.tclmarket:id/name').text == name:
                            apps[i].find_element(By.ID,r'com.tclmarket:id/actionOne').click()
                            self.common_fn.element_clk('OK',By.NAME)
                            return True
                    except:
                        s = sys.exc_info()
                        print 'Error "%s" happend on line %d' % (s[1],s[2].tb_lineno)
                newLastAPP = apps[-1].find_element(By.ID,r'com.tclmarket:id/name').text
                if lastAPP == newLastAPP:
                    return False
                lastAPP = newLastAPP
                self.common_fn.swipe_screen(percent=0.7,duration=2000)
        except:
            s = sys.exc_info()
            print 'Error "%s" happend on line %d' % (s[1],s[2].tb_lineno)
        
    