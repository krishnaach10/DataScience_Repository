# Handling missing value through sklearn module using SimpleImputer
import pandas as pd
from sklearn.impute import SimpleImputer

dataset = pd.read_csv(r"C:\Users\MEGHARAJ1\Downloads\loan.csv")
print(dataset.select_dtypes(include= ["int64", "float64"]).columns)

si = SimpleImputer(strategy= "mean")
si.fit(dataset[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History']])
ar= si.transform(dataset[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History']])

newdataset = pd.DataFrame(ar, columns = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History'])

for i in dataset.select_dtypes(include = ["int64", "float64"]).columns:
    dataset[i] = newdataset[i]

print(dataset.isnull().sum())


