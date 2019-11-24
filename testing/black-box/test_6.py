from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path=r'/home/tarun/Desktop/testing/geckodriver-v0.25.0-linux64/geckodriver')

print("Test 6: Check local browser instance")
driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/black-box")
time.sleep(3)


driver.close()
