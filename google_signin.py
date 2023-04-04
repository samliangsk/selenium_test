from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from seleniumbase import SB, BaseCase


import time
import random
import os
username = os.environ.get('GOOGLE_ACCT_USER')
password = os.environ.get('GOOGLE_ACCT_PASS')
phone = os.environ.get('GOOGLE_ACCT_PHONE')
def type(elem: WebElement, text: str) -> None:

        for l in text:
                elem.send_keys(l)
                pause(30)

def pause(max_delay: int = 1000):

        time.sleep(random.triangular(100, max_delay) / 1000)
        







browser: BaseCase
with SB(uc=True,headless=True) as browser:

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
        browser.open_new_window()
        browser.get('https://meet.google.com/new/')
        time.sleep(2)


        browser.type("#identifierId", username+'\n')

        time.sleep(3)
        browser.save_screenshot('000.png')

        browser.type("#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input", password+'\n')
        time.sleep(5)
        
        browser.click("#view_container > div.zWl5kd > div.DRS7Fe.bxPAYd.k6Zj8d > div.pwWryf.bxPAYd > div.Wxwduf.Us7fWe.JhUD8d > div.WEQkZc > div.bCAAsb > form > span > section.aTzEhb.S7S4N > div.CxRgyd > div > div.pQ0lne > ul.OVnw0d > li.JDAKTe.cd29Sd.zpCp3.SmR8 > div.lCoei.YZVTmd.SmR8[data-challengeindex=\"2\"]")
        time.sleep(5)
        browser.type("#phoneNumberId", phone+'\n')
        time.sleep(20)
        browser.get('https://meet.google.com/new/')
        time.sleep(10)
        browser.save_screenshot('001.png')
        
        # set the duration of the meeting
        time.sleep(10)
        browser.click_xpath('//button[@aria-label = "Leave call"]')
        time.sleep(7)
        
        time.sleep(2)
        browser.save_screenshot('002.png')
        
        browser.switch_to_window(0)
        browser.click_xpath('/html/body/p/details/summary')
        time.sleep(1)
        browser.click_xpath('/html/body/p/details/div/div[1]/a/button')
