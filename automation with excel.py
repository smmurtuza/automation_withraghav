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
import pandas as pd


# Load Excel file
df = pd.read_excel('C:\\Users\\Hp\\Desktop\\automation\\data.xlsx')




# Creating Instance
option = Options()

# Working with the 'add_argument' Method to modify Driver Default Notification
option.add_argument('--disable-notifications')

driver =webdriver.Chrome(executable_path="C:\\murtuza\\chromedriver_win32\chromedriver.exe", chrome_options= option)

driver.maximize_window()
driver.implicitly_wait(10)
base_url = "https://user-dev.petcareclub.vet/testsmmrstax/signup"
verificationErrors = []
driver.get(base_url)



#time.sleep(5)

# Load Excel file
#df = pd.read_excel('C:\\Users\\Hp\\Desktop\\automation\\data.xlsx',sheet_name='Sheet2')




# Load Excel file
df = pd.read_excel('C:\\Users\\Hp\\Desktop\\automation\\data.xlsx', sheet_name='Sheet2')

# Get data from Excel
try:
    name = df.iloc[0]['Name'].strip()
except KeyError:
    print("Column 'Name' not found in the Excel sheet")
    exit()


try:
    # Pet Name
    driver.find_element(By.XPATH,"//input[@formcontrolname='name']").send_keys(name)
except Exception as e:
    print(f"Error filling pet name: {e}")


# Cat /Dog
try:
    pet_type = str(df.iloc[0]['button']).strip()
except KeyError:
    print("radio button 'Dog/cat' not found in the Excel sheet")
    exit()

try:
    if pet_type.lower() == 'cat':
        driver.find_element(By.ID, 'pet_info_cat_inactive').click()
    elif pet_type.lower() == 'dog':
        driver.find_element(By.ID, 'pet_info_dog_inactive').click()
    else:
        print(f"Invalid pet type: {pet_type}")
except Exception as e:
    print(f"Error filling pet name: {e}")


# Male / Female
try:
    sex_type = str(df.iloc[0]['sex']).strip()
except KeyError:
    print("radio button 'Male / Female' not found in the Excel sheet")
    exit()

try:
    if sex_type.lower() == 'female':
        driver.find_element(By.ID, 'pet_info_female_inactive').click()
    elif sex_type.lower() == 'male':
        driver.find_element(By.ID, 'pet_info_male_inactive').click()
    else:
        print(f"Invalid sex type: {sex_type}")
except Exception as e:
    print(f"Error filling pet name: {e}")


# breed

try:
    breed = df.iloc[0]['Pet breed'].strip()
except KeyError:
    print("Column 'Breed' not found in the Excel sheet")
    exit()    
try:
    # Breed
    breed_input = driver.find_element(By.XPATH, "//input[@formcontrolname='breed']")
    breed_input.send_keys(breed)
except Exception as e:
    print(f"Error filling breed: {e}")


# age
try:
    age = str(df.iloc[0]['ageYear']).strip()
except KeyError:
    print("Column 'Age (Year)' not found in the Excel sheet")
    exit()
try:
    # age
    breed_input = driver.find_element(By.XPATH, "//input[@formcontrolname='ageYear']")
    breed_input.send_keys(age)
except Exception as e:
    print(f"Error filling breed: {e}")
   




# Month
try:
    month = str(df.iloc[0]['ageMonth']).strip()
except KeyError:
    print("Column 'Age (Month)' not found in the Excel sheet")
    exit()
try:
    # Month
    breed_input = driver.find_element(By.XPATH, "//input[@formcontrolname='ageMonth']")
    breed_input.send_keys(month)
except Exception as e:
    print(f"Error filling breed: {e}")




# weight
try:
    weight = str(df.iloc[0]['weightNumber']).strip()
except KeyError:
    print("Column 'Weight' not found in the Excel sheet")
    exit()
try:
    # Breed
    breed_input = driver.find_element(By.XPATH, "//input[@formcontrolname='weightNumber']")
    breed_input.send_keys(weight)
except Exception as e:
    print(f"Error filling breed: {e}")
   
#next button
driver.find_element(By.XPATH,"/html/body/app-root/app-signup/div/mat-horizontal-stepper/div[2]/div[1]/div/div/div/div/form/div[8]/button").click()


try:
    first_name = df.iloc[0]['first_name'].strip()
except KeyError:
    print("Column 'First Name' not found in the Excel sheet")
    exit()
try:
    # Breed
    breed_input = driver.find_element(By.XPATH, "//input[@formcontrolname='first_name']")
    breed_input.send_keys(first_name)
except Exception as e:
    print(f"Error filling breed: {e}")



try:
    last_name = df.iloc[0]['last_name'].strip()
except KeyError:
    print("Column 'Last Name' not found in the Excel sheet")
    exit()
try:
    # Breed
    breed_input = driver.find_element(By.XPATH, "//input[@formcontrolname='last_name']")
    breed_input.send_keys(breed)
except Exception as e:
    print(f"Error filling breed: {e}")



try:
    phone_no = str(df.iloc[0]['phone_no']).strip()
