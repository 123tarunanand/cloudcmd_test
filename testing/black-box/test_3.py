# Copy file to higher directory and delete

print("Test 3: Copy files")
from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path=r'/home/tarun/Desktop/testing/geckodriver-v0.25.0-linux64/geckodriver')

driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/black-box")
time.sleep(3)
driver.maximize_window()
file = driver.find_element_by_xpath("/html/body/div[1]/section[1]/ul/li[6]")
file.click()
time.sleep(1)
menu = driver.find_element_by_id("f9")
menu.click()
time.sleep(1)
copy = driver.find_element_by_xpath("/html/body/div[1]/ul[2]/li[10]")
copy.click()
driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/")
time.sleep(3)
menu = driver.find_element_by_id("f9")
menu.click()
paste = driver.find_element_by_xpath("/html/body/div[1]/ul[1]/li[1]")
paste.click()

driver.close()
