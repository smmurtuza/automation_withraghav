# Load Excel file
df = pd.read_excel('C:\\Users\\Hp\\Desktop\\automation\\data.xlsx', sheet_name='Sheet2')

# Get data from Excel
try:
    name = df.iloc[0]['Name'].strip()
except KeyError:
    print("Column 'Name' not found in the Excel sheet")
    exit()

# ...

# Fill the form with data from the Excel sheet
try:
    # Pet Name
    driver.find_element(By.XPATH,"//input[@formcontrolname='name']").send_keys(name)
except Exception as e:
    print(f"Error filling pet name: {e}")

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

try:
    # Card Number
    card_number_input = driver.find_element(By.XPATH,
