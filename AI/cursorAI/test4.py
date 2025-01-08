from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the YouTube Shorts link
driver.get("https://www.youtube.com/shorts/d3Z4clFFKIw")

# Wait for the video to load
time.sleep(5)

# Pause the video
pause_button = driver.find_element(By.CSS_SELECTOR, 'button.ytp-large-play-button')
pause_button.click()  # Click to pause

# Wait for a moment
time.sleep(2)

# Seek the video by 10 seconds
video = driver.find_element(By.CSS_SELECTOR, 'video')
current_time = driver.execute_script("return arguments[0].currentTime", video)
driver.execute_script("arguments[0].currentTime = arguments[1];", video, current_time + 10)

# Wait for a moment
time.sleep(2)

# Play the video
play_button = driver.find_element(By.CSS_SELECTOR, 'button.ytp-play-button')
play_button.click()  # Click to play

# Wait for a while to observe the playback
time.sleep(10)

# Close the driver
driver.quit()
