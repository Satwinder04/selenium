from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver (make sure to specify the correct path to your WebDriver)
driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox

try:
    # Open the Flipkart website
    driver.get("https://www.flipkart.com/#")

    # Wait for the page to load
    time.sleep(5)  # Adjust sleep time as necessary

    # Close the login popup if it appears
    try:
        close_button = driver.find_element(By.XPATH, "//button[contains(text(), '✕')]")
        close_button.click()
    except Exception as e:
        print("Login popup not found or already closed.")

    # Locate the "Electronics" menu and hover over it
    electronics_menu = driver.find_element(By.XPATH, "//span[text()='Electronics']")
    ActionChains(driver).move_to_element(electronics_menu).perform()

    # Wait for the submenu to appear
    time.sleep(2)

    # Locate the "Audio" submenu and hover over it
    audio_menu = driver.find_element(By.XPATH, "//a[text()='Audio']")
    ActionChains(driver).move_to_element(audio_menu).perform()

    # Wait for the submenu to appear
    time.sleep(2)

    # Click on "Bluetooth Speakers"
    bluetooth_speakers = driver.find_element(By.XPATH, "//a[text()='Bluetooth Speakers']")
    bluetooth_speakers.click()

    # Wait for a while to see the results
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()