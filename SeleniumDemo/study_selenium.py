# from selenium.webdriver import Chrome
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.maximize_window()
driver.get('https://www.baidu.com')
time.sleep(5)
input = driver.find_element_by_id('kw')
driver.quit()
