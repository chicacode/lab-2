import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Lab 6
# Geraldine Hernandez A


# 1. Basic DataFrame Operations:

# 1.1 Load the dataset into a Pandas DataFrame.
data = pd.read_csv('student_grades.csv')
print('Students')
print(data)

# 1.2 Display the first 5 rows of the DataFrame.
print('first 5 rows of the DataFrame')
print(data.head())

# 1.3 Display the summary statistics of the DataFrame.
print('Statistics of the dataframe')
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
subject_means = data[['Math', 'Science', 'English', 'History', 'Physical_Education']].mean()
sns.barplot(x=subject_means.index, y=subject_means.values)
plt.title("Average Grade per Subject")
plt.show()

# 4.2 Create a bar plot showing the total grades of each student.
sns.barplot(x=data['Name'], y=data['Total_Grades'])
plt.xticks(rotation=45)
plt.title("Total Grades per Student")
plt.show()

# 4.3 Create a histogram showing the distribution of Math scores.
sns.histplot(data['Math'], bins=10, kde=True)
plt.title("Distribution of Math Scores")
plt.show()

# 4.4 Create a box plot to show the distribution of grades for each subject.

sns.boxplot(data=data.iloc[:, 3:-1])
plt.title("Grade Distribution for Each Subject")
plt.show()

# 4.5 Create a scatter plot showing the relationship between Math and Science scores.
sns.scatterplot(x=data['Math'], y=data['Science'])
plt.title("Math vs Science Scores")
plt.show()

# Questions for Dataset 2:

# 1.1 Load the dataset into a Pandas DataFrame.
employees = pd.read_csv('employee_data.csv')
print('Employees')
print(employees)

# 1.2 Display the first 5 rows of the DataFrame.
print('first 5 rows of the DataFrame')
print(employees.head())

# 1.3 Display the summary statistics of the DataFrame.
print('summary statistics of the DataFrame')
print(employees.describe())

department_stats = employees.groupby('Department')[['Salary', 'YearsAtCompany']].mean()
print(department_stats)
# 1.4 Display the column names of the DataFrame.
print('Column names')
print(employees.columns)

# 1.5 Count the number of employees in each department.
print('Number of employees')
print(employees['Department'].value_counts())

# 2. Filtering and Subsetting:
# 2.1 Filter the DataFrame to show only employees who are older than 40.
print('employees who are older than 40')
print(employees[employees['Age'] > 40])

# 2.2 Filter the DataFrame to show only employees in the 'IT' department.
print('employees in the IT department')
print(employees[employees['Department'] == 'IT'])

# 2.3 Filter the DataFrame to show employees with a salary above 75000.
print('employees with a salary above 75000')
print(employees[employees['Salary'] > 75000])

# 2.4 Select the Name and Salary columns for all employees.
print('Name and Salary columns for all employees')
print(employees[['Name', 'Salary']])

# 2.5 Calculate the average salary for each department.
print(employees.groupby('Department')['Salary'].mean())

# 3. Aggregation and Grouping:
# 3.1 Calculate the average salary of all employees.
print('Average salary of all employees')
print(employees['Salary'].mean())

# 3.2 Calculate the average age of employees in each department.

print('Average age of all employees')
print(employees['Age'].mean())

# 3.3 Calculate the total years worked at the company for all employees.
print('Total years at the company')
print(employees['YearsAtCompany'].sum())

# 3.4 Find the employee with the highest salary.
print('Employee with the highest salary')
print(employees.sort_values(by='Salary', ascending=False).head(1))
# 3.5 Calculate the average years at the company for each department.
print('Average years at the company for each department')
print(employees.groupby('Department')['YearsAtCompany'].mean())

# 4. Data Visualization:

# 4.1 Create a bar plot showing the average salary for each department.
department_avg_salary = employees.groupby('Department')['Salary'].mean().reset_index()
sns.barplot(x='Department', y='Salary', data=department_avg_salary, color='orange')
plt.title("Average Salary per Department")
plt.show()

# 4.2 Create a bar plot showing the total years at the company for each employee.
sns.barplot(x=employees['Name'], y=employees['YearsAtCompany'],  color='orange')
plt.xticks(rotation=45)
plt.title("Total Years at Company per Employee")
plt.show()

# 4.3 Create a histogram showing the distribution of employee ages.
sns.histplot(employees['Age'], bins=10, kde=True,  color='orange')
plt.title("Distribution of Employee Ages")
plt.show()

# 4.4 Create a box plot to show the distribution of salaries for each department.
sns.boxplot(x=employees['Department'], y=employees['Salary'],  color='orange')
plt.title("Salary Distribution per Department")
plt.show()

# 4.5 Create a scatter plot showing the relationship between age and salary.
sns.scatterplot(x=employees['Age'], y=employees['Salary'],  color='orange')
plt.title("Age vs Salary")
plt.show()