# dq.py
import pandas as pd

def isValidValue(fileInput,fileDomain,domainName,errorFile):
  df1 = pd.read_csv(fileInput)
  df2 = pd.read_csv(fileDomain)
  isCityValid = df1.city.isin(df2.city).astype(str)
  isCityValid.to_csv(errorFile)
