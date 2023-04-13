import pickle
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="HomePage",
    page_icon="💻",
)

st.write("# Welcome to Stock Trend Predictor Predictor 👨‍💻")

st.markdown(
    """
    Stock trend prediction is the process of using historical stock market data and statistical models to predict
    the future direction of stock prices. The goal of stock trend prediction is to help investors and traders make
    informed decisions about when to buy, hold, or sell stocks in order to maximize profits or minimize losses.
    There are a variety of techniques and models that can be used for stock trend prediction. These include time 
    series analysis, regression analysis, machine learning algorithms, and artificial neural networks. 
    These models use past stock prices and other relevant data, such as company financial statements and economic 
    indicators, to identify patterns and relationships that can be used to predict future stock prices.
    However, it's important to note that stock trend prediction is a challenging task and there is no guarantee of 
    accuracy. Stock prices are influenced by a multitude of factors, including company performance, industry trends, 
    economic conditions, and global events. It's difficult to account for all of these factors in a model and 
    accurately predict future prices. As such, stock trend prediction should be used as a tool for informing 
    investment decisions, but should not be relied on as the sole basis for making investment decisions.

    Note :- This prediction is purely based on various Data and Algorithms
"""
)

