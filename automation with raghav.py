from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver =webdriver.Chrome(executable_path="C:\\murtuza\\chromedriver_win32\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://google.com")
#print(driver.title)

    @classmethod
    def test_search_automationstepbystep(self):
        
        self.driver.get("https://google.com")
        self.driver.find_element("name","q").send_keys("psl")
        self.driver.find_element("name","btnk").click()
#search.send_keys("test")
#search.send_keys(keys.RETURN)

        self.driver.close()
        self.driver.quit()
print("test completed")



"""#driver.get("http://gmail.com")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# initialize the web driver
#driver = webdriver.Firefox()

# open the Gmail login page
driver.get("https://gmail.com")

# locate the username and password fields
username = driver.find_element_by_id("identifierId")
password = driver.find_element_by_name("password")

# enter your Gmail username and password
username.send_keys("invision.murtuza@gmail.com")
username.send_keys(Keys.RETURN)
password.send_keys("Pakistan@321")
password.send_keys(Keys.RETURN)
"""