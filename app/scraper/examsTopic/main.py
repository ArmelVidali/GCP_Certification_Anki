from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import json
from login import login
from downloadQuestions import downloadQuestions
from checkCaptcha import checkCaptcha  

# Login and get the initial page source
driver, soup = login()
page_visited_count = 0

# Loop until there is no "next page" button
while True:
    try:
        # Call the downloadQuestions function
        downloadQuestions(driver, soup)

        # Wait for the "Next Page" button to become clickable
        next_page_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-success.pull-right"))
        )

        # Click the "Next Page" button
        next_page_btn.click()

        # Wait for the page to load 
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))  
        )

        # Check if CAPTCHA is present
        captcha_present = checkCaptcha(driver)

        # If CAPTCHA is present, wait until you solved manually
        while captcha_present:
            WebDriverWait(driver, 10000000000000000000000000000).until(
            EC.presence_of_element_located((By.CLASS_NAME, "exam-question-card"))
        )
            captcha_present = checkCaptcha(driver)

        # Update the soup object to reflect the new page
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Increment the page counter
        page_visited_count += 1
        print(f"Scraping page {page_visited_count}...")

    except Exception as e:
        print(f"Finished scraping {page_visited_count} pages. Error: {e}")
        break  
