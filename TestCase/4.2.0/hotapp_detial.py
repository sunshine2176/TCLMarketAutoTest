# -*- coding: utf-8 -*-
# AS4-34:查看最热app详情

import sys
import time
from common.py_common_keyword.common_class import common_class


class hotapp_detial():
    def __init__(self):
        self.con = common_class()

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

    def view_hot(self):
        try:
            icon_text = []
            icon = self.con.driver.find_elements_by_id(r'com.tclmarket:id/name')
            for i in icon:
                icon_text.append(i.text)

            print icon_text[2]

        except:
            print u'不能获取到指定APP的名称'
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
            return False

        try:
            icon[2].click()
            time.sleep(22)
            if self.con.driver.find_element_by_id(r'com.tclmarket:id/home_title').text == icon_text[2]:
                print u'进入软件 %s 成功，软件title 获取正常' % icon_text[2]
            else:
                print u'进入软件 %s 失败，实际进入的软件为：%s' % (icon_text[2],self.con.driver.find_element_by_id(r'com.tclmarket:id/home_title').text)
                return False
        except:
            print u'进入软件 %s 异常，不能获取其title' % icon_text[2]
            return False
        
        try:
            if self.con.driver.find_element_by_id(r'com.tclmarket:id/name').text == icon_text[2]:
                print u'进入软件 %s 成功,软件名称获取正常' % icon_text[2]
            else:
                print u'获取到软件名称为： %s ,与软件title %s不一致' %(self.con.driver.find_element_by_id(r'com.tclmarket:id/name').text,self.con.driver.find_element_by_id(r'com.tclmarket:id/home_title').text) 
                return False
        except:
            print u'加载软件 %s 的名称出现异常' % icon_text[2]
            return False            
        
        try:
            self.con.driver.find_elements_by_id(r'com.tclmarket:id/app_detail_item_img')
            print u'加载软件的图片正常'
        except:
            print u'加载软件 %s 的图片失败' % self.con.driver.find_element_by_id(r'com.tclmarket:id/name').text
            return False

        try:
            self.con.driver.find_element_by_id(r'com.tclmarket:id/description_title_tv')
            print u'获取软件的 功能介绍 正常'
        except:
            print u'获取软件的 功能介绍 失败'
            return False

        try:
            self.con.driver.find_element_by_id(r'com.tclmarket:id/version_title_tv')
            print u'获取软件的 版本信息及大小 正常'
        except:
            print u'获取软件的 版本信息及大小 失败'
            return False

        try:
            self.con.driver.find_element_by_id(r'com.tclmarket:id/action_down_button')
            print u'获取软件的 安装按钮 正常'
            return True
        except:
            print u'获取软件的 安装按钮 失败'
            return False

    def exit_hot(self):
        try:
            self.con.driver.find_element_by_id(r'com.tclmarket:id/actionbar_up').click()
            time.sleep(2)
            if self.con.driver.find_element_by_id(r'com.tclmarket:id/home_title').text == u'飙升':
                print u'退出app详情成功'
                return True
            else:
                print u'退出app详情失败'
                return False

        except:
            print u'退出app详情失败'
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
            return False

    def hotappdetial(self):
        return self.con.run_test_case(lambda: self.con.launch_app(),
                                      lambda: self.entry_hot(),
                                      lambda: self.view_hot())


if __name__ == '__main__':
    test = hotapp_detial()
    test.hotappdetial()
