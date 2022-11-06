import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_functions import interactive_plot

### --- READ CLEANED DATA
df = pd.read_csv(
    "https://raw.githubusercontent.com/mr-emreerturk/crypto_scraping_project/main/streamlit_app/cleaned_data.csv"
)

### --- CREATE SIDEBAR WITH HEADER AND SELECTBOX
with st.sidebar:
    st.header("Crypto Price & Dev App")
    ticker_list = pd.read_csv(
        "https://raw.githubusercontent.com/mr-emreerturk/crypto_scraping_project/main/streamlit_app/crypto_list.txt"
    )  # Read Ticker List
    crypto_selected = st.selectbox(
        "Select the crypto of your choice:", ticker_list
    )  # Create Selectbox
    st.markdown(
        """
    This application shows the result of a web-scraping project where different data was 
    retrieved to describe cryptocurrencies. For more information on the scraping process please 
    visit this repo 👉 [click here](https://github.com/mr-emreerturk/crypto_scraping_project) \n
    **Credits**
    - App built by [Emre Ertürk](https://www.linkedin.com/in/mr-emre-erturk/)
    - Built in `Python` using `streamlit`,`pandas`, `plotly.express`, and `selenium`
    """
    )
    st.write("---")
    with st.expander("Additional Information"):  # Add additional information
        st.markdown(
            """
        The data was retrieved from **November 1st, 2022 to November 7th 2022**. As part of the scraping project, this dashboard 
        is a sheer visualization fo said data. In a normal environment a suitable API would have been chosen.
        """
        )

### --- DISPLAY LINECHART OF CHOSEN CRYPTO
# TODO: Add crypto logo next to header
st.header(f"{crypto_selected}-Dashboard")
with st.expander("If no data is displayed"):
    st.markdown(
        """
        During the scraping process some values were retrieved as **NaN**.
        These could not be filtered as other valuable information would be lost. Please excuse the inconvenience.
        """
    )

interactive_plot(df, crypto_selected)

### --- CREATE DATAFRAME TABS
tab1, tab2 = st.tabs(["Avg. Data", "Raw Data"])

with tab1:
    ### --- LOAD GROUPED DATAFRAME
    df_mean = df.groupby(by="name").mean()
    st.dataframe(df_mean)
with tab2:
    ### --- LOAD RAW DATAFRAME
    st.dataframe(df)

st.write("---")
