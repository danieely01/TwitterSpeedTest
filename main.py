import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import win32api

PROMISED_UP = 150
PROMISED_DOWN = 10
path = os.environ['PATH']
TWITTER_EMAIL = os.environ['TWITTER_MAIL']
TWITTER_PASSWORD = os.environ['PASSWORD']
URL = "https://www.speedtest.net/"
TWITTER = "https://twitter.com/home?lang=hu"
TWITTER_nAME = os.environ['TWITTER_NAME']
ONE_MIN = 60


class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = PROMISED_UP
        self.down = PROMISED_DOWN
        self.s = Service()
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=self.s, options=self.options)

    def get_internet_speed(self):
        self.driver.get(url=URL)
        time.sleep(2)
        accept_cookie = self.driver.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']")
        accept_cookie.click()
        go_button = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        go_button.click()
        time.sleep(ONE_MIN)

        download_data = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        upload_data = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        if float(download_data.text) < self.down or float(upload_data.text) < self.up:
            self.up = float(upload_data.text)
            self.down = float(download_data.text)
            twitter.tweet_at_provider()
        else:
            win32api.MessageBox(0, 'Your Internet Connection is good.', '')

    def tweet_at_provider(self):
        self.driver.get(url=TWITTER)
        time.sleep(5)
        input_shelf = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        input_shelf.send_keys(TWITTER_EMAIL)

        continue_button = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]")
        continue_button.click()
        time.sleep(3)
        try:
            #-----------Human Verification---------------
            twitter_name_check = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
            twitter_name_check.send_keys(TWITTER_nAME)
            twitter_name_check_button = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div")
            twitter_name_check_button.click()
            time.sleep(2)
            #------ Pop-up window----------------------
            twitter_cookie = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]")
        except:
            pass
        finally:
            time.sleep(3)
            input_password = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            input_password.send_keys(TWITTER_PASSWORD)
            login_button = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")
            login_button.click()
            time.sleep(5)
            tweeting = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
            message = f"Hey Internet Provider! " \
                      f"Why is my internet speed {self.down} down/{self.up} up when I pay " \
                      f"for {PROMISED_DOWN} down/{PROMISED_UP} up?"

            tweeting.send_keys(message)


twitter = InternetSpeedTwitterBot()
twitter.get_internet_speed()
