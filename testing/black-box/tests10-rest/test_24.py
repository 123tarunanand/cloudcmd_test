from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path=r'/home/tarun/Desktop/testing/geckodriver-v0.25.0-linux64/geckodriver')
print("Test 24: Check whether vim is supported")
driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/black-box/tests10-rest")
time.sleep(3)

menu = driver.find_element_by_id("f10")
menu.click()
dword = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/form/ul/li[7]/select/option[2]")
dword.click()

vim = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/form/ul/li[8]/label/input")
if not vim.is_selected():
    vim.click()

close = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]")
close.click()


file = driver.find_element_by_xpath("/html/body/div[1]/section[1]/ul/li[27]")
file.click()

menu = driver.find_element_by_id("f9")
menu.click()

edit = driver.find_element_by_xpath("/html/body/div[1]/ul[2]/li[2]")
edit.click()
time.sleep(2)
view = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div[1]/textarea")

view.send_keys("Editted using vim")
close = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]")
close.click()

ok = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/button[1]")
ok.click()

driver.close()
