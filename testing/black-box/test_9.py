from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path=r'/home/tarun/Desktop/testing/geckodriver-v0.25.0-linux64/geckodriver')

print("Test 9: Zip files")
driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/black-box")
time.sleep(3)

menu = driver.find_element_by_id("f10")
menu.click()
zip_op = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/form/ul/li[12]/select/option[2]")
zip_op.click()
close = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]")
close.click()
file = driver.find_element_by_xpath("/html/body/div[1]/section[1]/ul/li[15]")
file.click()
menu = driver.find_element_by_id("f9")
menu.click()
zip = driver.find_element_by_xpath("/html/body/div[1]/ul[2]/li[5]")
zip.click()

driver.close()
