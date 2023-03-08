from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

from seleniumbase import SB
import undetected_chromedriver as uc

import time
import random
def type(elem: WebElement, text: str) -> None:

        for l in text:
                elem.send_keys(l)
                pause(30)

def pause(max_delay: int = 1000):

        time.sleep(random.triangular(100, max_delay) / 1000)
        
# options = Options()
# options.add_argument("start-maximized")
# # options.add_experimental_option("useAutomationExtension", False)
# # options.add_experimental_option('excludeSwitches', ['enable-automation'])
# # options.add_experimental_option("prefs", {
# #             "profile.default_content_setting_values.media_stream_mic": 1,
# #             "profile.default_content_setting_values.media_stream_camera": 1,
# #             "profile.default_content_setting_values.geolocation": 0,
# #             "profile.default_content_setting_values.notifications": 1
# #         })


# options.add_argument("--disable-extensions")
# options.add_argument("--profile-directory=Default")
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--disable-plugins-discovery")
# options.add_argument("user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0'")

# options.add_argument('--use-fake-device-for-media-stream')
# options.add_argument('--disable-gpu')
# options.add_argument('start-maximized')
# options.add_argument(
#         '--disable-blink-features=AutomationControlled')
# options.add_argument("--no-sandbox")
# # options.add_argument("--headless")
# options.add_argument('--allow-running-insecure-content')

# browser = uc.Chrome(options=options)
with SB(uc=True,headless=True) as browser:
# browser.get("https://stackoverflow.com")
        browser.get("chrome://webrtc-internals")
        time.sleep(1)
        browser.open_new_window('tab')
        browser.get('https://meet.google.com/new/')
        print('hello?')
        time.sleep(2)
        # browser.find_elements(By.ID,'identifierId')
        # actions = ActionChains(browser)
        # browser.refresh()


        browser.type("#identifierId", 'samliangsk@gmail.com\n')
        # print('hello??')
        time.sleep(3)
        browser.save_screenshot('000.png')

        browser.type("#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input", '#ENTER YOUR PASSWORD#\n')
        # print(browser.title)
        time.sleep(3)
        browser.save_screenshot('001.png')
        time.sleep(3)
        browser.save_screenshot('002.png')
        browser.get_title()
        
        browser.close()



