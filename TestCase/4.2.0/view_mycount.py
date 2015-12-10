# -*- coding: utf-8 -*-
#  AS4-1139:查看我的账户
import sys
from common.py_common_keyword.common_class import common_class


class view_mycount:
    def __init__(self):
        self.con = common_class()
        '''
      try:
         self.driver.switch_to.context("WEBVIEW")
         #self.driver.switch_to.context('NATIVE_APP')    用完后再转回来
         print u'转换控件成功'
      except:
         print u'转换控件失败'
         s = sys.exc_info()
         print s[0]
         print s[1]
         self.driver.quit()
         sys.exit(0)          
      
      try:
         
         current = self.driver.current_context
         print current
         #contexts=self.driver.contexts
         #for context in contexts:
            #print context
      except:
         print u'获取控件失败'
         s = sys.exc_info()
         print s[0]
         print s[1]
         self.driver.quit()
         sys.exit(0)         
      '''

    def check_login(self):
        try:
            me = self.con.driver.find_elements_by_id(r'com.tclmarket:id/menu_item_tv')
            if me[2].text == u'注销账号':
                print u'我的账户变成注销账号，登录成功'
                return True
            else:
                print u'经检查，登录失败'
                return False
        except:
            print u'检查是否已登录，异常'
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
            return False

    def viewmycount(self):
        return self.con.run_test_case(lambda: self.con.launch_app(),
                                      lambda: self.con.launch_menu(),
                                      lambda: self.con.quit_menu(),
                                      lambda: self.con.rank_page(),
                                      lambda: self.con.launch_menu(),
                                      lambda: self.con.quit_menu(),
                                      lambda: self.con.classify_page(),
                                      lambda: self.con.launch_menu(),
                                      lambda: self.con.mycount(),
                                      lambda: self.con.launch_menu(),
                                      lambda: self.check_login(),
                                      lambda: self.con.quit_menu()
                                      )


if __name__ == '__main__':
    test = view_mycount()
    test.viewmycount()
