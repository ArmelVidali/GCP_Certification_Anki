from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import json


def login():
    """ Login to Exams topic website """
    
    # Initialize the WebDriver 
    driver = webdriver.Chrome()

    # Open the website and navigate to the login page
    driver.get('https://www.examtopics.com/')
    output_page_html = driver.page_source
    soup = BeautifulSoup(output_page_html, 'html.parser')

    # Find the login link and click it
    login_link = soup.find('a', href='/login/')
    login_link_url = login_link['href'] if login_link else None

    if login_link_url:
        driver.get(f"https://www.examtopics.com{login_link_url}")
        
        # Wait until the email input field is available
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "etemail")))

        # Locate the email and password fields 
        email_field = driver.find_element(By.ID, "etemail")
        password_field = driver.find_element(By.ID, "etpass")
        login_button = driver.find_element(By.CLASS_NAME, "btn.btn-primary.btn-lg.login-button")

        # Send the credentials 
        with open("params.json", "r", encoding="utf-8") as paramsFile:
                credentials = json.load(paramsFile)
                print(credentials)
        email_field.send_keys(credentials["examTopicEmail"]) 
        password_field.send_keys(credentials["examTopicPassword"])       

        login_button.click()



        driver.get('https://www.examtopics.com/exams/google/professional-cloud-developer/view/10')

        # Process the page content
        output_page_html = driver.page_source
        soup = BeautifulSoup(output_page_html, 'html.parser')
        
    else:
        print("Login link not found.")

    # Close the driver when done
    return [driver, soup]
