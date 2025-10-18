import pandas as pd

df=pd.DataFrame([[1,2],[3,4]], columns=['Col1','Col2'], index=[1,2]);
print("***************df['Col1']")
print(df['Col1'])
print(df['Col2'])
df.set_index(keys='Col2')

print("******************************df[['Col1','Col2']]")
print(df[['Col1','Col2']])

print('******************************df.loc[:1]')
print(df.loc[:1])

print("******************************df.loc[[1],['Col1']]")
print(df.loc[[1],['Col1']])

print("******************************df.loc[[1],['Col1','Col2' ]]")
print(df.loc[[1],['Col1','Col2']])

print('******************************df.iloc[1]')
print(df.iloc[1])


