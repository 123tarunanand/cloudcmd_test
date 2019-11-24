from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path=r'/home/tarun/Desktop/testing/geckodriver-v0.25.0-linux64/geckodriver')
print("Test 22: Check Terminal Support")
driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/black-box/tests10-rest")
time.sleep(3)

menu = driver.find_element_by_id("~")
menu.click()
time.sleep(3)
driver.close()
