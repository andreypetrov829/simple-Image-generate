import ast, glob, os, shutil, time
from dotenv import load_dotenv, find_dotenv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import base64
from io import BytesIO
from PIL import Image

class RegisterClass:
    def __init__(self):
        self.first_name = "sdfsdf"
        self.run_browser()
        self.download()
        
    def run_browser(self):
        options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(options=options)
        # self.browser.maximize_window()
        self.browser.get("https://instant-portrait.com/")
    def download(self):
        WebDriverWait(self.browser, 10)
        leafs = self.browser.find_element(by=By.TAG_NAME, value="input")
        leafs.send_keys(os.getcwd() + "/photo.jpg")
        time.sleep(3)
        self.browser.find_elements(by=By.TAG_NAME, value='button')[1].click()
        time.sleep(5)
        img = self.browser.find_elements(by=By.TAG_NAME, value='img')[2]
        img_bytes = base64.b64decode(img.get_attribute("src").split(',')[1])
        image = Image.open(BytesIO(img_bytes))
        image.save('./image/my_image.jpg')
        i = 0
        for j in range(100):
            time.sleep(2)
            self.browser.find_elements(by=By.TAG_NAME, value='button')[0].click()
            time.sleep(5)
            img_bytes = base64.b64decode(img.get_attribute("src").split(',')[1])
            image = Image.open(BytesIO(img_bytes))
            image.save('./image/my_image' + str(i) + '.jpg')
            i = i + 1
        
        
if __name__ == "__main__":
    RegisterClass()
        