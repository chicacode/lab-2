import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Lab 6
# Geraldine Hernandez A


# 1. Basic DataFrame Operations:

# 1.1 Load the dataset into a Pandas DataFrame.
data = pd.read_csv('student_grades.csv')
print(data)

# 1.2 Display the first 5 rows of the DataFrame.
print(data.head())

# 1.3 Display the summary statistics of the DataFrame.
print(data.describe())

# 1.4 Display the column names of the DataFrame.
print(data.columns)

# 1.5 Count the number of male and female students.
print('Male and Females count')
print(data['Gender'].value_counts())

# 2. Filtering and Subsetting:

# 2.1 Filter the DataFrame to show only students who are 16 years old.
print('Student 16 years old')
print(data[data['Age'] == 16])

# 2.2 Filter the DataFrame to show only female students.
print('Female Students')
print(data[data['Gender'] == 'F'])

# 2.3 Filter the DataFrame to show students with Math scores above 85.
print('Math scores above 85')
print(data[data['Math'] > 85])

# 2.4 Select the Name and Total_Grades columns for all students.
print('Name and Total_Grades')
data['Total_Grades'] = data[['Math', 'Science', 'English', 'History', 'Physical_Education']].sum(axis=1)
print(data[['Name', 'Total_Grades']])

# 2.5 Calculate the average Math score for male and female students.
print('Average Math score for male and female students')
average_math_score_by_gender = data.groupby('Gender')['Math'].mean()
print(average_math_score_by_gender)

# 3. Aggregation and Grouping:

# 3.1 Calculate the average grade for each subject.
print('Average grade for each subject')
print(data.mean(numeric_only=True))

# 3.2 Calculate the average grade for each gender.
print('Average grade for each gender')
print(data.groupby('Gender').mean(numeric_only=True))

# 3.3 Calculate the total grades for each student (sum of all subjects).
# 3.4 Find the student with the highest total grade.
print('Total grades for each student (sum of all subjects)')
print(data[['Name', 'Total_Grades']].sort_values(by='Total_Grades', ascending=False).head(1))

# 3.5 Calculate the average age of the students.
print('Calculate the average age of the students')
print(data['Age'].mean())

# 4. Data Visualization:

# 4.1 Create a bar plot showing the average grade for each subject.
# 4.2 Create a bar plot showing the total grades of each student.
# 4.3 Create a histogram showing the distribution of Math scores.
# 4.4 Create a box plot to show the distribution of grades for each subject.
# 4.5 Create a scatter plot showing the relationship between Math and Science scores.