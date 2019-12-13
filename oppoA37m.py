from appium import webdriver
import time
import re

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "NJLBYHRS4DU4AIBM"
caps["appPackage"] = "com.android.browser"
caps["appActivity"] = "com.android.browser.BrowserActivity"
caps["unicodeKeyboard"] = "True"
caps["resetKeyboard"] = "True"
caps["noReset"] = "True"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(30)


def find_index():
    list1 = []
    i = 0
    while i < 200:
        i = i + 4
        list1.append(i)
    return list1


# 菜单里面的收藏
e12 = driver.find_element_by_id('com.android.browser:id/aax')
e12.click()
# 打开之后的收藏
e13 = driver.find_element_by_id('com.android.browser:id/ab1')
e13.click()
# 点击了网页
e14 = driver.find_element_by_id('com.android.browser:id/a9k')
e14.click()
# 点击活动页面
e15 = driver.find_element_by_xpath('//android.view.View[@text="【测试】OPPO书城精选书单测试"]')
e15.click()
# 进入第一本书
# e16 = driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="热门畅销榜"]/android.view.View[4]')
# tt = e16.get_attribute('name')
# print(tt)
# e16.click()
# e17 = driver.find_element_by_id('com.oppo.book:id/book_detail_left_back')
# e17.click()
#
# e18 = driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="热门畅销榜"]/android.view.View[8]')
# tt = e18.get_attribute('name')
# print(tt)
# e18.click()
# e19 = driver.find_element_by_id('com.oppo.book:id/book_detail_left_back')
# e19.click()
#
# e20 = driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="热门畅销榜"]/android.view.View[12]')
# tt = e20.get_attribute('name')
# print(tt)
# e20.click()
# e21 = driver.find_element_by_id('com.oppo.book:id/book_detail_left_back')
# e21.click()


ttt = 1
t = 1
while t < 50:

    # 点击第一本书
    list1 = find_index()
    # 不断的返回然后重新进的过程
    for times in list1:
        print(times)
        e16 = driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="精选好书"]/android.view.View['+
                                           str(times)+']')
        # 打印标签中第几页的
        # print(times)
        # 过滤其中的空格
        t1 = e16.get_attribute('name').strip()
        # 提取其中的汉字
        import re
        res1 = ''.join(re.findall('[\u4e00-\u9fa5]', t1))
        # 输出列表的书名
        # print(res1)
        # 点击此书名
        e16.click()
        # 找到内部的书名
        e17 = driver.find_element_by_id('com.oppo.book:id/bookinfo_name')
        t2 = e17.get_attribute('text').strip()
        # print(e17.get_attribute('text'))

        if res1 == t2:
            # print('《'+t1+'》'+'====核对成功，正确')
            print('《%s》核对正确' % t1)
            with open('result.text', 'a+') as f:
                f.write(('《%s》核对正确 \n'% t1))
        else:
            print(t1+'============================================================核对失败，请检查')
            with open('result.text', 'a+') as f:
                f.write((t1+'============================================================核对失败，请检查'))
        # 点击返回上一页
        e18 = driver.find_element_by_id('com.oppo.book:id/book_detail_left_back')
        e18.click()
        # 打印t计数的
        # print(t)

        if t % 3 == 0 and t != 0:
            driver.swipe(320, 1139, 320, 710)

        t = t+1
        if t == 51 and ttt == 2:
            iii = 0
            while iii < 10:
                driver.swipe(320, 300, 320, 1200)
                iii = iii + 1
            e20 = driver.find_element_by_xpath('//android.view.View[@content-desc="出版"]')
            e20.click()
            t = 1
            ttt = 3
        if t == 51 and ttt == 1:
            ii = 0
            while ii < 10:
                driver.swipe(320, 300, 320, 1200)
                ii = ii+1
            e19 = driver.find_element_by_xpath('//android.view.View[@content-desc="女频"]')
            e19.click()
            t = 1
            ttt = 2

        print(t)





































# # 点击菜单
# driver.implicitly_wait(30)
# el7 = driver.find_element_by_accessibility_id("菜单")
# el7.click()
# print('1=======点击浏览器菜单成功')
# # 点击书签
# el8 = driver.find_element_by_accessibility_id("书签/历史")
# el8.click()
# print('2=======点击书签成功')
# # 点击网页
# el9 = driver.find_element_by_xpath(r"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
#                                    "FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.wid"
#                                    "get.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android"
#                                    ".view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widg"
#                                    "et.TextView")
# el9.click()
# print('3=======点击收藏的网页成功')
# # 点击活动网址
# el10 = driver.find_element_by_accessibility_id("【开发】白牌限免书书单11.15-11.16 -- huawei")
#
#
# el10.click()
# print('4=============点击测试网站成功')
# # 点击打开
# el11 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]")
# el11.click()
# print('5=========已经按了打开')
# i = 1
# while i < 230:
#     i += 1
#     el12 = driver.find_element_by_accessibility_id("(可抽")
#     el12.click()
#     print('点击了抽奖了')
#     text_1 = el12.text
#     text_2 = el12.get_attribute('name')
#     print('T1'+text_1, 'T2'+text_2)
#     el13 = driver.find_element_by_accessibility_id("确定")
#     el13.click()
