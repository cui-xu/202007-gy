from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()

def test_a():
    driver.get("https://www.baidu.com/")
    driver.maximize_window()
    sleep(2)
    driver.quit()