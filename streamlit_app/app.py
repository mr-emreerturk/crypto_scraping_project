import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_functions import interactive_plot, add_logo, add_bar_chart, add_pie_chart

st.set_page_config(
    page_title="Crypto Price & Dev App",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": "# This is a header. This is an *extremely* cool app!",
    },
)
### --- READ CLEANED DATA
df = pd.read_csv(
    "https://raw.githubusercontent.com/mr-emreerturk/crypto_scraping_project/main/streamlit_app/cleaned_data.csv"
)

### --- CREATE SIDEBAR WITH HEADER AND SELECTBOX
with st.sidebar:
    st.title("Crypto Price & Dev App")
    df_copy = df["name"].drop_duplicates()
    ticker_list = [x.upper() for x in df_copy]
    crypto_selected_sidebar = st.selectbox(  # Create Selectbox
        "Select the crypto of your choice:",
        ticker_list,
    )
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
col1, col2 = st.columns([4, 1])
with col1:
    st.title(f"{crypto_selected_sidebar}-Dashboard")
    with st.expander("If no data is displayed"):
        st.markdown(
            """
            During the scraping process some values were retrieved as **NaN**.
            These could not be filtered as other valuable information would be lost.
            See the raw dataframe at the bottom of this page.
            Please excuse the inconvenience.
            """
        )

with col2:
    add_logo(crypto_selected_sidebar)

### --- CREATE FIRST VISUALIZATIONS
interactive_plot(df, crypto_selected_sidebar)

y_axis_val = st.select_slider("Select feature:", options=df.columns[3:])
col1, col2 = st.columns([1, 1])
with col1:
    add_bar_chart(df, y_axis_val)
with col2:
    add_pie_chart(df, y_axis_val)


### --- CREATE DATAFRAME TABS
st.header("Data from the web scrapers")
tab1, tab2 = st.tabs(["Avg. Data", "Raw Data"])
with tab1:
    ### --- LOAD RAW DATAFRAME
    st.dataframe(df)
with tab2:
    ### --- LOAD GROUPED DATAFRAME
    df_mean = df.groupby(by="name").mean()
    st.dataframe(df_mean)
