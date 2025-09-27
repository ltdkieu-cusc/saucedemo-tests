#Script chạy test login với tài khoản "locked_out_user", cố ý fail để tạo log lỗi (e.g., "Epic sadface"). 
#Lỗi được in ra console, pipeline sẽ capture.
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)

# try:
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
# except Exception as e:
#     print(f"[ERROR] {str(e)}")  # In lỗi ra console
# finally:
#     driver.quit()
#Lấy Log Thực Tế Từ Saucelabs.com
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Remote(
    command_executor='https://ondemand.saucelabs.com:443/wd/hub',
    options=options,
    desired_capabilities={
        'username': 'oauth-ltdkieu-aafe7',
        'accessKey': 'yf65bb46c-1103-4980-85f2-03798b069609',
        'browserName': 'chrome'
    }
)

try:
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    logs = driver.get_log('browser')  # Lấy log từ browser
    with open('error_log.txt', 'w') as f:
        for log in logs:
            if 'ERROR' in log['message']:
                f.write(f"[ERROR] {log['message']}\n")
except Exception as e:
    with open('error_log.txt', 'a') as f:
        f.write(f"[ERROR] {str(e)}\n")
finally:
    driver.quit()
