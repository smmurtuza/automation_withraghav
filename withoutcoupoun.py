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
from selenium.webdriver.support.ui import Select
import os
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import subprocess
#import pandas as pd


# Load Excel file
#df = pd.read_excel('C:\\Users\\Hp\\Desktop\\automation\\data.xlsx')




# Creating Instance
option = Options()

# Working with the 'add_argument' Method to modify Driver Default Notification
option.add_argument('--disable-notifications')

driver =webdriver.Chrome(executable_path="C:\\murtuza\\chromedriver_win32\chromedriver.exe", chrome_options= option)

driver.maximize_window()
driver.implicitly_wait(10)
base_url = "https://user-dev.petcareclub.vet/pdmpdm/signup"
verificationErrors = []
driver.get(base_url)



#time.sleep(15)


#driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@formcontrolname='name']").send_keys("gifttyyy")
#driver.implicitly_wait(10)
time.sleep(2)
driver.find_element(By.ID,"pet_info_dog_inactive").click()

#time.sleep(10)
driver.find_element(By.ID,"pet_info_male_inactive").click()


time.sleep(2)
driver.find_element(By.XPATH,"//button[@type='button']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@formcontrolname='breed']").send_keys("Mixed")




driver.find_element(By.XPATH,"//input[@formcontrolname='ageYear']").send_keys("1")

driver.find_element(By.XPATH,"//input[@formcontrolname='ageMonth']").send_keys("2")

driver.find_element(By.XPATH,"//input[@formcontrolname='weightNumber']").send_keys("3")

time.sleep(4)
driver.find_element(By.XPATH,"/html/body/app-root/app-signup/div/mat-horizontal-stepper/div[2]/div[1]/div/div/div/div/form/div[8]/button").click()

#driver.implicitly_wait(10)

time.sleep(2)
#wait = WebDriverWait(driver, 10)
#element = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='button']")))

driver.find_element(By.XPATH,"//input[@formcontrolname='first_name']").send_keys("staxtestcardy")

driver.find_element(By.XPATH,"//input[@formcontrolname='last_name']").send_keys("testing")


driver.find_element(By.XPATH,"//input[@formcontrolname='phone_no']").send_keys("1234567891")


driver.find_element(By.XPATH,"//input[@formcontrolname='email']").send_keys("giftey@yopmail.com")


driver.find_element(By.XPATH,"//input[@formcontrolname='password']").send_keys("abc123")

driver.find_element(By.XPATH,"//input[@formcontrolname='confirm_password']").send_keys("abc123")

driver.find_element(By.XPATH,"//input[@formcontrolname='zip_code']").send_keys("12345")

time.sleep(2)

driver.find_element(By.XPATH,"/html/body/app-root/app-signup/div/mat-horizontal-stepper/div[2]/div[2]/div/div/div/div/form/div/div[8]/button").click()
# Creating Instance


# Working with the 'add_argument' Method to modify Driver Default Notification

time.sleep(2)


element = driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator rounded-pill text-center border-primary border text-primary signup-btn mr-18 mat-flat-button mat-button-base']")
element.click()
time.sleep(2)

#giftcard
checkbox = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/mat-dialog-container/app-payment-popup/div[2]/div[2]/form/mat-checkbox/label/span[1]")
is_displayed = checkbox.is_displayed()
if checkbox.is_displayed():
    checkbox.click()

giftcard=driver.find_element(By.XPATH,"//input[@formcontrolname='code']").send_keys("CT7KLQ9M3N")

redeem=driver.find_element(By.CSS_SELECTOR,'.btn-redeem')
redeem.click()

#acceptrules
acceptrules_checkbox = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/mat-dialog-container/app-payment-popup/div[2]/div[2]/form/div[2]/mat-radio-group")
is_displayed = acceptrules_checkbox.is_displayed()
if acceptrules_checkbox.is_displayed():
    acceptrules_checkbox.click()


#signup
signup=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/mat-dialog-container/app-payment-popup/div[2]/div[2]/form/div[3]/button")
signup.click()
time.sleep(5)


# take a screenshot and save it to a file
driver.get_screenshot_as_file("stax.smmr1111thmay.png")



driver.implicitly_wait(3)
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)