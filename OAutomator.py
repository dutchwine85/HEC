import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome("/Users/tomweston/.wdm/drivers/chromedriver/mac64/96.0.4664.45/chromedriver")
driver.get(redirect_url)

driver.find_element_by_xpath("//*[@id=\"username_or_email\"]").send_keys("randomPDFbot")
driver.find_element_by_xpath("//*[@id=\"password\"]").send_keys("acrobathill9.")
driver.find_element_by_xpath("//*[@id=\"allow\"]").click()
time.sleep(3)
oaPIN = driver.find_element_by_xpath("//*[@id=\"oauth_pin\"]/p/kbd/code").text
print("\n")

auth.get_access_token(oaPIN)
time.sleep(1.5)
driver.close()
print("OAuth PIN = "+oaPIN)