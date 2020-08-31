import pandas as pd
import numpy as np
import yfinance as yf



#Create a dictionary with all tickers
    #skip rows = 1 to remove header
    #index_col -> select tickers
    #.T is numpy transpose
tickers_dict = pd.read_excel(Universe + ".xlsx", index_col ="ticker" ,skiprows=0).T.to_dict()

