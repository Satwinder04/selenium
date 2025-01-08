# Make sure to install the required packages
# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time  # Import the time module

# Set up the Chrome WebDriver
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")
time.sleep(3)  # Wait for 3 seconds

# Find the search box
search_box = driver.find_element("name", "q")
time.sleep(3)  # Wait for 3 seconds

# Send keys "selenium" and execute the search
search_box.send_keys("selenium")
time.sleep(3)  # Wait for 3 seconds
search_box.send_keys(Keys.RETURN)
time.sleep(3)  # Wait for 3 seconds

# Find and click the search button (assuming it's the first button)
search_button = driver.find_element("name", "btnK")  # Adjust the selector if necessary
search_button.click()
time.sleep(3)  # Wait for 3 seconds

# Optionally, you can add a wait here to see the results
# driver.implicitly_wait(10)

# Close the browser after a while (optional)
# driver.quit()
