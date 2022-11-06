import h5py
import numpy as np


class Saving_to_h5:
    def __init__(self) -> None:
        pass

    def create_h5(self, yahoo_data, cmc_data, coindesk_data):
        """This method creates a new h5 dataset

        Args:
            yahoo_data (list): add scraped data from finance.yahoo.com
            cmc_data (list): add scraped data from coinmarketcap.com
            coindesk_data (list): add scraped data from coindesk.com
        """

        with h5py.File("data.h5", "w") as hdf:
            yahoo_dataset_mask = hdf.create_dataset(
                "yahoo_prices",
                data=yahoo_data,
                shape=(
                    50,
                    10,
                ),
                maxshape=(
                    None,
                    1000,
                ),
                chunks=True,
            )
            yahoo_dataset_mask.attrs["USER"] = "Emre Ertürk"

            cmc_dataset_mask = hdf.create_dataset(
                "dev_data",
                data=cmc_data,
                shape=(
                    50,
                    10,
                ),
                maxshape=(
                    None,
                    1000,
                ),
                chunks=True,
            )
            cmc_dataset_mask.attrs["USER"] = "Emre Ertürk"

            coindesk_dataset_mask = hdf.create_dataset(
                "news_data",
                data=coindesk_data,
                shape=(
                    50,
                    10,
                ),
                maxshape=(
                    None,
                    1000,
                ),
                chunks=True,
            )
            coindesk_dataset_mask.attrs["USER"] = "Emre Ertürk"

    def append_to_h5(self, yahoo_data, cmc_data, coindesk_data):
        """This method appends data to an existing h5 dataset

        Args:
            yahoo_data (list): add scraped data from finance.yahoo.com
            cmc_data (list): add scraped data from coinmarketcap.com
            coindesk_data (list): add scraped data from coindesk.com
        """
        # Condition whether file already exists or not
        with h5py.File("data.h5", "a") as hdf:
            yahoo_mask = np.array(yahoo_data)  # Transform data to array
            # Resize h5 filetest
            hdf["yahoo_prices"].resize(
                (hdf["yahoo_prices"].shape[0] + yahoo_mask.shape[0]), axis=0
            )
            hdf["yahoo_prices"][-yahoo_mask.shape[0] :] = yahoo_mask  # append data

            cmc_mask = np.array(cmc_data)
            hdf["dev_data"].resize(
                (hdf["dev_data"].shape[0] + cmc_mask.shape[0]), axis=0
            )
            hdf["dev_data"][-cmc_mask.shape[0] :] = cmc_mask

            coindesk_mask = np.array(coindesk_data)
            hdf["news_data"].resize(
                (hdf["news_data"].shape[0] + coindesk_mask.shape[0]), axis=0
            )
            hdf["news_data"][-coindesk_mask.shape[0] :] = coindesk_mask
