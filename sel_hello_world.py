import logging
import os
import random
import time
import typing
import sys
import re
import subprocess

from pyvirtualdisplay.display import Display
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('http://www.google.com')
print(driver.title)
driver.close()