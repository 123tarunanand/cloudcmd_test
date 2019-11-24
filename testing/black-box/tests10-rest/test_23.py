from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path=r'/home/tarun/Desktop/testing/geckodriver-v0.25.0-linux64/geckodriver')
print("Test 23: Check Hotkey Support")
driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/black-box/tests10-rest")
time.sleep(3)

menu = driver.find_element_by_id("f1")
menu.click()
time.sleep(1)
close = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]")
close.click()

menu = driver.find_element_by_id("f2")
menu.click()
time.sleep(1)
close = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]")
close.click()

menu = driver.find_element_by_id("f3")
menu.click()
time.sleep(1)
close = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]")
close.click()

menu = driver.find_element_by_id("f4")
menu.click()
time.sleep(1)
close = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]")
close.click()

menu = driver.find_element_by_id("f5")
menu.click()
time.sleep(1)
close = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]")
close.click()

menu = driver.find_element_by_id("f6")
menu.click()
time.sleep(1)
close = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]")
close.click()

menu = driver.find_element_by_id("f7")
menu.click()
time.sleep(1)
close = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]")
close.click()

menu = driver.find_element_by_id("f8")
menu.click()
time.sleep(1)
close = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]")
close.click()


driver.close()
