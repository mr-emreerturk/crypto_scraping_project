%%
from coindesk_scraper import CoinDeskScraper
from yahoo_scraper import YahooScraper
from coinmarket_scraper import CoinMarketCapScraper

#%%
coindesk = CoinDeskScraper()
coindesk.scrape_coindesk()
#%%
yahoo = YahooScraper()
yahoo.scrape_yahoo()
# %%
from coinmarket_scraper import CoinMarketCapScraper

cmc = CoinMarketCapScraper()
cmc.scrape_coinmarketcap()

coindesk.news_list
# %%
