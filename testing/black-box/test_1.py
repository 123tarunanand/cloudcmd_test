
# Create Folder and delete after

print("Test 1: Create a new Folder")

from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path=r'/home/tarun/Desktop/testing/geckodriver-v0.25.0-linux64/geckodriver')

driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/black-box")
time.sleep(3)
driver.maximize_window()
id = driver.find_element_by_id("f7")
id.click()
time.sleep(2)
name = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/input")
name.send_keys("New Folder")
ok = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/button[1]")
ok.click()
driver.close()
