from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path=r'/home/tarun/Desktop/testing/geckodriver-v0.25.0-linux64/geckodriver')

print("Test 10: Rename Files and check time")
driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/performance/tests10-rest")
time.sleep(3)
start = time.time()

file = driver.find_element_by_xpath("/html/body/div[1]/section[1]/ul/li[4]")
file.click()
menu = driver.find_element_by_id("f9")
menu.click()
rename = driver.find_element_by_xpath("/html/body/div[1]/ul[2]/li[3]")
rename.click()

newname = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/input")
newname.send_keys("test_10_copy.txt")

ok = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/button[1]")
ok.click()

end = time.time()
driver.close()

print("Time required - ",end-start, " seconds")
