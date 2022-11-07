import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image
import requests
from io import BytesIO

ticker_list = pd.read_csv(
    "https://raw.githubusercontent.com/mr-emreerturk/crypto_scraping_project/main/streamlit_app/crypto_list.txt"
)  # Read Ticker List


def add_logo(crypto):
    crypto_selected_sidebar = str(crypto).lower()  # Convert to string
    url = f"https://raw.githubusercontent.com/mr-emreerturk/crypto_scraping_project/main/streamlit_app/crypto_logos/{crypto_selected_sidebar}.jpeg"

    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    st.image(img)


def interactive_plot(df, crypto):
    """A method which creates an interactive plotly.express plot in the streamlit app.

    Args:
        df (dataframe): dataframe object read in app.py
        crypto (string): The cryptocurrency the user selects in the Selectbox
    """
    x_axis_val = "date"  # Set x axis to "date"
    crypto_selected_sidebar = str(crypto).lower()  # Convert to string

    col1, col2 = st.columns(
        [3, 1]
    )  # Setting two columns for selectbox and multiselect --> Ratio 3:1

    with col1:  # Column for multiselect for other crypto
        global ticker_list  # Import global ticker_list
        ticker_list_2 = ticker_list.iloc[:, 0].values.tolist()
        ticker_list_2.remove(f"{crypto}")

        extra_crypto = st.multiselect(
            "Compare to aother crypto:",
            ticker_list_2,
        )
        mask_list = [x.lower() for x in extra_crypto]

    with col2:  # Column for y-axis selectbox
        y_axis_val = st.selectbox(  # Set selectable columns to numeric only
            "Select the Y-axis", options=df.columns[2:]
        )
        # Create condition where column names get seperated at "_" and written in Title format for labeling of plot
        if "_" in y_axis_val:  # Replace "_" with whitespace " "
            mask = y_axis_val[:].replace("_", " ")
            formatted_y_axis = mask.title()
        else:  # Format to Title
            formatted_y_axis = y_axis_val.title()

    mask_list.append(crypto_selected_sidebar)  # Append Seelcted Crypto
    df_plot = df[df.name.isin(mask_list) == True]  # Filter for selected crytocurrency

    fig = px.line(  # lineplot using Plotly.Express
        df_plot,
        x=x_axis_val,
        y=y_axis_val,
        color="name",
        template="plotly_white",
        labels={
            "date": x_axis_val.title(),
            f"{y_axis_val}": formatted_y_axis,
            "name": "Cryptocurrency",
        },
    )
    fig.update_layout(  # update background to white
        {
            "plot_bgcolor": "rgba(0, 0, 0, 0)",
            "paper_bgcolor": "rgba(0, 0, 0, 0)",
        }
    )
    fig.update_traces(line=dict(width=3))  # update line_width to 3

    st.plotly_chart(fig, use_container_width=True)  # Plot on streamlit
