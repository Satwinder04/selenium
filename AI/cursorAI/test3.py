from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the parent website
driver.get("https://testautomationpractice.blogspot.com/")

# Capture a screenshot of the entire webpage
driver.save_screenshot('screenshot_full_page.png')

# Open a new tab/window
driver.execute_script("window.open('https://www.example.com', '_blank');")

# Get the window handles
parent_window = driver.current_window_handle
all_windows = driver.window_handles

# Switch to the new window
for window in all_windows:
    if window != parent_window:
        driver.switch_to.window(window)
        break

# Perform actions in the new window
time.sleep(5)  # Wait for demonstration purposes

# Capture a screenshot of a specific element (example: an element with id 'exampleElement')
try:
    element = driver.find_element_by_id('exampleElement')  # Replace with actual element ID
    element.screenshot('AI\cursorAI\screenshot_element.png')
except NoSuchElementException:
    print("Element not found, capturing screenshot of the entire page instead.")
    driver.save_screenshot('screenshot_element_failed.png')

# Close the new window
driver.close()

# Switch back to the parent window
driver.switch_to.window(parent_window)

# Continue with actions in the parent window
# ...

# Close the driver
driver.quit()