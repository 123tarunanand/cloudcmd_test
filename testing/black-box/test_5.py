# Copy file to upper directory and delete

print("Test 5: Paste Copied Files")
from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path=r'/home/tarun/Desktop/testing/geckodriver-v0.25.0-linux64/geckodriver')

driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/black-box")
time.sleep(3)
driver.maximize_window()
file = driver.find_element_by_xpath("/html/body/div[1]/section[1]/ul/li[8]")
file.click()
time.sleep(1)
menu = driver.find_element_by_id("f5")
menu.click()
time.sleep(1)
copy = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/input")
copy.send_keys("/home/tarun/Desktop/testing/")
ok = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/button[1]")
ok.click()
ok = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/button[1]")
ok.click()

driver.close()
