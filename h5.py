import h5py 

# Context Manager to create HDF5 file for yahoo

with h5py.File('/Users/emre/Documents/GitHub/crypto_scraping_project/hdf5_data.h5', 'w') as hdf:
    yahoo_group = hdf.create_group('crypto_prices') # Name of Group
    yahoo_prices = yahoo_group.create_dataset(
        'yahoo_prices', # name of dataset
        data=cryptocurrencies_list, # name of data
        maxshape=(None,len(yahoo_cols)), # shape of dataset set up for resizing and appending later
        chunks=True, # Set up access pattern
    )
    yahoo_prices.attrs['USER'] = 'Emre Erturk' # Add metadata


# Append to existing dataset

with h5py.File('/Users/emre/Documents/GitHub/crypto_scraping_project/hdf5_data.h5', 'a') as hdf:
    mask_lsit = np.array(cryptocurrencies_list) # Convert list of tuples to Numpy array
    # resize target dataset and add shape of new data to it
    hdf['crypto_prices']['yahoo_prices'].resize((hdf['crypto_prices']['yahoo_prices'].shape[0] + mask_lsit.shape[0]), axis=0)
    # fill newly created rows/columns with new data
    hdf['crypto_prices']['yahoo_prices'][mask_lsit.shape[0]:] = mask_lsit