#%%
from coindesk_scraper import CoinDeskScraper
from yahoo_scraper import YahooScraper
from coinmarket_scraper import CoinMarketCapScraper
import h5py

#%%
coindesk = CoinDeskScraper()
coindesk_data = coindesk.scrape_coindesk()
#%%
yahoo = YahooScraper()
yahoo_data = yahoo.scrape_yahoo()
#%%
cmc = CoinMarketCapScraper()
cmc_data = cmc.scrape_coinmarketcap()
#%%
yahoo_data
# %%
try:
    with h5py.File(
        "/Users/emre/Documents/GitHub/crypto_scraping_project/data.h5", "a"
    ) as hdf:
        yahoo_mask = yahoo_data.copy()
        hdf["crypto_prices_yahoo"].resize(
            (hdf["crypto_prices_yahoo"].shape[0] + yahoo_mask.shape[0]), axis=0
        )
        hdf["crypto_prices_yahoo"][yahoo_mask[0] :] = yahoo_mask
except:
    with h5py.File(
        "/Users/emre/Documents/GitHub/crypto_scraping_project/data.h5", "a"
    ) as hdf:
        yahoo_mask = hdf.create_dataset(
            "crypto_prices_yahoo",  # name of dataset
            data=yahoo_data,  # name of data
            maxshape=(
                None,
                None,
            ),  # shape of dataset set up for resizing and appending later
            chunks=True,  # Set up access pattern
        )
        yahoo_mask.attrs["USER"] = "Emre Erturk"  # Add metadata


# try:
#     with h5py.File(
#         "/Users/emre/Documents/GitHub/crypto_scraping_project/data.h5", "a"
#     ) as hdf:
#         yahoo_mask = yahoo_data.copy()  # Convert list of tuples to Numpy array
#         # resize target dataset and add shape of new data to it
#         hdf["crypto_prices_yahoo"].resize(
#             (hdf["crypto_prices_yahoo"].shape[0] + yahoo_mask.shape[0]), axis=0
#         )
#         # fill newly created rows/columns with new data
#         hdf["crypto_prices_yahoo"][yahoo_mask.shape[0] :] = yahoo_mask

#     with h5py.File(
#         "/Users/emre/Documents/GitHub/crypto_scraping_project/data.h5", "a"
#     ) as hdf:
#         coindesk_mask = coindesk_data.copy()  # Convert list of tuples to Numpy array
#         # resize target dataset and add shape of new data to it
#         hdf["news_development_data"]["development_data"].resize(
#             (hdf["news_development_data"]["development_data"].shape[0] + coindesk_mask.shape[0]), axis=0
#         )
#         # fill newly created rows/columns with new data
#         hdf["news_development_data"]["development_data"][coindesk_mask.shape[0] :] = coindesk_mask

#     with h5py.File(
#         "/Users/emre/Documents/GitHub/crypto_scraping_project/data.h5", "a"
#     ) as hdf:
#         cmc_mask = yahoo_data.copy()  # Convert list of tuples to Numpy array
#         # resize target dataset and add shape of new data to it
#         hdf["news_development_data"]["news_data"].resize(
#             (hdf["news_development_data"]["news_data"].shape[0] + cmc_mask.shape[0]), axis=0
#         )
#         # fill newly created rows/columns with new data
#         hdf["news_development_data"]["news_data"][cmc_mask.shape[0] :] = cmc_mask

# except (KeyError):
#     with h5py.File(
#         "/Users/emre/Documents/GitHub/crypto_scraping_project/data.h5", "w"
#     ) as hdf:
#         # Create dataset for yahoo data
#         yahoo_mask = hdf.create_dataset(
#             "crypto_prices_yahoo",  # name of dataset
#             data=yahoo_data,  # name of data
#             maxshape=(
#                 None,
#                 None,
#             ),  # shape of dataset set up for resizing and appending later
#             chunks=True,  # Set up access pattern
#         )
#         yahoo_mask.attrs["USER"] = "Emre Erturk"  # Add metadata

#         news_dev_group = hdf.create_group("news_development_data")
#         cmc_mask = news_dev_group.create_dataset(
#             "development_data",  # name of dataset
#             data=cmc_data,  # name of data
#             maxshape=(
#                 None,
#                 None,
#             ),  # shape of dataset set up for resizing and appending later
#             chunks=True,  # Set up access pattern
#         )
#         cmc_mask.attrs["USER"] = "Emre Erturk"  # Add metadata  # Name of Group

#         coindesk_maks = news_dev_group.create_dataset(
#             "news_data",  # name of dataset
#             data=coindesk_data,  # name of data
#             maxshape=(
#                 None,
#                 None,
#             ),  # shape of dataset set up for resizing and appending later
#             chunks=True,  # Set up access pattern
#         )
#         coindesk_maks.attrs["USER"] = "Emre Erturk"  # Add metadata  # Name of Group
# # %%

# %%
