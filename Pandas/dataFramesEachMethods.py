import pandas as pd

# stdInfo={"name":['Mukund', 'Chandan', 'Ritesh','Prahlad'],
#         "Address":['MV3','Patna','Ranchi','Pune']
#         }
# df1=pd.DataFrame(stdInfo)
# df2=pd.DataFrame(stdInfo,index=[1,2,3,4]) #Original df1 value is not chaging 
# df2=pd.DataFrame(stdInfo).describe() #Original df1 value is not chaging 

# print(df1)
# print(df2)

# stdInfo1={"name":['Mukund', 'Chandan', 'Ritesh','Prahlad'],
#         "Address":['MV3','Patna','Ranchi','Pune']
#         }
#df3=pd.DataFrame(stdInfo1) #Error on this lin

data = {'Name':['A','B','C','D'],
        'Age':[1,2,3,4]}

df4 = pd.DataFrame(data) 
#print(df4)
#print(pd.options.display.min_rows)
df4.info()
print(df4[['Name']])
print(df4.groupby('Name'))
 
print(df4.info())