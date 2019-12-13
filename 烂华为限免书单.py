from appium import webdriver
import time

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "QMS4C16219004473"
caps["appPackage"] = "com.android.browser"
caps["appActivity"] = "com.tencent.mtt.MainActivity"
caps["unicodeKeyboard"] = "True"
caps["resetKeyboard"] = "True"
caps["noReset"] = "True"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(30)
time.sleep(5)
driver.keyevent(3)
time.sleep(5)


el1 = driver.find_element_by_xpath("//android.view.ViewGroup[@content-desc=\"第 2 屏，共 4 屏\"]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[1]")
el1.click()
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]")
el2.click()
el4 = driver.find_element_by_accessibility_id("t5_13499864")
el4.click()
e15 = driver.find_element_by_id('com.huawei.hnreader:id/bookinfo_name')
tt = e15.get_attribute(e15)
driver.find_element_by
print(tt)











































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
