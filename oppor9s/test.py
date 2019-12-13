from selenium import webdriver


driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

ele = driver.find_element_by_xpath('//*[@id="kw"]')
ele.send_keys('123')
