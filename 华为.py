
from appium import webdriver


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'FMGRX19603002197'
# desired_caps['app'] = 'com.iqilu.cloud.MyApplication'
desired_caps['appPackage'] = 'com.miui.calculator'
desired_caps['appActivity'] = 'com.miui.calculator.cal.CalculatorActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

el1 = driver.find_element_by_id("com.miui.calculator:id/btn_1_s")
el1.click()
el2 = driver.find_element_by_id("com.miui.calculator:id/btn_plus_s")
el2.click()
el3 = driver.find_element_by_id("com.miui.calculator:id/btn_2_s")
el3.click()
el4 = driver.find_element_by_id("com.miui.calculator:id/btn_equal_s")
el4.click()