# -*- coding: utf-8 -*-
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os
import sys
import time
from common.py_common_keyword.CommonFunctions import CommonFunctions

class CommonFunctions_wll(CommonFunctions):
    def __init__(self):
        CommonFunctions.__init__(self)
        self.download = None
        self.apps = None

    def Launch_LabelPage(self, label):
        '''
        功能：启动任一标签页
        参数：label:标签名称（如必备）
        返回值：无
        作者：liling.wang
        '''
        try:
            frame = self.driver.find_element_by_id('com.tclmarket:id/remark_layout')
            buttons = frame.find_elements_by_class_name('android.widget.TextView')
            flag = False
            for button in buttons:
                if button.text == label:
                    button.click()
                    flag = True
                    break
            if not flag:
                return False

            WebDriverWait(self.driver, 20).until(lambda d: d.find_elements_by_id('com.tclmarket:id/name'))
            title = self.driver.find_element_by_id('com.tclmarket:id/home_title')
            if title.text == label:
                print 'must page display normally'
                return True
            else:
                print 'must page display abnormally'
                return False
        except:
            return False

    def Check_ad_Page(self):
        """
        功能：启动广告页并检测是否显示在正常
        参数：无
        返回值：无
        作者：liling.wang
        """
        try:
            import re
            if re.match('^4.1.*', self.version):
                banner = self.wait_for_element('com.tclmarket:id/banner2')
            elif re.match('^4.2.*', self.version):
                banner_parent = self.wait_for_element('com.tclmarket:id/banner_layout')
                banner = banner_parent.find_element_by_class_name('android.widget.ImageView')
            else:
                banner = self.wait_for_element('com.tclmarket:id/banner2')
            banner.click()
            time.sleep(3)
            activity = self.driver.current_activity
            if activity == u'.activity.AppDetailActivity':
                con = self.driver.find_element_by_id('com.tclmarket:id/description_title_tv')
                if con:
                    print 'you have entered appdetailpage'
                    return True
                else:
                    print 'Network is unavaliable'
                    return False

            else:
                app_list = self.driver.find_element_by_id('com.tclmarket:id/app_info_layout')
                if app_list:
                    print 'you have entered the subject page'
                    return True
                else:
                    print 'Network is unavaliable'
                    return False

        except:
            s = sys.exc_info()
            print 'Error "%s" happend on line %d' % (s[1], s[2].tb_lineno)
            return False

    def Check_App_Detail(self):
        """
        功能：启动广告页并检测是否显示在正常
        参数：无
        返回值：无
        作者：liling.wang
        """

        # 获取当前页面的app,若app名称不为空时就点击app，为空则抛出异常
        try:
            apps = self.driver.find_elements_by_id('com.tclmarket:id/name')
            for app in apps:
                if app.text != '':
                    appname = app.text
                    app.click()
                    time.sleep(5)
                    break
                else:
                    print 'no app in must page'
                    return False

                    # 验证详情页面是否显示正常
            detailtitle = self.driver.find_element_by_id('com.tclmarket:id/home_title')
            if detailtitle.text == appname:
                print 'you have entered appdetailpage'
                return True
            else:
                print 'you have entered wrong'
                return False
        except:
            s = sys.exc_info()
            print 'Error "%s" happend on line %d' % (s[1], s[2].tb_lineno)
            return False

    # 不受屏幕大小限制的滑动方式

    def swipe_page_to_end(self):
        """
        功能：滑动页面，加载出所有的app
        参数：无
        返回值：无
        作者：liling.wang
        """
        new_app = ''  # 定义一个空字符串，用于存放app列表中的最后一个
        old_app = []  # 定义一个空列表，用于存放加载出来的app的名称

        while True:
            try:
                apps = self.driver.find_elements_by_id('com.tclmarket:id/name')
                for app in apps:
                    name = app.text
                    print name
                    old_app.append(name)
                if old_app[-1] != new_app:
                    new_app = old_app[-1]
                    self.swipe()
                else:
                    print 'you load all app on the page'
                    return True
            except:
                return False

    def swipe(self):  # 不受屏幕大小限制的滑动方式

        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x / 2, y * 4 / 5, x / 2, 1 * y / 3, 0)
        time.sleep(5)

    def Check_App_Status(self):
        """
        功能：检测当前页面app的安装状态，如果当前页面的app是打开则打印出提示文字，若有未安装的app则点击安装并返回True
        参数：无
        返回值：无
        作者：liling.wang
        """
        os.system("adb shell rm -rf /sdcard/tclmarket/apps")  # 删除手机内存中tclmarket下的app文件夹
        activity = self.driver.current_activity
        flag = True
        while flag:
            try:
                download_buttons = self.driver.find_elements_by_id('com.tclmarket:id/action_button')
                for download in download_buttons:
                    if download.text == u'打开':
                        print 'The app had been installed in device'
                        if activity == u'.activity.AppDetailActivity':
                            return False
                    else:
                        flag = False
                        download.click()
                        self.download = download
                        return True
                self.swipe()
            except:
                s = sys.exc_info()
                print 'Error "%s" happend on line %d' % (s[1], s[2].tb_lineno)
                return False

    def Check_Downloading(self):
        """
        功能：#每隔5S检测一次安装状态，当页面取不到download按钮时退出循环
        参数：无
        返回值：无
        作者：liling.wang
        """
        while True:
            try:
                print self.download.text
                import re
                if self.download.text == u'暂停' or re.match('*%$', self.download.text):
                    print 'Downloading is ongoing'
                elif self.download.text == u'继续':
                    if not self.click(self.download):
                        return False

                elif self.download.text == u'安装':
                    print 'Downloading is completed'
                    return True
                else:
                    print 'Downloading is False'
                    return False

            except:
                button = self.wait_for_element(value='android:id/action_bar_title', element_text='Package Installer')
                if button:
                    print 'Downloading is completed1'
                    return True
                else:
                    button1 = self.wait_for_element(value='com.android.packageinstaller:id/ok_button',
                                                    element_text='Next')
                    if button1:
                        print 'Downloading is completed2'
                        return True
                return False
            time.sleep(5)

    def click(self, element):
        count = 2
        element.click()
        for i in range(count):
            if element.text == u'暂停':
                return True
            if element.text == u'继续':
                element.click()
        return False

    def Check_Installing(self):
        """
        功能：每隔3S检测一次安装是否完成
        参数：无
        返回值：无
        作者：liling.wang
        """

        try:
            time.sleep(2)
            button = self.driver.find_element_by_id('com.android.packageinstaller:id/ok_button')
            while button.text == u'Next':
                button.click()
            button.click()

            while True:
                try:
                    b = self.driver.find_element_by_id('com.android.packageinstaller:id/center_text')
                    time.sleep(2)
                    if b.text == u'App installed.':
                        print 'install completed'

                        return True
                    elif b.text == u'Installing…':
                        print 'Install is ongoing'

                    else:
                        print 'package is wrong'
                        return False
                    time.sleep(3)

                except:
                    print 'Install is not start'
                    return False

        except:
            return False
            # open=self.driver.find_element_by_id('com.android.packageinstaller:id/launch_button')
            # if open:
            # print 'The app had been installed in device'
