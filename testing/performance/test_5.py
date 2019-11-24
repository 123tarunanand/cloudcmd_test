from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path=r'/home/tarun/Desktop/testing/geckodriver-v0.25.0-linux64/geckodriver')

print("Test 5: Check local browser instance")
start = time.time()
driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/black-box")
end = time.time()
print("Time required - ",end-start, " seconds")
time.sleep(3)


driver.close()
