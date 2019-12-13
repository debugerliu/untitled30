from time import sleep

from appium import webdriver

# 配置信息
caps = {"platformName": "Android", "deviceName": "c3e0d4dd", "appPackage": "com.android.settings",
        "appActivity": "com.oppo.settings.SettingsActivity", "unicodeKeyboard": "True", "resetKeyboard": "True",
        "noReset": "True"}

# 初始化driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

# 显示等待，超时时间30s
driver.implicitly_wait(1)

list1 = ["儿童空间", "使用说明", "浏览器"]
for i in list1:
    while True:
        try:
            ele = driver.find_element_by_xpath('//*[@text=' + '"' + i + '"' + ']')
            ele.click()
            driver.keyevent(4)
            break
        except Exception as e:
            driver.swipe(320, 1500, 310, 900)


