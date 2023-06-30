from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string

driver = webdriver.Chrome()


num_submissions = 10
driver.get("http://www.midwilinc.com/web/index.php/contact")

time.sleep(2)

for i in range(num_submissions):
    name = ''.join(random.choices(string.ascii_letters, k=10))
    email = ''.join(random.choices(string.ascii_lowercase, k=5)) + "@example.com"

    name_input = driver.find_element(By.ID, "name")
    email_input = driver.find_element(By.ID, "email")
    subject_input = driver.find_element(By.ID, "subject")
    message_input = driver.find_element(By.ID, "message")

    name_input.clear()
    name_input.send_keys(name)

    email_input.clear()
    email_input.send_keys(email)

    subject_input.clear()
    subject_input.send_keys("Example Subject")

    message_input.clear()
    message_input.send_keys("Example message.")

    submit_button = driver.find_element(By.ID, "sp_qc_submit")
    submit_button.click()

    time.sleep(2)

driver.quit()
