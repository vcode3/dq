# dq.py
import pandas as pd

df1 = pd.read_csv('$path/dq1.csv')

df2 = pd.read_csv('$path/domain_city.csv')

isCityValid = df1.city.isin(df2.city).astype(str) 
isCityValid.to_csv('$path/domain_error.csv')
