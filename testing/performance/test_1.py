from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path=r'/home/tarun/Desktop/testing/geckodriver-v0.25.0-linux64/geckodriver')

print("Test 1: Unzip zip files and note the time")
driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/performance")
time.sleep(3)
start = time.time()
file = driver.find_element_by_xpath("/html/body/div[1]/section[1]/ul/li[5]")
file.click()
menu = driver.find_element_by_id("f9")
menu.click()
extract = driver.find_element_by_xpath("/html/body/div[1]/ul[2]/li[6]")
extract.click()
end = time.time()
driver.close()

print("Time required - ",end-start, " seconds")