except KeyError:
    print("Column 'Phone Number' not found in the Excel sheet")
    exit()
try:
    # Breed
    breed_input = driver.find_element(By.XPATH, "//input[@formcontrolname='phone_no']")
    breed_input.send_keys(breed)
except Exception as e:
    print(f"Error filling breed: {e}")



try:
    email = df.iloc[0]['email'].strip()
except KeyError:
    print("Column 'Email' not found in the Excel sheet")
    exit()
try:
    # Breed
    breed_input = driver.find_element(By.XPATH, "//input[@formcontrolname='email']")
    breed_input.send_keys(breed)
except Exception as e:
    print(f"Error filling breed: {e}")



try:
    password = str(df.iloc[0]['password']).strip()
except KeyError:
    print("Column 'Password' not found in the Excel sheet")
    exit()
try:
    # Breed
    breed_input = driver.find_element(By.XPATH, "//input[@formcontrolname='password']")
    breed_input.send_keys(breed)
except Exception as e:
    print(f"Error filling breed: {e}")



try:
    Confpassword = str(df.iloc[0]['confirm_password']).strip()
except KeyError:
    print("Column 'Confirm Password' not found in the Excel sheet")
    exit()
try:
    # Breed
    breed_input = driver.find_element(By.XPATH, "//input[@formcontrolname='confirm_password']")
    breed_input.send_keys(breed)
except Exception as e:
    print(f"Error filling breed: {e}")



try:
    zip_code = str(df.iloc[0]['zip_code']).strip()
except KeyError:
    print("Column 'Zip Code' not found in the Excel sheet")
    exit()
try:
    # Breed
    breed_input = driver.find_element(By.XPATH, "//input[@formcontrolname='zip_code']")
    breed_input.send_keys(breed)
except Exception as e:
    print(f"Error filling breed: {e}")


driver.find_element(By.XPATH,"/html/body/app-root/app-signup/div/mat-horizontal-stepper/div[2]/div[2]/div/div/div/div/form/div/div[8]/button").click()


element = driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator rounded-pill text-center border-primary border text-primary signup-btn mr-18 mat-flat-button mat-button-base']")
#time.sleep(10)
# Click the element

element.click()



try:
    card_number = str(df.iloc[0]['Card_number']).strip()
except KeyError:
    print("Column 'Card Number' not found in the Excel sheet")
    exit()
try:
    # Breed
    breed_input = driver.find_element(By.XPATH, "//input[@formcontrolname='number']")
    breed_input.send_keys(breed)
except Exception as e:
    print(f"Error filling breed: {e}")



try:
    cvv = str(df.iloc[0]['CVV']).strip()
except KeyError:
    print("Column 'CVV' not found in the Excel sheet")
    exit()
try:
    # Breed
    breed_input = driver.find_element(By.XPATH, "//input[@formcontrolname='breed']")
    breed_input.send_keys(breed)
except Exception as e:
    print(f"Error filling breed: {e}")


try:
    # Pet Name
    driver.find_element(By.XPATH,"//input[@formcontrolname='name']").send_keys(name)
except Exception as e:
    print(f"Error filling pet name: {e}")
try:
    
    breed_input = driver.find_element(By.XPATH, "//input[@formcontrolname='breed']")
    breed_input.send_keys(breed)
except Exception as e:
    print(f"Error filling breed: {e}")



try:
    # Breed
    breed_input = driver.find_element(By.XPATH, "//input[@formcontrolname='breed']")
    breed_input.send_keys(breed)
except Exception as e:
    print(f"Error filling breed: {e}")
try:
    # Breed
    breed_input = driver.find_element(By.XPATH, "//input[@formcontrolname='breed']")
    breed_input.send_keys(breed)
except Exception as e:
    print(f"Error filling breed: {e}")



try:
    # Age
    age_year_input = driver.find_element(By.XPATH, "//input[@formcontrolname='ageYear']")
    age_year_input.send_keys(age_year)

    age_month_input = driver.find_element(By.XPATH, "//input[@formcontrolname='ageMonth']")
    age_month_input.send_keys(age_month)
except Exception as e:
    print(f"Error filling age: {e}")

try:
    # Weight
    weight_input = driver.find_element(By.XPATH, "//input[@formcontrolname='weightNumber']")
    weight_input.send_keys(weight)
except Exception as e:
    print(f"Error filling weight: {e}")

try:
    # Owner First Name
    first_name_input = driver.find_element(By.XPATH, "//input[@formcontrolname='first_name']")
    first_name_input.send_keys(first_name)
except Exception as e:
    print(f"Error filling first name: {e}")

try:
    # Owner Last Name
    last_name_input = driver.find_element(By.XPATH, "//input[@formcontrolname='last_name']")
    last_name_input.send_keys(last_name)
except Exception as e:
    print(f"Error filling last name: {e}")

try:
    # Phone Number
    phone_no_input = driver.find_element(By.XPATH, "//input[@formcontrolname='phone_no']")
    phone_no_input.send_keys(phone_no)
except Exception as e:
    print(f"Error filling phone number: {e}")

try:
    # Email
    email_input = driver.find_element(By.XPATH, "//input[@formcontrolname='email']")
    email_input.send_keys(email)
