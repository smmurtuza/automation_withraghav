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
base_url = "https://user-dev.petcareclub.vet/seventeenmay/signup"
verificationErrors = []
driver.get(base_url)



#time.sleep(15)




"""
# Get data from Excel
name = df.iloc[0]['Name']
breed = df.iloc[0]['Breed']
age_year = df.iloc[0]['Age (Year)']
age_month = df.iloc[0]['Age (Month)']
weight = df.iloc[0]['Weight']
first_name = df.iloc[0]['First Name']
last_name = df.iloc[0]['Last Name']
phone_no = df.iloc[0]['Phone Number']
email = df.iloc[0]['Email']
password = df.iloc[0]['Password']
zip_code = df.iloc[0]['Zip Code']
card_number = df.iloc[0]['Card Number']
cvv = df.iloc[0]['CVV']

"""

#driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@formcontrolname='name']").send_keys("seventenmixed")
#driver.implicitly_wait(10)
time.sleep(5)
driver.find_element(By.ID,"pet_info_dog_inactive").click()

#time.sleep(10)
driver.find_element(By.ID,"pet_info_male_inactive").click()


time.sleep(5)
driver.find_element(By.XPATH,"//button[@type='button']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@formcontrolname='breed']").send_keys("Mixed")




driver.find_element(By.XPATH,"//input[@formcontrolname='ageYear']").send_keys("1")

driver.find_element(By.XPATH,"//input[@formcontrolname='ageMonth']").send_keys("2")

driver.find_element(By.XPATH,"//input[@formcontrolname='weightNumber']").send_keys("3")

driver.implicitly_wait(10)
driver.find_element(By.XPATH,"/html/body/app-root/app-signup/div/mat-horizontal-stepper/div[2]/div[1]/div/div/div/div/form/div[8]/button").click()

#driver.implicitly_wait(10)

time.sleep(5)
#wait = WebDriverWait(driver, 10)
#element = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='button']")))

driver.find_element(By.XPATH,"//input[@formcontrolname='first_name']").send_keys("seventen")

driver.find_element(By.XPATH,"//input[@formcontrolname='last_name']").send_keys("testing")


driver.find_element(By.XPATH,"//input[@formcontrolname='phone_no']").send_keys("2345678910")


driver.find_element(By.XPATH,"//input[@formcontrolname='email']").send_keys("2023@yopmail.com")


driver.find_element(By.XPATH,"//input[@formcontrolname='password']").send_keys("abc123")

driver.find_element(By.XPATH,"//input[@formcontrolname='confirm_password']").send_keys("abc123")

driver.find_element(By.XPATH,"//input[@formcontrolname='zip_code']").send_keys("12345")

time.sleep(2)

driver.find_element(By.XPATH,"/html/body/app-root/app-signup/div/mat-horizontal-stepper/div[2]/div[2]/div/div/div/div/form/div/div[8]/button").click()
# Creating Instance


# Working with the 'add_argument' Method to modify Driver Default Notification

time.sleep(5)


element = driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator rounded-pill text-center border-primary border text-primary signup-btn mr-18 mat-flat-button mat-button-base']")
#time.sleep(10)
# Click the element

element.click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@formcontrolname='number']").send_keys("4012888888881881")

# Find the select element by its XPath
select_element = driver.find_element(By.XPATH,"//mat-select[@formcontrolname='exp_month']")


# Click on the mat-select element to open the dropdown menu
ActionChains(driver).move_to_element(select_element).click().perform()

# Click on the desired option in the dropdown menu
option = driver.find_element(By.ID,"mat-option-391")
option.click()

# Find the select element by its XPath
select_element = driver.find_element(By.XPATH,"//mat-select[@formcontrolname='exp_year']")


# Click on the mat-select element to open the dropdown menu
ActionChains(driver).move_to_element(select_element).click().perform()

# Click on the desired option in the dropdown menu
option = driver.find_element(By.ID,"mat-option-402")
option.click()


driver.find_element(By.XPATH,"//input[@formcontrolname='cvv']").send_keys("123")
redeem=driver.find_element(By.XPATH,"//input[@formcontrolname='couponCode']").send_keys("ttt")
driver.find_element(By.ID,"mat-radio-2").click()

time.sleep(1)
redeem=driver.find_element(By.CSS_SELECTOR,'.btn-redeem')
redeem.click()
time.sleep(5)

driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/mat-dialog-container/app-payment-popup/div[2]/div[2]/form/div[7]/button").click()


time.sleep(10)


membership=driver.find_element(By.XPATH,"/html/body/app-root/app-drawer/mat-drawer-container/mat-drawer/div/div[2]/mat-nav-list/mat-list-item[5]/div/a/div/div/div/span")
membership.click()
time.sleep(5)
# take a screenshot and save it to a file
driver.get_screenshot_as_file("stax.smmr17thmay.png")



driver.implicitly_wait(3)
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)