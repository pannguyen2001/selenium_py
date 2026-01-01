import os
from selenium import webdriver
from loguru import logger
from dotenv import load_dotenv
from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

load_dotenv()
DEMO_URL = os.getenv("DEMO_URL")

def main():
    try:
        # options to prevent default open browser before run test
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument('--headless')
        options.add_argument('--profile-directory=Default') # here
        # get browser
        browser = webdriver.Chrome(options=options)
        # visit link by browser
        browser.get(DEMO_URL)
        # get maximize window
        browser.maximize_window()
        # get header title
        title = browser.title
        logger.info(title)
        # Assert that title contains 'Swag Labs' or not
        assert "Swag Labs" in title, f"Title is not correct. Expected: 'Swag Labs' in title, Actual: {title}."

        # get element
        element: any = browser.find_element(By.NAME, "user-name") # return first element found
        logger.info(f"{element = }, {type(element) = }")
        element.send_keys("standard_user")

        elements: List = browser.find_elements(By.NAME, "password") # return list element found
        logger.info(f"{elements = }, {type(elements) = }")

        # close browser
        browser.close()
        # browser.quit()
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    main()
    pass
