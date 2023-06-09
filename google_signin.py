from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium import common
from seleniumbase import SB, BaseCase


import time
import random
import os
import signal
import subprocess
import sys

# take Google Account info from the system defined by users

username = os.environ.get('GOOGLE_ACCT_USER')
password = os.environ.get('GOOGLE_ACCT_PASS')
phone = os.environ.get('GOOGLE_ACCT_PHONE')

        
def start_ffmpeg():
        prog = subprocess.Popen('ffmpeg -hide_banner -loglevel error -stream_loop -1 -re -i ./fake_video.mp4 -f v4l2 /dev/video64',shell=True)
        return prog


def main():
        browser: BaseCase
        with SB(uc=True) as browser:
                
                # store program info for later termination of ffmpeg, or it might keep running in the background
                prog = start_ffmpeg()
                
                # set browser options to default microphone and camera to on
                browser.driver.execute_cdp_cmd(
                        "Browser.grantPermissions",
                        {
                                "origin": 'https://meet.google.com',
                                "permissions": ["geolocation", "audioCapture", "displayCapture", "videoCapture",
                                        "videoCapturePanTiltZoom"]
                        },
                )
                
                # open WebRTC page which will later dump WebRTC data
                browser.get("chrome://webrtc-internals")
                time.sleep(1)
                
                
                # open a new window to join the meeting
                browser.open_new_window()
                
                
                # login
                browser.get('http://accounts.google.com')
                time.sleep(2)
                browser.type("#identifierId", username+'\n')
                time.sleep(3)
                # enter the password, skip it if automatically logined
                try:
                        browser.type("#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input", password+'\n')
                except common.exceptions.NoSuchElementException:
                        pass
                
                # wait for a while for the page to load and take a screenshot to verify the current progress
                time.sleep(3)
                browser.save_screenshot('000.png')
                
                # try enter phone number to pass verification, skip if automatically logined
                try:
                        browser.click("#view_container > div.zWl5kd > div.DRS7Fe.bxPAYd.k6Zj8d > div.pwWryf.bxPAYd > div.Wxwduf.Us7fWe.JhUD8d > div.WEQkZc > div.bCAAsb > form > span > section.aTzEhb.S7S4N > div.CxRgyd > div > div.pQ0lne > ul.OVnw0d > li.JDAKTe.cd29Sd.zpCp3.SmR8 > div.lCoei.YZVTmd.SmR8[data-challengeindex=\"2\"]")
                        
                        time.sleep(5)
                        browser.save_screenshot('001.png')
                        
                        browser.type("#phoneNumberId", phone+'\n')
                        time.sleep(20)
                except common.exceptions.NoSuchElementException:
                        pass
                
                
                
                # Join meeting if address is passed in
                if len(sys.argv)==2:
                        browser.get(sys.argv[1])
                        time.sleep(3)
                        browser.click_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[14]/div[3]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/button/span')
                        time.sleep(2)
                else:
                        # Start meeting
                        browser.get('https://meet.google.com/new/')
                        time.sleep(5)
                        # if this is a new started meeting, print the url for others to join
                        print(str(browser.get_current_url()))
                
                
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
        
if __name__ =='__main__':
        main()
