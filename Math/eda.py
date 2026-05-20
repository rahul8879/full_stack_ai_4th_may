import pandas as pd

data = pd.read_csv('churn_data.csv')
print(type(data))
print(data.head(2)) # select * from table limit 10
print(data.columns)
