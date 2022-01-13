######### Notes #########
# Javascript DOM can access any elements on web page just like Selenium
# Selenium has a method to execute javascript code
# text method doesn't grab text that the test has entered into a field
# get attribute value is inherited from javascript DOM
# driver.execute_script allows you to pass javascript through selenium
######### Imports #########
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
######### Declarations #########
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
######### Test #########
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").click()
driver.find_element_by_name("name").send_keys("Dusty")
print(driver.find_element_by_name("name").get_attribute("value"))
driver.execute_script('return document.getElementsByName("name")[0].value')

shopButton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();",shopButton)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")