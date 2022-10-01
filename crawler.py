#%% Import
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#%% Initial set up
url = 'https://finance.yahoo.com/cryptocurrencies/'

# installing driver making sure that new driver is
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

search = driver.find_elements(by=By.TAG_NAME,value='tr')

driver.quit()
# %%
