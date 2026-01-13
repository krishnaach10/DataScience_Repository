si = SimpleImputer(strategy= "mean")
# si.fit(dataset[[]])
# newdataset = si.transform(dataset[[]])

# for i in dataset.select_dtypes(include = ["int64", "float64"]).columns:
#     dataset[i] = newdataset[i]

# print(dataset.isnull().sum())