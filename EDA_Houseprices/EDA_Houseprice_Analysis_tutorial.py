import pandas as pd
from pandas_profiling import ProfileReport
df = pd.read_csv('melb_data.csv')
print(df.head())
profile = ProfileReport(df,title= 'EDA Houseprices')
profile.to_file('EDA_Houseprice_Analysis.html')