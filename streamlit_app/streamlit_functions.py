import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image
import requests
from io import BytesIO

ticker_list = pd.read_csv(
    "https://raw.githubusercontent.com/mr-emreerturk/crypto_scraping_project/main/streamlit_app/crypto_list.csv"
)  # Read Ticker List


def add_logo(crypto):
    crypto_selected_sidebar = str(crypto).lower()  # Convert to string
    url = f"https://raw.githubusercontent.com/mr-emreerturk/crypto_scraping_project/main/streamlit_app/crypto_logos/{crypto_selected_sidebar}.png"

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
        df_copy = df["name"].drop_duplicates()
        ticker_list = df_copy[df.name.isin([crypto_selected_sidebar]) != True]
        ticker_list_2 = [x.upper() for x in ticker_list]

        extra_crypto = st.multiselect(
            "Compare to another crypto:",
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

    line = px.line(  # lineplot using Plotly.Express
        df_plot,
        x=x_axis_val,
        y=y_axis_val,
        color="name",
        title=f"What are the changes in '{formatted_y_axis}' from Nov 1st to Nov7th?",
        template="plotly_white",
        markers=True,
        labels={
            "date": x_axis_val.title(),
            f"{y_axis_val}": formatted_y_axis,
            "name": "Cryptocurrency",
        },
    )
    line.update_layout(  # update background to white
        {
            "plot_bgcolor": "rgba(0, 0, 0, 0)",
            "paper_bgcolor": "rgba(0, 0, 0, 0)",
        }
    )
    line.update_traces(
        line=dict(width=3),
        marker={"size": 9},
        marker_line={"width": 2, "color": "#FFFFFF"},
    )  # update line_width to 3 and set markersize

    st.plotly_chart(line, use_container_width=True)  # Plot on streamlit


def add_bar_chart(df, y_axis_val):
    x_axis_val = "name"
    if "_" in y_axis_val:  # Replace "_" with whitespace " "
        mask = y_axis_val[:].replace("_", " ")
        formatted_y_axis = mask.title()
    else:  # Format to Title
        formatted_y_axis = y_axis_val.title()
    fig = px.bar(
        df,
        x=x_axis_val,
        y=y_axis_val,
        template="plotly_white",
        title=f"What are the absolute proportions?",
        labels={
            "name": x_axis_val.title(),
            f"{y_axis_val}": formatted_y_axis,
        },
    )
    fig.update_layout(  # update background to white
        {
            "plot_bgcolor": "rgba(0, 0, 0, 0)",
            "paper_bgcolor": "rgba(0, 0, 0, 0)",
        }
    )
    fig.update_traces(
        marker=dict(line=dict(color="#FFFFFF", width=0)),
    )
    st.plotly_chart(fig, use_container_width=True)


def add_pie_chart(df, pie_values):
    pie_names = "name"
    fig = px.pie(
        df,
        values=pie_values,
        names=pie_names,
        template="plotly_white",
        title=f"What are the relative proportions?",
    )
    fig.update_layout(  # update background to white
        {
            "plot_bgcolor": "rgba(0, 0, 0, 0)",
            "paper_bgcolor": "rgba(0, 0, 0, 0)",
        }
    )
    fig.update_traces(
        hoverinfo="label+percent",
        textinfo="value",
        marker=dict(line=dict(color="#FFFFFF", width=2)),
    )
    st.plotly_chart(fig, use_container_width=True)
