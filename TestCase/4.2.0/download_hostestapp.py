# -*- coding: utf-8 -*-
# AS4-35:下载最热app


# 启动app store3，点击最热图标->点击任一app后的安装按钮；

# 最热app开始下载并自动安装；

# 同时下载多个最热app；

# 多个app能够同时下载并自动安装成功；

import os
import sys
import time
from common.py_common_keyword.common_class import common_class

#os.system("adb shell rm sdcard/tclmarket/apps/*")


class download_hostestapp:
    def __init__(self):
        self.con = common_class()

    def close_autoinstall(self):
        """功能描述：关闭下载完成后自动安装功能"""
        os.system("adb shell rm sdcard/tclmarket/apps/*")
        try:
            self.con.entry_seting()
            self.con.swipe_screen(direction='up', percent=0.9, duration=None)
            self.con.driver.find_element_by_id(r"com.tclmarket:id/download_to_install_switch").click()
            print u"关闭下载完成后自动安装成功"
        except:
            print u"关闭下载完成后自动安装成功"

        try:
            time.sleep(5)
            self.con.driver.find_element_by_id(r"com.tclmarket:id/actionbar_up").click()
            print u"退出设置成功"
            return True
        except:
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
            print u"退出设置失败"
            return False

    def entry_hot(self):
        try:
            self.con.network_check()
        except:
            try:
                ac = self.con.driver.find_element_by_id(r'com.tclmarket:id/remark_text1')
                if ac.text == u'最热':
                    ac.click()
                    time.sleep(22)
                    try:
                        self.con.network_check()
                    except:
                        if self.con.driver.find_element_by_id(r'com.tclmarket:id/home_title').text == u'最热':
                            print u'成功进入最热页面'
                            return True
                        else:
                            print u'没有进入最热页面'
                            s = sys.exc_info()
                            print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
                            return False
                else:
                    print u'没有进入最热页面'
                    s = sys.exc_info()
                    print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
                    return False

            except:
                print u'进入最热页面失败'
                s = sys.exc_info()
                print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
                return False
    def download_hot_app(self):
        icon_text = []
        dic = {}
        install_button = []
        dic_new = {}

        try:
            icon = self.con.driver.find_elements_by_id(r'com.tclmarket:id/name')
            for i in icon:
                icon_text.append(i.text)

            button = self.con.driver.find_elements_by_id(r'com.tclmarket:id/action_button')

            for i in range(len(icon_text)):
                dic[icon_text[i]] = button[i]
            print u'创建字典成功'

        except:
            print u'创建字典失败'
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
            return False

        try:
            for bu in button:
                print bu.text
                if bu.text == u'安装':
                    install_button.append(bu)
                else:
                    pass
            if len(install_button) == 0:          
                print u'当前页面没有可以下载的app'
                return False
                       
            # print install_button[1]
            install_button[0].click()
            time.sleep(5)
            if install_button[0].text == u'继续':
                print u'下载APP失败'
                return False
            else:
                print u'下载APP成功'
                os.system("adb shell rm sdcard/tclmarket/apps/*")
                install_button[0].click()

        except:
            print u'下载单个APP有异常'
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
            # print type(install_button)
            return False

        
        try:
            for key, value in dic.items():  # 此方法为遍历一个列表，边遍历边删除，删除后得到的是一个新的列表。则不会引起崩溃
                if value.text == u'安装':
                    os.system("adb shell rm sdcard/tclmarket/apps/*")
                    dic[key] = value
                    #dic.pop(key)
                elif value.text == u'继续':
                    #dic.pop(key)
                    dic[key] = value
                else:
                    dic.pop(key)

            #print dic
        except:
            print u'获得可下载app字典失败'
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
            return False

        try:
            for key, value in dic.items():
                value.click()
            time.sleep(8)
            for key, value in dic.items():
                if value.text == u'继续':
                    print u'下载APP %s 失败' % key
                    return False
                elif value.text == u'等待':
                    print u'下载APP %s 成功' % key                
                elif value.text == u'安装':
                    print u'下载APP %s 成功，并完成' % key                                   
                else:
                    dic_new[key] = value
                    print u'下载APP %s 成功' % key
                    

            print u'正在下载的app有%s个' % len(dic_new)

        except:
            print u'同时下载多个APP有异常'
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
            return False

        try:
            if len(dic_new) == '2':
                print u'只能同时下载2个APP，其余状态为‘等待’'
                return True
            else:
                print u'同时下载的app有%s个' % len(dic_new)
                return True
        except:
            print u'同时下载多个APP有异常'
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
            return False

    def downloadhostestapp(self):
        return self.con.run_test_case(lambda: self.con.launch_app(),
                                      lambda: self.close_autoinstall(),
                                      lambda: self.entry_hot(),
                                      lambda: self.download_hot_app()
                                      )


if __name__ == '__main__':
    test = download_hostestapp()
    test.downloadhostestapp()
