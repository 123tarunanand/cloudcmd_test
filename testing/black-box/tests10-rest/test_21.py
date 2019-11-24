from selenium import webdriver
import time
print("Test 21: Download Files")
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 1)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', "image/png,image/jpeg")
driver = webdriver.Firefox(executable_path=r'/home/tarun/Desktop/testing/geckodriver-v0.25.0-linux64/geckodriver', firefox_profile = profile)

driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/black-box/tests10-rest")
time.sleep(3)

file = driver.find_element_by_xpath("/html/body/div[1]/section[1]/ul/li[23]")
file.click()

menu = driver.find_element_by_id("f9")
menu.click()

download = driver.find_element_by_xpath("/html/body/div[1]/ul[2]/li[7]")
download.click()
driver.close()
