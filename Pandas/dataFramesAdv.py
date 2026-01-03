import pandas as pd
from pathlib import Path

path_file=Path('../Content')/'Movie+Assignment+Data.csv'
df=pd.read_csv(path_file)
# df[df['content_rating']=='R']
# print(df[df['content_rating']=='R'])

# canada_movies=df[df.Country=='Australia']
# print(canada_movies)

df['IFUS']=df['Country'].apply(lambda x: 'USA' if x=='USA' else 'Non-USA')
#(df['IFUS'])

arlst=[1,2,3,4,5,6,7,8,9,10]
df=pd.DataFrame(arlst)
#print(type(df))
print(df.describe())

# count  10.00000 
# mean    5.50000 total/count , 55/10=5.5
# std     3.02765 Sqrt((Sum of each sqr(number-mean)) divide by n-1)
# min     1.00000
# 25%     3.25000
# 50%     5.50000
# 75%     7.75000
# max    10.00000