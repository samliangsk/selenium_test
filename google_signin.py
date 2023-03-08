from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

from seleniumbase import SB, undetected
# import undetected_chromedriver as uc

import time
import random
def type(elem: WebElement, text: str) -> None:

        for l in text:
                elem.send_keys(l)
                pause(30)

def pause(max_delay: int = 1000):

        time.sleep(random.triangular(100, max_delay) / 1000)
        
# options = undetected.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_experimental_option("useAutomationExtension", False)
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# options.add_experimental_option("prefs", {
#             "profile.default_content_setting_values.media_stream_mic": 1,
#             "profile.default_content_setting_values.media_stream_camera": 1,
#             "profile.default_content_setting_values.geolocation": 0,
#             "profile.default_content_setting_values.notifications": 1,
#             "profile.managed_default_content_settings.popups": 0,
#             "profile.default_content_setting_values.automatic_downloads": 1,
#         })

# options.add_argument('--allow-running-insecure-content')

from seleniumbase import BaseCase
from seleniumbase.core.browser_launcher import _set_chrome_options
# class OverriddenBaseCase(BaseCase):
#         def __init__(self, *args, **kwargs):
#                 super().__init__(*args, **kwargs)
#                 self.settings_file = None
#                 self.slow_mode = False
#                 self.log_path = "latest_logs"
#                 self.headless2 = False
#                 self.report_on = False
#     def get_new_driver(self, *args, **kwargs):
#         """ This method overrides get_new_driver() from BaseCase. """
#         options: webdriver.ChromeOptions = _set_chrome_options()
#         options.add_experimental_option(
#             "excludeSwitches", ["enable-automation"]
#         )
#         options.add_experimental_option("useAutomationExtension", False)
#         if self.headless:
#             options.add_argument("--headless")
#         return webdriver.Chrome(options=options)


# browser = uc.Chrome(options=options)

# new_driver = webdriver.Chrome(options=options)

browser: BaseCase
with SB(uc=True,headless=True) as browser:
        # browser: BaseCase
        # browser.switch_to_driver(new_driver)
# try:
#         browser = OverriddenBaseCase()
#         browser.browser = "chrome"
#         browser.headless = True
#         browser.headed = False
#         browser.undetectable = True
        # browser.setUp()
# browser.get("https://stackoverflow.com")
        browser.driver.execute_cdp_cmd(
                "Browser.grantPermissions",
                {
                        "origin": 'https://meet.google.com',
                        "permissions": ["geolocation", "audioCapture", "displayCapture", "videoCapture",
                                "videoCapturePanTiltZoom"]
                },
        )
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

        browser.type("#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input", 'ENTER YOUR PASSWORD\n')
        # print(browser.title)
        time.sleep(3)
        browser.save_screenshot('001.png')
        time.sleep(3)
        browser.save_screenshot('002.png')
        browser.get_title()
        time.sleep(100)
        # browser.close()
