# Selenium imports
from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# General imports
import datetime
import logging

# Global settings for the driver
chrome_options = Options()
chrome_options.add_experimental_option(
    "detach", True
)  # keeps driver open until manual termination
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
)  # Set up user-agent for ethical scraping


class Scrapers:
    def __init__(self):
        super().__init__()
        # Initializing web driver
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            chrome_options=chrome_options,
        )
        self.top_crypto = [  # Crypto currencies of interest
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
            "polygon",
            "tron",
        ]
        # empty lists for methods
        self.cryptocurrencies_list = []
        self.crypto_project_info = []
        self.news_list = []

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

    def scrape_coinmarketcap(self):
        """A method that returns the body of the table from coinmarketcap.com"""

        for crypto in self.top_crypto:
            try:
                self.driver.get(
                    f"https://coinmarketcap.com/currencies/{crypto}/project-info/"
                )
                self.driver.implicitly_wait(10)  # seconds

                # Not all pages have an additional layer in dynamic component. If there is no dynamic component, the try block is not needed.
                # The try block clicks on "Social Stats"
                try:
                    # Cookie element blocks the selection of target element "Social Stats"
                    cookie = self.driver.find_element(
                        By.XPATH, '//*[@id="cmc-cookie-policy-banner"]/div[2]'
                    )
                    cookie.click()
                except NoSuchElementException:
                    pass

                # Depending on the information available, there are multiple menus to click,
                # determining the length of that block is key to find the correct X-Path for "Social Status"
                mask_number_of_buttons = self.driver.find_elements(
                    By.XPATH,
                    '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div[2]/div/div[1]',
                )

                # For loop to check the lenghth of sub-menu
                for e in mask_number_of_buttons:
                    test = e.text.split("\n")
                    number_of_buttons = len(test)

                # finding "social status" element depending on page
                if number_of_buttons == 2:
                    element = self.driver.find_element(
                        By.XPATH,
                        '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div[2]',
                    )
                elif number_of_buttons == 3:
                    element = self.driver.find_element(
                        By.XPATH,
                        '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div[3]',
                    )
                elif number_of_buttons == 4:
                    element = self.driver.find_element(
                        By.XPATH,
                        '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div[4]',
                    )
                else:
                    pass

                try:
                    # clicking on "Social Status"
                    WebDriverWait(self.driver, timeout=5)
                    element.click()
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "selected"))
                    )
                except NoSuchElementException:  # if there is only social stats, then this exception would kick in
                    pass
                except StaleElementReferenceException:  # if there was no clickable element, this exception would kick in
                    pass

                date = datetime.datetime.now().strftime("%D")
                github_commits = self.driver.find_element(
                    By.XPATH,
                    '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div[2]',
                )
                github_stars = self.driver.find_element(
                    By.XPATH,
                    '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]',
                )
                github_forks = self.driver.find_element(
                    By.XPATH,
                    '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[3]/div[2]',
                )
                github_contributors = self.driver.find_element(
                    By.XPATH,
                    '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[4]/div[2]',
                )
                github_followers = self.driver.find_element(
                    By.XPATH,
                    '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[5]/div[2]',
                )
                twitter_followers = self.driver.find_element(
                    By.XPATH,
                    '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[6]/div[2]',
                )
                reddit_members = self.driver.find_element(
                    By.XPATH,
                    '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[7]/div[2]',
                )

                list = [
                    date,
                    crypto,
                    github_commits.text,
                    github_stars.text,
                    github_forks.text,
                    github_contributors.text,
                    github_followers.text,
                    twitter_followers.text,
                    reddit_members.text,
                ]

                list_new = [n.replace(",", "") for n in list]  # Drop commas from texts

                self.crypto_project_info.append(list_new)  # Append to target list

            # Catch errarnous sites
            except NoSuchElementException:
                logging.info(f"{crypto.title()}")

        return self.crypto_project_info

    def scrape_coindesk(self):
        """A method that returns the body of the table from coindesk.com"""

        for crypto in self.top_crypto:

            self.driver.get(f"https://www.coindesk.com/search?s={crypto}&df=24")
            date = datetime.datetime.now().strftime("%D")
            coin = crypto
            news = self.driver.find_element(
                By.XPATH,
                '//*[@id="queryly_advanced_container"]/div[5]/div[1]/div[1]/span/h6',
            )
            # The news string consists of multiple words.
            # The second string is the targeted number, that's why the string is splitted.
            self.news_list.append([date, coin, str(news.text.split(" ")[1])])
        # self.driver.quit()

        return self.news_list
