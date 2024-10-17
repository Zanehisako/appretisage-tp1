import numpy as np 
dfo =np.genfromtxt('evaluation_scores.csv',delimiter=',',skip_header=1)
print('question 2')
df = dfo[:,2:]
print('question 3')
print(dfo.shape,dfo.size)
print(df.shape,df.size)
print('question 4')
print(df.reshape(5,10,4))
print(df.reshape(5,10,4).transpose(1,0,2))
print(df.reshape(5,10,4).transpose(2,0,1))
min =df[:,1].min()
max =df.max()
avg =df.mean()
yearCube = df.reshape(5,10,4)
print('question 5')
print(max,min,avg)
print('question 6')
print(  df * [(2,1.5,3,3.5)])
print('quesion 7')
print(yearCube[2:,:,:]*[[(2,1.5,3,3.5)],[(1.5,3.5,2.5,2.5)],[(2,2,3,3)]])



