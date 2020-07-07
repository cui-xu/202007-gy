from time import sleep

from selenium import webdriver
import urllib3
driver = webdriver.Chrome("../chromedriver/chromedriver.exe")
#最大化窗口
driver.maximize_window()
#打开网址
driver.get("http://ui.yansl.com/#/checkbox")
#线程等待
sleep(2)
driver.get("http://auth.xnjd.cn/login?service=http%3A%2F%2Fstudy.xnjd.cn%2Fstudy%2FHomework_list.action")
sleep(2)
driver.get("https://wallhaven.cc/")
#后退
driver.back()
sleep(1)
#前进
driver.forward()
sleep(1)
#刷新
driver.refresh()
sleep(1)
driver.close()
