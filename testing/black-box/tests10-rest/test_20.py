from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path=r'/home/tarun/Desktop/testing/geckodriver-v0.25.0-linux64/geckodriver')
print("Test 20: Upload Files")
driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/black-box/tests10-rest")
time.sleep(3)

menu = driver.find_element_by_id("f9")
menu.click()

upload = driver.find_element_by_xpath("/html/body/div[1]/ul[1]/li[3]")
upload.click()
time.sleep(3)
browse = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/input")
browse.send_keys("/home/tarun/Desktop/testing/test_20_sample.txt")

driver.close()
