#Script chạy test login với tài khoản "locked_out_user", cố ý fail để tạo log lỗi (e.g., "Epic sadface"). 
#Lỗi được in ra console, pipeline sẽ capture.
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
except Exception as e:
    print(f"[ERROR] {str(e)}")  # In lỗi ra console
finally:
    driver.quit()
