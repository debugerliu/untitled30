import requests
import json
from appium import webdriver
res = requests.get('https://hd.book.qq.com/act2/noah/index?activityId=156158493&f=-1')
print(res.text)
