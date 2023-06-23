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
base_url = "https://user-dev.petcareclub.vet/murtuza/signup"
verificationErrors = []
driver.get(base_url)


#petdetails


driver.find_element(By.XPATH,"//input[@formcontrolname='name']").send_keys("testt")
driver.implicitly_wait(10)
#time.sleep(5)
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


time.sleep(5)


#vetdetails

driver.find_element(By.XPATH,"//input[@formcontrolname='first_name']").send_keys("stacx")

driver.find_element(By.XPATH,"//input[@formcontrolname='last_name']").send_keys("testing")


driver.find_element(By.XPATH,"//input[@formcontrolname='phone_no']").send_keys("12345678910")


driver.find_element(By.XPATH,"//input[@formcontrolname='email']").send_keys("staxxcsw@yopmail.com")


driver.find_element(By.XPATH,"//input[@formcontrolname='password']").send_keys("abc123")

driver.find_element(By.XPATH,"//input[@formcontrolname='confirm_password']").send_keys("abc123")

driver.find_element(By.XPATH,"//input[@formcontrolname='zip_code']").send_keys("123456")

time.sleep(2)

driver.find_element(By.XPATH,"/html/body/app-root/app-signup/div/mat-horizontal-stepper/div[2]/div[2]/div/div/div/div/form/div/div[8]/button").click()
time.sleep(5)


package_continue = driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator rounded-pill text-center border-primary border text-primary signup-btn mr-18 mat-flat-button mat-button-base']")
#time.sleep(10)
# Click the element

package_continue.click()
time.sleep(5)

#Payment details

driver.find_element(By.XPATH,"//input[@formcontrolname='number']").send_keys("4100000000000011")
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

# ...

# Input coupon details
coupon = driver.find_element(By.XPATH, "//input[@formcontrolname='couponCode']")
if coupon.is_displayed():
    coupon.send_keys("t")

# Select radio button
radio_button = driver.find_element(By.ID, "mat-radio-2")
if radio_button.is_displayed():
    radio_button.click()

# Redeem the coupon
redeem = driver.find_element(By.CSS_SELECTOR, '.btn-redeem')
if redeem.is_displayed():
    redeem.click()

time.sleep(2)

# Check for error message or checkbox
#error_message = driver.find_element(By.XPATH, "//span[contains(text(), 'Your card number is incorrect.')]")
checkbox = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-payment-popup/div[2]/div[2]/form/mat-checkbox/label/span[1]')

if error_message.is_displayed() or not checkbox.is_selected():
    # Invalid coupon or checkbox not selected, proceed to Point 8
    package_continue = driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator rounded-pill text-center border-primary border text-primary signup-btn mr-18 mat-flat-button mat-button-base']")
    package_continue.click()
else:
    # Valid coupon and checkbox selected, proceed to Point 9
    packagebuy = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/mat-dialog-container/app-payment-popup/div[2]/div[2]/form/div[3]/button")
    packagebuy.click()

# ...



"""
# Input coupon details
coupon = driver.find_element(By.XPATH, "//input[@formcontrolname='couponCode']")
if coupon.is_displayed():
    coupon.send_keys("t")

# Select radio button
radio_button = driver.find_element(By.ID, "mat-radio-2")
if radio_button.is_displayed():
    radio_button.click()

# Redeem the coupon
redeem = driver.find_element(By.CSS_SELECTOR, '.btn-redeem')
if redeem.is_displayed():
    redeem.click()

time.sleep(2)

"""
packagebuy=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/mat-dialog-container/app-payment-popup/div[2]/div[2]/form/div[7]/button").click()
# Check for error message or checkbox
#error_message = driver.find_element(By.XPATH, "//span[contains(text(), 'Your card number is incorrect.')]")
checkbox = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-payment-popup/div[2]/div[2]/form/mat-checkbox/label/span[1]').click()

# Enter gift card code
gift_card = driver.find_element(By.XPATH, "//input[@formcontrolname='code']")
gift_card.send_keys("WBI4SXZB79")

    # Redeem the gift card
redeem = driver.find_element(By.CSS_SELECTOR, '.btn-redeem')
redeem.click()

packagebuy=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/mat-dialog-container/app-payment-popup/div[2]/div[2]/form/div[3]/button").click()

giftcard_crossbutton=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/mat-dialog-container/app-payment-popup/div[1]/button").click()

package_continue = driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator rounded-pill text-center border-primary border text-primary signup-btn mr-18 mat-flat-button mat-button-base']")

#packagebuy=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/mat-dialog-container/app-payment-popup/div[2]/div[2]/form/div[7]/button").click()


package_continue.click()
time.sleep(5)

#Payment details

driver.find_element(By.XPATH,"//input[@formcontrolname='number']").send_keys("4242424242424242")
select_element = driver.find_element(By.XPATH,"//mat-select[@formcontrolname='exp_month']")


# Click on the mat-select element to open the dropdown menu
ActionChains(driver).move_to_element(select_element).click().perform()

# Click on the desired option in the dropdown menu
option = driver.find_element(By.ID,"mat-option-425")
option.click()

# Find the select element by its XPath
select_element = driver.find_element(By.XPATH,"//mat-select[@formcontrolname='exp_year']")


# Click on the mat-select element to open the dropdown menu
ActionChains(driver).move_to_element(select_element).click().perform()

# Click on the desired option in the dropdown menu
option = driver.find_element(By.ID,"mat-option-436")
option.click()

driver.find_element(By.XPATH,"//input[@formcontrolname='cvv']").send_keys("123")

# Select radio button
radio_button = driver.find_element(By.ID, "mat-radio-4")
if radio_button.is_displayed():
    radio_button.click()


packagebuy=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/mat-dialog-container/app-payment-popup/div[2]/div[2]/form/div[7]/button").click()
#membership=driver.find_element(By.XPATH,"/html/body/app-root/app-drawer/mat-drawer-container/mat-drawer/div/div[2]/mat-nav-list/mat-list-item[5]/div/a/div/div/div/span")
#membership.click()
#time.sleep(5)
# take a screenshot and save it to a file
driver.get_screenshot_as_file("stax.smmr17thmay.png")



driver.implicitly_wait(3)
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)