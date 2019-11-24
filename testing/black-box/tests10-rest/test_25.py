from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox(executable_path=r'/home/tarun/Desktop/testing/geckodriver-v0.25.0-linux64/geckodriver')
print("Test 25: Check User Menu")
driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/black-box/tests10-rest")
time.sleep(3)

file  = driver.find_element_by_xpath("/html/body/div[1]/section[1]/ul/li[29]")
file.click()
menu = driver.find_element_by_id("f2")
menu.click()
time.sleep(2)
rename = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/select/option[1]")
rename.send_keys(Keys.F2)

time.sleep(2)

rename = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/input")
rename.send_keys("test_25_rename.txt")

ok = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/button[1]")
ok.click()


driver.close()
