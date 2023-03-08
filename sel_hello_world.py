import logging
import os
import random
import time
import typing
import sys
import re
import subprocess

# from pyvirtualdisplay.display import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=options)
driver.get('http://www.google.com')
print(driver.title)
driver.close()