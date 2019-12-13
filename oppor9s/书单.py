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

# 检测打开网页了吗？顺便下滑
c.check_cancelBtn(driver)

# 点击男生高分
c.chose_link(driver)

# 获得列表的书名
i = 1
while i < 50:
        out_list, NAME_LIST = c.get_out_list_name(driver)
        i +=1


# 获得需求给的名字
text_name = c.get_text_name()

# 核对书名
c.check_booklist(out_list, text_name)
