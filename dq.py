# dq.py


df1 = pd.read_csv('$path/dq1.csv')

saved_column = df.city 

print (saved_column)

df2 = pd.read_csv('$path/domain_city.csv')
domainCity = df1.city #you can also use df['column_name']
print (domainCity)

isCityValid = df1.city.isin(df2.city).astype(str) 
isCityValid.to_csv('$path/domain_error.csv')
