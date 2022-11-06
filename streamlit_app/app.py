import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime

# App title
st.markdown(
    """
# Crypto Price and Dev App
Shown are the stock price data for query companies!
**Credits**
- App built by [Emre Ertürk](https://www.linkedin.com/in/mr-emre-erturk/)
- Built in `Python` using `streamlit`,`yfinance`, `cufflinks`, `pandas` and `datetime`
"""
)
st.write("---")

# Sidebar
st.sidebar.subheader("Query parameters")
start_date = st.sidebar.date_input("Start date", datetime.date(2022, 11, 1))
end_date = st.sidebar.date_input("End date", datetime.date(2022, 11, 7))

# Retrieving tickers data
ticker_list = pd.read_csv(
    "https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt"
)
tickerSymbol = st.sidebar.selectbox("Stock ticker", ticker_list)  # Select ticker symbol
tickerData = yf.Ticker(tickerSymbol)  # Get ticker data
tickerDf = tickerData.history(
    period="1d", start=start_date, end=end_date
)  # get the historical prices for this ticker
