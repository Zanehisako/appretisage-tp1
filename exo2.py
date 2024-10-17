import pandas as pd
import matplotlib.pyplot as mlp

dfo = pd.read_csv('evaluation_scores.csv')
df:pd.DataFrame = dfo.iloc[1:,2:]

print(dfo.loc[:,'Year'])
print('size:',df.size)

student_year_grades = dfo.set_index('Name')
print(student_year_grades)

year_student_grades= dfo.set_index('Year')
print(year_student_grades)

grades_year_student= dfo.set_index(['Listening','Speaking','Reading','Writing'])
print(grades_year_student)

#maximum number of details
print(dfo.describe())

#calculate the new coeffiants
print(dfo['Year'].mul(2))

#Data visualization
for i in range(1,dfo['Name'].size):
    dfo[dfo['Name'] == f'Student {i}'].plot(kind='line',x='Year',y=['Listening','Speaking','Reading','Writing'],title=f'Student {i} progression')

    mlp.show()

