import pandas as pd

#load the dataset
# df = pd.read_csv('dataset.csv')

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





data = {
    'Name': ['John', 'Paul', 'Ringo', 'George','Paul','John'],
    'Age': [22, 21, 23, 22,21,22],
    'City': ['New York', 'London', 'Liverpool', 'Liverpool','London','New York'],
}

df = pd.DataFrame(data)
# print("Original DataFrame")
# print(df)

#1. Detect Duplicates
duplicates = df.duplicated()
print("Duplicate rows")
print(df[duplicates])

#2. Count Duplicates
duplicates = duplicates.sum()
print("Number of duplicate rows: ", duplicates)


df_no_duplicates = df.drop_duplicates()
print("DataFrame without duplicates")
print(df_no_duplicates)

df_no_duplicates_specific_cols = df.drop_duplicates(subset=['Name'])
print("DataFrame without duplicates based on Name")
print(df_no_duplicates_specific_cols)


df_keep_first = df.drop_duplicates(keep='first')
print("DataFrame keeping first duplicate")
print(df_keep_first)

df_keep_last = df.drop_duplicates(keep='last')
print("DataFrame keeping last duplicate")
print(df_keep_last)
