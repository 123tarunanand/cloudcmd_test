from selenium import webdriver
import time
print("Test 7: Check if a load of 45 files can be downloaded")
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 1)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', "image/png,image/jpeg")
driver = webdriver.Firefox(executable_path=r'/home/tarun/Desktop/testing/geckodriver-v0.25.0-linux64/geckodriver', firefox_profile = profile)
n = 25
driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/performance/tests10-rest")

start = time.time()
file = driver.find_element_by_xpath("/html/body/div[1]/section[1]/ul/li[7]")
file.click()

for i in range(n):
    menu = driver.find_element_by_id("f9")
    menu.click()

    download = driver.find_element_by_xpath("/html/body/div[1]/ul[2]/li[7]")
    download.click()

print("Error - Out of memory")
driver.close()
