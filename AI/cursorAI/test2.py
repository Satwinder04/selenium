from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (make sure to specify the correct path to your WebDriver)
driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox

# URL of the login page
login_url = "https://online.btes.co.in/login/index.php"

# Open the login page
driver.get(login_url)

# Locate the username and password fields
username_field = driver.find_element(By.ID, "username")  # Adjust the selector if necessary
password_field = driver.find_element(By.ID, "password")  # Adjust the selector if necessary

# Enter your credentials
username_field.send_keys("satwinder@123")  # Replace with your username
password_field.send_keys("Satwinder@123")    # Replace with your password

# Submit the form
password_field.send_keys(Keys.RETURN)

# Wait for a few seconds to see the result
time.sleep(5)


# Close the browser
driver.quit()