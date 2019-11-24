from selenium import webdriver
import time


print("Test 3: Test if 25 local instances can be run")
a = []
n = 25
for i in range(n):
    driver = webdriver.Firefox(executable_path=r'/home/tarun/Desktop/testing/geckodriver-v0.25.0-linux64/geckodriver')
    driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/performance")
    a.append(driver)

for i in range(n):
    a[i].close()
