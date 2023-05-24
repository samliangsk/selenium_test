from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium import common
from seleniumbase import SB, BaseCase


import time
import random
import os
import signal
import subprocess

username = os.environ.get('GOOGLE_ACCT_USER')
password = os.environ.get('GOOGLE_ACCT_PASS')
phone = os.environ.get('GOOGLE_ACCT_PHONE')
def type(elem: WebElement, text: str) -> None:

        for l in text:
                elem.send_keys(l)
                pause(30)

def pause(max_delay: int = 1000):

        time.sleep(random.triangular(100, max_delay) / 1000)
        



# run on machines out of docker sudo modprobe -r v4l2loopback\nsudo modprobe v4l2loopback devices=2 video_nr=0,64 exclusive_caps=1,1\n
browser: BaseCase
with SB(uc=True,headless=False) as browser:
        prog = subprocess.Popen('ffmpeg -hide_banner -loglevel error -stream_loop -1 -re -i ./fake_video.flv -f v4l2 /dev/video64',shell=True)
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
        print('opening webRTC collection page')
        browser.open_new_window()
        
        # login
        browser.get('http://accounts.google.com')
        time.sleep(2)
        browser.type("#identifierId", username+'\n')
        time.sleep(3)
        try:
                browser.type("#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input", password+'\n')
        except common.exceptions.NoSuchElementException:
                pass
        time.sleep(5)
        browser.save_screenshot('000.png')
        
        # try going around the security check
        try:
                browser.click("#view_container > div.zWl5kd > div.DRS7Fe.bxPAYd.k6Zj8d > div.pwWryf.bxPAYd > div.Wxwduf.Us7fWe.JhUD8d > div.WEQkZc > div.bCAAsb > form > span > section.aTzEhb.S7S4N > div.CxRgyd > div > div.pQ0lne > ul.OVnw0d > li.JDAKTe.cd29Sd.zpCp3.SmR8 > div.lCoei.YZVTmd.SmR8[data-challengeindex=\"2\"]")
                time.sleep(5)
                browser.save_screenshot('001.png')
                browser.type("#phoneNumberId", phone+'\n')
                time.sleep(20)
        except common.exceptions.NoSuchElementException:
                pass
        
        # Join meeting
        browser.get('https://meet.google.com/new/')
        time.sleep(10)
        browser.save_screenshot('002.png')
        # set the duration of the meeting
        time.sleep(30)
        
        # leave call
        browser.click_xpath('//button[@aria-label = "Leave call"]')
        time.sleep(7)
        time.sleep(2)
        browser.save_screenshot('003.png')
        
        # download WebRTC data
        browser.switch_to_window(0)
        browser.click_xpath('/html/body/p/details/summary')
        time.sleep(1)
        browser.click_xpath('/html/body/p/details/div/div[1]/a/button')
        time.sleep(5)
        # os.kill(prog.pid, signal.SIGKILL)
        os.killpg(os.getpgid(prog.pid), signal.SIGTERM)
        # subprocess.call(['v4l2loopback-ctl delete /dev/video2'])
        
