import pandas as pd
import plotly.express as px
import streamlit as st

# TODO: add multiple crypto for comparison
def interactive_plot(df, crypto):
    """A method which creates an interactive plotly.express plot in the streamlit app.

    Args:
        df (dataframe): dataframe object read in app.py
        crypto (string): The cryptocurrency the user selects in the Selectbox
    """
    crypto_formatted = str(crypto).lower()  # Convert to string
    x_axis_val = "date"  # Set x axis to "date"
    y_axis_val = st.selectbox(
        "Select the Y-axis", options=df.columns[2:]
    )  # Set selectable columns to numeric only
    df_plot = df[
        df.name.isin([crypto_formatted]) == True
    ]  # Filter for selected crytocurrency

    plot = px.line(df_plot, x=x_axis_val, y=y_axis_val)  # Plot using Plotly.Express
    st.plotly_chart(plot, use_container_width=True)  # Plot on streamlit
