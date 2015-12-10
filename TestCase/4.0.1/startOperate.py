#coding:utf-8

from common.py_common_keyword.CommonFunctions import CommonFunctions
from selenium.webdriver.common.by import By
import time


class startOperate():
    """4.0.1启动类"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.common_fn = CommonFunctions()
        
    #----------------------------------------------------------------------
    def baseOperate(self):
        """4.0.1版本基本操作"""
        
        #关闭升级提示
        if not self.common_fn.wait_for_element(r'android:id/alertTitle',By.ID) == None:
            print 'find alertTitle'
            self.common_fn.element_clk(r'android:id/button2')
            
        time.sleep(5)
        
        return True
    
    