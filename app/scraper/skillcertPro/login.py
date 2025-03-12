from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import json


def login():
    """ Login to skillcert website """
    
    # Initialize the WebDriver 
    driver = webdriver.Firefox()

    # Open the website and navigate to the login page
    driver.get('https://skillcertpro.com/sign-in/')
    output_page_html = driver.page_source
    soup = BeautifulSoup(output_page_html, 'html.parser')

        
    # Wait until the email input field is available
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username-1661")))

    # Locate the email and password fields 
    email_field = driver.find_element(By.ID, "username-1661")
    password_field = driver.find_element(By.ID, "user_password-1661")
    login_button = driver.find_element(By.ID, "um-submit-btn")
    
    # Send the credentials 
    with open("params.json", "r", encoding="utf-8") as paramsFile:
            credentials = json.load(paramsFile)
            
            
    email_field.send_keys(credentials["skillCertProEmail"]) 
    password_field.send_keys(credentials["skillCertProPassword"])       
    login_button.click()
    driver.get('https://skillcertpro.com/professional-cloud-developer-practice-tests/')
    # Process the page content
    output_page_html = driver.page_source
    soup = BeautifulSoup(output_page_html, 'html.parser')
 

    # Close the driver when done
    return [driver, soup]


login()