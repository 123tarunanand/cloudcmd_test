from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path=r'/home/tarun/Desktop/testing/geckodriver-v0.25.0-linux64/geckodriver')

print("Test 8: Test Directory Navigation time")
start = time.time()
driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/black-box")
driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing")
driver.get("http://localhost:8000/fs/home/tarun/Desktop")
driver.get("http://localhost:8000/fs/home/tarun")
driver.get("http://localhost:8000/fs/home")
end = time.time()
driver.close()

print("Time required - ",end-start, " seconds")
