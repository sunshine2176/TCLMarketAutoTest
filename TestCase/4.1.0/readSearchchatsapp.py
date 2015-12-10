# -*- coding: utf-8 -*-
from appium import webdriver
import time
from loadApp import *


class readSearchchatsapp:
    def __init__(self):
        self.com = CommonFunctions()

    def readSearchchatsapp(self):

        button = self.com.wait_for_element('com.tclmarket:id/actionbar_search')
        button.click()
        time.sleep(5)

        loadApp().loadApp()

        try:
            apps = self.com.driver.find_elements_by_id('com.tclmarket:id/name')
            for a in apps:
                if a.text != '':
                    a.click()
                    time.sleep(5)
                    break
            return True
        except:
            print 'Abnormal search rankings'
            return False

    def readapVerify(self):
        try:
            button = self.com.wait_for_element(value='com.tclmarket:id/description_title_tv', element_text=u'功能介绍')
            if button:
                print 'You check the application successfully'
                return True
            return False
        except:
            print 'Details page displays abnormal'
            return False

    def run_readSearchchatsapp(self):
        return self.com.run_test_case(lambda: self.com.launch_app(),
                                      lambda: self.readSearchchatsapp(),
                                      lambda: self.readapVerify())
if __name__ == '__main__':
    print readSearchchatsapp().run_readSearchchatsapp()
