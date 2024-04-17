#Importing required modules
import pandas as pd
import matplotlib.pyplot as plt
import os

#Setting the path of Excel file through 'os'
os.chdir("C:\\Users\\navit\\.pygalaxy")

#Reading the excel file
df = pd.read_excel("dataset.xls") 

#This is conversion to set all values to numeric if all are not found as numeric
df['%age(0-10)'] = pd.to_numeric(df['%age(0-10)'], errors='coerce')
df['age(11-20)'] = pd.to_numeric(df['age(11-20)'], errors='coerce')
df['age(21-30)'] = pd.to_numeric(df['age(21-30)'], errors='coerce')
df['age(31-40)'] = pd.to_numeric(df['age(31-40)'], errors='coerce')
df['%age(41-50)'] = pd.to_numeric(df['age(41-50)'], errors='coerce')

#x-axis coordinate(groouping ages)
age_categories = ['0-10', '11-20', '21-30','31-40','41-50']

#Making columns
df_stacked = df[['%age(0-10)', 'age(11-20)', 'age(21-30)','age(31-40)','age(41-50)']].copy()
df_stacked.columns = age_categories

total_population = df_stacked.sum()

# Create a bar chart for age distribution
plt.figure(figsize=(10, 6))
plt.bar(age_categories, total_population)
plt.xlabel('Age Category')
plt.ylabel('Population Count')
plt.title('Bar Chart for Age Distribution in the Population')
plt.show()