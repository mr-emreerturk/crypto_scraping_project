# Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import datetime
import numpy as np

# Global settings for the driver
chrome_options = Options()
chrome_options.add_experimental_option(
    "detach", True
)  # keeps driver open until manual termination
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
)  # Set up user-agent for ethical scraping


class CoinDeskScraper:
    def __init__(self):
        super().__init__()
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            chrome_options=chrome_options,
        )
        self.top_crypto = [
            "bitcoin",
            "ethereum",
            "tether",
            "usd-coin",
            "bnb",
            "xrp",
            "binance-usd",
            "cardano",
            "solana",
            "dogecoin",
            "polkadot-new",
            "polygon",
            "tron",
        ]
        self.news_list = []

    def scrape_coindesk(self):
        for crypto in self.top_crypto:

            self.driver.get(f"https://www.coindesk.com/search?s={crypto}&df=24")
            date = datetime.datetime.now().strftime("%D")
            coin = crypto
            news = self.driver.find_element(
                By.XPATH,
                '//*[@id="queryly_advanced_container"]/div[5]/div[1]/div[1]/span/h6',
            )
            self.news_list.append([date, coin, str(news.text.split(" ")[1])])
        # self.driver.quit()

        return self.news_list
