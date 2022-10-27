# Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import datetime

# Global settings for the driver
chrome_options = Options()
chrome_options.add_experimental_option(
    "detach", True
)  # keeps driver open until manual termination


class YahooScraper:
    def __init__(self):
        super().__init__()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.cryptocurrencies_list = []

    def scrape_yahoo(self):
        """A method that returns the body of the table from finance.yahoo.com/cryptocurrencies"""

        # Checking length of table on URL
        self.driver.get("https://finance.yahoo.com/cryptocurrencies/")
        x = len(
            self.driver.find_elements(
                By.XPATH, '//*[@id="scr-res-table"]/div[1]/table/tbody/tr'
            )
        )

        # Looping through every row on URL until last row
        for row_n in range(1, x):
            # date_time = ct = datetime.datetime.now().strftime("%D %T")

            # Finding elements matching to headers using relative XPATH
            date = datetime.datetime.now().strftime("%D")
            name = self.driver.find_element(
                By.XPATH,
                f'//*[@id="scr-res-table"]/div[1]/table/tbody/tr[{row_n}]/td[2]',
            )  # Name
            price = self.driver.find_element(
                By.XPATH,
                f'//*[@id="scr-res-table"]/div[1]/table/tbody/tr[{row_n}]/td[3]',
            )  # Price (Intraday)
            marketcap = self.driver.find_element(
                By.XPATH,
                f'//*[@id="scr-res-table"]/div[1]/table/tbody/tr[{row_n}]/td[6]',
            )  # MarketCap
            circ_supply = self.driver.find_element(
                By.XPATH,
                f'//*[@id="scr-res-table"]/div[1]/table/tbody/tr[{row_n}]/td[10]',
            )  # Circulating Supply

            # Adding to body
            self.cryptocurrencies_list.append(
                [date, name.text, price.text, marketcap.text, circ_supply.text]
            )

        return self.cryptocurrencies_list
