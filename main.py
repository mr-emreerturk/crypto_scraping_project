# Import modules
import cronitor
import os.path
from operations_h5 import Saving_to_h5
from scrapers import Scrapers

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

    scraper = Scrapers()  # Assign scraper object from scraper class

    yahoo_data = scraper.scrape_yahoo()  # Call Yahoo scraper method
    cmc_data = scraper.scrape_coinmarketcap()  # Call Coinmarketcap scraper method
    coindesk_data = scraper.scrape_coindesk()  # Call Coindesk scraper method

    # Assign operations object to operation class
    operations = Saving_to_h5()

    # Create flag to check if H5 file alreadye exists
    file_exists = os.path.exists("data.h5")

    # Condition whether file already exists or not
    if file_exists == True:  # If file does exists -> append
        operations.append_to_h5(yahoo_data, cmc_data, coindesk_data)

    elif file_exists == False:  # If file does NOT exists -> create file
        operations.create_h5(yahoo_data, cmc_data, coindesk_data)

    else:
        raise Exception("The file exist flag is ambigous")


# Execute function
scrape_save()
