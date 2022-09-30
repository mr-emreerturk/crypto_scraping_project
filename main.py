# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Screen Scrapers and Spiders - Selenium

# %% load packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# %% specifiy a webdriver
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# %% use the browser to go to a web page
browser.get('http://quotes.toscrape.com/')

# %% maximize the window
browser.maximize_window()

# use a simple script to scroll down 2000 units
browser.execute_script("window.scrollTo(0, 2000)")

# %% locate the next button
next_button = browser.\
    find_element(By.PARTIAL_LINK_TEXT,'Next')

# %% click the next button
next_button.click()
# %%