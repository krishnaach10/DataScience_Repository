import pandas as pd

dataset = pd.read_csv(r"C:\Users\MEGHARAJ1\Downloads\loan.csv")
print(dataset.isnull().sum())

for i in dataset.select_dtypes(include = "object").columns:
    dataset[i] = dataset[i].fillna(dataset[i].mode()[0])

for i in dataset.select_dtypes(include = ["int64" , "float64"]).columns:
    dataset[i] = dataset[i].fillna(dataset[i].mean())

print(dataset.isnull().sum())