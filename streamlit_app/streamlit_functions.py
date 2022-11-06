import pandas as pd
import plotly.express as px
import streamlit as st

c


def interactive_plot(df, crypto):
    crypto_formatted = str(crypto).lower()
    x_axis_val = "date"
    y_axis_val = st.selectbox("Select the Y-axis", options=df.columns[2:])
    df_plot = df[df.name.isin([crypto_formatted]) == True]

    plot = px.line(df_plot, x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot, use_container_width=True)
