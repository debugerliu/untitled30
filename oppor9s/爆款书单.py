from time import sleep

from appium import webdriver
from oppor9s.func_list import ReadList
import time
import re

from selenium.common.exceptions import NoSuchElementException

# 配置信息
caps = {"platformName": "Android", "deviceName": "c3e0d4dd", "appPackage": "com.android.browser",
        "appActivity": "com.android.browser.BrowserActivity", "unicodeKeyboard": "True", "resetKeyboard": "True",
        "noReset": "True"}

# 初始化driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

# 显示等待，超时时间30s
driver.implicitly_wait(30)

# 做好任务前的清理工作
c = ReadList()
c.clean_evn(driver)

# 输入网址
c.enter_text(driver)

# 点击男生高分
c.chose_link(driver)

# 获取奇数序列
times = c.jishu_num()
# 循环读取列表名字以及内部名字

i = 0
while i < 51:
    for time in times:
        out_element = driver.find_element_by_xpath(
            '//android.webkit.WebView[@content-desc="男生完本爆款"]/android.view.View/andro'
            'id.view.View/android.view.View['+str(time)+']/android.view.View[1]')
        name = out_element.get_attribute('name')
        out_element.click()
        print(name)
        driver.keyevent(4)

        if time % 3 == 0:
            sleep(1)
            driver.swipe(320, 1500, 310, 900)


# i = 0
# while i <= 50 :
#         for num, name in zip()


# # 获得列表的书名
# i = 1
# while i < 50:
#         out_list, NAME_LIST = c.get_out_list_name(driver)
#         i +=1
#
#
# # 获得需求给的名字
# text_name = c.get_text_name()
#
# # 核对书名
# c.check_booklist(out_list, text_name)
