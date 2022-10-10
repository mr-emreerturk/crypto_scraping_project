#%%
#Selenium imports
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
import logging

logging.basicConfig(filename="//Users/emre/Documents/GitHub/crypto_scraping_project/scraper.log",level=logging.DEBUG)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# %%
def launch_chrome(url):
    '''A method to install the latest Chrome driver and get url
    ---------
    Parameters:
    url = url defined by user'''
    global driver
    # installing driver making sure that new driver is up to date
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    return driver

def yahoo_header():
    '''Returns headers from finance.yahoo.com/cryptocurrencies'''

    global cols
    target_columns = ['Name', 'Price (Intraday)', 'Market Cap', 'Circulating Supply'] 
    # Getting all columns on URL using XPATH
    cols_mask = driver.find_elements(By.XPATH,'//*[@id="scr-res-table"]/div[1]/table/thead/tr/th')
    # Sequencing all elements to list if the header is in target columns
    cols = [i.text for i in cols_mask if i.text in target_columns]
    # Return final list
    return cols

def yahoo_body():
    global cryptocurrencies_list
    if len(cryptocurrencies_list) == 0:
        cryptocurrencies_list = []

    # Checking length of table on URL
    x = len(driver.find_elements(By.XPATH,'//*[@id="scr-res-table"]/div[1]/table/tbody/tr'))

    # Looping through every row on URL until last row
    for row_n in range(1, x): 
        # date_time = ct = datetime.datetime.now().strftime("%D %T")

        # Finding elements matching to headers using relative XPATH
        name = driver.find_element(By.XPATH,f'//*[@id="scr-res-table"]/div[1]/table/tbody/tr[{row_n}]/td[2]') # Name
        price = driver.find_element(By.XPATH,f'//*[@id="scr-res-table"]/div[1]/table/tbody/tr[{row_n}]/td[3]') # Price (Intraday)
        marketcap = driver.find_element(By.XPATH,f'//*[@id="scr-res-table"]/div[1]/table/tbody/tr[{row_n}]/td[6]') # MarketCap
        circ_supply = driver.find_element(By.XPATH,f'//*[@id="scr-res-table"]/div[1]/table/tbody/tr[{row_n}]/td[10]') # Circulating Supply

        # Creating Tuple as preperation for HDF5 file
        my_tuple = (name.text, price.text, marketcap.text, circ_supply.text)
        # Adding to body
        cryptocurrencies_list.append(my_tuple)
# %%
launch_chrome('https://finance.yahoo.com/cryptocurrencies/')
yahoo_header()
# %%
