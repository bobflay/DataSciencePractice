import pandas as pd

#load the dataset
df = pd.read_csv('dataset.csv')

#display the first 5 rows of the dataset
# print(df.head())

#display the last 5 rows of the dataset 
# print(df.tail())

#return information about the dataframe
# print(df.info())

#print the summary statics of the dataframe
# print(df.describe())

#check for missing values
# print(df.isnull().sum())



# numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
# categorical_cols = df.select_dtypes(include=['object']).columns
# print("Numerical columns: ", numerical_cols)
# print("Categorical columns: ", categorical_cols)

# #drop the missing values
# df = df.dropna(axis=0) #axis=0 means drop rows with missing values
# df = df.dropna(axis=1) #axis=1 means drop columns with missing values