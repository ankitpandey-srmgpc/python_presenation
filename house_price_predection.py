import pandas as pd
import matplotlib as mat 


houseDataSet = pd.read_csv('C:/Users/AnkitPandey/Downloads/california_housing_test.csv')
#print(houseDataSet.head)
print(houseDataSet[houseDataSet.median_house_value>500000])

#location_stats = houseDataSet.groupby('location')['location'].count().sort_values(ascending = False)
#print(location_stats)