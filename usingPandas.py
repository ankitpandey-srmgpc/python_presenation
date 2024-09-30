import pandas as pd

dataSet = {
    "name":["Ankit","Shubham","Nikhli"],"Age":[25,24,26]
}

df = pd.DataFrame(dataSet)

filteredDf = df[df["Age"] >= 25]
print(filteredDf)