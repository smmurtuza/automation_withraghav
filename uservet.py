from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Creating Instance
option = Options()

# Working with the 'add_argument' Method to modify Driver Default Notification
option.add_argument('--disable-notifications')

driver =webdriver.Chrome(executable_path="C:\\murtuza\\chromedriver_win32\chromedriver.exe", chrome_options= option)
#driver.maximize_window()
driver.implicitly_wait(10)
base_url = "https://user-dev.petcareclub.vet/twentyfab/"
verificationErrors = []
driver.get(base_url)

#time.sleep(5)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("testusertwentyfab@yopmail.com")
#driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("abc123")
#driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(10)
driver.get("https://user-dev.petcareclub.vet/twentyfab")
#driver.implicitly_wait(3)



time.sleep(10)
#wait = WebDriverWait(driver, 10)
#element = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='button']")))



driver.find_element(By.XPATH,"//button[@type='button']").click()
# Creating Instance


# Working with the 'add_argument' Method to modify Driver Default Notification

time.sleep(5)


driver.find_element(By.XPATH,"//button[@type='button']").click()
time.sleep(12)


mdriver.find_element(By.NAME,"text").send_keys("testusertwentyfab@yopmail.com")
time.sleep(3)

driver.find_element(By.CLASS_NAME,"msg-send-btn").click()
time.sleep(3)

driver.find_element(By.XPATH,"//button[@type='button']").click()
time.sleep(5)

driver.find_element(By.CLASS_NAME,"br-units").click()
time.sleep(3)


driver.find_element(By.XPATH,"//input[@formcontrolname='review']").send_keys("testusertwentyfab@yopmail.com")
time.sleep(3)

driver.find_element(By.XPATH,"//textarea[@formcontrolname='description']").send_keys("testusertwentyfab@yopmail.com")
time.sleep(3)

driver.find_element(By.XPATH,"/html/body/div/div[2]/div/mat-dialog-container/app-end-chat/div/div/div[2]/div/form/div[3]/button").click()

driver.implicitly_wait(3)
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)