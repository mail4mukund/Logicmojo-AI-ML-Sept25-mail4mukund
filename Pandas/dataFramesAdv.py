import pandas as pd
from pathlib import Path

path_file=Path('../Content')/'Movie+Assignment+Data.csv'
df=pd.read_csv(path_file)
# df[df['content_rating']=='R']
# print(df[df['content_rating']=='R'])

# canada_movies=df[df.Country=='Australia']
# print(canada_movies)

df['IFUS']=df['Country'].apply(lambda x: 'USA' if x=='USA' else 'Non-USA')
print(df['IFUS'])