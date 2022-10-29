# Import modules
import numpy as np
import h5py
import cronitor
import os.path

# Import scraper classes
from scraper_coindesk import CoinDeskScraper
from scraper_yahoo import YahooScraper
from scraper_coinmarket import CoinMarketCapScraper

# Set up cronjob using cronitor
from credentials import cronitor_api  # Import credentials

cronitor.api_key = cronitor_api  # Setting of API key object secretly
cronitor.Monitor.put(
    key="web_scraping",  # Name of cronjob
    type="job",  # Define the cron job
    schedule="0 9 * * *",  # Scrape website everyday at 9 am
)

# define function for main.py and add decorator
@cronitor.job("web_scraping")
def scrape_save():

    # Import scraper objects from scraper classes
    yahoo = YahooScraper()
    yahoo_data = yahoo.scrape_yahoo()

    cmc = CoinMarketCapScraper()
    cmc_data = cmc.scrape_coinmarketcap()

    coindesk = CoinDeskScraper()
    coindesk_data = coindesk.scrape_coindesk()

    # Create flag to check if H5 file alreadye exists
    file_exists = os.path.exists(
        "/Users/emre/Documents/GitHub/crypto_scraping_project/data.h5"
    )

    # Condition whether file already exists or not
    if file_exists == True:  # If file does exists -> append
        with h5py.File(
            "/Users/emre/Documents/GitHub/crypto_scraping_project/data.h5", "a"
        ) as hdf:
            yahoo_mask = np.array(yahoo_data)  # Transform data to array
            # Resize h5 file
            hdf["yahoo_prices"].resize(
                (hdf["yahoo_prices"].shape[0] + yahoo_mask.shape[0]), axis=0
            )
            hdf["yahoo_prices"][yahoo_mask.shape[0] :] = yahoo_mask  # append data

            cmc_mask = np.array(cmc_data)
            hdf["dev_data"].resize(
                (hdf["dev_data"].shape[0] + cmc_mask.shape[0]), axis=0
            )
            hdf["dev_data"][cmc_mask.shape[0] :] = cmc_mask

            coindesk_mask = np.array(coindesk_data)
            hdf["news_data"].resize(
                (hdf["news_data"].shape[0] + coindesk_mask.shape[0]), axis=0
            )
            hdf["news_data"][coindesk_mask.shape[0] :] = coindesk_mask

    elif file_exists == False:  # If file does NOT exists -> create file
        with h5py.File(
            "/Users/emre/Documents/GitHub/crypto_scraping_project/data.h5", "w"
        ) as hdf:
            yahoo_dataset_mask = hdf.create_dataset(
                "yahoo_prices",
                data=yahoo_data,
                maxshape=(
                    None,
                    10,
                ),
                chunks=True,
            )
            yahoo_dataset_mask.attrs["USER"] = "Emre Ertürk"

            cmc_dataset_mask = hdf.create_dataset(
                "dev_data",
                data=cmc_data,
                maxshape=(
                    None,
                    10,
                ),
                chunks=True,
            )
            cmc_dataset_mask.attrs["USER"] = "Emre Ertürk"

            coindesk_dataset_mask = hdf.create_dataset(
                "news_data",
                data=coindesk_data,
                maxshape=(
                    None,
                    10,
                ),
                chunks=True,
            )
            coindesk_dataset_mask.attrs["USER"] = "Emre Ertürk"


# Execute function
scrape_save()