except Exception as e:
    print(f"Error filling email: {e}")

try:
    # Password
    password_input = driver.find_element(By.XPATH, "//input[@formcontrolname='password']")
    password_input.send_keys(password)
except Exception as e:
    print(f"Error filling password: {e}")

try:
    # Confirm Password
    confirm_password_input = driver.find_element(By.XPATH, "//input[@formcontrolname='confirm_password']")
    confirm_password_input.send_keys(Confpassword)
except Exception as e:
    print(f"Error filling confirm password: {e}")

try:
    # Zip Code
    zip_code_input = driver.find_element(By.XPATH, "//input[@formcontrolname='zip_code']")
    zip_code_input.send_keys(zip_code)
except Exception as e:
    print(f"Error filling zip code: {e}")



"""
# Get data from Excel
try:
    name = df.iloc[0]['Name'].strip()
except KeyError:
    print("Column 'Name' not found in the Excel sheet")
    exit()
    
try:
    breed = df.iloc[0]['breed'].strip()
except KeyError:
    print("Column 'Breed' not found in the Excel sheet")
    exit()
    
try:
    age_year = str(df.iloc[0]['ageYear']).strip()
except KeyError:
    print("Column 'Age (Year)' not found in the Excel sheet")
    exit()
    
try:
    age_month = str(df.iloc[0]['ageMonth']).strip()
except KeyError:
    print("Column 'Age (Month)' not found in the Excel sheet")
    exit()
    
try:
    weight = str(df.iloc[0]['weightNumber']).strip()
except KeyError:
    print("Column 'Weight' not found in the Excel sheet")
    exit()
    
try:
    first_name = df.iloc[0]['first_name'].strip()
except KeyError:
    print("Column 'First Name' not found in the Excel sheet")
    exit()
    
try:
    last_name = df.iloc[0]['last_name'].strip()
except KeyError:
    print("Column 'Last Name' not found in the Excel sheet")
    exit()
    
try:
    phone_no = str(df.iloc[0]['phone_no']).strip()
except KeyError:
    print("Column 'Phone Number' not found in the Excel sheet")
    exit()
    
try:
    email = df.iloc[0]['email'].strip()
except KeyError:
    print("Column 'Email' not found in the Excel sheet")
    exit()
    
try:
    password = str(df.iloc[0]['password']).strip()
except KeyError:
    print("Column 'Password' not found in the Excel sheet")
    exit()
    
try:
    Confpassword = str(df.iloc[0]['confirm_password']).strip()
except KeyError:
    print("Column 'Confirm Password' not found in the Excel sheet")
    exit()
    

try:
    zip_code = str(df.iloc[0]['zip_code']).strip()
except KeyError:
    print("Column 'Zip Code' not found in the Excel sheet")
    exit()
    
try:
    card_number = str(df.iloc[0]['Card_number']).strip()
except KeyError:
    print("Column 'Card Number' not found in the Excel sheet")
    exit()
    
try:
    cvv = str(df.iloc[0]['pet_info_dog_inactive']).strip()
except KeyError:
    print("Column 'CVV' not found in the Excel sheet")
    exit()
"""
#driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@formcontrolname='name']").send_keys("smmrstaxthmay")
#name = df.iloc[0]['name']
#driver.implicitly_wait(10)
time.sleep(5)
driver.find_element(By.ID,"pet_info_dog_inactive").click()
#breed = df.iloc[0]['Breed']
#time.sleep(10)
driver.find_element(By.ID,"pet_info_male_inactive").click()


time.sleep(5)
driver.find_element(By.XPATH,"//button[@type='button']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@formcontrolname='breed']").send_keys("Mixed")




driver.find_element(By.XPATH,"//input[@formcontrolname='ageYear']").send_keys("1")

driver.find_element(By.XPATH,"//input[@formcontrolname='ageMonth']").send_keys("2")

driver.find_element(By.XPATH,"//input[@formcontrolname='weightNumber']").send_keys("3")

time.sleep(4)
driver.find_element(By.XPATH,"/html/body/app-root/app-signup/div/mat-horizontal-stepper/div[2]/div[1]/div/div/div/div/form/div[8]/button").click()

driver.implicitly_wait(10)

time.sleep(5)
#wait = WebDriverWait(driver, 10)
#element = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='button']")))

driver.find_element(By.XPATH,"//input[@formcontrolname='first_name']").send_keys("staxusermay")

driver.find_element(By.XPATH,"//input[@formcontrolname='last_name']").send_keys("test")


driver.find_element(By.XPATH,"//input[@formcontrolname='phone_no']").send_keys("2345678910")


driver.find_element(By.XPATH,"//input[@formcontrolname='email']").send_keys("qastaxthmay50price@yopmail.com")


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
driver.find_element(By.XPATH,"//input[@formcontrolname='number']").send_keys("4111111111111111")

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
redeem=driver.find_element(By.XPATH,"//input[@formcontrolname='couponCode']").send_keys("50%")
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
driver.get_screenshot_as_file("stax.smmr10thmay.png")



driver.implicitly_wait(3)
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)