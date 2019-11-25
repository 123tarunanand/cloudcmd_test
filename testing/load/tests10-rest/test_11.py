from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path=r'/home/tarun/Desktop/testing/geckodriver-v0.25.0-linux64/geckodriver')
print("Test 11: Time required to upload files")
driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/performance/tests10-rest")
time.sleep(3)
start = time.time()
menu = driver.find_element_by_id("f9")
menu.click()

upload = driver.find_element_by_xpath("/html/body/div[1]/ul[1]/li[3]")
upload.click()
time.sleep(3)
browse = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/input")
browse.send_keys("/home/tarun/Desktop/testing/test_20_sample.txt")
end = time.time()
driver.close()

print("Time required - ",end-start, " seconds")
