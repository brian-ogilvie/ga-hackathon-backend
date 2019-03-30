import csv
import pandas as pd 

df = pd.read_csv("updated_data.csv")

print(df.head(0))

for i in df.head(0):
    i = i.lower()
    i = i.split(' ')
    i = '_'.join(i)
    print(
        i + ''' = models.FloatField'''
    )

