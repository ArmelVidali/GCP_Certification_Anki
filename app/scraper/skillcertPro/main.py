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

""" # Get alls tests from the website
test_links = soup.find_all("a",class_="post-page-numbers")
for link in test_links:
    try:
        #Start test to show questions and links
        start_test_btn = soup.find("input", class_='wpProQuiz_button')
        start_test_btn.click()
        
        # Call the downloadQuestions function
        downloadQuestions(driver, soup)
        
        #Go to the next test
        link.click()
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')


        print(f"Scraping page {page_visited_count}...")

    except Exception as e:
        print(f"Finished scraping {page_visited_count} pages. Error: {e}")
        break  
 """