from time import sleep

from appium import webdriver
from oppor9s.func_list import ReadList
import time
import re

from selenium.common.exceptions import NoSuchElementException

# 配置信息
caps = {"platformName": "Android", "deviceName": "c3e0d4dd", "appPackage": "com.android.settings",
        "appActivity": "com.oppo.settings.SettingsActivity", "unicodeKeyboard": "True", "resetKeyboard": "True",
        "noReset": "True"}

# 初始化driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

# 显示等待，超时时间30s
driver.implicitly_wait(1)

while True:
    try:
        ele = driver.find_element_by_xpath('//*[@text="浏览器"]')
        ele.click()
        driver.keyevent(4)
        break
    except Exception as e:
        driver.swipe(320, 1500, 310, 900)
