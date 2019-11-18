from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'f0cfde8a'
# desired_caps['app'] = 'com.iqilu.cloud.MyApplication'
desired_caps['appPackage'] = 'com.tencent.mtt'
desired_caps['appActivity'] = 'com.tencent.mtt.MainActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

el1 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ImageView")
el1.click()
el2 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ImageView")
el2.send_keys("http://oahd.book.qq.com/noah/201907777")
el3 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView")
el3.click()
el4 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView")
el4.click()
el5 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]")
el5.click()
TouchAction(driver).press(x=521, y=366).move_to(x=-17, y=1222).release()
TouchAction(driver).press(x=538, y=572).move_to(x=4, y=1159).release()

el6 = driver.find_element_by_accessibility_id("活动规则")
el6.click()
