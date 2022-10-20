from coindesk_scraper import CoinDeskScraper
from yahoo_scraper import YahooScraper
from coinmarket_scraper import CoinMarketCapScraper
import h5py
import numpy as np

yahoo = YahooScraper()
yahoo_data = yahoo.scrape_yahoo()

cmc = CoinMarketCapScraper()
cmc_data = cmc.scrape_coinmarketcap()

coindesk = CoinDeskScraper()
coindesk_data = coindesk.scrape_coindesk()

try:
    with h5py.File(
        "/Users/emre/Documents/GitHub/crypto_scraping_project/ZZZ.h5", "a"
    ) as hdf:
        yahoo_mask = np.array(yahoo.cryptocurrencies_list)
        hdf["yahoo_prices"].resize(
            (hdf["yahoo_prices"].shape[0] + yahoo_mask.shape[0]), axis=0
        )
        hdf["yahoo_prices"][yahoo_mask.shape[0] :] = yahoo_mask

        cmc_mask = np.array(cmc.crypto_project_info)
        hdf["dev_data"].resize((hdf["dev_data"].shape[0] + cmc_mask.shape[0]), axis=0)
        hdf["dev_data"][cmc_mask.shape[0] :] = cmc_mask

        coindesk_mask = np.array(coindesk.news_list)
        hdf["news_data"].resize(
            (hdf["news_data"].shape[0] + coindesk_mask.shape[0]), axis=0
        )
        hdf["news_data"][coindesk_mask.shape[0] :] = coindesk_mask

except:
    with h5py.File(
        "/Users/emre/Documents/GitHub/crypto_scraping_project/ZZZ.h5", "w"
    ) as hdf:
        yahoo_dataset_mask = hdf.create_dataset(
            "yahoo_prices",
            data=yahoo.cryptocurrencies_list,
            maxshape=(
                None,
                None,
            ),
            chunks=True,
        )
        yahoo_dataset_mask.attrs["USER"] = "Emre Ertürk"

        cmc_dataset_mask = hdf.create_dataset(
            "dev_data",
            data=cmc.crypto_project_info,
            maxshape=(
                None,
                None,
            ),
            chunks=True,
        )
        cmc_dataset_mask.attrs["USER"] = "Emre Ertürk"

        coindesk_dataset_mask = hdf.create_dataset(
            "news_data",
            data=coindesk_data,
            maxshape=(
                None,
                None,
            ),
            chunks=True,
        )
        coindesk_dataset_mask.attrs["USER"] = "Emre Ertürk"
