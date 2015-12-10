# -*- coding: utf-8 -*-
# tclmarket 公共方法存放地方
import os
import sys
import ConfigParser
from appium import webdriver
import time
import re
from selenium.webdriver.common.by import By


class CommonFunctions(object):
    driver = None
    program_path = ''
    err_image_path = ''

    def __init__(self):
        self.programName = 'TCLMarketAutoTest'
        self.version = ''


    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(CommonFunctions, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

    def get_run_version(self):
        run_argu = open(os.path.join(self.program_path, 'config/runArgument.txt'))
        for line in run_argu.readlines():
            if re.match('^--include=(.*)', line):
                version = line[line.find('--include=')+len('--include='):]
                run_argu.close()
                self.version = version.replace('\n', '')
                break
        return self.version



    def get_app_file(self):
        """
        功能描述：获取version版本的apk路径
        :param version: 版本号
        :return: apk路径
        作者：wei.y
        """
        app_dir = self.program_path + 'app' + os.path.sep
        list_files = os.listdir(app_dir)
        for app_file in list_files:
            if os.path.isfile(app_dir + app_file):
                # 使用正则表达是匹配相应的apk文件（注意：app文件夹下面一个版本只能放一个apk文件，否则会出现异常）
                matchobj = re.match('(.*)' + self.version + '(.*)\.apk$', app_file)
                if matchobj:
                    return app_dir + app_file
        return ''

    def init_devices(self):
        """
         功能：初始化设备信息;
         参数：version:版本号
         返回值：设备信息的字典对象；
         作者：wei.y
        """
        app_path = self.get_app_file()
        self.err_image_path = self.program_path + 'image' + os.sep
        if os.path.isdir(self.program_path):
            config_file = os.path.join(self.program_path, 'config/conf.ini')
            config = ConfigParser.ConfigParser()
            config.readfp(open(config_file))
            device = {
                'platformName': config.get("Device", "platformName"),
                'deviceName': config.get("Device", "deviceName"),
                'version': config.get("Device", "version"),
                'app': app_path,
                'app-package': config.get("Device", "app-package"),
                'app-activity': config.get("Device", "app-activity"),
                'unicodeKeyboard': config.get("Device", "unicodeKeyboard"),
                'resetKeyboard': config.get("Device", "resetKeyboard")
            }
            return device

    def get_driver(self):
        """
         功能：安装并打开app;
         参数：version:版本号
         返回值：driver 对象
         作者：wei.y
        """
        device = self.init_devices()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', device)
        print 'Install and open success!'
        return self.driver

    def launch_app(self, version=None):
        """
         功能：清除app运行后;
         参数：version:版本号
         返回值：无执行结果
         作者：wei.y

        """
        if version:
            self.version = version
        print " start launch_app "
        # pwd = os.getcwd()
        pwd = sys.argv[-1]
        self.program_path = pwd[0:(pwd.index(self.programName) + len(self.programName))] + os.path.sep
        if version is None:
            version = self.get_run_version()
        print self.version
        self.get_driver()

        time.sleep(2)
        #判断是否出现获取root权限的弹出框，如果存在，点击允许按钮
        get_root = self.wait_for_element('com.kingroot.kinguser:id/button_allow')
        if get_root:
            get_root.click()
        else:
            print u'未出现申请root权限弹出框'

        if re.match('^4.2.*', version):
            return self.launch_4_2_0()
        elif re.match('^4.3.*', version):
            return self.launch_4_3_0()
        elif re.match('^4.0.*', version):
            return self.launch_4_0_1()
        elif re.match('^4.1.*', version):
            return self.launch_4_1_0()
        else:
            raise Exception('No such version Launch function')

    def launch_4_0_1(self):
        """
        功能：4.0.1版本的launch方法

        :return: 执行结果
        """
        is_click_succ1 = self.element_clk(r'android:id/button1', message='click the "ok" button of reminder',
                                          err_message='not find the rButton')
        #is_click_succ2 = self.element_clk(r'com.tclmarket:id/negativeButton', message='not create the quick icon',
                                          #err_message='not find the create quick icon remind')

        return is_click_succ1

    def launch_4_0_4(self):
        """
        功能：4.0.4版本的launch方法

        :return: 执行结果
        """

        is_click_succ1 = self.element_clk(r'android:id/button1', message='click the "ok" button of reminder',
                                          err_message='not find the rButton')
        is_click_succ2 = self.element_clk(r'com.tclmarket:id/negativeButton', message='not create the quick icon',
                                          err_message='not find the create quick icon remind')
        # is_click_succ3 = self.element_clk(r'android:id/button2',message='refuse to update the app store',
        # err_message='not find the update remind')
        return is_click_succ1 and is_click_succ2  # and is_click_succ3

    def launch_4_1_0(self):
        """
        功能：4.0.1版本的launch方法

        :return: 执行结果
        """
        self.element_clk(value='com.tclmarket:id/start_experience_btn',
                         err_message='you are not first time to launch app')
        self.element_clk(value='android:id/button2')
        self.element_clk(value='com.tclmarket:id/positiveButton',
                         err_message='The shortcut has been created')
        try:
            self.wait_for_element(value='com.tclmarket:id/remark1')
        except:
            print "Launch the appstore failure."
            return False
        return True

    def launch_4_2_0(self):
        """
        功能：4.2.0版本的launch方法

        :return: 执行结果
        """

        time.sleep(2)
        self.swipe_screen(direction='left')
        self.swipe_screen(direction='left')
        self.swipe_screen(direction='left')
        #self.element_clk(value=r'com.tclmarket:id/zero_flow_update_mode_checkbox')
        self.element_clk(value=r'com.tclmarket:id/start_experience_btn')
        time.sleep(5)
        click_result = {'is_cancel_click': False,
                        'is_negative_click': False,
                        'is_positive_click': False}

        for i in range(0, 3, 1):
            if (not click_result.get('is_cancel_click')) and \
                    self.element_clk(r'com.tclmarket:id/cancel', message='cancel click success'):  # 跳过按钮
                click_result['is_cancel_click'] = True
            try:
                time.sleep(2)
                if not click_result.get('is_negative_click'):
                    negative_button = self.wait_for_element(value=r'com.tclmarket:id/negativeButton')
                    if negative_button.text == u'暂不更新':
                        negative_button.click()
                        print u'点击暂不更新成功'
                        click_result['is_negative_click'] = True
                    else:
                        print u"Can't find the button '暂不更新' "
            except:
                print u"Can't find the button '暂不更新' "

            try:
                time.sleep(2)
                if not click_result.get('is_positive_click'):
                    positive_button = self.wait_for_element(value=r'com.tclmarket:id/positiveButton')
                    if positive_button.text == u'确定':
                        positive_button.click()
                        print "Create a shortcut success"
                        click_result['is_positive_click'] = True
                    else:
                        print u"Can't find the button '确定' "
            except:
                print u"Can't find the button '确定' "
        time.sleep(2)
        if self.wait_for_element(r'com.tclmarket:id/drawer_menu'):
            print 'install and launch successful'
            return True
        else:
            return False

    def launch_4_3_0(self):
        """
        功能：4.3.0版本的launch方法

        :return: 执行结果
        """
        # time.sleep(2)
        # self.swipe_screen(direction='left')
        # self.swipe_screen(direction='left')
        # self.swipe_screen(direction='left')
        return self.launch_4_2_0()

    def element_clk(self, value, by=By.ID, message='element click success',
                    err_message='An element could not be located on the page using the given search parameters.',
                    timeout=10, is_normal_screen=False, element_text=None):
        """
        功能描述：根据value 找到元素并点击
        参数：value:元素查找匹配字符，by：查找方式，message：成功后打印信息,err_message：出现异常打印信息，
            timeout:查找元素超时时间，element——text：元素的text，默认为空
        返回值：True 表示执行点击操作成功，False：执行查找元素并点击操作失败
        作者：wei.y
        """
        try:
            time.sleep(2)
            im_exp_btn = self.wait_for_element(by=by, value=value, time_out=timeout,
                                               is_normal_screen=is_normal_screen, element_text=element_text)
            if im_exp_btn:
                im_exp_btn.click()
                print message
                return True

        except:
            print err_message
        return False

    def app_quit(self):
        """
        功能描述：退出app
        参数：无
        返回值：无
        作者：wei.y
        """
        if self.driver:
            self.driver.quit()

    def swipe_screen(self, direction='up', percent=0.9, duration=None):
        """
        功能描述：滑屏操作，默认冲percent位置滑到屏幕的整个的1/10处
        参数 direction：滑屏的方向，目前只支持上下左右，分别传递up,dowm,right,left
             percent:滑屏的的距离，传递屏幕的相对比例
             - duration - (optional) time to take the swipe, in ms.
        """
        time.sleep(1)
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        if direction == 'up':
            self.driver.swipe(x / 2, y * percent, x / 2, y / 10, duration)
        elif direction == 'down':
            self.driver.swipe(x / 2, y / 10, x / 2, y * percent, duration)
        elif direction == 'right':
            self.driver.swipe(x / 10, y / 2, x * percent, y / 2, duration)
        else:  # left
            self.driver.swipe(x * percent, y / 2, x / 10, y / 2, duration)

    def com_find_element(self, value, by=By.ID, element_text=None, is_ignore_case=False):
        element = self.driver.find_element(by=by, value=value)
        if element_text is None:
            return element

        if element_text:
            if not is_ignore_case:
                if element_text == element.text:
                    return element
            else:
                if element_text.upper() == element.text.upper():
                    return element
        return None


    def wait_for_element(self, value, by=By.ID, time_out=10,
                         poll_frequency=1, is_normal_screen=False, element_text=None, error_msg=u'查找元素异常'):
        """
        功能描述：等待元素出现，并返回该元素，未找到返回None
        参数：exp：查找相关字符 ，by：查找方式，time_out：超时时间，poll_frequency：查找间隔时间
             is_normal_screen 正常找到元素是否截图
        返回值：查找到的webElement
        作者：wei.y
        """
        try:
            from selenium.webdriver.support.wait import WebDriverWait
            wait = WebDriverWait(self.driver, time_out, poll_frequency)
            web_element = wait.until(lambda x: self.com_find_element(by=by, value=value, element_text=element_text))
            if is_normal_screen:
                self.get_screen(exp_name='normal_image_%s' % value)
            # if element_text and element_text != web_element.text:
            #     return None
            return web_element
        except Exception, e:
            print error_msg
            print '%s:%s' % (Exception.message, e)
            self.get_screen(exp_name='not_find_err_%s' % value)
            return None

    def wait_for_elements(self, value, by=By.CLASS_NAME,
                          time_out=10, poll_frequency=1, is_normal_screen=False, error_msg=u'查找元素异常'):
        """
        功能描述：等待一组元素出现，并返回该组元素，未找到返回None
        参数：exp：查找相关字符 ，by：查找方式，time_out：超时时间，poll_frequency：查找间隔时间
        返回值：查找到的webElements
        作者：wei.y
        """
        try:
            from selenium.webdriver.support.wait import WebDriverWait
            wait = WebDriverWait(self.driver, time_out, poll_frequency)
            web_elements = wait.until(lambda d: d.find_elements(by=by, value=value))
            if is_normal_screen:
                self.get_screen(exp_name='normal_image')
            return web_elements
        except Exception, e:
            print error_msg
            self.get_screen(exp_name='not_find_err')
            print '%s:%s' % (Exception.message, e)
            return None

    def get_screen(self, exp_name='', save_path=''):
        """
        功能描述：截屏
        参数：exp_name图片保存前缀名
        :rtype : object
        """
        if self.driver is None:
            return
        if save_path == '':
            save_path = self.err_image_path
        crt_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
        self.driver.get_screenshot_as_file(filename=save_path + exp_name + crt_time + '.jpg')

    def run_test_case(self, *logic_methods):
        """
        功能描述：统一处理测试用例调用是断言，以及出现断言异常的处理并截图
        参数：*logic_methods：测试用例需要调用的方法；
        eg：
            test = CommonFunctions()
            test.run_test_case(lambda: test.launch_app('4.0.1'))
            在类的方法中直接调用：
            CommonFunctions().run_test_case(lambda: self.launch_app('4.0.1'))
        :rtype : object
        """
        print 'start run test case '
        try:
            if logic_methods:
                for method in logic_methods:
                    assert method()
            return True
        except:
            self.get_screen('assert_err')
            a = sys.exc_info()
            print a[0]
            print a[1]
            return False
        finally:
            self.app_quit()



if __name__ == '__main__':
    test = CommonFunctions()
    test.run_test_case(lambda:  test.launch_app('4.3.0'))
    # print time.strftime('%Y%m%d%H%M%S')
    # print test.get_run_version()
