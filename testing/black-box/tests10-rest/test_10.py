from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path=r'/home/tarun/Desktop/testing/geckodriver-v0.25.0-linux64/geckodriver')
print("Test 10: Untar files")
driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/black-box/tests10-rest")
time.sleep(3)
file = driver.find_element_by_xpath("/html/body/div[1]/section[1]/ul/li[4]")
file.click()
menu = driver.find_element_by_id("f9")
menu.click()
extract = driver.find_element_by_xpath("/html/body/div[1]/ul[2]/li[6]")
extract.click()
driver.close()
