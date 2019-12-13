from time import sleep

from selenium.common.exceptions import NoSuchElementException


class ReadList(object):
    # 清理运行环境
    def clean_evn(self, driver):
        driver.keyevent(82)
        driver.find_element_by_id('com.coloros.recents:id/progress_bar').click()

    # 输入马蕊的网址
    def enter_text(self, driver):

        # 点击搜索栏
        driver.find_element_by_id('com.android.browser:id/ayz').click()

        # 输入网址
        driver.find_element_by_xpath('//android.widget.RelativeLayout[@resource-id="com.android.browser:id/b61"]/brow'
                                     'ser.widget.EditText').send_keys('https://hd.book.qq.com/noah/20190777')
        # 点击搜索
        driver.find_element_by_id('com.android.browser:id/zn').click()

    # 检测测试按钮出现了
    def check_cancelBtn(self, driver):
        print("check cancel button")
        try:
            cancelBtn = driver.find_element_by_xpath('//android.view.View[@text="测试"]')
        except NoSuchElementException:
            print("检测不到测试的标题")
        else:
            print('到了测试页面了，可以下滑了')
            driver.swipe(320, 1000, 320, 500)
            driver.implicitly_wait(5)

    # 点击测试连接
    def chose_link(self, driver):
        driver.find_element_by_xpath('//android.view.View[contains(@text,"男生完本爆款")]').click()

    # 拿到列表的名字
    def get_list_name(self, driver, i):
        # 拿到列表的里面的书名哦
        driver.implicitly_wait(30)
        el_1 = driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="男生高分精选"]/android.view.View'
                                            '[' + str(i) + ']')
        name = el_1.get_attribute('name').strip()
        el_1.click()
        # 拿到里面的名字哦
        real_name = driver.find_element_by_id('com.oppo.book:id/bookinfo_name')
        real_name = real_name.get_attribute('name').strip()
        print(real_name+'=================')
        #  点击返回哦
        el_2 = driver.find_element_by_id('com.oppo.book:id/book_detail_left_back')
        el_2.click()
        return name, real_name

    # 循环拿名字
    def get_out_list_name(self, driver):
        c = ReadList()
        out_name_list = []
        i = 1
        while i < 401:
            name = c.get_list_name(driver, i)
            i += 4
            import re
            name = ''.join(re.findall('[\u4e00-\u9fa5]', name))
            out_name_list.append(name.strip())
            # print(name)


        return out_name_list

    # 读取文件名字，写入到一个列表里面
    def get_text_name(self):
        name_list = []
        with open('book_list_nan.txt', encoding='utf-8') as f:
            for i in f:
                import re
                i = ''.join(re.findall('[\u4e00-\u9fa5]', i))
                name_list.append(i.strip())
        return name_list

    def check_booklist(self, out_list, text_name):
        for i, v in zip(out_list, text_name):
            if i == v:
                print(i + '验证成功')
            else:
                print(i + '验证失败')

    def jishu_num(self):
        i = 1
        num_list = []
        while i < 101:
            i += 2
            num_list.append(i)
            print(i)
        return num_list



c = ReadList()
c.jishu_num()
