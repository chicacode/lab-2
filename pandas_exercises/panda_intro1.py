import pandas as pd

from lab4_data_structures_dictionaries_tuples import employees

# reading from csv file
df = pd.read_csv('employee_data.csv')
print(df)
print(df[['Name', 'Salary']])
print(df.iloc[[1,2,3], [0,1,2]])

employees = {
    'Name': ['Derrick', 'James', 'Justin'],
    'City': ['Vancouver', 'Burnaby', 'Surrey']
}

# reading from dictionary
df1 = pd.DataFrame(employees)
print(df1)