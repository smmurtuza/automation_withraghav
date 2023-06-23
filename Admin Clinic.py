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


# Creating Instance
option = Options()

# Working with the 'add_argument' Method to modify Driver Default Notification
option.add_argument('--disable-notifications')

driver =webdriver.Chrome(executable_path="C:\\murtuza\\chromedriver_win32\chromedriver.exe", chrome_options= option)

driver.maximize_window()
driver.implicitly_wait(10)
base_url = "https://admin-dev.itmedicalvetsolutions.com/authentication"
verificationErrors = []
driver.get(base_url)

driver.find_element(By.XPATH,"//input[@formcontrolname='email']").send_keys("admin@admin.com")
driver.find_element(By.XPATH,"//input[@formcontrolname='password']").send_keys("admin")

time.sleep(15)

driver.find_element(By.XPATH,"/html/body/app-root/app-signin/div/div/div[2]/div[1]/div/div/form/button").click()

time.sleep(5)

vetcare=driver.find_element(By.ID,"menuitem-15")
vetcare.click()

time.sleep(15)

"""
time.sleep(10)
#driver.implicitly_wait(10)
Create=driver.find_element(By.CSS_SELECTOR,"//a[@href='/admin/vetcare/clinics']")
Create.click()
#driver.implicitly_wait(10)
"""
driver.find_element(By.XPATH,"/html/body/app-root/app-admin-layout/div/mat-drawer-container/mat-drawer-content/div/div/app-clinics/div/div/div/div/div/div[1]/div[2]/div[2]").click()
time.sleep(5)


driver.find_element(By.XPATH,"//input[@formcontrolname='name']").send_keys("test clinic")




driver.find_element(By.XPATH,"//input[@formcontrolname='clinic_name']").send_keys("sixteen may")

driver.find_element(By.XPATH,"//input[@formcontrolname='email']").send_keys("16mayh@yopmail.com")

driver.find_element(By.XPATH,"//input[@formcontrolname='password']").send_keys("abc123")

driver.find_element(By.XPATH,"//input[@formcontrolname='phone_no']").send_keys("12345678910")

driver.find_element(By.XPATH,"//input[@formcontrolname='support_email']").send_keys("16may@yopmail.com")

driver.find_element(By.XPATH,"//input[@formcontrolname='support_phone']").send_keys("123456789")

driver.find_element(By.XPATH,"//input[@formcontrolname='address']").send_keys("abctest")

driver.find_element(By.XPATH,"//input[@formcontrolname='email_to']").send_keys("16may@yopmail.com")

time.sleep(4)
Add=driver.find_element(By.XPATH,"/html/body/app-root/app-admin-layout/div/mat-drawer-container/mat-drawer-content/div/div/app-add/div/div/form/div/div/div/div/div[2]/button[1]")
Add.click()

driver.implicitly_wait(10)

time.sleep(5)
#wait = WebDriverWait(driver, 10)
#element = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='button']")))

driver.find_element(By.XPATH,"//input[@formcontrolname='first_name']").send_keys("test")

driver.find_element(By.XPATH,"//input[@formcontrolname='last_name']").send_keys("smmmmmr")


driver.find_element(By.XPATH,"//input[@formcontrolname='phone_no']").send_keys("2345678910")


driver.find_element(By.XPATH,"//input[@formcontrolname='email']").send_keys("today@yopmail.com")


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
driver.find_element(By.XPATH,"//input[@formcontrolname='number']").send_keys("4242424242424242")

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
redeem=driver.find_element(By.XPATH,"//input[@formcontrolname='couponCode']").send_keys("MURTUZA123")
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
driver.get_screenshot_as_file("screenshot3.png")



driver.implicitly_wait(3)
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)