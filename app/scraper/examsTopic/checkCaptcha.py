from selenium.webdriver.common.by import By

""" Check for Captcha, to interrupt scraping as solve it by hand """


def checkCaptcha(driver):
    try:
        captcha = driver.find_element(By.CLASS_NAME, "captcha-container")
        return True
    except:
        return False
