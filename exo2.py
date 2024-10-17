from matplotlib.axes import Axes
import pandas as pd
import matplotlib.pyplot as plt 

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

#average
dfo['Average']= (dfo['Listening'] + dfo['Speaking'] + dfo['Reading'] + dfo['Writing'] / 4)

#Data visualization
'''fig,axes = plt.subplots(nrows=2,ncols=2)

dfo[dfo['Name'] == 'Student 1'].plot(ax=axes[0,0],kind='line',x='Year',y=['Listening','Speaking','Reading','Writing'],title='Student 1 progression')
dfo[dfo['Name'] == 'Student 2'].plot(ax=axes[0,1],kind='line',x='Year',y=['Listening','Speaking','Reading','Writing'],title='Student 2 progression')
dfo[dfo['Name'] == 'Student 3'].plot(ax=axes[1,0],kind='line',x='Year',y=['Listening','Speaking','Reading','Writing'],title='Student 3 progression')
dfo[dfo['Name'] == 'Student 4'].plot(ax=axes[1,1],kind='line',x='Year',y=['Listening','Speaking','Reading','Writing'],title='Student 4 progression')

plt.show()
'''
#3d plot
fig = plt.figure()
ax= fig.add_subplot(projection = '3d')
ax.scatter(dfo['Name'].astype('category').cat.codes,dfo['Year'],dfo['Average'])
ax.set_xlabel('Name')
ax.set_ylabel('Year')
ax.set_zlabel('Average')
plt.show()
