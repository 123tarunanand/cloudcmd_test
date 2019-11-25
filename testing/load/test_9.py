from selenium import webdriver
import time
print("Test 9: Check 45 folders can be opened")

driver = webdriver.Firefox(executable_path=r'/home/tarun/Desktop/testing/geckodriver-v0.25.0-linux64/geckodriver')
n = 9

for i in range(n):
    driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/performance/tests10-rest")
    driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/load/tests10-rest")
    driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/black-box/tests10-rest")

driver.close()
