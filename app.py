import pandas as pd
import yfinance as yf

#Obter os dados de cotação em bolsa
df= yf.download('TSLA', start='2025-12-01', end='2025-12-31')

print(df)