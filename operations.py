# Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Rest
from bs4 import BeautifulSoup
import time
import pandas as pd
import datetime
import h5py
import numpy as np

# Global settings for the driver
chrome_options = Options()
chrome_options.add_experimental_option(
    "detach", True
)  # keeps driver open until manual termination


class Operations:
    def __init__(self):
        super().__init__()

    def launch_chrome(self, url):
        """A method to install the latest Chrome driver and get url
        ---------
        Parameters:
        url = url defined by user"""

        global driver
        # installing driver making sure that new driver is up to date
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)
        return driver
