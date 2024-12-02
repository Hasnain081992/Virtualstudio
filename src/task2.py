import pandas as pd
import numpy as np    # import numpy libraries
df = pd.read_csv(r"C:\Users\44754\Documents\tempfile.csv")
df.head(10)  # to see top 5 rows
df.head(2)
# add newrow data
newrow = {'EmployeeID' :6,'Firstname':'Ahmedi','Lastname':'Hajari', 'Salary': 31000, 'Jobtitle':'MBA','SEX': 'Male','Age':33}
newrowdf = pd.DataFrame([newrow])
# add newrow data into dataframed
df = pd.concat([df,newrowdf],ignore_index = True)
print(df)
df.describe() # summary of statatistics
print(df.shape) # no of rows and columns
print(df['Firstname'])  # access column by name
 print(df[['Firstname','Lastname']])
print(df[df['Salary'] >31000])  #  check salary moretahn 31000
print(df.isnull().sum()) # checking null value
data = df.to_numpy()
print(data)
salary = df['Salary'].to_numpy()  # for salary
print(salary)  
age = df['Age'].to_numpy()
print(age)
newsalary = salary * 1.10
print('New salary by 10 percent hike', newsalary)
# increment salary 20 percent whose job title  = manager
df['Salary'] = np.where(df['Jobtitle'] =='Manager', df['Salary'] * 1.20, df['Salary'])
# creating retirement (new column)
retirementage = 50
df['yearretirement'] = np.where(df['Age'] < retirementage, retirementage - df['Age'],0)
print(df)
# sql
pip install sqlalchemy
import pandas as pd 
from sqlalchemy import create_engine
df.head()
pip install mysql-connector-python
import mysql.connector 
dbconnection = mysql.connector.connect( host = 'localhost', user = 'root', password = 'root', database = 'challenge1')
cursor = dbconnection.cursor()
query = 'select * from employee1'
cursor.execute(query)
rows = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
print(rows)
# Convert to Pandas DataFrame
df = pd.DataFrame(rows, columns=columns)

# Step 2: Upload DataFrame to Another Table
# Create SQLAlchemy engine for the database
pip install pymysql
engine = create_engine('mysql+pymysql://root:root@localhost/challenge1')
df.to_sql('employee_backup', con=engine, if_exists='replace', index=False)

# finish






