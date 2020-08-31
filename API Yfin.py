import pandas as pd
import numpy as np
import yfinance as yf



#Df = yf.Ticker("^FCHI").history(period="ytd")

msft = yf.Ticker("msft")

# get stock info
msft.info


# get historical market data
hist = msft.history(period="max")
df = hist.index

# show actions (dividends, splits)
msft.actions

# show dividends
msft.dividends

# show splits
msft.splits

# show financials
msft.financials
msft.quarterly_financials

# show balance heet
msft.balance_sheet
msft.quarterly_balance_sheet

# show cashflow
msft.cashflow
msft.quarterly_cashflow

# show earnings
msft.earnings
msft.quarterly_earnings

# show sustainability
msft.sustainability

# show analysts recommendations
msft.recommendations

# show next event (earnings, etc)
msft.calendar

