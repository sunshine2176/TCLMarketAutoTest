# -*- coding: utf-8 -*-
# AS4-977:搜索有效字符

import re
import sys
import time
from common.py_common_keyword.common_class import common_class
import chardet
# content = [u'H&M',u'浏览器'，u'%%^&#']
content = u'浏览器'
reload(sys)
sys.setdefaultencoding("utf-8")


class effective_search():
    def __init__(self, content=content):
        self.con = common_class()
        self.content = content

    def input_search(self):

        try:
            inputElement = self.con.wait_for_element(r'com.tclmarket:id/search_editor')
            inputElement.send_keys(self.content)
            self.con.driver.find_element_by_id(r'com.tclmarket:id/actionbar_search').click()
            time.sleep(3)
            return True
        except:
            print u'搜索失败，请检查网络'
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
            return False

    def analysis_result(self):
        """
        功能描述：将搜索出的所有APP依次遍历，找到匹配的，搜索成功。找不到匹配的，用例失败
        """
        self.app_names_temp = []
        all_apps = []
        match = []
        try:
            time.sleep(20)
            apps = self.con.driver.find_elements_by_class_name(r'android.widget.TextView')
            for a in apps:
                print a.text
                if a.text == u'搜索无结果':
                    print u'搜索无结果'
                    return False
                else:
                    continue

            while True:
                app_names = []
                apps = self.con.driver.find_elements_by_id(r'com.tclmarket:id/name')
                for a in apps:
                    app_names.append(a.text.replace(u'\xa0', u' '))
                new_app = list(set(app_names) - set(self.app_names_temp))
                self.app_names_temp = app_names

                if new_app:
                    for al in new_app:
                        all_apps.append(al)
                    
                    time.sleep(2)
                    self.con.swipe_screen(direction='up', percent=0.6, duration=None)
                    time.sleep(4)
                    continue
                else:
                    print u'页面加载完毕'
                    break

            for n in all_apps:
                ma = re.search(self.content, n, re.IGNORECASE)
                if ma:
                    #print chardet.detect(n)
                    #print n
                    #n.decode("utf8")
                    match.append(n)

                else:
                    continue
            #chardet.detect(match[0])    查看其实什么编码格式
            if match:
                # for m in match:
                # m.encode("utf8")
                print u'搜索到app:%s' % match
                return True

            else:
                print u"搜索不到结果，用例失败"
                return False


        except:
            s = sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
            return False

    def effectivesearch(self):
        return self.con.run_test_case(lambda: self.con.launch_app(),
                                      lambda: self.con.entry_search_box(),
                                      lambda: self.input_search(),
                                      lambda: self.analysis_result()
                                      )


if __name__ == '__main__':
    test = effective_search()
    test.effectivesearch()
