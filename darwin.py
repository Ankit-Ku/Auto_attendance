from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path=r'C:/Users/Ankit Singh/Desktop/tutorial/chromedriver.exe')
driver.get("https://toppr.darwinbox.in/user/login")
driver.maximize_window()
driver.find_element_by_id('UserLogin_username').send_keys('ankit.ku@toppr.in')
driver.find_element_by_id('UserLogin_password').send_keys('Ankit.123')
driver.find_element_by_id('login-submit').click()
driver.find_element_by_link_text('Attendance').click()
time.sleep(1)
driver.find_element_by_id('attendance_request').click()
time.sleep(1)
driver.find_element_by_name('AttendanceRequestForm[message]').send_keys('Work from home')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="edit_attendance_form"]/div[1]/div[6]/div[1]/div/input').click()
driver.find_element_by_xpath('//*[@id="edit_attendance_form"]/div[1]/div[6]/div[1]/div/div[2]/div[2]').click()
driver.find_element_by_id('add_request_btn').click()
driver.quit()